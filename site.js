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
