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
 *  - No carga popunder ni onclick. Push solo en artículos (PUSH_RE). El clic principal del sitio es
 *    "Convertir": un popunder enganchado al clic del documento abriría una
 *    ventana en la primera conversión, que es justo lo contrario de lo que la
 *    herramienta promete. Decisión tomada al migrar a Monetag.
 *  - Los anuncios cargan desde el inicio, sin esperar al aviso de cookies (decisión
 *    del titular, 23-10-2026). Si el visitante rechaza, se quitan los tags y se
 *    ocultan los huecos: "no" se guarda y no vuelven a cargarse en visitas futuras.
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
    host: 'https://nap5k.com/tag.min.js',   // host del tag de Monetag, p. ej. 'https://xxxxx.com/tag.min.js'
    zones: {
      native:   ''  // Zona 12090903 desactivada por Monetag (incumple sus términos). No volver a poner sin revisar la cuenta.
    },
    // Push Notifications: solo en artículos y guías (ver PUSH_RE). Usa el mismo
    // service worker de la raíz, /sw.js, que es el de esta zona.
    push: {
      src:  'https://5gvci.com/act/files/tag.min.js?z=12106804',
      zone: '12106804'
    }
  };

  var CONSENT_KEY = 'vidtoflac_consent';   // 'yes' | 'no'

  // Push solo en artículos (no en la portada ni en las páginas de conversión).
  // Así la petición de suscripción nunca aparece junto al botón Convertir.
  var PUSH_RE = /^\/(en\/)?(articulos|articles)\/[^\/]+\/?$/;

  // ───────────────────────────────────────────────────────────────────────────
  // Utilidades
  // ───────────────────────────────────────────────────────────────────────────
  var EN = (document.documentElement.lang || 'es').toLowerCase().indexOf('en') === 0;

  function t(es, en) { return EN ? en : es; }

  // Elección de consentimiento. Si localStorage falla (modo privado, bloqueado),
  // se recuerda en memoria solo durante esta carga; setConsent devuelve si quedó guardada.
  var memConsent = null;

  function getConsent() {
    try { var v = localStorage.getItem(CONSENT_KEY); if (v !== null) return v; }
    catch (_) {}
    return memConsent;
  }

  function setConsent(v) {
    memConsent = v;
    try { localStorage.setItem(CONSENT_KEY, v); return true; }
    catch (_) { return false; }
  }

  function configured() { return !!(CONFIG.zones.native || CONFIG.push.zone); }

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
    if (!el || !CONFIG.host || !CONFIG.zones.native || getConsent() === 'no') return;
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

  function pushAllowed() {
    return !!CONFIG.push.zone && PUSH_RE.test(location.pathname) &&
      !/\/index\.html$/.test(location.pathname);
  }

  // Tag de Push Notifications en el <head>, una sola vez por página.
  function pushTag() {
    if (document.querySelector('script[data-zone="' + CONFIG.push.zone + '"]')) return;
    var s = document.createElement('script');
    s.src = CONFIG.push.src;
    s.async = true;
    s.setAttribute('data-zone', CONFIG.push.zone);
    s.setAttribute('data-cfasync', 'false');
    document.head.appendChild(s);
  }

  function load() {
    if (loaded || !configured() || getConsent() === 'no') return;
    loaded = true;
    var slots = document.querySelectorAll('.ad-slot');
    for (var i = 0; i < slots.length; i++) mount(slots[i]);
    if (pushAllowed()) pushTag();
  }

  // Al rechazar: se quitan los tags y los huecos, se cancela la suscripción push
  // y se da de baja el service worker de la red, y después se recarga la página
  // para que no quede nada de la red en memoria.
  function unload(reload) {
    loaded = false;
    var scripts = document.querySelectorAll('script[data-zone]');
    for (var i = 0; i < scripts.length; i++) scripts[i].remove();
    var frames = document.querySelectorAll('.ad-slot iframe, .ad-slot-wrap iframe');
    for (var j = 0; j < frames.length; j++) frames[j].remove();
    hideSlots();
    // Solo se recarga si la elección quedó guardada; si no, recargar haría
    // volver el aviso y el rechazo se perdería.
    cleanupPush(function () { if (reload) location.reload(); });
  }

  // Da de baja los service workers de la red (/sw.js) y cancela sus suscripciones
  // push. Se ejecuta al rechazar y en cada carga posterior, por si el navegador
  // conserva un registro de una visita anterior.
  function cleanupPush(done) {
    var finish = function () { if (done) done(); };
    try {
      if (!('serviceWorker' in navigator)) return finish();
      navigator.serviceWorker.getRegistrations().then(function (regs) {
        return Promise.all(regs.filter(function (r) {
          var w = r.active || r.waiting || r.installing;
          return w && /\/sw\.js$/.test(w.scriptURL);
        }).map(function (r) {
          var sub = r.pushManager ? r.pushManager.getSubscription() : Promise.resolve(null);
          return sub.then(function (s) { return s ? s.unsubscribe() : false; })
                    .then(function () { return r.unregister(); });
        }));
      }).catch(function () {}).then(finish);
    } catch (_) { finish(); }
  }

  // ───────────────────────────────────────────────────────────────────────────
  // Aviso de consentimiento
  // ───────────────────────────────────────────────────────────────────────────
  // Se construye desde JS para no repetir el markup en 46 páginas. Los colores
  // salen de las custom properties del sitio, así que hereda el tema.
  // Se muestra mientras no haya elección guardada. Los anuncios ya cargan.
  function banner() {
    if (getConsent() || !configured()) return;

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
      '.cc,.cc *{box-sizing:border-box}' +
      '@media (max-width:560px){.cc{left:0;right:0;width:min(76vw,22rem);padding:1.6rem 1.2rem;' +
      'flex-direction:column;align-items:stretch;gap:1rem}' +
      '.cc p{flex:none}.cc-btns{width:100%}.cc-btns button{flex:1 1 0;min-width:0}}' +
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
      'mostramos publicidad de terceros, que usa cookies. Si la rechazas, los anuncios ' +
      'desaparecen y la herramienta funciona igual. ' +
      '<a href="/politica-de-privacidad/">Política de privacidad</a>.',
      'This site is free and your files never leave your browser. To keep it running we ' +
      'show third-party ads, which use cookies. If you decline, the ads disappear and the ' +
      'tool works just the same. ' +
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
        var saved = setConsent(value);
        box.remove();
        if (value === 'no') unload(saved);
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
  window.ads = { load: load, mount: mount, consent: function () { return getConsent(); } };

  // Sin configurar, o tras rechazar, los huecos no se muestran: así no quedan
  // recuadros vacíos de 90 px en medio del contenido.
  function hideSlots() {
    if (document.getElementById('ads-hide')) return;
    var css = document.createElement('style');
    css.id = 'ads-hide';
    css.textContent = '.ad-slot,.ad-slot-wrap{display:none!important}';
    document.head.appendChild(css);
  }

  function start() {
    if (!configured() || getConsent() === 'no') hideSlots();
    if (getConsent() === 'no') cleanupPush();   // visitas posteriores al rechazo
    banner();
    load();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
})();
