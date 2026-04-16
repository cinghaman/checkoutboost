(function () {
  var prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function initLenis() {
    if (prefersReduced || typeof Lenis === "undefined") return null;
    var lenis = new Lenis({
      duration: 1.1,
      smoothWheel: true,
      wheelMultiplier: 0.9
    });

    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }

    requestAnimationFrame(raf);
    return lenis;
  }

  function initReveal() {
    if (typeof gsap === "undefined") return;

    gsap.registerPlugin(ScrollTrigger);

    var revealEls = document.querySelectorAll(".reveal");
    revealEls.forEach(function (el, index) {
      gsap.to(el, {
        opacity: 1,
        y: 0,
        duration: 0.9,
        ease: "power3.out",
        delay: index < 6 ? index * 0.05 : 0,
        scrollTrigger: index < 6 ? undefined : {
          trigger: el,
          start: "top 88%"
        }
      });
    });

    gsap.to(".hero-floating-left", {
      y: 14,
      repeat: -1,
      yoyo: true,
      duration: 2.8,
      ease: "sine.inOut"
    });

    gsap.to(".hero-floating-right", {
      y: -16,
      repeat: -1,
      yoyo: true,
      duration: 3.4,
      ease: "sine.inOut"
    });

    gsap.to(".hero-device", {
      y: 12,
      repeat: -1,
      yoyo: true,
      duration: 3.8,
      ease: "sine.inOut"
    });

    gsap.utils.toArray(".feature-spotlight, .premium-card, .metric-card, .blog-card, .pricing-card").forEach(function (card) {
      gsap.to(card, {
        yPercent: -4,
        ease: "none",
        scrollTrigger: {
          trigger: card,
          start: "top bottom",
          end: "bottom top",
          scrub: 0.8
        }
      });
    });
  }

  function initHeroCanvas() {
    if (typeof THREE === "undefined") return;

    var canvas = document.getElementById("hero-canvas");
    if (!canvas) return;

    var renderer = new THREE.WebGLRenderer({
      canvas: canvas,
      alpha: true,
      antialias: true
    });

    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(55, 1, 0.1, 100);
    camera.position.z = 7.5;

    var geometry = new THREE.BufferGeometry();
    var count = 1200;
    var positions = new Float32Array(count * 3);
    var colors = new Float32Array(count * 3);
    var colorA = new THREE.Color("#a18cff");
    var colorB = new THREE.Color("#ffd4ea");
    var colorC = new THREE.Color("#8ce5db");

    for (var i = 0; i < count; i++) {
      var i3 = i * 3;
      positions[i3] = (Math.random() - 0.5) * 12;
      positions[i3 + 1] = (Math.random() - 0.5) * 7;
      positions[i3 + 2] = (Math.random() - 0.5) * 4;

      var mixed = i % 3 === 0 ? colorA : (i % 3 === 1 ? colorB : colorC);
      colors[i3] = mixed.r;
      colors[i3 + 1] = mixed.g;
      colors[i3 + 2] = mixed.b;
    }

    geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute("color", new THREE.BufferAttribute(colors, 3));

    var material = new THREE.PointsMaterial({
      size: 0.06,
      transparent: true,
      opacity: 0.8,
      vertexColors: true
    });

    var particles = new THREE.Points(geometry, material);
    scene.add(particles);

    function resize() {
      var width = canvas.clientWidth || window.innerWidth;
      var height = canvas.parentElement ? canvas.parentElement.offsetHeight : window.innerHeight;
      renderer.setSize(width, height, false);
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
    }

    resize();
    window.addEventListener("resize", resize);

    function render(time) {
      particles.rotation.y = time * 0.00006;
      particles.rotation.x = Math.sin(time * 0.00008) * 0.08;
      renderer.render(scene, camera);
      requestAnimationFrame(render);
    }

    requestAnimationFrame(render);
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

  initLenis();
  initReveal();
  initHeroCanvas();
  initFaqAccordion();
})();
