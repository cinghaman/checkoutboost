/* ============================================================
   Smart Checkout Widgets — cookie consent + analytics (GDPR)
   Category-based consent: strictly necessary (always on),
   analytics, functional, marketing. GA (G-T9GSXKCN10) and
   Microsoft Clarity only load after the visitor opts in to
   analytics. Consent Mode v2 defaults are set to "denied".
   Until then, page views and outbound clicks go to the
   scw-events Worker (worker/index.js), which forwards them to GA4
   with no cookies, no IP and one shared client_id. Each event
   takes one path, so nothing is counted twice.
   Same pattern as cartrocket.dev/assets/consent.js.
   ============================================================ */
(function () {
  var GA_ID = "G-T9GSXKCN10";
  var CLARITY_ID = "z0tfn76wd1";
  var EVENT_URL = "https://scw-events.flat-violet-9b0d.workers.dev/api/event";
  var KEY = "scw-cookie-consent-v2"; // JSON: {analytics,functional,marketing}

  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;

  // Consent Mode v2: everything denied until the visitor opts in
  gtag("consent", "default", {
    ad_storage: "denied",
    ad_user_data: "denied",
    ad_personalization: "denied",
    analytics_storage: "denied",
    functionality_storage: "denied",
    personalization_storage: "denied",
    security_storage: "granted"
  });

  // Only real visitors on the live site: no localhost or previews, and no
  // headless browsers or our screenshot tooling's fixed window sizes.
  var PRODUCTION_HOSTS = { "smartcheckoutwidgets.com": 1, "www.smartcheckoutwidgets.com": 1 };
  var trackingAllowed =
    !!PRODUCTION_HOSTS[location.hostname] &&
    !navigator.webdriver &&
    !/HeadlessChrome/.test(navigator.userAgent) &&
    ["800x600", "1280x1200"].indexOf(screen.width + "x" + screen.height) === -1;

  var gaLoaded = false;
  var cookielessPageViewSent = false;

  function loadGA() {
    if (gaLoaded || !trackingAllowed) return;
    gaLoaded = true;
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + GA_ID;
    document.head.appendChild(s);
    gtag("js", new Date());
    // If this page was already counted cookieless, don't count it again.
    gtag("config", GA_ID, { anonymize_ip: true, send_page_view: !cookielessPageViewSent });
  }

  // Microsoft Clarity (heatmaps + session recordings), analytics consent only.
  var clarityLoaded = false;

  function syncClarity(granted) {
    if (granted && !clarityLoaded && trackingAllowed) {
      clarityLoaded = true;
      (function (c, l, a, r, i, t, y) {
        c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
        t = l.createElement(r); t.async = 1; t.src = "https://www.clarity.ms/tag/" + i;
        y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
      })(window, document, "clarity", "script", CLARITY_ID);
    }
    if (clarityLoaded) {
      var state = granted ? "granted" : "denied";
      window.clarity("consentv2", { ad_Storage: state, analytics_Storage: state });
    }
  }

  // Cookieless events for visitors without analytics consent. Nothing is
  // stored on the device. Sent as text/plain so the cross-origin request
  // needs no preflight; see worker/index.js.
  function sendCookieless(event, params) {
    if (gaLoaded || !trackingAllowed) return;
    try {
      var body = JSON.stringify({ event: event, params: params });
      if (!(navigator.sendBeacon && navigator.sendBeacon(EVENT_URL, new Blob([body], { type: "text/plain" })))) {
        fetch(EVENT_URL, { method: "POST", body: body, keepalive: true, mode: "cors", credentials: "omit", headers: { "Content-Type": "text/plain" } });
      }
    } catch (e) {}
  }

  function sendCookielessPageView() {
    var referrer;
    try {
      // Origin only: a full referrer URL can carry someone else's query params.
      referrer = document.referrer ? new URL(document.referrer).origin : undefined;
    } catch (e) {}
    sendCookieless("page_view", {
      page_path: location.pathname,
      page_location: location.origin + location.pathname,
      page_title: document.title,
      page_referrer: referrer,
      traffic_source: new URLSearchParams(location.search).get("utm_source") || undefined
    });
    cookielessPageViewSent = true;
  }

  function trackCookielessClick(e) {
    if (gaLoaded) return;
    var a = e.target.closest ? e.target.closest("a[href]") : null;
    if (!a || /^(mailto|tel):/.test(a.getAttribute("href"))) return;
    var url;
    try { url = new URL(a.href); } catch (err) { return; }
    if (url.origin === location.origin) return;
    var section = a.closest("header, footer, nav, section, article");
    sendCookieless(url.hostname === "apps.shopify.com" ? "install_click" : "outbound_click", {
      link_url: url.href,
      link_text: (a.textContent || "").trim() || undefined,
      link_location: section ? (section.id || section.tagName.toLowerCase()) : undefined,
      page_path: location.pathname
    });
  }

  // GA used to load for everyone, so returning visitors can still carry
  // _ga cookies from before the banner. Expire them unless analytics is on.
  function clearStaleGaCookies() {
    document.cookie.split("; ").forEach(function (c) {
      var name = c.split("=")[0];
      if (!/^_ga($|_)|^_gid$/.test(name)) return;
      var expire = name + "=; Max-Age=0; path=/";
      document.cookie = expire;
      document.cookie = expire + "; domain=." + location.hostname.replace(/^www\./, "");
    });
  }

  function applyConsent(prefs) {
    gtag("consent", "update", {
      analytics_storage: prefs.analytics ? "granted" : "denied",
      functionality_storage: prefs.functional ? "granted" : "denied",
      personalization_storage: prefs.functional ? "granted" : "denied",
      ad_storage: prefs.marketing ? "granted" : "denied",
      ad_user_data: prefs.marketing ? "granted" : "denied",
      ad_personalization: prefs.marketing ? "granted" : "denied"
    });
    if (prefs.analytics) loadGA();
    else clearStaleGaCookies();
    syncClarity(!!prefs.analytics);
  }

  function readPrefs() {
    try {
      var raw = localStorage.getItem(KEY);
      if (raw) return JSON.parse(raw);
    } catch (e) {}
    return null;
  }

  function savePrefs(prefs) {
    try { localStorage.setItem(KEY, JSON.stringify(prefs)); } catch (e) {}
  }

  var saved = readPrefs();
  if (saved) applyConsent(saved);

  var styleInjected = false;
  function injectStyles() {
    if (styleInjected) return;
    styleInjected = true;
    var css =
      ".scw-consent{position:fixed;z-index:2147483647;left:16px;right:16px;bottom:16px;margin:0 auto;max-width:560px;" +
      "background:var(--color-paper-0,#f8f6f1);color:var(--color-ink-0,#17132b);" +
      "border:1px solid var(--color-paper-3,#dcd7cc);border-radius:var(--radius-lg,20px);" +
      "padding:20px;font:15px/1.5 var(--font-body,'Inter',system-ui,sans-serif);box-shadow:0 16px 48px rgba(23,19,43,.18)}" +
      ".scw-consent h3{margin:0 0 8px;font:700 18px/1.2 var(--font-display,'Bricolage Grotesque',system-ui,sans-serif)}" +
      ".scw-consent p{margin:0 0 14px;color:var(--color-ink-1,#4a4560)}" +
      ".scw-consent a{color:var(--color-accent,#6d4aff);text-decoration:underline}" +
      ".scw-consent-cats{margin:0 0 16px;display:none}" +
      ".scw-consent.scw-expanded .scw-consent-cats{display:block}" +
      ".scw-consent-cat{display:flex;align-items:flex-start;justify-content:space-between;gap:14px;padding:10px 0;border-top:1px solid var(--color-paper-2,#e8e4db)}" +
      ".scw-consent-cat strong{display:block;font-size:14px}" +
      ".scw-consent-cat span{display:block;font-size:13px;color:var(--color-ink-2,#6e6983)}" +
      ".scw-switch{position:relative;flex:none;width:42px;height:24px;margin-top:2px}" +
      ".scw-switch input{position:absolute;opacity:0;width:100%;height:100%;margin:0;cursor:pointer}" +
      ".scw-switch input:disabled{cursor:not-allowed}" +
      ".scw-switch i{display:block;width:42px;height:24px;border-radius:999px;background:var(--color-paper-3,#dcd7cc);transition:background .15s;pointer-events:none}" +
      ".scw-switch i:after{content:'';position:absolute;top:3px;left:3px;width:18px;height:18px;border-radius:50%;background:#fff;box-shadow:0 1px 2px rgba(23,19,43,.2);transition:left .15s}" +
      ".scw-switch input:checked+i{background:var(--color-accent,#6d4aff)}" +
      ".scw-switch input:checked+i:after{left:21px}" +
      ".scw-switch input:disabled+i{opacity:.55}" +
      ".scw-switch input:focus-visible+i{outline:2px solid var(--color-focus,#5b37f5);outline-offset:2px}" +
      ".scw-consent-btns{display:flex;gap:10px;flex-wrap:wrap;align-items:center}" +
      ".scw-consent button{font:600 14px var(--font-body,'Inter',system-ui,sans-serif);border-radius:999px;padding:10px 20px;cursor:pointer;border:1px solid transparent}" +
      ".scw-consent button:focus-visible{outline:2px solid var(--color-focus,#5b37f5);outline-offset:2px}" +
      ".scw-consent .scw-accept{background:var(--color-accent,#6d4aff);color:#fff}" +
      ".scw-consent .scw-decline{background:transparent;color:var(--color-ink-0,#17132b);border-color:var(--color-paper-3,#dcd7cc)}" +
      ".scw-consent .scw-save{background:transparent;color:var(--color-accent,#6d4aff);border:none;text-decoration:underline;padding:10px 6px}";
    var style = document.createElement("style");
    style.textContent = css;
    document.head.appendChild(style);
  }

  var CATS = [
    { id: "necessary", name: "Strictly necessary", desc: "Required for the site to work. Can't be turned off.", locked: true },
    { id: "analytics", name: "Analytics & performance", desc: "Help us understand how visitors use the site (Google Analytics and Microsoft Clarity)." },
    { id: "functional", name: "Functional", desc: "Extra features and personalization. We don't use any at the moment." },
    { id: "marketing", name: "Marketing & advertising", desc: "Ads and campaign measurement. We don't use any at the moment." }
  ];

  function showBanner(expanded) {
    if (document.querySelector(".scw-consent")) return;
    injectStyles();

    var current = readPrefs() || { analytics: false, functional: false, marketing: false };

    var catsHtml = CATS.map(function (c) {
      var checked = c.locked || current[c.id] ? " checked" : "";
      var disabled = c.locked ? " disabled" : "";
      return (
        "<div class=\"scw-consent-cat\"><div><strong>" + c.name + "</strong><span>" + c.desc + "</span></div>" +
        "<label class=\"scw-switch\"><input type=\"checkbox\" aria-label=\"" + c.name + "\" data-cat=\"" + c.id + "\"" + checked + disabled + "><i></i></label></div>"
      );
    }).join("");

    var el = document.createElement("div");
    el.className = "scw-consent" + (expanded ? " scw-expanded" : "");
    el.setAttribute("role", "dialog");
    el.setAttribute("aria-label", "Cookie consent");
    el.innerHTML =
      "<h3>We use cookies</h3>" +
      "<p>With your OK, we use cookies to see how people use this site and which pages help. " +
      "Say no and we only count visits and link clicks, with no cookies. " +
      "See our <a href=\"/privacy/#cookies\">Privacy Policy</a>.</p>" +
      "<div class=\"scw-consent-cats\">" + catsHtml + "</div>" +
      "<div class=\"scw-consent-btns\">" +
      "<button type=\"button\" class=\"scw-accept\">Accept all</button>" +
      "<button type=\"button\" class=\"scw-decline\">Reject all</button>" +
      "<button type=\"button\" class=\"scw-save\">" + (expanded ? "Save preferences" : "Choose") + "</button>" +
      "</div>";
    document.body.appendChild(el);

    function decide(prefs) {
      savePrefs(prefs);
      el.remove();
      applyConsent(prefs);
    }
    el.querySelector(".scw-accept").addEventListener("click", function () {
      decide({ analytics: true, functional: true, marketing: true });
    });
    el.querySelector(".scw-decline").addEventListener("click", function () {
      decide({ analytics: false, functional: false, marketing: false });
    });
    el.querySelector(".scw-save").addEventListener("click", function () {
      if (!el.classList.contains("scw-expanded")) {
        el.classList.add("scw-expanded");
        this.textContent = "Save preferences";
        return;
      }
      var prefs = {};
      el.querySelectorAll("input[data-cat]").forEach(function (input) {
        if (input.getAttribute("data-cat") !== "necessary") {
          prefs[input.getAttribute("data-cat")] = input.checked;
        }
      });
      decide(prefs);
    });
  }

  // Let footer "Cookie preferences" links reopen the panel
  window.scwOpenCookiePreferences = function () { showBanner(true); };

  function init() {
    document.addEventListener("click", function (e) {
      var t = e.target.closest ? e.target.closest("[data-cookie-preferences]") : null;
      if (t) { e.preventDefault(); showBanner(true); }
    });
    if (!saved) {
      clearStaleGaCookies();
      showBanner(false);
    }
    if (!(saved && saved.analytics)) sendCookielessPageView();
    document.addEventListener("click", trackCookielessClick);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
