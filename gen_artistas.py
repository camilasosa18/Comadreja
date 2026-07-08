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

national = [
    ("assets/img/artist-julieta-enzo.jpg", "Julieta y Enzo", "🇦🇷", "Río Cuarto"),
    ("assets/img/artist-lucas-lula.jpg", "Lucas y Lula", "🇦🇷", "Córdoba"),
    ("assets/img/artist-santiago-davor.jpg", "Santiago y Davor", "🇦🇷", "Río Cuarto"),
    ("assets/img/artist-nacho-vega.jpg", "Nacho Vega", "🇦🇷", "Córdoba"),
    ("assets/img/artist-stephanie-lucero.jpg", "Stephanie Lucero", "🇦🇷", "Buenos Aires"),
    ("assets/img/artist-isidora-cristian.jpg", "Isidora y Cristian", "🇨🇱", "Chile"),
    ("assets/img/artist-ivan-silvana.jpg", "Iván y Silvana", "🇦🇷", "Córdoba"),
    ("assets/img/artist-juan-de-la-cruz.jpg", "Juan De La Cruz", "🇦🇷", "Córdoba"),
    ("assets/img/artist-jose-maria-onaindia.jpg", "José María Onaindia", "🇦🇷", "Tucumán"),
    ("assets/img/artist-victoria-jorge.jpg", "Victoria y Jorge", "🇦🇷", "Córdoba"),
    ("assets/img/artist-william-corona.jpg", "William Corona", "🇨🇱", "Chile"),
    ("assets/img/artist-angel-carly.jpg", "Angel y Carly", "🇻🇪", "Venezuela · Chile"),
    ("assets/img/artist-cami-blanes.jpg", "Cami Blanes", "🇦🇷", "Córdoba"),
    ("assets/img/artist-dario-burgenes.jpg", "Darío Burgenes", "🇦🇷", "San Francisco, Córdoba"),
    ("assets/img/artist-fabian-laura.jpg", "Fabián y Laura", "🇦🇷", "Córdoba"),
    ("assets/img/artist-gabriela-mancini.jpg", "Gabriela Mancini", "🇦🇷", "Buenos Aires"),
    ("assets/img/artist-guaracheros-dc.jpg", "Guaracheros DC", "🇦🇷", "Tito Pérez · Córdoba"),
]
national_html = ""
for img, name, flag, place in national:
    national_html += f"""<div class="artist">
      <img src="{img}" alt="{name}, artista nacional invitado desde {place}">
      <div class="artist-info">
        <span class="flag">{flag}</span>
        <h3>{name}</h3>
        <p>{place}</p>
      </div>
    </div>\n"""

companies = [
    ("assets/img/group-mi-mambo.jpg", "Mi Mambo", "by Angel Rojas · Chile"),
    ("assets/img/group-bailatino.jpg", "Bailatino", "Chile"),
]
companies_html = ""
for img, name, place in companies:
    companies_html += f"""<div>
      <img src="{img}" alt="{name}, compañía invitada de {place}" style="border-radius:4px;width:100%">
      <h3 style="margin-top:1rem" class="gold">{name}</h3>
      <p style="color:var(--cream-2);font-size:.9rem;letter-spacing:0;text-transform:none">{place}</p>
    </div>\n"""

djs = ["DJ Moon · Buenos Aires", "DJ Tito · Córdoba", "DJ Fede Ramírez · Córdoba", "DJ Matias Casco · Tucumán", "DJ Joseco · Mendoza"]
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
    <div class="grid grid-4" style="margin-top:2.2rem">
      {national_html}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <span class="eyebrow">Compañías invitadas</span>
    <h2 class="kicker-title">Grupos de baile</h2>
    <div class="grid grid-2" style="margin-top:2.2rem">
      {companies_html}
    </div>
  </div>
</section>

<section class="section section-wine">
  <div class="container">
    <span class="eyebrow">En el escenario</span>
    <h2 class="kicker-title">Conducción</h2>
    <p class="lede" style="margin-top:1rem">Ariel Cechel, Gaby Amor, Seba La Vega y Maxi Vergara conducen los cuatro días de Comadreja Salsa Congress.</p>
    <img src="assets/img/group-locutores.jpg" alt="Ariel Cechel, Gaby Amor, Seba La Vega y Maxi Vergara, conducción del Comadreja Salsa Congress 2026" style="border-radius:4px;margin-top:2.2rem;max-width:520px">
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
    <img src="assets/img/dj-lineup.jpg" alt="DJ Joseco, DJ Fede Ramírez, DJ Moon, DJ Tito y DJ Matias Casco en cabina" style="border-radius:4px;margin-top:2.2rem;max-width:520px">
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
