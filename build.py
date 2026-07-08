import os

ROOT = os.path.dirname(os.path.abspath(__file__))

WA_ISA = "5493512066467"
WA_RODRIGO = "5493512066472"

def wa(number, text):
    import urllib.parse
    return f"https://wa.me/{number}?text={urllib.parse.quote(text)}"

WA_FULLPASS = wa(WA_ISA, "Hola Isa! Quiero acceder al FULL PASS del Comadreja Salsa Congress 2026.")
WA_MUNDIAL_INFO = wa(WA_ISA, "Hola! Quiero información para inscribirme en El Mundial 2026, sede Córdoba.")
WA_ASESOR = wa(WA_ISA, "Hola! Quiero más información sobre el Comadreja Salsa Congress 2026.")
WA_SOCIAL = wa(WA_ISA, "Hola! Quiero reservar entrada para una noche social del Comadreja Salsa Congress 2026.")
WA_BATTLE = wa(WA_RODRIGO, "Hola Rodrigo! Quiero inscribirme en el Comadreja Battle Master 1vs1.")

NAV_ITEMS = [
    ("index.html", "Inicio"),
    ("el-mundial.html", "El Mundial"),
    ("battle-master.html", "Battle Master"),
    ("talleres.html", "Talleres"),
    ("artistas.html", "Artistas"),
    ("precios.html", "Precios"),
    ("contacto.html", "Contacto"),
]

def header(active):
    links = ""
    for href, label in NAV_ITEMS:
        cls = " active" if href == active else ""
        links += f'<a href="{href}" class="{cls.strip()}">{label}</a>\n'
    return f"""<header class="nav">
  <div class="nav-inner">
    <a href="index.html" class="nav-logo"><img src="assets/img/logo.png" alt="Comadreja Salsa Congress 2026"></a>
    <nav class="nav-links">
      {links}
      <a href="{WA_FULLPASS}" class="nav-cta" target="_blank" rel="noopener">Full Pass</a>
    </nav>
    <button class="nav-toggle" aria-label="Abrir menú">☰</button>
  </div>
</header>"""

FOOTER = f"""<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <img src="assets/img/logo.png" alt="Comadreja Salsa Congress" style="height:44px;margin-bottom:1rem">
        <p style="color:var(--cream-2);font-size:.92rem;max-width:320px">Más que historia, una experiencia. Congreso mundial de salsa y bachata en Villa Carlos Paz, Córdoba. Del 26 al 29 de noviembre de 2026.</p>
      </div>
      <div>
        <h4>Navegación</h4>
        <a href="el-mundial.html">El Mundial</a>
        <a href="battle-master.html">Battle Master 1vs1</a>
        <a href="talleres.html">Talleres y cronograma</a>
        <a href="artistas.html">Artistas y DJs</a>
        <a href="precios.html">Precios</a>
      </div>
      <div>
        <h4>Contacto</h4>
        <a href="{WA_ASESOR}" target="_blank" rel="noopener">WhatsApp Isa · Full Pass e inscripciones</a>
        <a href="https://www.instagram.com/comadrejasalsacongress/?hl=en" target="_blank" rel="noopener">Instagram · Comadreja Salsa Congress</a>
        <a href="https://www.instagram.com/elmundial.argentina/?hl=en" target="_blank" rel="noopener">Instagram · El Mundial Argentina</a>
        <a href="https://www.instagram.com/elmundial.oficial/?hl=en" target="_blank" rel="noopener">Instagram · El Mundial Oficial</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Comadreja Producciones. Hotel Estilo MB, Almafuerte 40, Villa Carlos Paz, Córdoba.</span>
      <span>Programa sujeto a cambios.</span>
    </div>
  </div>
</footer>
<a class="wa-float" href="{WA_ASESOR}" target="_blank" rel="noopener" aria-label="WhatsApp">☎</a>
<script src="js/main.js"></script>"""

def page(title, desc, active, body, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="css/styles.css">
{extra_head}
</head>
<body>
{header(active)}
{body}
{FOOTER}
</body>
</html>"""

def write(fname, html):
    with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", fname)

__all__ = ["page", "write", "WA_FULLPASS", "WA_MUNDIAL_INFO", "WA_ASESOR", "WA_SOCIAL", "WA_BATTLE"]
