// Marsicalluminio — menu mobile e invio del modulo di contatto
(function () {
  var head = document.querySelector('.site-head');
  var btn = document.querySelector('.menu-btn');
  if (head && btn) {
    btn.addEventListener('click', function () {
      var open = head.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && head.classList.contains('open')) {
        head.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
        btn.focus();
      }
    });
  }

  var form = document.querySelector('form.quote');
  if (!form || !window.fetch) return;
  var msg = form.querySelector('.form-msg');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.checkValidity()) { form.reportValidity(); return; }
    var submit = form.querySelector('button[type=submit]');
    submit.disabled = true;
    submit.textContent = 'Invio in corso…';
    fetch(form.action, {
      method: 'POST',
      body: new FormData(form),
      headers: { 'Accept': 'application/json' }
    }).then(function (r) {
      if (!r.ok) throw new Error('send');
      window.location.href = 'grazie.html';
    }).catch(function () {
      msg.className = 'form-msg err show';
      msg.textContent = 'La richiesta non è partita. Controlla la connessione e riprova, oppure chiamaci al 335 758 4371.';
      submit.disabled = false;
      submit.textContent = 'Invia la richiesta';
    });
  });
})();
