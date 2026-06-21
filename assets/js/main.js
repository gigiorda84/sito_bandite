/* BANDITE — minimal interactions: mobile nav + slideshows */
(function () {
  "use strict";

  // ----- mobile navigation -----
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") nav.classList.remove("open");
    });
  }

  // ----- slideshows -----
  document.querySelectorAll(".slides").forEach(function (root) {
    var track = root.querySelector(".slides__track");
    var slides = root.querySelectorAll(".slide");
    var dotsWrap = root.parentElement.querySelector(".slides__dots");
    var i = 0;
    var n = slides.length;
    if (n < 1) return;

    var dots = [];
    if (dotsWrap) {
      for (var d = 0; d < n; d++) {
        var b = document.createElement("button");
        b.type = "button";
        b.setAttribute("aria-label", "Slide " + (d + 1));
        (function (idx) { b.addEventListener("click", function () { go(idx); }); })(d);
        dotsWrap.appendChild(b);
        dots.push(b);
      }
    }

    function render() {
      track.style.transform = "translateX(" + (-i * 100) + "%)";
      dots.forEach(function (dot, idx) {
        dot.setAttribute("aria-selected", idx === i ? "true" : "false");
      });
    }
    function go(idx) { i = (idx + n) % n; render(); }

    var prev = root.querySelector(".slides__btn--prev");
    var next = root.querySelector(".slides__btn--next");
    if (prev) prev.addEventListener("click", function () { go(i - 1); });
    if (next) next.addEventListener("click", function () { go(i + 1); });

    render();
  });
})();
