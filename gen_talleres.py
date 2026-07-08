from build import page, write, WA_FULLPASS

body = f"""
<section class="hero bg-cover" style="background-image:url('assets/img/stage-bg.jpg');min-height:56vh">
  <div class="spotlights"></div>
  <div class="hero-inner">
    <span class="eyebrow">Programa sujeto a cambios</span>
    <h1>Cronograma y <span class="gold">talleres</span></h1>
    <p class="hero-sub">Cuatro días de competencia, formación y fiesta, todo en el mismo hotel: Estilo MB, Villa Carlos Paz.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow">Del 26 al 29 de noviembre</span>
    <h2 class="kicker-title">Día por día</h2>
    <div style="margin-top:2.5rem;max-width:760px">

      <div class="day-block">
        <span class="day-tag">Jueves 26 · Noviembre</span>
        <h3>Final Nacional El Mundial — Parte 1</h3>
        <div class="slot"><time>08:00</time><span>Acreditaciones</span></div>
        <div class="slot"><time>09:00</time><span>Comienza la competencia</span></div>
        <div class="slot"><time>23:00</time><span>Final de la competencia y entrega de premios</span></div>
      </div>

      <div class="day-block">
        <span class="day-tag">Viernes 27 · Noviembre</span>
        <h3>Final Nacional El Mundial — Parte 2</h3>
        <div class="slot"><time>08:00</time><span>Acreditaciones</span></div>
        <div class="slot"><time>09:00</time><span>Comienza la competencia</span></div>
        <div class="slot"><time>23:00</time><span>Final de la competencia y entrega de premios</span></div>
        <div class="slot"><time>00:00</time><span>Social, toda la noche</span></div>
      </div>

      <div class="day-block">
        <span class="day-tag">Sábado 28 · Noviembre</span>
        <h3>Talleres internacionales y noche de shows</h3>
        <div class="slot"><time>—</time><span>Talleres internacionales</span></div>
        <div class="slot"><time>—</time><span>Show social</span></div>
        <div class="slot"><time>—</time><span>Battles y DJs en vivo</span></div>
      </div>

      <div class="day-block">
        <span class="day-tag">Domingo 29 · Noviembre</span>
        <h3>Talleres, masterclass all stars y gran final Battle Master</h3>
        <div class="slot"><time>—</time><span>Talleres internacionales</span></div>
        <div class="slot"><time>—</time><span>Masterclass All Stars</span></div>
        <div class="slot"><time>—</time><span>Final Comadreja Battle Master 1vs1</span></div>
        <div class="slot"><time>—</time><span>Social de cierre</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section section-wine">
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow">Talleres sábado</span>
        <h2 class="kicker-title" style="font-size:1.7rem">Con nuestros artistas internacionales</h2>
        <ul class="workshop-list">
          <li><b>Charla para competidores</b><br>con Karen y Ricardo</li>
          <li><b>Salsa · shines y vueltas combinadas</b><br>con Karen y Ricardo</li>
          <li><b>Bachata · shines y vueltas combinadas</b><br>con Estefanie Lucero</li>
          <li><b>Bachata · shines y vueltas combinadas</b><br>con Christian Paredes e Isadora Jacob</li>
          <li><b>Salsa · shines y vueltas combinadas</b><br>con Carine y Rafael</li>
        </ul>
      </div>
      <div>
        <span class="eyebrow">Talleres domingo</span>
        <h2 class="kicker-title" style="font-size:1.7rem">Mega Stars Class y más</h2>
        <ul class="workshop-list">
          <li><b>Mega Stars Class Bachata</b><br>masterclass de bachata coreográfica con 8 profesores reconocidos</li>
          <li><b>Salsa fusión</b><br>con Darío Burguenes</li>
          <li><b>Mambo · shines y vueltas combinadas</b><br>con Ángel Rojas y Carla Martínez</li>
          <li><b>Bachata · shines y vueltas combinadas</b><br>con Anthony y Belén</li>
        </ul>
      </div>
    </div>
    <div class="btn-row" style="margin-top:2.4rem">
      <a href="{WA_FULLPASS}" class="btn btn-solid" target="_blank" rel="noopener">Reservar mi lugar en los talleres</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow">Todas las noches</span>
    <h2 class="kicker-title">Shows, banda en vivo y social</h2>
    <p class="lede" style="margin-top:1rem">Shows internacionales y nacionales en el escenario de Comadreja. Social 50% bachata y 50% salsa para bailar todos. Música en vivo con Ramón Vacilón y sets de DJ Moon, DJ Tito, DJ Fede Ramírez, DJ Mate Casco y DJ Joseco.</p>
    <a href="artistas.html" class="btn btn-ghost" style="margin-top:1rem">Ver DJs y artistas</a>
  </div>
</section>
"""

write("talleres.html", page(
    "Cronograma y talleres | Comadreja Salsa Congress 2026",
    "Programa completo del Comadreja Salsa Congress 2026: cronograma día por día, talleres internacionales, shows y noches sociales.",
    "talleres.html",
    body
))
