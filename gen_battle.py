from build import page, write, WA_BATTLE, WA_FULLPASS

body = f"""
<section class="hero bg-cover" style="background-image:url('assets/img/stage-bg.jpg')">
  <div class="spotlights"></div>
  <div class="hero-inner">
    <span class="eyebrow">1 vs 1 · Eliminación directa</span>
    <h1>Comadreja <span class="gold">Battle Master</span></h1>
    <p class="hero-sub">Acá no hay coreografía: manda la improvisación real, la conexión con la música y la actitud en escena. Solo los verdaderos masters dominan la pista.</p>
    <div class="btn-row">
      <a href="{WA_BATTLE}" class="btn btn-solid" target="_blank" rel="noopener">Inscribirme con Rodrigo</a>
      <a href="assets/pdf/reglamento-battle-master.pdf" class="btn btn-ghost" target="_blank">Descargar reglamento</a>
    </div>
  </div>
</section>

<section class="section">
  <img src="assets/img/decor/decor-02.png" alt="" class="decor-figure decor-right">
  <div class="container">
    <span class="eyebrow">Formato</span>
    <h2 class="kicker-title">Duelo cara a cara frente al jurado</h2>
    <div class="grid grid-4" style="margin-top:2.2rem">
      <div class="card"><h3 class="gold" style="font-size:1.05rem">2 rounds</h3><p style="color:var(--cream-2);font-size:.9rem">por bailarín, 30 segundos cada uno</p></div>
      <div class="card"><h3 class="gold" style="font-size:1.05rem">5 jueces</h3><p style="color:var(--cream-2);font-size:.9rem">deciden por voto de mayoría simple</p></div>
      <div class="card"><h3 class="gold" style="font-size:1.05rem">Salsa y bachata</h3><p style="color:var(--cream-2);font-size:.9rem">música sorteada de una lista oficial</p></div>
      <div class="card"><h3 class="gold" style="font-size:1.05rem">4 rondas</h3><p style="color:var(--cream-2);font-size:.9rem">eliminatorias, cuartos, semifinal y final</p></div>
    </div>
  </div>
</section>

<section class="section section-wine">
  <div class="container split">
    <div>
      <span class="eyebrow">Qué se evalúa</span>
      <h2 class="kicker-title">Improvisación, musicalidad y estilo personal</h2>
      <p class="lede">No es una coreografía preparada, sino una interpretación espontánea del bailarín. El jurado evalúa musicalidad, técnica, tiempo y ritmo, y presencia escénica.</p>
      <div style="margin-top:1.2rem">
        <span class="tag">Shines</span><span class="tag">Footwork</span><span class="tag">Estilo libre</span>
        <span class="tag">Movimientos corporales</span><span class="tag">Interpretación musical</span>
      </div>
    </div>
    <div>
      <span class="eyebrow">No se permite</span>
      <ul class="price-list">
        <li>Contacto físico agresivo</li>
        <li>Insultos o gestos obscenos</li>
        <li>Coreografía preparada evidente</li>
        <li>Bailar fuera del género musical sorteado</li>
        <li>Acrobacias peligrosas</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="split">
      <div class="card" style="text-align:center;padding:3rem 2rem">
        <span class="small-caps">Premio</span>
        <div class="amount" style="font-size:2.8rem">$250.000</div>
        <p style="color:var(--cream-2)">+ cinturón Battle Master, para el Master de Salsa y el Master de Bachata. Cada cinturón lleva una chapa con la fecha y el nombre del campeón.</p>
      </div>
      <div>
        <h2 class="kicker-title">Inscripción</h2>
        <p class="lede">Los competidores que quieran ser parte deben inscribirse directamente con Rodrigo Perazolo.</p>
        <a href="{WA_BATTLE}" class="btn btn-solid" target="_blank" rel="noopener">Escribir a Rodrigo · 351 206 6472</a>
        <p class="lede" style="margin-top:1.4rem">La inscripción al Battle Master ya está incluida dentro del Full Pass del congreso.</p>
        <a href="{WA_FULLPASS}" class="btn btn-ghost" target="_blank" rel="noopener">Ver Full Pass</a>
      </div>
    </div>
  </div>
</section>
"""

write("battle-master.html", page(
    "Comadreja Battle Master 1vs1 | Comadreja Salsa Congress 2026",
    "Comadreja Battle Master: competencia de baile 1 vs 1 de salsa y bachata. Reglamento, premios y forma de inscripción, en el Comadreja Salsa Congress 2026, Córdoba.",
    "battle-master.html",
    body
))
