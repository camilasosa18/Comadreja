from build import page, write, WA_ASESOR, WA_FULLPASS, WA_MUNDIAL_INFO, WA_BATTLE

videos = [
    ("Q8_uu1Bvp50", "Congreso anterior"),
    ("7aqsAMHaa5Y", "Congreso anterior"),
    ("Q5g_2ngOzIw", "Congreso anterior"),
    ("WFRqV3ro49U", "El Mundial · presentación"),
]

video_html = ""
for vid, label in videos:
    video_html += f"""<div>
      <div class="video-wrap"><iframe src="https://www.youtube.com/embed/{vid}" title="{label}" frameborder="0" allowfullscreen loading="lazy"></iframe></div>
      <p class="small-caps" style="margin-top:.6rem">{label}</p>
    </div>\n"""

body = f"""
<section class="hero bg-cover" style="background-image:url('assets/img/hero-congreso.jpg');min-height:52vh">
  <div class="spotlights"></div>
  <div class="hero-inner">
    <span class="eyebrow">Estamos para ayudarte</span>
    <h1>Contacto</h1>
    <p class="hero-sub">Escribinos por WhatsApp según lo que necesites, o seguinos en Instagram para novedades del congreso.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid grid-3">
      <div class="card">
        <h3 class="gold" style="font-size:1.1rem">Full Pass</h3>
        <p style="color:var(--cream-2);font-size:.92rem">Reservá tu lugar en el congreso completo.</p>
        <a href="{WA_FULLPASS}" class="btn btn-solid" target="_blank" rel="noopener" style="margin-top:1rem">Quiero el Full Pass</a>
      </div>
      <div class="card">
        <h3 class="gold" style="font-size:1.1rem">Inscripción a El Mundial</h3>
        <p style="color:var(--cream-2);font-size:.92rem">Info sobre categorías y precios de inscripción.</p>
        <a href="{WA_MUNDIAL_INFO}" class="btn btn-ghost" target="_blank" rel="noopener" style="margin-top:1rem">Quiero inscribirme</a>
      </div>
      <div class="card">
        <h3 class="gold" style="font-size:1.1rem">Hablar con un asesor</h3>
        <p style="color:var(--cream-2);font-size:.92rem">Cualquier otra consulta sobre el congreso.</p>
        <a href="{WA_ASESOR}" class="btn btn-ghost" target="_blank" rel="noopener" style="margin-top:1rem">Más información</a>
      </div>
    </div>
    <div class="card" style="margin-top:1.6rem;display:flex;gap:1.6rem;align-items:center;flex-wrap:wrap">
      <img src="assets/img/organizador-rodrigo-perazolo.jpg" alt="Rodrigo Perazolo, organizador del Battle Master 1vs1" style="width:110px;height:110px;object-fit:cover;border-radius:50%;border:1px solid rgba(201,162,77,.28)">
      <div>
        <h3 class="gold" style="font-size:1.1rem">Battle Master 1vs1</h3>
        <p style="color:var(--cream-2);font-size:.92rem">Inscripción directa con Rodrigo Perazolo, organizador, 351 206 6472.</p>
        <a href="{WA_BATTLE}" class="btn btn-ghost" target="_blank" rel="noopener" style="margin-top:1rem">Escribir a Rodrigo</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-wine">
  <div class="container">
    <span class="eyebrow">Seguinos</span>
    <h2 class="kicker-title" style="font-size:1.8rem">Instagram oficial</h2>
    <div class="grid grid-3" style="margin-top:1.6rem">
      <a class="card" href="https://www.instagram.com/comadrejasalsacongress/?hl=en" target="_blank" rel="noopener">
        <h3 class="gold" style="font-size:1.05rem">@comadrejasalsacongress</h3>
        <p style="color:var(--cream-2);font-size:.88rem">Cuenta oficial del congreso</p>
      </a>
      <a class="card" href="https://www.instagram.com/elmundial.argentina/?hl=en" target="_blank" rel="noopener">
        <h3 class="gold" style="font-size:1.05rem">@elmundial.argentina</h3>
        <p style="color:var(--cream-2);font-size:.88rem">Final Nacional Argentina</p>
      </a>
      <a class="card" href="https://www.instagram.com/elmundial.oficial/?hl=en" target="_blank" rel="noopener">
        <h3 class="gold" style="font-size:1.05rem">@elmundial.oficial</h3>
        <p style="color:var(--cream-2);font-size:.88rem">Cuenta oficial de El Mundial</p>
      </a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow">Así se vive Comadreja</span>
    <h2 class="kicker-title">Videos de ediciones anteriores</h2>
    <div class="grid grid-2" style="margin-top:2rem">
      {video_html}
    </div>
  </div>
</section>

<section class="section section-wine">
  <div class="container">
    <span class="eyebrow">Dónde es</span>
    <h2 class="kicker-title" style="font-size:1.8rem">Hotel Estilo MB</h2>
    <p class="lede" style="margin-top:.6rem">Almafuerte 40, Villa Carlos Paz, Córdoba, Argentina.</p>
    <div style="border:1px solid rgba(201,162,77,.28);border-radius:4px;overflow:hidden;margin-top:1.4rem">
      <iframe src="https://www.google.com/maps?q=Almafuerte+40,+Villa+Carlos+Paz,+C%C3%B3rdoba&output=embed" width="100%" height="380" style="border:0;display:block" loading="lazy"></iframe>
    </div>
  </div>
</section>
"""

write("contacto.html", page(
    "Contacto | Comadreja Salsa Congress 2026",
    "Contactate por WhatsApp para el Full Pass, inscripciones a El Mundial o al Battle Master. Seguinos en Instagram y encontrá la ubicación del Hotel Estilo MB.",
    "contacto.html",
    body
))
