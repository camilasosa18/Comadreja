from build import page, write, WA_MUNDIAL_INFO, WA_ASESOR

sedes = [
    ("Mié 5 ago", "Jujuy", "yujuy_producciones"),
    ("Sáb 15 ago", "La Pampa", "micaytincho_tym"),
    ("Sáb 5 sep", "San Juan", "ndc_productora"),
    ("Sáb 19 sep", "Neuquén", "Gonza_Gonzalez2016"),
    ("Sáb 26 sep", "Buenos Aires", "GabyMancini_"),
    ("Sáb 26 sep", "Santiago del Estero", "Deryk712"),
    ("Sáb 3 oct", "Tucumán", "PalladiumTuc"),
    ("Sáb 10 oct", "Mendoza", "EduBoschi"),
    ("Sáb 17 oct", "Formosa", "IvanLarRosaOK"),
    ("Sáb 24 oct", "San Luis", "ArcenioPrimo"),
    ("Sáb 24 oct", "Santa Fe", "elite.danceclub"),
    ("Sáb 31 oct", "Mar del Plata", "elmundial.mdp.arg"),
    ("Dom 1° nov", "Córdoba · Final Nacional", "ComadrejaProducciones"),
]

sede_html = ""
for fecha, prov, ig in sedes:
    sede_html += f"""<li class="sede-item">
      <div><span class="date">{fecha}</span><span class="prov">{prov}</span></div>
      <a href="https://www.instagram.com/{ig}" target="_blank" rel="noopener">@{ig} ↗</a>
    </li>\n"""

categorias = ["Salsa", "Bachata", "Chachachá", "Merengue", "Urbano / Contemporáneo / Moderno / Tango / Ballroom"]
cat_tags = "".join(f'<span class="tag">{c}</span>' for c in categorias)

niveles = ["Amateur", "Profesional", "ProAm"]
niveles_tags = "".join(f'<span class="tag">{n}</span>' for n in niveles)

edades = ["Baby 4-7", "Junior 8-12", "Juvenil 13-17", "Adulto 18+", "Senior 40+"]
edades_tags = "".join(f'<span class="tag">{e}</span>' for e in edades)

body = f"""
<section class="hero bg-cover" style="background-image:url('assets/img/mundial-bg-1.jpg');min-height:70vh" >
  <div class="hero-inner" style="color:var(--charcoal)">
    <span class="eyebrow" style="color:#7a5f22">Final Nacional Argentina · Sede Córdoba</span>
    <h1 style="color:#2B2416">El <span style="color:#9a7a2e">Mundial</span></h1>
    <p class="hero-sub" style="color:#4a4030">Creado por Karen y Ricardo, nueve veces campeones mundiales. Más de 20 años llevando el baile latino a un nivel profesional sin precedentes. Un nuevo comienzo, un nuevo legado: donde los sueños se convierten en historia.</p>
    <div class="btn-row">
      <a href="{WA_MUNDIAL_INFO}" class="btn btn-wine" target="_blank" rel="noopener">Info de inscripción</a>
      <a href="assets/pdf/reglamento-el-mundial-2026.pdf" class="btn btn-ghost" style="border-color:#9a7a2e;color:#7a5f22" target="_blank">Descargar reglamento</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow">Cómo se compite</span>
    <h2 class="kicker-title">Cinco etapas hasta coronar a los mejores del mundo</h2>
    <div class="grid grid-2" style="margin-top:2.5rem;gap:1.6rem">
      <div class="day-block">
        <span class="day-tag">Etapa 1</span>
        <h3>Eliminatorias y selección nacional</h3>
        <p style="color:var(--cream-2);font-size:.94rem">Cada país clasifica a sus representantes. Los primeros lugares avanzan directo a duelos de semifinal; segundos, terceros y cuartos pasan a repechaje.</p>
      </div>
      <div class="day-block">
        <span class="day-tag">Etapa 2</span>
        <h3>MasteryCamp El Mundial</h3>
        <p style="color:var(--cream-2);font-size:.94rem">Semana intensiva y obligatoria de formación en estilo, nutrición, maquillaje y proyección escénica para todos los clasificados.</p>
      </div>
      <div class="day-block">
        <span class="day-tag">Etapa 3</span>
        <h3>Repechaje</h3>
        <p style="color:var(--cream-2);font-size:.94rem">Segundos, terceros y cuartos lugares compiten por un lugar en semifinales junto a los campeones de cada país.</p>
      </div>
      <div class="day-block">
        <span class="day-tag">Etapa 4 y 5</span>
        <h3>Semifinal y Final</h3>
        <p style="color:var(--cream-2);font-size:.94rem">Duelos y tríos definen a los finalistas, que presentan su coreografía por última vez para coronar a los nuevos campeones mundiales.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section-wine">
  <div class="container">
    <span class="eyebrow">Categorías</span>
    <h2 class="kicker-title">Un lugar para cada bailarín</h2>
    <div class="grid grid-2" style="margin-top:2rem">
      <div class="card">
        <h3 class="gold" style="font-size:1.1rem">Por estilo de baile</h3>
        <div style="margin-top:.8rem">{cat_tags}</div>
        <p style="color:var(--cream-2);font-size:.9rem;margin-top:1rem">Cada estilo incluye solista, dúo shine, parejas classic y cabaret, grupos, team shine y categoría Queer.</p>
      </div>
      <div class="card">
        <h3 class="gold" style="font-size:1.1rem">Por nivel y por edad</h3>
        <div style="margin-top:.8rem">{niveles_tags}</div>
        <div style="margin-top:.6rem">{edades_tags}</div>
        <p style="color:var(--cream-2);font-size:.9rem;margin-top:1rem">El reglamento completo detalla puntajes, tiempos de presentación y penalizaciones por categoría.</p>
      </div>
    </div>
    <div class="pdf-row">
      <a class="pdf-chip" href="assets/pdf/reglamento-el-mundial-2026.pdf" target="_blank" rel="noopener">📄 Reglamento oficial completo (PDF)</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow">Sedes en toda la Argentina</span>
    <h2 class="kicker-title">Encontrá tu eliminatoria más cercana</h2>
    <p class="lede" style="margin-top:1rem">Cada sede organiza su propia inscripción. Si no encontrás tu provincia, podés presentarte en la sede más cercana. La gran final se disputa en Córdoba, el 26 y 27 de noviembre.</p>
    <ul class="sede-list" style="margin-top:2.2rem">
      {sede_html}
    </ul>
  </div>
</section>

<section class="section section-cream">
  <div class="container">
    <div class="split">
      <div>
        <span class="eyebrow">Inscripción a El Mundial</span>
        <h2 class="kicker-title">Desde $60.000</h2>
        <ul class="price-list" style="color:#4a4030">
          <li>1 categoría — $60.000</li>
          <li>2 categorías — $60.000 + $30.000</li>
          <li>3 o más categorías — $60.000 + $20.000 por cada categoría extra</li>
        </ul>
        <a href="{WA_MUNDIAL_INFO}" class="btn btn-wine" target="_blank" rel="noopener">Quiero inscribirme</a>
      </div>
      <div class="card-cream card" style="color:#2B2416">
        <h3 style="color:#2B2416">¿Full Pass o solo Mundial?</h3>
        <p style="color:#4a4030;font-size:.95rem">El Full Pass incluye tu inscripción a El Mundial, al Battle Master, todos los talleres y las noches de social. Si solo querés competir jueves y viernes, la inscripción a El Mundial te alcanza.</p>
        <a href="precios.html" class="btn btn-ghost" style="border-color:#9a7a2e;color:#7a5f22;margin-top:.6rem">Comparar precios</a>
      </div>
    </div>
  </div>
</section>
"""

write("el-mundial.html", page(
    "El Mundial 2026 · Final Nacional Córdoba | Comadreja Salsa Congress",
    "El Mundial, competencia creada por Karen y Ricardo. Final Nacional Argentina en el Comadreja Salsa Congress 2026, Córdoba. Categorías, sedes y reglamento oficial.",
    "el-mundial.html",
    body
))
