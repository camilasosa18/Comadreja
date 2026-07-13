from build import page, write, WA_FULLPASS, WA_MUNDIAL_INFO, WA_SOCIAL, WA_ASESOR

body = f"""
<section class="hero bg-cover" style="background-image:url('assets/img/stage-bg.jpg');min-height:50vh">
  <div class="spotlights"></div>
  <div class="hero-inner">
    <span class="eyebrow">Córdoba, Villa Carlos Paz, Argentina</span>
    <h1>Precios y <span class="gold">formas de pago</span></h1>
    <p class="hero-sub">Efectivo, transferencia y tarjeta a través de Mercado Pago. El único contacto oficial para el Full Pass e inscripciones es Isa.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-2">
      <div class="price-card featured">
        <span class="small-caps">Full Pass 2026</span>
        <div class="amount">$180.000</div>
        <ul class="price-list">
          <li>Inscripción a la competencia El Mundial, todas las categorías</li>
          <li>Inscripción al Comadreja Battle Master 1vs1</li>
          <li>Clases y talleres nacionales e internacionales</li>
          <li>Noches de shows y banda en vivo</li>
          <li>Noches de social</li>
        </ul>
        <a href="{WA_FULLPASS}" class="btn btn-solid" target="_blank" rel="noopener">Quiero el Full Pass</a>
      </div>

      <div class="price-card">
        <span class="small-caps">Inscripción El Mundial</span>
        <div class="amount">Desde $60.000</div>
        <ul class="price-list">
          <li>1 categoría — $60.000</li>
          <li>2 categorías — $60.000 + $30.000</li>
          <li>3 o más categorías — $60.000 + $20.000 por categoría extra</li>
          <li>Acceso jueves y viernes, días de competencia</li>
        </ul>
        <a href="{WA_MUNDIAL_INFO}" class="btn btn-ghost" target="_blank" rel="noopener">Info para inscribirme</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-wine">
  <div class="container">
    <span class="eyebrow">Solo por una noche</span>
    <h2 class="kicker-title">Entradas a las noches de social</h2>
    <div class="grid grid-3" style="margin-top:2rem">
      <div class="card" style="text-align:center">
        <h3 class="gold" style="font-size:1rem;text-transform:uppercase;letter-spacing:.1em">Viernes</h3>
        <div class="amount" style="font-size:2rem">$25.000</div>
      </div>
      <div class="card" style="text-align:center">
        <h3 class="gold" style="font-size:1rem;text-transform:uppercase;letter-spacing:.1em">Sábado</h3>
        <div class="amount" style="font-size:2rem">$35.000</div>
      </div>
      <div class="card" style="text-align:center">
        <h3 class="gold" style="font-size:1rem;text-transform:uppercase;letter-spacing:.1em">Domingo</h3>
        <div class="amount" style="font-size:2rem">$20.000</div>
      </div>
    </div>
    <div class="btn-row" style="margin-top:2rem;justify-content:center">
      <a href="{WA_SOCIAL}" class="btn btn-solid" target="_blank" rel="noopener">Reservar entrada a la social</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow">Cómo pagar</span>
    <h2 class="kicker-title">Formas de pago</h2>
    <div class="grid grid-3" style="margin-top:2rem">
      <div class="card"><h3 class="gold" style="font-size:1.1rem">Efectivo</h3><p style="color:var(--cream-2);font-size:.92rem">Coordinalo directamente con Isa por WhatsApp.</p></div>
      <div class="card"><h3 class="gold" style="font-size:1.1rem">Transferencia</h3><p style="color:var(--cream-2);font-size:.92rem">Los datos bancarios se comparten al confirmar tu reserva.</p></div>
      <div class="card"><h3 class="gold" style="font-size:1.1rem">Tarjeta · Mercado Pago</h3><p style="color:var(--cream-2);font-size:.92rem">Escribinos y te enviamos el link de pago directo a tu WhatsApp.</p></div>
    </div>
    <div class="card" style="margin-top:2rem;border-color:var(--gold)">
      <h3 class="gold" style="font-size:1.2rem">Único contacto oficial</h3>
      <p style="color:var(--cream-2)">Todo el Full Pass y las inscripciones se coordinan exclusivamente con <b style="color:var(--cream)">Isa</b>. Desconfiá de cualquier otro canal de venta.</p>
      <a href="{WA_ASESOR}" class="btn btn-solid" target="_blank" rel="noopener">Hablar con Isa · WhatsApp</a>
    </div>
  </div>
</section>
"""

write("precios.html", page(
    "Precios y formas de pago | Comadreja Salsa Congress 2026",
    "Full Pass, inscripción a El Mundial y entradas a las noches de social del Comadreja Salsa Congress 2026. Pagos por efectivo, transferencia o Mercado Pago.",
    "precios.html",
    body
))
