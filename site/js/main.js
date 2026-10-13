/* Comportamento mínimo. O conteúdo funciona sem JS (R8). */
(function () {
  'use strict';

  // Vídeo de fundo do hero: sempre em loop. O autoplay vem do HTML; aqui só reforçamos
  // para navegadores que bloqueiam ou pausam (economia de energia, aba em segundo plano).
  var bg = document.querySelector('[data-autoplay]');
  if (bg) {
    bg.muted = true;
    bg.defaultMuted = true;
    bg.setAttribute('muted', '');
    var tryPlay = function () {
      if (bg.paused) { var p = bg.play(); if (p && p.catch) p.catch(function () {}); }
    };
    tryPlay();
    bg.addEventListener('canplay', tryPlay);
    bg.addEventListener('pause', function () { if (!document.hidden) setTimeout(tryPlay, 200); });
    document.addEventListener('visibilitychange', function () { if (!document.hidden) tryPlay(); });
    // Se o navegador exigir interação, o primeiro toque/rolagem já inicia o loop.
    ['pointerdown', 'touchstart', 'scroll', 'keydown'].forEach(function (ev) {
      window.addEventListener(ev, tryPlay, { once: true, passive: true });
    });
  }

  // Parallax do fundo do hero (pedido do humano): a camada desce a 35% da rolagem.
  // Só transform, em uma camada própria, sem texto dentro. Desliga com prefers-reduced-motion.
  var layer = document.querySelector('[data-parallax-bg]');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)');
  if (layer && !(reduce && reduce.matches)) {
    var hero = layer.parentElement;
    var ticking = false;
    var update = function () {
      ticking = false;
      var rect = hero.getBoundingClientRect();
      if (rect.bottom < 0 || rect.top > window.innerHeight) return;
      var y = Math.max(0, -rect.top) * 0.35;
      layer.style.transform = 'translate3d(0,' + y.toFixed(1) + 'px,0)';
    };
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  }

  // Vídeo completo do tour: sem JS o link abre o mp4; com JS abre num <dialog>.
  var dialog = document.getElementById('video-dialog');
  var opener = document.querySelector('[data-video-open]');
  if (dialog && opener && typeof dialog.showModal === 'function') {
    var video = dialog.querySelector('video');
    opener.addEventListener('click', function (e) {
      e.preventDefault();
      dialog.showModal();
      video.play().catch(function () {});
    });
    dialog.addEventListener('close', function () { video.pause(); });
    dialog.addEventListener('click', function (e) { if (e.target === dialog) dialog.close(); });
  }
})();
