// Cookieless analytics endpoint for smartcheckoutwidgets.com.
// The site is a static build on Sevalla, which can't run server code, so this
// Worker lives on workers.dev instead (same pattern as cartrocket.dev's
// /api/event and thoughtbulb.dev's worker).
//
// Visitors who haven't accepted analytics cookies: assets/js/consent.js
// beacons {event, params} here and we forward it to GA4 via Measurement
// Protocol with no cookies, no IP and one shared client_id, tagged
// tracking_mode=cookieless. Visitors who accepted use gtag instead, so nothing
// is counted twice. Needs the GA_MP_SECRET secret; without it this is a no-op.

const GA_MEASUREMENT_ID = "G-T9GSXKCN10";
const ALLOWED_ORIGINS = new Set([
  "https://smartcheckoutwidgets.com",
  "https://www.smartcheckoutwidgets.com",
]);
const BOT_UA = /bot|crawl|spider|slurp|preview|facebookexternalhit|headless|lighthouse/i;

// Every cookieless event shares one client_id, so visitors who declined
// cookies show up as a single "user" instead of inflating user counts. No
// session_id either, so sessions and engagement stay consented-only.
const ANONYMOUS_CLIENT_ID = "1000000000.1000000000";

const ALLOWED_EVENTS = new Set(["page_view", "outbound_click", "install_click"]);

const STRING_PARAMS = {
  page_path: 200,
  page_location: 300,
  page_title: 200,
  page_referrer: 200,
  link_url: 300,
  link_text: 100,
  link_location: 60,
  traffic_source: 100,
};

function pickParams(raw) {
  const params = {};
  for (const [key, max] of Object.entries(STRING_PARAMS)) {
    const value = raw?.[key];
    if (typeof value === "string" && value) params[key] = value.slice(0, max);
  }
  return params;
}

function reply(status, origin, extra = {}) {
  const headers = { Vary: "Origin", ...extra };
  if (ALLOWED_ORIGINS.has(origin)) headers["Access-Control-Allow-Origin"] = origin;
  return new Response(null, { status, headers });
}

async function handleTrackingEvent(request, env) {
  const origin = request.headers.get("Origin") || "";

  if (request.method === "OPTIONS") {
    return reply(204, origin, {
      "Access-Control-Allow-Methods": "POST",
      "Access-Control-Allow-Headers": "Content-Type",
      "Access-Control-Max-Age": "86400",
    });
  }
  if (request.method !== "POST") {
    return reply(405, origin, { Allow: "POST, OPTIONS" });
  }
  // Cross-origin by design, so the Origin header must be one of ours.
  if (!ALLOWED_ORIGINS.has(origin)) {
    return new Response(null, { status: 403 });
  }

  if (!env.GA_MP_SECRET) {
    return reply(204, origin, { "X-Tracking": "no-secret" });
  }
  if (BOT_UA.test(request.headers.get("User-Agent") || "")) {
    return reply(204, origin, { "X-Tracking": "bot" });
  }

  // The browser sends text/plain (a CORS-safelisted type, so no preflight);
  // the body is still JSON.
  let body;
  try {
    body = JSON.parse(await request.text());
  } catch {
    return reply(400, origin);
  }
  if (!ALLOWED_EVENTS.has(body?.event)) {
    return reply(400, origin);
  }

  const params = pickParams(body.params);
  params.tracking_mode = "cookieless";
  params.engagement_time_msec = 1;

  const endpoint = `https://www.google-analytics.com/mp/collect?measurement_id=${GA_MEASUREMENT_ID}&api_secret=${encodeURIComponent(env.GA_MP_SECRET)}`;
  // The header carries GA's status code, never the secret.
  let gaStatus = "error";
  try {
    const gaResponse = await fetch(endpoint, {
      method: "POST",
      body: JSON.stringify({
        client_id: ANONYMOUS_CLIENT_ID,
        non_personalized_ads: true,
        events: [{ name: body.event, params }],
      }),
      signal: AbortSignal.timeout(5000),
    });
    gaStatus = String(gaResponse.status);
  } catch {
    // Network failure or timeout reaching GA; report it below.
  }

  return reply(204, origin, { "X-Tracking": `ga-${gaStatus}` });
}

export default {
  async fetch(request, env) {
    if (new URL(request.url).pathname.replace(/\/$/, "") === "/api/event") {
      return handleTrackingEvent(request, env);
    }
    return new Response("Not found", { status: 404 });
  },
};
