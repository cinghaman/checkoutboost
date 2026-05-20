(function () {
  var prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function initReveal() {
    var revealEls = document.querySelectorAll(".reveal");

    if (prefersReduced || typeof gsap === "undefined" || typeof ScrollTrigger === "undefined") {
      revealEls.forEach(function (el) {
        el.classList.add("is-visible");
      });
      return;
    }

    gsap.registerPlugin(ScrollTrigger);

    revealEls.forEach(function (el, index) {
      gsap.to(el, {
        opacity: 1,
        y: 0,
        duration: 0.45,
        ease: "power2.out",
        scrollTrigger: {
          trigger: el,
          start: "top 90%"
        }
      });
    });
  }

  function initHeroCanvas() {
    return;
  }

  function initFaqAccordion() {
    var items = document.querySelectorAll(".faq-item");
    if (!items.length) return;

    items.forEach(function (item) {
      item.addEventListener("toggle", function () {
        if (!item.open) return;

        items.forEach(function (other) {
          if (other !== item) {
            other.open = false;
          }
        });
      });
    });
  }

  function initFooterAccordion() {
    var items = Array.prototype.slice.call(document.querySelectorAll(".footer-accordion"));
    if (!items.length) return;

    var mobileQuery = window.matchMedia("(max-width: 720px)");

    function syncFooterState() {
      if (mobileQuery.matches) {
        items.forEach(function (item, index) {
          item.open = index === 0;
        });
      } else {
        items.forEach(function (item) {
          item.open = true;
        });
      }
    }

    items.forEach(function (item) {
      item.addEventListener("toggle", function () {
        if (!mobileQuery.matches || !item.open) return;

        items.forEach(function (other) {
          if (other !== item) {
            other.open = false;
          }
        });
      });
    });

    if (typeof mobileQuery.addEventListener === "function") {
      mobileQuery.addEventListener("change", syncFooterState);
    } else if (typeof mobileQuery.addListener === "function") {
      mobileQuery.addListener(syncFooterState);
    }

    syncFooterState();
  }

  initReveal();
  initHeroCanvas();
  initFaqAccordion();
  initFooterAccordion();
})();
