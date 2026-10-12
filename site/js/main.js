/* Comportamento mínimo (sem animação nesta fase). O conteúdo funciona sem JS. */
(function () {
  'use strict';
  // Vídeo do tour: sem JS o link abre o mp4; com JS abre num <dialog>.
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
