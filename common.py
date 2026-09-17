# -*- coding: utf-8 -*-
"""Briques partagees par les trois generateurs : en-tete, menu, pied de page, mentions.

Un seul endroit pour le menu et le pied de page : si une categorie change de nom,
elle change partout.
"""

SITE = "https://analytics-ds.github.io/comparmutuelle"  # domaine reel a brancher avant mise en ligne
NOM = "Comparmutuelle"
BASELINE = "Les comparatifs de la mutuelle santé, de la retraite à la fonction publique."

CATS = {
 "mutuelle-senior":          dict(menu="Senior",       nom="Mutuelle senior"),
 "garanties-remboursements": dict(menu="Garanties",    nom="Garanties et remboursements"),
 "mutuelle-pro":             dict(menu="Par métier",   nom="Mutuelle par métier"),
 "prix-et-aides":            dict(menu="Prix",         nom="Prix et économies"),
 "droits-et-demarches":      dict(menu="Démarches",    nom="Droits et démarches"),
}

import os as _os

def _logo_exts():
    """Extension reelle de chaque logo present dans assets/logos."""
    d = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "assets", "logos")
    out = {}
    for f in _os.listdir(d):
        slug, ext = _os.path.splitext(f)
        if ext in (".svg", ".png", ".jpg") and "@" not in slug:
            out.setdefault(slug, ext.lstrip("."))
            if ext != ".svg":
                out[slug] = ext.lstrip(".")
    return out

LOGO_EXT = _logo_exts()  # vrais logos des assureurs, en SVG ou en PNG selon la source

def logo_src(R, slug):
    """Chemin du logo d'un assureur depuis la profondeur R."""
    return f'{R}assets/logos/{slug}.{LOGO_EXT.get(slug, "svg")}'

ICON_SEARCH = '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="M16 16l5 5"/></svg>'
BURGER = ('<svg width="22" height="14" viewBox="0 0 22 14" fill="none" stroke="#111" stroke-width="1.7">'
          '<path d="M0 1h22M0 7h22M0 13h22"/></svg>')
ARROW = '<svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800'
         '&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">')

def head(R, title, desc, canonical=None, extra=""):
    can = f'\n<link rel="canonical" href="{canonical}">' if canonical else ""
    return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">{can}
<meta property="og:site_name" content="{NOM}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
{FONTS}
<link rel="icon" href="{R}assets/logo/favicon.svg" type="image/svg+xml">
<meta name="theme-color" content="#0D1A14">
<link rel="stylesheet" href="{R}assets/css/site.css?v=1">
{extra}'''

def header(R, current=None, scrolled=False):
    menu = "".join(
      f'      <li><a href="{R}{s}/"' +
      (' style="text-decoration:underline;text-underline-offset:6px"' if s == current else '') +
      f'>{c["menu"]}</a></li>\n' for s, c in CATS.items())
    return f'''<header{' class="scrolled"' if scrolled else ''}>
  <div class="wrap nav">
    <a class="logo" href="{R or './'}" aria-label="{NOM}, accueil"><img class="l-light" src="{R}assets/logo/logo-light.svg" alt="{NOM}" width="620" height="133"><img class="l-dark" src="{R}assets/logo/logo.svg" alt="" aria-hidden="true" width="620" height="133"></a>
    <ul class="menu">
{menu}    </ul>
    <div class="nav-actions">
      <a class="iconbtn" href="{R}#outil" aria-label="Rechercher">{ICON_SEARCH}</a>
      <a class="btn btn-dark" href="{R}#outil">Comparer 2 mutuelles</a>
      <button class="burger" aria-label="Menu">{BURGER}</button>
    </div>
  </div>
</header>'''

def newsletter(titre="Recevez chaque comparatif de mutuelle avant tout le monde"):
    return f'''<section class="news" id="newsletter">
  <div class="wrap">
    <div class="news-card">
      <div>
        <h2>{titre}</h2>
        <p>Un email par mois : les hausses de cotisation repérées, les tableaux de garanties relus ligne à ligne et les nouveaux comparatifs.</p>
      </div>
      <div>
        <form class="form" onsubmit="return false">
          <input type="email" placeholder="Votre adresse email" aria-label="Adresse email" required>
          <button class="btn btn-accent" type="submit">Je m'inscris</button>
        </form>
        <p class="form-note">Pas de publicité, pas de revente de fichier, désinscription en un clic.</p>
      </div>
    </div>
  </div>
</section>'''

def footer(R):
    cats = "".join(f'<li><a href="{R}{s}/">{c["nom"]}</a></li>' for s, c in CATS.items())
    return f'''<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand"><a class="logo" href="{R or './'}" aria-label="{NOM}, accueil"><img src="{R}assets/logo/logo.svg" alt="{NOM}" width="620" height="133" loading="lazy"></a><p>{BASELINE} Nous relevons les garanties dans le tableau contractuel, nous les convertissons en euros de reste à charge et nous publions la méthode.</p></div>
      <div><h4>Comparatifs</h4><ul>{cats}</ul></div>
      <div><h4>Outils</h4><ul><li><a href="{R}#outil">Comparer deux mutuelles</a></li><li><a href="{R}#simulateur">Calculer un reste à charge</a></li><li><a href="{R}#classement">Le classement du mois</a></li><li><a href="{R}#methode">Notre méthode</a></li></ul></div>
      <div><h4>À propos</h4><ul><li><a href="{R}#methode">Comment nous comparons</a></li><li><a href="{R}a-propos/">Qui sommes-nous</a></li><li><a href="{R}a-propos/#corrections">Signaler une erreur</a></li><li><a href="{R}mentions-legales/">Mentions légales</a></li></ul></div>
    </div>
    <div class="foot-bottom"><span>© 2026 {NOM}. Comparatifs de mutuelles santé, senior, fonction publique et indépendants.</span><span>Information non contractuelle, relevé de démonstration, ne constitue pas un conseil personnalisé.</span></div>
  </div>
</footer>'''

DISCLOSURE = ('<div class="disclosure"><b>Information, pas conseil.</b> Les notes et les montants publiés ici sont un relevé '
              'de démonstration établi sur des tableaux de garanties, en formule intermédiaire, pour un profil de référence. '
              'Ils ne constituent pas une recommandation personnalisée. Les remboursements réels dépendent de la formule, '
              'du département, du professionnel de santé et du respect du parcours de soins.</div>')
