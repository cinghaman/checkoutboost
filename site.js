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
