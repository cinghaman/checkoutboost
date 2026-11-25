/* Hallmark · motion primitives: counter · marquee (CSS) · hover-tilt */

(function () {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  const liveOffers = document.getElementById("live-offers");
  const benchOffers = document.getElementById("bench-offers");

  let offers = 3;

  function tick() {
    offers += Math.random() > 0.55 ? 1 : 0;
    if (offers > 5) offers = 3;
    if (offers < 2) offers = 2;

    if (liveOffers) liveOffers.textContent = String(offers);
    if (benchOffers) benchOffers.textContent = String(offers);
  }

  if (!reduceMotion && (liveOffers || benchOffers)) {
    setInterval(tick, 2400);
  }

  const tiltCards = document.querySelectorAll("[data-tilt]");

  if (!reduceMotion) {
    tiltCards.forEach(function (card) {
      var raf = null;

      card.addEventListener("mousemove", function (e) {
        var rect = card.getBoundingClientRect();
        var x = (e.clientX - rect.left) / rect.width - 0.5;
        var y = (e.clientY - rect.top) / rect.height - 0.5;
        if (raf) cancelAnimationFrame(raf);
        raf = requestAnimationFrame(function () {
          card.style.transform =
            "perspective(900px) rotateX(" + (-y * 4).toFixed(2) + "deg) rotateY(" + (x * 5).toFixed(2) + "deg) translateY(-2px)";
        });
      });

      card.addEventListener("mouseleave", function () {
        if (raf) cancelAnimationFrame(raf);
        card.style.transform = "";
      });
    });
  }
})();

/* Mobile navigation.
   The links collapse behind a button below 900px. Pages whose markup has no
   .nav__toggle are simply skipped. */
(function () {
  var nav = document.querySelector(".nav");
  var toggle = nav && nav.querySelector(".nav__toggle");
  if (!toggle) return;

  toggle.addEventListener("click", function () {
    var open = nav.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", String(open));
  });

  // Following a link should not leave the menu open behind the new page.
  nav.addEventListener("click", function (event) {
    if (!event.target.closest(".nav__link")) return;
    nav.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
  });
})();

/* Console tabs · the homepage "console" rail switches the screen preview.
   Each tab carries its image, alt text, title and plan; the next image is
   warmed on hover so the swap never flashes. */
(function () {
  var tabs = document.querySelectorAll("[data-bench-src]");
  var screen = document.getElementById("bench-screen");
  var title = document.getElementById("bench-title");
  var plan = document.getElementById("bench-plan");
  if (!tabs.length || !screen) return;

  function warm(tab) { var img = new Image(); img.src = tab.getAttribute("data-bench-src"); }

  tabs.forEach(function (tab) {
    tab.addEventListener("mouseenter", function () { warm(tab); }, { once: true });
    tab.addEventListener("focus", function () { warm(tab); }, { once: true });
    tab.addEventListener("click", function () {
      tabs.forEach(function (t) { t.setAttribute("aria-pressed", String(t === tab)); });
      screen.src = tab.getAttribute("data-bench-src");
      screen.alt = tab.getAttribute("data-bench-alt");
      if (title) title.textContent = tab.getAttribute("data-bench-title").replace("&amp;", "&");
      if (plan) {
        var plus = tab.getAttribute("data-bench-plan") === "plus";
        plan.textContent = plus ? "Shopify Plus" : "Every Shopify plan";
        plan.classList.toggle("feature__plan--plus", plus);
      }
    });
  });
})();

/* Articles: "On this page" list built from the headings. */
(function () {
  var layout = document.querySelector(".post-layout");
  var content = layout && layout.querySelector(":scope > .post-content");
  if (!content || document.querySelector(".rubik-toc")) return;
  var heads = [].filter.call(content.querySelectorAll("h2"), function (h) { return !h.closest(".answer-brief, aside"); });
  if (heads.length < 3) return;
  var used = {};
  var list = document.createElement("ol");
  var links = heads.map(function (h) {
    if (!h.id) {
      var base = h.textContent.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "") || "section";
      var id = base, n = 2;
      while (used[id] || document.getElementById(id)) id = base + "-" + n++;
      h.id = id;
    }
    used[h.id] = true;
    var li = document.createElement("li");
    var a = document.createElement("a");
    a.href = "#" + h.id;
    a.textContent = h.id === "faq-heading" ? "FAQ" : h.textContent;
    li.appendChild(a);
    list.appendChild(li);
    return a;
  });
  var toc = document.createElement("nav");
  toc.className = "post-toc";
  toc.setAttribute("aria-label", "On this page");
  toc.innerHTML = '<p class="post-toc__title">On this page</p>';
  toc.appendChild(list);
  layout.appendChild(toc);

  var queued = false;
  function mark() {
    queued = false;
    var at = 0;
    heads.forEach(function (h, i) { if (h.getBoundingClientRect().top < 160) at = i; });
    links.forEach(function (a, i) { i === at ? a.setAttribute("aria-current", "true") : a.removeAttribute("aria-current"); });
  }
  window.addEventListener("scroll", function () { if (!queued) { queued = true; requestAnimationFrame(mark); } }, { passive: true });
  mark();
  // A link to a heading whose id was only just added.
  if (location.hash) { var t = document.getElementById(location.hash.slice(1)); if (t) t.scrollIntoView(); }
})();

/* Videos: YouTube loads only after a click. Without JavaScript the link opens YouTube. */
document.addEventListener("click", function (event) {
  var play = event.target.closest(".post-video__play");
  if (!play || event.metaKey || event.ctrlKey) return;
  event.preventDefault();
  var frame = document.createElement("iframe");
  frame.src = "https://www.youtube-nocookie.com/embed/" + play.getAttribute("data-video") + "?autoplay=1&rel=0";
  frame.title = play.getAttribute("data-title") || "Video";
  frame.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
  frame.allowFullscreen = true;
  play.parentNode.replaceChildren(frame);
});
