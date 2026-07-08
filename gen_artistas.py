from build import page, write, WA_FULLPASS

featured = [
    ("assets/img/artist-karen-ricardo.jpg", "Karen y Ricardo", "🇨🇱", "Chile", "9 veces campeones mundiales de salsa, creadores y organizadores de la competencia El Mundial."),
    ("assets/img/artist-carine-rafael.jpg", "Carine y Rafael", "🇧🇷", "Brasil", "Reconocidos mundialmente en la salsa, referentes de estilo y técnica."),
    ("assets/img/artist-antoni-belen.jpg", "Anthony y Belén", "🇪🇸", "España", "Reconocidos mundialmente en la bachata y su técnica."),
]

feat_html = ""
for img, name, flag, country, desc in featured:
    feat_html += f"""<div class="artist">
      <img src="{img}" alt="{name}, artistas invitados desde {country}">
      <div class="artist-info">
        <span class="flag">{flag}</span>
        <h3>{name}</h3>
        <p>{country}</p>
        <p style="text-transform:none;color:var(--cream-2);font-size:.9rem;letter-spacing:0;margin-top:.6rem">{desc}</p>
      </div>
    </div>\n"""

lineup = ["Ángel Rojas y Carla Martínez", "Cristian Paredes e Isadora Jacob", "Gabriela Mancini", "Stephanie Lucero",
          "Iván y Vichy", "Fabián y Laura", "Lucas y Lula", "Aquiles Goro", "Cato Sosa", "Nacho Vega",
          "Juan De La Cruz", "Santiago y Davor", "Aymará", "Darío Burguenes", "Julieta y Enzo", "Jorge López"]
lineup_html = "".join(f'<span class="tag">{n}</span>' for n in lineup)

djs = ["DJ Moon · Buenos Aires", "DJ Tito · Córdoba", "DJ Fede Ramírez · Córdoba", "DJ Mate Casco · Tucumán", "DJ Joseco · Mendoza"]
dj_html = "".join(f'<div class="card" style="padding:1.4rem"><h3 style="font-size:1.05rem;margin:0" class="gold">{d}</h3></div>' for d in djs)

body = f"""
<section class="hero bg-cover" style="background-image:url('assets/img/hero-congreso.jpg');min-height:60vh">
  <div class="spotlights"></div>
  <div class="hero-inner">
    <span class="eyebrow">+20 artistas en escena</span>
    <h1>Artistas y <span class="gold">DJs</span></h1>
    <p class="hero-sub">Tres parejas internacionales de primer nivel encabezan una grilla de más de veinte bailarines nacionales, con música en vivo y los mejores DJs del país.</p>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow">Cabezas de cartel</span>
    <h2 class="kicker-title">Artistas internacionales</h2>
    <div class="grid grid-3" style="margin-top:2.2rem">
      {feat_html}
    </div>
  </div>
</section>

<section class="section section-wine">
  <div class="container">
    <span class="eyebrow">Y muchos más</span>
    <h2 class="kicker-title">El resto de la grilla nacional</h2>
    <p class="lede" style="margin-top:1rem">Más de 20 artistas argentinos suben al escenario de Comadreja durante los cuatro días de shows y talleres.</p>
    <div style="margin-top:1.4rem">{lineup_html}<span class="tag">y muchos más</span></div>
    <img src="assets/img/lineup-group.jpg" alt="Grupo completo de artistas del Comadreja Salsa Congress 2026" style="border-radius:4px;margin-top:2.2rem;max-width:520px">
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow">En cabina</span>
    <h2 class="kicker-title">DJs y música en vivo</h2>
    <p class="lede" style="margin-top:1rem">Música en vivo con <b class="gold">Ramón Vacilón</b>, y sets de los mejores DJs de salsa y bachata del país.</p>
    <div class="grid grid-4" style="margin-top:1.6rem">
      {dj_html}
    </div>
    <div class="btn-row" style="margin-top:2.2rem">
      <a href="{WA_FULLPASS}" class="btn btn-solid" target="_blank" rel="noopener">Quiero mi Full Pass</a>
      <a href="talleres.html" class="btn btn-ghost">Ver talleres con estos artistas</a>
    </div>
  </div>
</section>
"""

write("artistas.html", page(
    "Artistas y DJs | Comadreja Salsa Congress 2026",
    "Karen y Ricardo, Carine y Rafael, Anthony y Belén, y más de 20 artistas nacionales. DJs y música en vivo en el Comadreja Salsa Congress 2026.",
    "artistas.html",
    body
))
