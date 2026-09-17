# -*- coding: utf-8 -*-
"""Genere les 5 pages categorie a partir d'un template unique.
Usage : python3 build_categories.py  (depuis le dossier comparepargne)
"""
import os, json
from common import *
from linkify import linkify

from cats_data import CATS_DATA

def render(c):
    R = "../"
    subnav = "".join(f'''
    <a class="subcard" href="#articles"><img src="{R}assets/img/{ic}.svg" alt="" width="56" height="56" loading="lazy"><span>{lab}</span><i>{ARROW}</i></a>''' for lab, ic in c["subnav"])
    side = "".join(f'''
        <a class="side-item" href="#"><img src="{R}assets/img/{img}" alt="" width="96" height="80" loading="lazy"><div><span class="eyebrow">{k}</span><h3>{t}</h3><small>{m}</small></div></a>''' for img, k, t, m in c["side"])
    grid = "".join(f'''
      <a class="post big" href="#"><img src="{R}assets/img/{img}" alt="" width="800" height="560" loading="lazy"><div class="post-body"><span class="eyebrow">{k}</span><h3>{t}</h3><p class="excerpt">{ex}</p><span class="meta">{n} <i></i> {d}</span></div></a>''' for img, k, t, ex, n, d in c["grid"])
    rank = "".join(f'''
      <div class="rank-row"><span class="pos{" first" if i==0 else ""}">0{i+1}</span><img src="{logo_src(R, logo)}" alt="{alt}" width="120" height="33" loading="lazy"><div class="why"><b>{b}</b>{why}</div><div class="score"><b>{sc}</b><small>/10</small><span class="chip{"" if cls=="up" else " "+cls}">{chip}</span></div></div>''' for i, (logo, alt, b, why, sc, cls, chip) in enumerate(c["rank"]))
    faq = "".join(f'''
      <details{" open" if i==0 else ""}><summary>{q}</summary><p>{a}</p></details>''' for i, (q, a) in enumerate(c["faq"]))
    f = c["feat"]
    ld = [
     {"@context":"https://schema.org","@type":"CollectionPage","name":c["title"],"description":c["desc"],
      "url":f'{SITE}/{c["slug"]}/',"inLanguage":"fr-FR","isPartOf":{"@type":"WebSite","name":NOM,"url":SITE}},
     {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
       {"@type":"ListItem","position":1,"name":"Accueil","item":SITE},
       {"@type":"ListItem","position":2,"name":c["nom"],"item":f'{SITE}/{c["slug"]}/'}]},
     {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
       {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in c["faq"]]},
    ]
    jsonld = "".join('<script type="application/ld+json">'+json.dumps(d, ensure_ascii=False)+"</script>\n" for d in ld)
    return f'''<!doctype html>
<html lang="fr">
<head>
{head(R, c["title"], c["desc"], canonical=f'{SITE}/{c["slug"]}/', extra=jsonld)}</head>
<body>

{header(R, current=c["slug"])}

<section class="hero cat-hero">
  <img class="hero-bg" src="{R}assets/img/{c["hero"]}" alt="{c["hero_alt"]}" width="2000" height="900" fetchpriority="high">
  <div class="wrap hero-inner">
    <nav class="crumbs" aria-label="Fil d'Ariane"><a href="{R}">Accueil</a><i></i><span>{c["nom"]}</span></nav>
    <h1>{c["h1"]}</h1>
    <p>{c["intro"]}</p>
  </div>
</section>

<nav class="subnav" aria-label="Sous-catégories">
  <div class="wrap subcards">{subnav}
  </div>
</nav>

<section class="cat-featured" id="articles">
  <div class="wrap">
    <div class="section-head">
      <h2>{c["une_h2"]}</h2>
      <a class="btn btn-ghost" href="#classement">Voir le classement</a>
    </div>
    <div class="feat-grid">
      <a class="feat-main" href="#">
        <img src="{R}assets/img/{f["img"]}" alt="" width="800" height="560">
        <div class="feat-body">
          <span class="tag">{f["tag"]}</span>
          <h2>{f["h2"]}</h2>
          <p>{f["p"]}</p>
          <span class="feat-meta">{f["meta"]}</span>
        </div>
      </a>
      <div class="feat-side">{side}
      </div>
    </div>
  </div>
</section>

<section class="cat-grid">
  <div class="wrap">
    <div class="section-head">
      <h2>{c["grid_h2"]}</h2>
      <span style="font-size:13px;color:var(--muted)">Du plus récent au plus ancien</span>
    </div>
    <div class="grid3">{grid}
    </div>
    <div class="pager"><a class="on" href="#">1</a><a href="#">2</a><a href="#" aria-label="Page suivante">→</a></div>
  </div>
</section>

<section class="cat-rank" id="classement">
  <div class="wrap rank-grid">
    <div class="rank-intro">
      <h2>{c["rank_h2"]}</h2>
      <p>{c["rank_p"]}</p>
      <a class="btn btn-dark" href="{R}#methode">Voir la méthode de notation</a>
    </div>
    <div class="rank-list">{rank}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <div class="cta-card">
      <div><h2>{c["cta_h2"]}</h2><p>{c["cta_p"]}</p></div>
      <a class="btn btn-dark" href="{R}#outil">Comparer 2 contrats</a>
    </div>
  </div>
</section>

<section class="faq">
  <div class="wrap faq-head">
    <h2>{c["faq_h2"]}</h2>
    <div>{faq}
    </div>
  </div>
</section>

<section style="padding-bottom:20px"><div class="wrap">{DISCLOSURE}</div></section>

{newsletter(c["news_h2"])}

{footer(R)}

<script src="{R}assets/js/site.js?v=1"></script>
</body>
</html>
'''

if __name__ == "__main__":
    for c in CATS_DATA:
        os.makedirs(c["slug"], exist_ok=True)
        open(os.path.join(c["slug"], "index.html"), "w", encoding="utf-8").write(linkify(render(c), "../"))
        print("ok", c["slug"])
