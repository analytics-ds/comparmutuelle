# -*- coding: utf-8 -*-
"""Genere la page d'accueil de Comparepargne.

Usage : python3 build_home.py  (depuis le dossier comparepargne)
"""
import json
from common import *
from linkify import linkify

R = ""
TITLE = "Comparateur de mutuelles santé : le classement des meilleures mutuelles senior"
DESC = ("Comparatif de mutuelles santé : remboursement réel du dentaire, de l'optique et de l'audition en euros, "
        "prix à 60, 65 et 70 ans, questionnaire de santé et agences. 11 mutuelles comparées, de Prévifrance à AXA.")

LOGOS = ["previfrance","harmonie-mutuelle","mgen","aesio","ag2r","malakoff-humanis","matmut","april","groupama","maif","axa"]
NOMS = {"previfrance":"Mutuelle Prévifrance","harmonie-mutuelle":"Harmonie Mutuelle","mgen":"MGEN","aesio":"Aésio Mutuelle",
        "ag2r":"AG2R La Mondiale","malakoff-humanis":"Malakoff Humanis","matmut":"Matmut","april":"April",
        "groupama":"Groupama","maif":"MAIF","axa":"AXA"}

# notes sur 10 : remboursements, prix et stabilite, conditions d'entree, service et proximite, note globale
CONTRATS = {
 "Mutuelle Prévifrance": [9.4, 8.6, 9.8, 9.2, 9.2],
 "Harmonie Mutuelle":    [8.8, 8.2, 9.4, 8.4, 8.6],
 "MGEN":                 [8.2, 9.0, 9.4, 7.8, 8.4],
 "Aésio Mutuelle":       [7.9, 8.6, 9.2, 7.4, 8.1],
 "AG2R La Mondiale":     [7.8, 7.6, 8.6, 7.8, 7.9],
 "Malakoff Humanis":     [7.5, 7.4, 9.0, 7.6, 7.8],
 "Matmut":               [7.0, 8.4, 6.8, 7.6, 7.6],
 "April":                [6.6, 8.8, 5.6, 7.0, 7.4],
 "Groupama":             [6.4, 7.6, 8.8, 7.4, 7.3],
 "MAIF":                 [6.2, 7.8, 8.0, 7.2, 7.2],
 "AXA":                  [5.8, 6.4, 5.4, 7.0, 6.9],
}
CRITS = [("Remboursements","dentaire, optique, audition, en euros"),
         ("Prix et stabilité","cotisation et hausse à 65 et 70 ans"),
         ("Conditions d'entrée","questionnaire, carence, âge limite"),
         ("Service et proximité","agences, tiers payant, délais"),
         ("Note globale","moyenne pondérée")]

CLASSEMENT = [
 ("previfrance","Mutuelle Prévifrance","La meilleure mutuelle senior du panel","Aucun questionnaire de santé ni délai de carence, 90 € de reste à charge sur une couronne, 1 100 € par aide auditive et 40 agences, dont le réseau d'Occitanie.","9,2","up","▲ +0,2"),
 ("harmonie-mutuelle","Harmonie Mutuelle","Le plus grand réseau de soins","Tiers payant généralisé, réseau de soins négociés qui fait baisser le prix des verres, 1 000 € par aide auditive.","8,6","up","▲ +0,1"),
 ("mgen","MGEN","La référence des agents publics","Garanties lisibles, la hausse la plus faible du panel entre 60 et 70 ans, grille publiée.","8,4","flat","= 0,0"),
 ("aesio","Aésio Mutuelle","Le bon rapport prix et garanties","164 € par mois pour un couple sans questionnaire, remboursements dans la moyenne haute.","8,1","flat","= 0,0"),
 ("ag2r","AG2R La Mondiale","Le contrat le plus modulable","Garanties à la carte, mais un tarif couple parmi les plus élevés du panel.","7,9","down","▼ -0,1"),
]

FEAT = dict(href="mutuelle-senior/meilleure-mutuelle-senior/", img="une.jpg",
  alt="Un couple de jeunes retraités marche dans un parc", tag="Classement",
  h2="Meilleure mutuelle senior : le comparatif de 11 contrats après 60 ans",
  p="Ce qu'il reste à payer sur une couronne, des verres progressifs et une aide auditive, en euros. Le prix pour un couple et sa hausse à 65 et 70 ans. Le questionnaire de santé, le délai de carence, l'agence. La mutuelle la mieux notée est celle qui tient les quatre critères ensemble, pas celle qui gagne sur un seul.",
  meta="11 contrats comparés · 11 min de lecture")

SIDE = [("garanties-remboursements/mutuelle-dentaire-optique-audition/","gar-1.jpg","Remboursements","Mutuelle qui rembourse bien le dentaire, l'optique et l'audition : le comparatif en euros","10 min de lecture"),
        ("mutuelle-senior/mutuelle-depart-retraite/","sen-2.jpg","Retraite","Quelle mutuelle prendre quand on part à la retraite : garder celle de l'entreprise ou changer","9 min de lecture"),
        ("prix-et-aides/prix-mutuelle-senior/","prix-1.jpg","Prix","Prix d'une mutuelle senior à 60, 65 et 70 ans : les tarifs relevés contrat par contrat","8 min de lecture"),
        ("droits-et-demarches/delai-carence-questionnaire-sante/","dro-2.jpg","Conditions","Délai de carence et questionnaire de santé : les mutuelles qui n'en imposent pas","7 min de lecture")]

TILES = [("mutuelle-senior","Mutuelle senior","3 comparatifs"),
         ("garanties-remboursements","Garanties et remboursements","2 comparatifs"),
         ("mutuelle-pro","Mutuelle par métier","2 comparatifs"),
         ("droits-et-demarches","Droits et démarches","2 comparatifs")]

POSTS = [("mutuelle-senior/mutuelle-senior-toulouse/","sen-3.jpg","Proximité","Meilleure mutuelle senior à Toulouse et en Occitanie : agences, tiers payant et tarifs","7 mutuelles","8 min"),
         ("garanties-remboursements/lire-tableau-garanties/","gar-2.jpg","Méthode","Lire un tableau de garanties : ce que veulent dire 100 %, 200 % et 300 % BR","4 notions","8 min"),
         ("mutuelle-pro/mutuelle-fonction-publique-hospitaliere/","pro-1.jpg","Fonction publique","Mutuelle fonction publique hospitalière et territoriale : le comparatif des contrats","6 mutuelles","9 min"),
         ("droits-et-demarches/changer-mutuelle-en-cours-annee/","dro-1.jpg","Résiliation","Changer de mutuelle en cours d'année : la résiliation infra-annuelle en pratique","5 cas","6 min")]

def jsonld():
    org = {"@context":"https://schema.org","@type":"Organization","name":NOM,"url":SITE,
           "description":BASELINE,"logo":f"{SITE}/assets/logo/logo.svg"}
    site = {"@context":"https://schema.org","@type":"WebSite","name":NOM,"url":SITE,"inLanguage":"fr-FR"}
    items = {"@context":"https://schema.org","@type":"ItemList","name":"Classement des mutuelles santé",
             "itemListOrder":"https://schema.org/ItemListOrderDescending","numberOfItems":len(CLASSEMENT),
             "itemListElement":[{"@type":"ListItem","position":i+1,"name":n,
               "description":f"Note {sc}/10. {b}. {why}"} for i,(_,n,b,why,sc,_,_) in enumerate(CLASSEMENT)]}
    return "".join('<script type="application/ld+json">'+json.dumps(d,ensure_ascii=False)+"</script>\n"
                   for d in (org,site,items))

side = "".join(f'''
        <a class="side-item" href="{h}">
          <img src="assets/img/{img}" alt="" width="96" height="80" loading="lazy">
          <div><span class="eyebrow">{k}</span><h3>{t}</h3><small>{m}</small></div>
        </a>''' for h,img,k,t,m in SIDE)

tiles = "".join(f'''
      <a class="tile" href="{s}/"><img src="assets/img/cat-{s}.jpg" alt="{n}" width="760" height="720" loading="lazy"><span class="tile-label"><span><strong>{n}</strong><em>{c}</em></span><span class="arrow">{ARROW}</span></span></a>''' for s,n,c in TILES)

rank = "".join(f'''
      <div class="rank-row"><span class="pos{" first" if i==0 else ""}">0{i+1}</span><img src="{logo_src("", logo)}" alt="{n}" width="120" height="33"><div class="why"><b>{b}</b>{why}</div><div class="score"><b>{sc}</b><small>/10</small><span class="chip{"" if cls=="up" else " "+cls}">{chip}</span></div></div>''' for i,(logo,n,b,why,sc,cls,chip) in enumerate(CLASSEMENT))

posts = "".join(f'''
      <a class="post" href="{h}"><img src="assets/img/{img}" alt="" width="800" height="560" loading="lazy"><div class="post-body"><span class="eyebrow">{k}</span><h3>{t}</h3><span class="meta">{n} <i></i> {d}</span></div></a>''' for h,img,k,t,n,d in POSTS)

marquee = "".join(f'<img src="{logo_src("", l)}" alt="{NOMS[l]}">' for l in LOGOS)

HTML = f'''<!doctype html>
<html lang="fr">
<head>
{head(R, TITLE, DESC, canonical=SITE + "/", extra=jsonld())}</head>
<body>

{header(R)}

<section class="hero hero-split">
  <div class="wrap hero-inner">
    <div class="hero-grid">
      <div>
        <h1>Le classement des meilleures <em>mutuelles senior</em></h1>
        <p>Quelle mutuelle choisir après 60 ans ? Nous comparons 11 mutuelles sur ce qu'il reste à payer sur une couronne, des lunettes et une aide auditive, sur le prix à 65 et 70 ans, sur le questionnaire de santé et sur l'agence.</p>
        <div class="btns">
          <a class="btn-pill" href="#comparatifs">Voir les comparatifs <span class="circ">{ARROW}</span></a>
          <a class="btn-link" href="#simulateur">Calculer mon reste à charge</a>
        </div>
      </div>
      <figure class="hero-figure">
        <div class="hero-portrait">
          <img src="assets/img/hero-portrait.jpg" alt="Une jeune retraitée sourit, les bras croisés" width="900" height="1200" fetchpriority="high">
          <figcaption class="hero-quote">
            <b>Des chiffres pris à la source</b>
            <span>Les garanties viennent du tableau contractuel, les tarifs d'un même profil de référence, et chaque pourcentage est converti en euros de reste à charge.</span>
          </figcaption>
        </div>
      </figure>
    </div>
  </div>
</section>

<section class="brands" id="assureurs">
  <div class="brands-head">Les mutuelles que nous suivons chaque trimestre</div>
  <div class="marquee"><div class="marquee-track" id="logoTrack">{marquee}</div></div>
</section>

<section class="featured" id="comparatifs">
  <div class="wrap">
    <div class="section-head">
      <div><h2>Le comparatif mutuelle du mois</h2></div>
      <a class="btn btn-ghost" href="#derniers">Tous les comparatifs</a>
    </div>
    <div class="feat-grid">
      <a class="feat-main" href="{FEAT["href"]}">
        <img src="assets/img/{FEAT["img"]}" alt="{FEAT["alt"]}" width="1300" height="860">
        <div class="feat-body">
          <span class="tag">{FEAT["tag"]}</span>
          <h2>{FEAT["h2"]}</h2>
          <p>{FEAT["p"]}</p>
          <span class="feat-meta">{FEAT["meta"]}</span>
        </div>
      </a>
      <div class="feat-side">{side}
      </div>
    </div>
  </div>
</section>

<section class="tool" id="outil">
  <div class="wrap">
    <div class="tool-card">
      <div class="tool-intro">
        <h2>Comparez deux mutuelles en un clic</h2>
        <p>Choisissez deux mutuelles, nous affichons leurs notes sur nos cinq critères, calculées à partir des tableaux de garanties convertis en euros et des tarifs relevés à trois âges.</p>
        <div class="selects">
          <div class="select"><select id="brandA" aria-label="Première mutuelle"></select></div>
          <span class="vs">VS</span>
          <div class="select"><select id="brandB" aria-label="Seconde mutuelle"></select></div>
        </div>
        <p class="tool-note">Notes sur 10, relevé de démonstration en formule intermédiaire pour un profil de référence. Les remboursements réels dépendent de la formule et du département.</p>
      </div>
      <div class="compare">
        <div class="cmp-head"><span>Critère</span><b id="nameA"></b><b id="nameB"></b></div>
        <div id="rows"></div>
        <div class="verdict"><b id="verdict"></b><span id="verdictSub"></span></div>
      </div>
    </div>
  </div>
</section>

<section class="tool" id="simulateur" style="padding-top:0">
  <div class="wrap">
    <div class="tool-card">
      <div class="tool-intro">
        <h2>Combien vous reste-t-il à payer ?</h2>
        <p>Le prix de l'acte, la base de remboursement de l'Assurance Maladie et le niveau de garantie de votre mutuelle. Nous calculons ce que rembourse la Sécurité sociale, ce que rembourse la mutuelle et ce qu'il vous reste à payer.</p>
        <div class="sim-grid">
          <div><label for="simPrix">Prix de l'acte (€)</label><input id="simPrix" type="number" value="550" min="0" step="10"></div>
          <div><label for="simBase">Base de remboursement (€)</label><input id="simBase" type="number" value="107.5" min="0" step="0.5"></div>
          <div><label for="simSecu">Taux Sécurité sociale (%)</label><input id="simSecu" type="number" value="60" min="0" max="100" step="5"></div>
        </div>
        <div class="sim-grid" style="grid-template-columns:1fr 1fr">
          <div><label for="simGar">Garantie mutuelle (% BR, Sécu comprise)</label><input id="simGar" type="number" value="300" min="100" max="600" step="25"></div>
          <div><label for="simForfait">Ou forfait mutuelle en euros (0 si aucun)</label><input id="simForfait" type="number" value="0" min="0" step="10"></div>
        </div>
        <p class="tool-note">Exemple pré-rempli : une couronne céramique à 550 €, base 107,50 €, remboursée 60 % par l'Assurance Maladie, mutuelle à 300 % BR. Hors participation forfaitaire et hors panier 100 % Santé.</p>
      </div>
      <div class="compare">
        <div class="sim-out">
          <div class="sim-card"><span>Rembourse la Sécurité sociale</span><b class="num" id="outSecu">–</b></div>
          <div class="sim-card"><span>Rembourse la mutuelle</span><b class="num" id="outMut">–</b></div>
          <div class="sim-card"><span>Total remboursé</span><b class="num" id="outTot">–</b></div>
        </div>
        <div class="sim-out" style="grid-template-columns:1fr">
          <div class="sim-card"><span>Ce qu'il vous reste à payer</span><b class="num" id="outReste">–</b></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cats" id="categories">
  <div class="wrap">
    <div class="section-head">
      <div><h2>Nos comparatifs par sujet</h2><p>La bonne mutuelle dépend de votre situation : la retraite, un soin lourd à prévoir, un statut d'agent public ou d'indépendant.</p></div>
    </div>
    <div class="grid4">{tiles}
    </div>
  </div>
</section>

<section class="ranking" id="classement">
  <div class="wrap rank-grid">
    <div class="rank-intro">
      <h2>Les mutuelles les mieux notées</h2>
      <p>Note globale sur 10, moyenne pondérée de nos cinq critères. Le classement bouge à chaque relevé de tarifs et à chaque mise à jour des tableaux de garanties.</p>
      <a class="btn btn-dark" href="#methode">Voir la méthode de notation</a>
    </div>
    <div class="rank-list">{rank}
    </div>
  </div>
</section>

<section class="posts" id="derniers">
  <div class="wrap">
    <div class="section-head">
      <div><h2>Derniers comparatifs publiés</h2></div>
      <a class="btn btn-ghost" href="mutuelle-senior/">Tous les comparatifs</a>
    </div>
    <div class="grid4">{posts}
    </div>
  </div>
</section>

<section class="method" id="methode">
  <div class="wrap">
    <div class="method-head">
      <h2>Comment nous comparons les mutuelles</h2>
      <p>Tout part de documents publics, vérifiables un par un : tableaux de garanties, conditions générales, bases de remboursement de l'Assurance Maladie et grilles tarifaires.</p>
    </div>
    <div class="steps">
      <div class="step"><span class="n">01</span><h3>Nous lisons le tableau de garanties</h3><p>Chaque ligne, dentaire, optique, audition, hospitalisation, dépassements d'honoraires, sur le document contractuel et non sur la page commerciale.</p></div>
      <div class="step"><span class="n">02</span><h3>Nous convertissons en euros</h3><p>Chaque pourcentage de base de remboursement devient un reste à charge en euros sur des actes courants, après la part de l'Assurance Maladie.</p></div>
      <div class="step"><span class="n">03</span><h3>Nous vérifions le service</h3><p>Présence d'une agence, conseiller nommé, tiers payant chez les opticiens et audioprothésistes, délai de remboursement constaté et conditions d'entrée lues dans les conditions générales.</p></div>
    </div>
    {DISCLOSURE}
  </div>
</section>

{newsletter()}

{footer(R)}

<script src="assets/js/site.js?v=1"></script>
<script>
(function(){{
  var contrats={json.dumps(CONTRATS, ensure_ascii=False)};
  var crits={json.dumps(CRITS, ensure_ascii=False)};
  var A=document.getElementById('brandA'),B=document.getElementById('brandB');
  Object.keys(contrats).forEach(function(n){{A.add(new Option(n,n));B.add(new Option(n,n));}});
  A.value="Mutuelle Prévifrance";B.value="Harmonie Mutuelle";
  function fmt(v){{return v.toFixed(1).replace('.',',');}}
  function render(){{
    var a=A.value,b=B.value,ra=contrats[a],rb=contrats[b],wins=0,rows='';
    document.getElementById('nameA').textContent=a;document.getElementById('nameB').textContent=b;
    crits.forEach(function(c,i){{
      var va=ra[i],vb=rb[i],wa=va>vb,wb=vb>va; if(i<4&&wa)wins++;
      rows+='<div class="cmp-row"><div class="crit">'+c[0]+'<small>'+c[1]+'</small></div>'
        +'<div class="bar'+(wa?' win':'')+'"><div class="track"><div class="fill" style="width:'+(va*10)+'%"></div></div><span class="val">'+fmt(va)+'</span></div>'
        +'<div class="bar'+(wb?' win':'')+'"><div class="track"><div class="fill" style="width:'+(vb*10)+'%"></div></div><span class="val">'+fmt(vb)+'</span></div></div>';
    }});
    document.getElementById('rows').innerHTML=rows;
    var v=document.getElementById('verdict'),s=document.getElementById('verdictSub');
    if(a===b){{v.textContent='Choisissez deux mutuelles différentes';s.textContent='';return;}}
    var lead=ra[4]>rb[4]?a:rb[4]>ra[4]?b:null;
    v.textContent=lead?lead+' l\\u2019emporte':'Égalité parfaite';
    s.textContent=lead?(lead===a?wins:4-wins)+' critères sur 4, note globale '+fmt(lead===a?ra[4]:rb[4])+' contre '+fmt(lead===a?rb[4]:ra[4]):'Même note globale sur nos relevés';
  }}
  A.addEventListener('change',render);B.addEventListener('change',render);render();
}})();
(function(){{
  var ids=['simPrix','simBase','simSecu','simGar','simForfait'],el={{}};
  ids.forEach(function(i){{el[i]=document.getElementById(i);}});
  if(!el.simPrix)return;
  var eur=new Intl.NumberFormat('fr-FR',{{style:'currency',currency:'EUR',maximumFractionDigits:2}});
  function calc(){{
    var prix=+el.simPrix.value||0,base=+el.simBase.value||0,ts=(+el.simSecu.value||0)/100,gar=(+el.simGar.value||0)/100,forfait=+el.simForfait.value||0;
    var secu=Math.min(prix,base*ts);
    var mut=forfait>0?forfait:Math.max(0,base*gar-secu);
    mut=Math.min(mut,Math.max(0,prix-secu));
    var tot=secu+mut, reste=Math.max(0,prix-tot);
    document.getElementById('outSecu').textContent=eur.format(secu);
    document.getElementById('outMut').textContent=eur.format(mut);
    document.getElementById('outTot').textContent=eur.format(tot);
    document.getElementById('outReste').textContent=eur.format(reste);
  }}
  ids.forEach(function(i){{el[i].addEventListener('input',calc);}});calc();
}})();
</script>
</body>
</html>
'''

if __name__ == "__main__":
    open("index.html", "w", encoding="utf-8").write(linkify(HTML, ""))
    print("ok index.html")
