# -*- coding: utf-8 -*-
"""Table des articles publies et remplacement automatique des href="#".

Chaque generateur appelle linkify() avant d'ecrire un fichier. Un lien reste en "#"
tant que l'article correspondant n'existe pas, ce qui evite les liens morts.
"""
import re

# fragment de titre  ->  chemin de l'article depuis la racine du site
LINKS = [
 ("Meilleure mutuelle senior : le comparatif",       "mutuelle-senior/meilleure-mutuelle-senior/"),
 ("Quelle mutuelle prendre quand on part",           "mutuelle-senior/mutuelle-depart-retraite/"),
 ("Meilleure mutuelle senior à Toulouse",            "mutuelle-senior/mutuelle-senior-toulouse/"),
 ("Mutuelle qui rembourse bien le dentaire",         "garanties-remboursements/mutuelle-dentaire-optique-audition/"),
 ("Lire un tableau de garanties",                    "garanties-remboursements/lire-tableau-garanties/"),
 ("Mutuelle fonction publique hospitalière",         "mutuelle-pro/mutuelle-fonction-publique-hospitaliere/"),
 ("Mutuelle TNS et loi Madelin",                     "mutuelle-pro/mutuelle-tns-madelin/"),
 ("Prix d'une mutuelle senior à 60",                 "prix-et-aides/prix-mutuelle-senior/"),
 ("Changer de mutuelle en cours d'année",            "droits-et-demarches/changer-mutuelle-en-cours-annee/"),
 ("Délai de carence et questionnaire de santé",      "droits-et-demarches/delai-carence-questionnaire-sante/"),
]

_A = re.compile(r'<a([^>]*?)href="#"([^>]*?)>(.*?)</a>', re.S)

def linkify(html, prefix=""):
    """Remplace href="#" par l'URL de l'article quand le libelle du lien le designe."""
    def sub(m):
        before, after, inner = m.group(1), m.group(2), m.group(3)
        for frag, url in LINKS:
            if frag in inner:
                return f'<a{before}href="{prefix}{url}"{after}>{inner}</a>'
        return m.group(0)
    return _A.sub(sub, html)
