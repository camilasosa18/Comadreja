from build import page, write, WA_FULLPASS, WA_MUNDIAL_INFO, WA_ASESOR

body = f"""
<section class="hero bg-cover" style="background-image:url('assets/img/hero-congreso.jpg')">
  <div class="spotlights"></div>
  <div class="hero-inner">
    <span class="eyebrow">Comadreja Producciones presenta</span>
    <h1 class="h1-logo">
      <span class="sr-only">Comadreja Salsa Congress 2026</span>
      <img src="assets/img/logo-comadreja.png" alt="" class="h1-mark h1-mark-comadreja">
      <img src="assets/img/logo-salsa.png" alt="" class="h1-mark h1-mark-salsa">
      <img src="assets/img/logo-congress.png" alt="" class="h1-mark h1-mark-congress">
      <img src="assets/img/logo-2026.png" alt="" class="h1-mark h1-mark-2026">
    </h1>
    <p class="hero-sub">Más que historia, una experiencia. El congreso mundial de salsa y bachata más esperado del año en Córdoba: artistas internacionales, competencias, talleres, shows y pura energía latina.</p>
    <div class="btn-row">
      <a href="{WA_FULLPASS}" class="btn btn-solid" target="_blank" rel="noopener">Quiero el Full Pass</a>
      <a href="el-mundial.html" class="btn btn-ghost">Conocer El Mundial</a>
    </div>
    <div class="hero-meta">
      <div><b>26 al 29 de noviembre</b>2026</div>
      <div><b>Hotel Estilo MB</b>Almafuerte 40, Villa Carlos Paz, Córdoba</div>
      <div><b>+20 artistas</b>Internacionales y nacionales</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow">La cuenta regresiva</span>
    <h2 class="kicker-title">Faltan menos días de lo que pensás</h2>
    <div id="countdown" class="countdown" style="margin-top:1.8rem"></div>
  </div>
</section>

<section class="section section-wine">
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow">20+ años de trayectoria</span>
        <h2 class="kicker-title">Un congreso que marcó generaciones de bailarines</h2>
        <p class="lede">Comadreja Salsa Congress reúne a estrellas internacionales y potencia el talento argentino, elevando la escena de la salsa y la bachata en Córdoba edición tras edición. Este año, la Final Nacional de <b class="gold">El Mundial</b> y la competencia 1 vs 1 <b class="gold">Comadreja Battle Master</b> se suman a los talleres, shows y noches sociales que ya son un clásico.</p>
        <div class="btn-row" style="margin-top:1.6rem">
          <a href="artistas.html" class="btn btn-ghost">Ver artistas invitados</a>
        </div>
      </div>
      <div class="video-wrap">
        <video controls poster="assets/img/video-poster.jpg">
          <source src="assets/video/resumen-congreso.mp4" type="video/mp4">
        </video>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow">Qué vas a vivir</span>
    <h2 class="kicker-title">Cuatro días, dos competencias, una sola experiencia</h2>
    <div class="grid grid-3" style="margin-top:2.5rem">
      <div class="card">
        <h3 class="gold">El Mundial</h3>
        <p style="color:var(--cream-2);font-size:.95rem">Final nacional argentina de la competencia creada por Karen y Ricardo, 9 veces campeones mundiales. Jueves y viernes.</p>
        <a href="el-mundial.html" class="btn btn-ghost" style="margin-top:1rem">Ver reglamento y sedes</a>
      </div>
      <div class="card">
        <h3 class="gold">Comadreja Battle Master 1vs1</h3>
        <p style="color:var(--cream-2);font-size:.95rem">Duelos de improvisación pura, dos rounds de 30 segundos. $500.000 en efectivo más cinturón para el campeón.</p>
        <a href="battle-master.html" class="btn btn-ghost" style="margin-top:1rem">Cómo se compite</a>
      </div>
      <div class="card">
        <h3 class="gold">Talleres y shows</h3>
        <p style="color:var(--cream-2);font-size:.95rem">Clases con Karen y Ricardo, Carine y Rafael, Anthony y Belén y más de 20 artistas. Shows, banda en vivo y social todas las noches.</p>
        <a href="talleres.html" class="btn btn-ghost" style="margin-top:1rem">Ver cronograma</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-cream">
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow">Artistas internacionales</span>
        <h2 class="kicker-title">Tres parejas de primer nivel mundial</h2>
        <p class="lede">Karen y Ricardo (Chile), Carine y Rafael (Brasil) y Anthony y Belén (España) encabezan una grilla de más de 20 artistas nacionales e internacionales.</p>
        <a href="artistas.html" class="btn btn-wine" style="margin-top:1.4rem">Conocer a todos los artistas</a>
      </div>
      <img src="assets/img/lineup-group.jpg" alt="Line up completo de artistas Comadreja Salsa Congress 2026" style="border-radius:4px">
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow">Full Pass</span>
    <h2 class="kicker-title">Todo el congreso, un solo acceso</h2>
    <div class="split" style="margin-top:2rem;align-items:flex-start">
      <div class="price-card featured">
        <span class="small-caps">Full Pass 2026</span>
        <div class="amount">$180.000</div>
        <ul class="price-list">
          <li>Inscripción a la competencia El Mundial, todas las categorías</li>
          <li>Inscripción al Comadreja Battle Master 1vs1</li>
          <li>Clases y talleres nacionales e internacionales</li>
          <li>Noches de shows y banda en vivo</li>
          <li>Noches de social, viernes a domingo</li>
        </ul>
        <a href="{WA_FULLPASS}" class="btn btn-solid" target="_blank" rel="noopener">Quiero el Full Pass</a>
      </div>
      <div>
        <p class="lede">¿Solo querés competir en la Final Nacional de El Mundial? También podés inscribirte únicamente para la competencia, jueves y viernes.</p>
        <a href="{WA_MUNDIAL_INFO}" class="btn btn-ghost" target="_blank" rel="noopener">Info inscripción a El Mundial</a>
        <p class="lede" style="margin-top:1.6rem">Ver todos los precios, noches de social sueltas y formas de pago.</p>
        <a href="precios.html" class="btn btn-ghost">Ver todos los precios</a>
      </div>
    </div>
  </div>
</section>
"""

write("index.html", page(
    "Comadreja Salsa Congress 2026 · Villa Carlos Paz, Córdoba",
    "Congreso mundial de salsa y bachata. 26 al 29 de noviembre 2026, Hotel Estilo MB, Villa Carlos Paz, Córdoba. Competencias, talleres, shows y artistas internacionales.",
    "index.html",
    body
))
