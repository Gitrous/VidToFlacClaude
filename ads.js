/* ads.js — publicidad y consentimiento, en un único sitio.
 *
 * Por qué existe este archivo (y es la única excepción a la regla de archivo
 * único de CLAUDE.md): la migración de AdSense a Monetag fueron 497
 * referencias repartidas por 46 páginas, porque el ID de publicador y los IDs
 * de slot estaban escritos a mano en cada una. Aquí no hay nada repetido: las
 * páginas solo traen `<script src="/ads.js" defer></script>` y los huecos
 * marcados con `.ad-slot`. Cambiar de red, de zona o de formato se hace
 * editando ESTE archivo y ningún otro.
 *
 * Qué NO hace, a propósito:
 *  - No carga popunder, onclick ni push. El clic principal del sitio es
 *    "Convertir": un popunder enganchado al clic del documento abriría una
 *    ventana en la primera conversión, que es justo lo contrario de lo que la
 *    herramienta promete. Decisión tomada al migrar a Monetag.
 *  - No carga NADA antes del consentimiento. Las cookies publicitarias
 *    requieren consentimiento previo (RGPD); hasta que alguien acepta, no se
 *    inserta ni un script de la red.
 */
(function () {
  'use strict';

  // ───────────────────────────────────────────────────────────────────────────
  // CONFIGURACIÓN — lo único que hay que tocar
  // ───────────────────────────────────────────────────────────────────────────
  // Rellena `host` y `zones` con lo que da el panel de Monetag
  // (Sites → el sitio → el formato → Get code). Mientras estén vacíos no se
  // carga publicidad: las páginas funcionan y los huecos quedan ocultos.
  var CONFIG = {
    host: '',            // host del tag de Monetag, p. ej. 'https://xxxxx.com/tag.min.js'
    zones: {
      native:   '',      // Native Banner — rellena los huecos .ad-slot
      vignette: ''       // Vignette — solo en artículos, nunca en el conversor
    }
  };

  // El vignette solo se permite en las páginas de artículo. En la portada y en
  // las landings vive el conversor, y un interstitial a mitad de una
  // conversión interrumpe el trabajo del usuario.
  var VIGNETTE_PATHS = ['/articulos/', '/en/articles/'];

  var CONSENT_KEY = 'vidtoflac_consent';   // 'yes' | 'no'

  // ───────────────────────────────────────────────────────────────────────────
  // Utilidades
  // ───────────────────────────────────────────────────────────────────────────
  var EN = (document.documentElement.lang || 'es').toLowerCase().indexOf('en') === 0;

  function t(es, en) { return EN ? en : es; }

  function store(key, val) {
    try { if (val === undefined) return localStorage.getItem(key); localStorage.setItem(key, val); }
    catch (_) { return null; }     // modo privado o almacenamiento bloqueado
  }

  function configured() { return !!(CONFIG.host && CONFIG.zones.native); }

  function vignetteAllowed() {
    for (var i = 0; i < VIGNETTE_PATHS.length; i++) {
      if (location.pathname.indexOf(VIGNETTE_PATHS[i]) === 0) return true;
    }
    return false;
  }

  // ───────────────────────────────────────────────────────────────────────────
  // Inserción de los tags
  // ───────────────────────────────────────────────────────────────────────────
  var loaded = false;

  function tag(zone, parent) {
    var s = document.createElement('script');
    s.src = CONFIG.host;
    s.async = true;
    s.setAttribute('data-zone', zone);
    s.setAttribute('data-cfasync', 'false');
    (parent || document.body).appendChild(s);
    return s;
  }

  // Un hueco concreto. Se usa también desde el conversor para los anuncios que
  // aparecen entre las vistas previas, por eso es público (window.ads.mount).
  function mount(el) {
    if (!el || !configured() || store(CONSENT_KEY) !== 'yes') return;
    if (el.dataset.adMounted) return;        // idempotente: no duplica tags
    el.dataset.adMounted = '1';
    el.hidden = false;
    tag(CONFIG.zones.native, el);
    watchEmpty(el);
  }

  // Si a los 2 s el hueco sigue vacío (bloqueador, sin relleno disponible, o
  // cuenta aún sin aprobar), se avisa donde haya un mensaje preparado y, si no,
  // se oculta el hueco para no dejar un recuadro vacío en medio del contenido.
  function watchEmpty(el) {
    setTimeout(function () {
      if (el.getBoundingClientRect().height > 20) return;
      var wrap = el.closest('.ad-slot-wrap');
      if (wrap) wrap.classList.add('is-empty');
      else el.hidden = true;
    }, 2000);
  }

  function load() {
    if (loaded || !configured() || store(CONSENT_KEY) !== 'yes') return;
    loaded = true;
    var slots = document.querySelectorAll('.ad-slot');
    for (var i = 0; i < slots.length; i++) mount(slots[i]);
    if (vignetteAllowed() && CONFIG.zones.vignette) tag(CONFIG.zones.vignette);
  }

  // ───────────────────────────────────────────────────────────────────────────
  // Aviso de consentimiento
  // ───────────────────────────────────────────────────────────────────────────
  // Se construye desde JS para no repetir el markup en 46 páginas. Los colores
  // salen de las custom properties del sitio, así que hereda el tema.
  function banner() {
    if (store(CONSENT_KEY) || !configured()) return;

    var css = document.createElement('style');
    css.textContent =
      '.cc{position:fixed;left:1rem;right:1rem;bottom:1rem;z-index:9998;margin:0 auto;' +
      'max-width:40rem;background:var(--panel-2,#15161a);color:var(--ink,#e8e6e1);' +
      'border:1px solid var(--line-strong,#2e3036);border-radius:var(--radius-sm,10px);' +
      'padding:1rem 1.1rem;display:flex;flex-wrap:wrap;gap:.85rem;align-items:center;' +
      'box-shadow:0 12px 32px rgba(0,0,0,.45);font-size:.84rem;line-height:1.5}' +
      '.cc p{margin:0;flex:1 1 16rem}' +
      '.cc a{color:var(--amber,#19c37d)}' +
      '.cc-btns{display:flex;gap:.5rem;flex:0 0 auto}' +
      '.cc button{font:inherit;font-size:.8rem;padding:.5rem .9rem;border-radius:8px;' +
      'cursor:pointer;border:1px solid var(--line-strong,#2e3036);background:transparent;' +
      'color:var(--ink,#e8e6e1)}' +
      '.cc button.ok{background:var(--amber,#19c37d);border-color:var(--amber,#19c37d);' +
      'color:#07120d;font-weight:600}' +
      '@media (prefers-reduced-motion:no-preference){.cc{animation:ccin .25s ease both}' +
      '@keyframes ccin{from{opacity:0;transform:translateY(8px)}}}';
    document.head.appendChild(css);

    var box = document.createElement('div');
    box.className = 'cc';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-live', 'polite');
    box.setAttribute('aria-label', t('Aviso de cookies', 'Cookie notice'));

    var p = document.createElement('p');
    p.innerHTML = t(
      'Este sitio es gratis y tus archivos nunca salen de tu navegador. Para mantenerlo ' +
      'mostramos publicidad, que usa cookies de terceros. ¿Nos dejas activarlas? ' +
      'Puedes rechazarlas y la herramienta funciona igual. ' +
      '<a href="/politica-de-privacidad/">Política de privacidad</a>.',
      'This site is free and your files never leave your browser. To keep it running we ' +
      'show ads, which use third-party cookies. May we switch them on? ' +
      'You can decline and the tool works just the same. ' +
      '<a href="/en/privacy-policy/">Privacy policy</a>.'
    );

    var btns = document.createElement('div');
    btns.className = 'cc-btns';

    function choice(label, value, cls) {
      var b = document.createElement('button');
      b.type = 'button';
      b.textContent = label;
      if (cls) b.className = cls;
      b.addEventListener('click', function () {
        store(CONSENT_KEY, value);
        box.remove();
        if (value === 'yes') load();
      });
      return b;
    }

    btns.appendChild(choice(t('Rechazar', 'Decline'), 'no'));
    btns.appendChild(choice(t('Aceptar', 'Accept'), 'yes', 'ok'));

    box.appendChild(p);
    box.appendChild(btns);
    document.body.appendChild(box);
  }

  // ───────────────────────────────────────────────────────────────────────────
  // Arranque
  // ───────────────────────────────────────────────────────────────────────────
  window.ads = { load: load, mount: mount, consent: function () { return store(CONSENT_KEY); } };

  function start() { banner(); load(); }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
})();
