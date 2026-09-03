(function () {
  var q = document.getElementById('q');
  var hoja = document.getElementById('hoja');
  var nada = document.getElementById('nada');
  var celdas = Array.prototype.slice.call(hoja.querySelectorAll('.cell'));
  var grupos = Array.prototype.slice.call(hoja.querySelectorAll('.grupo'));
  var filtro = '*';

  function aplicar() {
    var txt = q.value.trim().toLowerCase();
    var vistos = 0;
    celdas.forEach(function (c) {
      var okCat = filtro === '*' ? true
                : filtro === '!ko'  ? c.dataset.ko === '1'
                : filtro === '!fit' ? c.dataset.nc === '1'
                : c.dataset.cat === filtro;
      var okTxt = !txt
        || c.dataset.k.toLowerCase().indexOf(txt) > -1
        || c.textContent.toLowerCase().indexOf(txt) > -1;
      var ver = okCat && okTxt;
      c.hidden = !ver;
      if (ver) vistos++;
    });
    grupos.forEach(function (g) {
      g.hidden = !g.querySelector('.cell:not([hidden])');
    });
    nada.hidden = vistos > 0;
  }

  q.addEventListener('input', aplicar);

  document.querySelectorAll('.chip').forEach(function (b) {
    b.addEventListener('click', function () {
      var f = b.dataset.f;
      filtro = (filtro === f && f !== '*') ? '*' : f;
      document.querySelectorAll('.chip').forEach(function (o) {
        o.classList.toggle('activo', o.dataset.f === filtro);
      });
      aplicar();
    });
  });

  document.querySelectorAll('.seg [data-size]').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('.seg [data-size]').forEach(function (o) {
        o.classList.toggle('activo', o === b);
      });
      var s = +b.dataset.size;
      document.documentElement.style.setProperty('--sz', s + 'px');
      document.documentElement.style.setProperty('--celda-w', Math.max(126, s * 3) + 'px');
    });
  });

  var fondo = document.getElementById('fondo');
  fondo.addEventListener('click', function () {
    var on = document.body.classList.toggle('invertido');
    fondo.setAttribute('aria-pressed', on ? 'true' : 'false');
  });

  // clic en una celda: copia la clave, que es lo que se escribe en <Icon name="…">
  var t;
  hoja.addEventListener('click', function (e) {
    var c = e.target.closest('.cell');
    if (!c) return;
    var k = c.dataset.k;
    var listo = function () {
      clearTimeout(t);
      document.querySelectorAll('.copiada').forEach(function (o) { o.classList.remove('copiada'); });
      c.classList.add('copiada');
      t = setTimeout(function () { c.classList.remove('copiada'); }, 900);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(k).then(listo, listo);
    } else {
      var ta = document.createElement('textarea');
      ta.value = k; document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); } catch (err) {}
      document.body.removeChild(ta); listo();
    }
  });

  // "/" enfoca la busqueda
  document.addEventListener('keydown', function (e) {
    if (e.key === '/' && document.activeElement !== q) { e.preventDefault(); q.focus(); }
    if (e.key === 'Escape' && document.activeElement === q) { q.value = ''; aplicar(); q.blur(); }
  });
})();
