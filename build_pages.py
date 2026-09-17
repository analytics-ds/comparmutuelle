# -*- coding: utf-8 -*-
"""Genere les pages fixes : a propos et mentions legales."""
import os, json
from common import *
from linkify import linkify

PAGES = [
dict(slug="a-propos", title="Qui sommes-nous : la méthode de Comparmutuelle",
 desc="Qui écrit les comparatifs de Comparmutuelle, d'où viennent les chiffres publiés, comment les mutuelles sont notées et comment le site est financé.",
 h1="Qui sommes-nous", lead="Comparmutuelle compare les contrats de complémentaire santé à partir des tableaux de garanties et des conditions générales publiés par les mutuelles. Voici d'où viennent les chiffres et comment ils sont notés.",
 blocks=[
  ("h2","Ce que nous faisons"),
  ("p","Nous lisons les tableaux de garanties et les conditions générales des contrats du marché, nous convertissons chaque pourcentage en euros de reste à charge sur des actes courants, nous relevons les tarifs à plusieurs âges pour un même profil et nous publions le tout au même endroit, avec la méthode."),
  ("h2","Comment nous notons"),
  ("p","Chaque mutuelle reçoit une note sur 10 sur quatre critères, puis une note globale pondérée. Les remboursements pèsent le plus lourd, parce qu'ils sont la seule chose qu'on achète."),
  ("ul",["<b>Remboursements</b> : reste à charge en euros sur une couronne, des verres progressifs, une aide auditive, une chambre particulière et des dépassements d'honoraires",
         "<b>Prix et stabilité</b> : cotisation pour le profil de référence et hausse annoncée à 65 et 70 ans, grille publiée ou non",
         "<b>Conditions d'entrée</b> : questionnaire de santé, délai de carence, âge limite de souscription, reprise d'ancienneté",
         "<b>Service et proximité</b> : agences, conseiller nommé, tiers payant chez les professionnels, délai de remboursement constaté"]),
  ("h2","Qui édite ce site"),
  ("p","L'éditeur du site et le directeur de la publication sont indiqués dans les <a href=\"../mentions-legales/\">mentions légales</a>. Les comparatifs publiés ici sont une information générale et ne remplacent ni un devis ni l'avis d'un conseiller."),
  ("h2","Ce que nous ne faisons pas"),
  ("p","Nous ne vendons pas de contrat, nous ne transmettons aucune coordonnée à une mutuelle et nous ne donnons pas de conseil personnalisé. Les notes publiées à ce stade sont un relevé de démonstration qui illustre la méthode ; elles se remplacent par le relevé réel avant toute publication ouverte."),
  ("h2","Corrections et signalements"),
  ("p","Un chiffre erroné se corrige et se signale. Toute correction significative est indiquée en bas du comparatif concerné. Pour signaler une erreur, écrivez-nous à l'adresse indiquée dans les mentions légales."),
 ]),
dict(slug="mentions-legales", title="Mentions légales de Comparmutuelle",
 desc="Mentions légales, éditeur, hébergeur, propriété intellectuelle, données personnelles et avertissement sur la nature des informations publiées sur Comparmutuelle.",
 h1="Mentions légales", lead="Informations légales relatives au site Comparmutuelle et avertissement sur la portée des contenus publiés.",
 blocks=[
  ("h2","Éditeur du site"),
  ("p","À compléter avant mise en ligne : dénomination sociale, forme juridique, capital, siège social, numéro SIREN, numéro de TVA intracommunautaire, directeur de la publication et adresse de contact."),
  ("h2","Hébergement"),
  ("p","À compléter avant mise en ligne : nom, raison sociale et adresse de l'hébergeur du site."),
  ("h2","Nature des informations publiées"),
  ("p","Les contenus publiés sur ce site ont une vocation d'information générale. Ils ne constituent ni un conseil personnalisé, ni une offre de souscription, ni une intermédiation en assurance. Les notes et montants sont un relevé de démonstration."),
  ("h2","Sources et mise à jour"),
  ("p","Les garanties proviennent des tableaux de garanties et des conditions générales des contrats cités. Les bases de remboursement proviennent de l'Assurance Maladie. Les règles citées renvoient au code de la mutualité, au code des assurances et au code de la sécurité sociale."),
  ("h2","Crédits photo"),
  ("p","Les photographies publiées sur ce site proviennent d'Unsplash et sont utilisées dans les conditions de la licence Unsplash. La liste des visuels et le lien vers chaque photographie d'origine sont tenus dans le fichier de sources du site."),
  ("h2","Propriété intellectuelle"),
  ("p","Les textes, tableaux, classements et visuels publiés sur ce site sont protégés. Toute reproduction, même partielle, suppose une autorisation préalable. Les noms et logos des mutuelles citées appartiennent à leurs titulaires respectifs."),
  ("h2","Données personnelles"),
  ("p","Les adresses collectées via le formulaire d'inscription à la lettre d'information servent uniquement à l'envoi de celle-ci. Elles ne sont ni revendues ni transmises à des tiers. Vous disposez d'un droit d'accès, de rectification et de suppression en écrivant à l'adresse de contact."),
 ]),
]

def render(p):
    R = "../"
    body = ""
    for kind, val in p["blocks"]:
        if kind == "h2":
            body += f"<h2>{val}</h2>"
        elif kind == "p":
            body += f"<p>{val}</p>"
        elif kind == "ul":
            body += "<ul>" + "".join(f"<li>{li}</li>" for li in val) + "</ul>"
    ld = json.dumps({"@context":"https://schema.org","@type":"WebPage","name":p["title"],
                     "description":p["desc"],"url":f'{SITE}/{p["slug"]}/',"inLanguage":"fr-FR",
                     "isPartOf":{"@type":"WebSite","name":NOM,"url":SITE}}, ensure_ascii=False)
    return f'''<!doctype html>
<html lang="fr">
<head>
{head(R, p["title"], p["desc"], canonical=f'{SITE}/{p["slug"]}/', extra='<script type="application/ld+json">' + ld + '</script>')}</head>
<body>

{header(R, scrolled=True)}

<section class="art-head" style="padding-top:120px">
  <div class="wrap">
    <div class="art-card">
      <nav class="crumbs" aria-label="Fil d'Ariane"><a href="{R}">Accueil</a><i></i><span>{p["h1"]}</span></nav>
      <h1>{p["h1"]}</h1>
      <p class="art-lead">{p["lead"]}</p>
    </div>
  </div>
</section>

<section class="art-body">
  <div class="wrap">
    <article class="prose" style="max-width:820px;margin:0 auto">
      {body}
      {DISCLOSURE}
    </article>
  </div>
</section>

{footer(R)}

<script src="{R}assets/js/site.js?v=1"></script>
</body>
</html>
'''

if __name__ == "__main__":
    for p in PAGES:
        os.makedirs(p["slug"], exist_ok=True)
        open(os.path.join(p["slug"], "index.html"), "w", encoding="utf-8").write(linkify(render(p), "../"))
        print("ok", p["slug"])
