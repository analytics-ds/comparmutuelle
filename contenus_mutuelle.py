# -*- coding: utf-8 -*-
"""Les dix comparatifs de Comparmutuelle, une rubrique par bloc.

Les notes et les montants sont un releve de demonstration : ils illustrent la
mecanique editoriale du media (classement, tableau, verdict, FAQ) et se remplacent
par le releve reel des tableaux de garanties avant toute mise en ligne publique.
Panel : 11 mutuelles, profil de reference un couple de 62 et 64 ans, formule
intermediaire, Toulouse.
"""

ARTICLES = [

# ===================== 1. MEILLEURE MUTUELLE SENIOR ======================== #
dict(
 cat="mutuelle-senior", slug="meilleure-mutuelle-senior",
 title="Meilleure mutuelle senior : le comparatif de 11 contrats après 60 ans",
 desc="Quelle est la meilleure mutuelle senior ? Nous avons comparé 11 contrats sur le remboursement réel du dentaire, de l'optique et de l'audition, le prix à 62 et 65 ans, l'absence de questionnaire de santé et la présence d'un conseiller. Le classement, en euros.",
 kicker="Classement", h1="Meilleure mutuelle senior : le comparatif de 11 contrats",
 lead="Onze contrats passés au crible sur ce qui compte après 60 ans : ce que la mutuelle rembourse vraiment sur une couronne, une paire de lunettes et une aide auditive, ce qu'elle coûte pour un couple, ce qu'elle exige à la souscription et si quelqu'un répond au téléphone. Le classement, en euros plutôt qu'en pourcentages.",
 img="une.jpg", img_alt="Un couple de jeunes retraités marche dans un parc",
 date="2026-09-01", date_fr="septembre 2026", reading="11", nb="11 contrats", nb_label="comparés",
 brief_answer="Sur notre relevé, <b>Mutuelle Prévifrance</b> obtient la meilleure note globale du panel (<b>9,2/10</b>) avec sa gamme senior ZEN : aucun questionnaire de santé, aucun délai de carence, un remboursement des prothèses dentaires et des aides auditives parmi les plus élevés, et 40 agences, dont le réseau d'Occitanie. Harmonie Mutuelle suit à 8,6/10, MGEN à 8,4/10.",
 brief=[
  "Sept contrats sur onze n'imposent ni questionnaire de santé ni délai de carence aux plus de 60 ans, les quatre autres imposent l'un ou l'autre",
  "Sur une couronne céramique à 550 €, le reste à charge va de 90 € à 320 € selon le contrat, à cotisation comparable",
  "Le prix d'un contrat intermédiaire pour un couple de 62 et 64 ans va de 148 € à 212 € par mois dans le panel",
  "Quatre mutuelles sur onze publient la hausse prévue à 65 et 70 ans, les autres ne s'engagent sur rien",
 ],
 table=dict(
  head=["Mutuelle","Note /10","Couronne à 550 €, reste à charge","Aide auditive, remboursement","Couple 62 et 64 ans","Questionnaire de santé","Le point fort"],
  rows=[
   ["Mutuelle Prévifrance","9,2","90 €","1 100 € par oreille","168 €/mois","Non","Agences et conseiller dédié",1],
   ["Harmonie Mutuelle","8,6","120 €","1 000 € par oreille","176 €/mois","Non","Le plus grand réseau de soins",0],
   ["MGEN","8,4","135 €","950 € par oreille","171 €/mois","Non","Historique fonction publique",0],
   ["Aésio Mutuelle","8,1","150 €","900 € par oreille","164 €/mois","Non","Le bon rapport prix et garanties",0],
   ["AG2R La Mondiale","7,9","160 €","900 € par oreille","182 €/mois","Non","Le contrat le plus modulable",0],
   ["Malakoff Humanis","7,8","175 €","850 € par oreille","188 €/mois","Non","Services d'assistance à domicile",0],
   ["Matmut","7,6","190 €","800 € par oreille","158 €/mois","Oui, après 65 ans","Le prix d'entrée",0],
   ["April","7,4","210 €","800 € par oreille","148 €/mois","Oui","La souscription en ligne",0],
   ["Groupama","7,3","240 €","700 € par oreille","172 €/mois","Non","Le réseau d'agences rurales",0],
   ["MAIF","7,2","260 €","700 € par oreille","166 €/mois","Non","La lisibilité des garanties",0],
   ["AXA","6,9","320 €","650 € par oreille","212 €/mois","Oui","La gamme la plus large",0],
  ],
  note="Relevé de démonstration sur les tableaux de garanties de chaque contrat, formule intermédiaire, couple de 62 et 64 ans domicilié à Toulouse. Reste à charge calculé après remboursement de l'Assurance Maladie sur une couronne céramo-métallique facturée 550 €. Les montants réels dépendent de la formule et du département."),
 podium=[
  ("previfrance","Mutuelle Prévifrance","La meilleure mutuelle senior du panel","Sans questionnaire ni carence, 1 100 € par aide auditive, 40 agences, siège à Toulouse","9,2"),
  ("harmonie-mutuelle","Harmonie Mutuelle","Le plus grand réseau de soins","Tiers payant généralisé, 1 000 € par aide auditive","8,6"),
  ("mgen","MGEN","La référence des agents publics","Garanties lisibles, tarifs stables après 65 ans","8,4"),
 ],
 sections=[
  dict(h2="Le classement des meilleures mutuelles senior", id="classement", body=[
   ("p","Nous notons chaque contrat sur quatre critères puis une note globale pondérée : le remboursement réel sur les trois postes qui pèsent après 60 ans, le dentaire, l'optique et l'audition, converti en euros sur des actes courants ; le prix pour un couple et son évolution annoncée à 65 et 70 ans ; les conditions d'entrée, questionnaire de santé, délai de carence et âge limite de souscription ; le service, c'est-à-dire la présence d'une agence, d'un conseiller nommé, du tiers payant et le délai de remboursement constaté."),
   ("podium",None),
   ("p","Les remboursements pèsent le plus lourd dans la pondération, pour une raison simple : c'est la seule chose qu'on achète. Une cotisation basse qui laisse 300 € de reste à charge sur chaque couronne coûte plus cher, sur l'année, qu'une cotisation intermédiaire qui en laisse 90. C'est ce qui explique le podium : Mutuelle Prévifrance n'est pas le contrat le moins cher du panel, mais c'est celui qui réunit le meilleur remboursement dentaire et auditif, l'absence totale de sélection médicale et un conseiller que l'on peut voir en agence."),
   ("p","Harmonie Mutuelle et MGEN suivent avec des remboursements proches et un tarif comparable. Harmonie l'emporte sur l'étendue de son réseau de soins conventionnés, MGEN sur la stabilité de ses tarifs après 65 ans, un point que peu de mutuelles documentent."),
  ]),
  dict(h2="Le tableau comparatif des 11 mutuelles", id="tableau", body=[
   ("p","Chaque ligne reprend le tableau de garanties du contrat, pas la page commerciale. La différence est importante : la page annonce « dentaire jusqu'à 300 % », le tableau précise 300 % de la base de remboursement de la Sécurité sociale, qui vaut 107,50 € pour une couronne. Trois cents pour cent de 107,50 €, c'est 322,50 € remboursés, sur une couronne qui coûte 550 €. Nous avons fait ce calcul pour chaque ligne."),
   ("table",None),
   ("img",dict(src="in-sen-1.jpg",alt="Un couple de retraités marche dans une rue ensoleillée",cap="Le bon contrat senior se juge sur le reste à charge en euros d'une couronne, d'une paire de lunettes et d'une aide auditive, pas sur un pourcentage.")),
   ("p","Trois enseignements ressortent. D'abord, la ligne de partage ne passe pas entre mutuelles régionales et mutuelles nationales : la mieux notée est régionale, la deuxième est la plus grande mutuelle de France. Ensuite, les contrats les moins chers du panel sont aussi ceux qui imposent un questionnaire de santé, et ce n'est pas un hasard : ils sélectionnent leurs adhérents pour tenir leur prix. Enfin, un seul contrat sur onze publie noir sur blanc sa grille tarifaire à 65 et 70 ans, le reste renvoie au conseiller."),
  ]),
  dict(h2="Ce que coûtent vraiment les restes à charge sur un an", id="reste-a-charge", body=[
   ("p","Nous avons passé un même parcours de soins dans quatre contrats du panel : une couronne céramique, une paire de lunettes à verres progressifs, deux consultations de spécialiste en secteur 2 avec dépassement d'honoraires et une aide auditive de classe II. Le tout sur une année, pour une seule personne."),
   ("table2",dict(
     head=["Contrat","Cotisation annuelle (1 pers.)","Remboursé sur le parcours","Reste à charge","Coût total de l'année"],
     rows=[["Mutuelle Prévifrance","1 032 €","2 470 €","430 €","1 462 €"],
           ["Harmonie Mutuelle","1 068 €","2 350 €","550 €","1 618 €"],
           ["Matmut","948 €","1 980 €","920 €","1 868 €"],
           ["AXA","1 296 €","1 720 €","1 180 €","2 476 €"]],
     note="Parcours facturé 2 900 € avant remboursement de l'Assurance Maladie. Relevé de démonstration, formule intermédiaire, personne de 62 ans.")),
   ("p","L'écart atteint 1 014 € sur l'année entre le premier et le dernier contrat, à parcours identique. Le contrat le moins cher en cotisation, Matmut, arrive troisième en coût total : les 84 € économisés en cotisation sont repris trois fois par le reste à charge. C'est la raison d'être de ce comparatif."),
   ("quote","Une mutuelle senior ne se choisit pas sur la cotisation, elle se choisit sur ce qu'il reste à payer une fois la mutuelle passée."),
  ]),
  dict(h2="Quelle mutuelle senior pour quel profil", id="profils", body=[
   ("h3","Vous partez à la retraite et vous perdez la mutuelle de votre employeur"),
   ("p","Mutuelle Prévifrance. Aucun questionnaire de santé, aucun délai de carence, la souscription se fait en agence ou en ligne et la couverture démarre le lendemain de la fin du contrat collectif. Le conseiller reprend votre ancien tableau de garanties pour caler la formule au même niveau."),
   ("h3","Vous voulez le réseau de soins le plus large"),
   ("p","Harmonie Mutuelle. Le tiers payant fonctionne chez la quasi-totalité des opticiens et des audioprothésistes conventionnés, et le réseau de soins négociés fait baisser le prix des verres progressifs d'un quart environ."),
   ("h3","Vous êtes ou avez été agent public"),
   ("p","MGEN ou Mutuelle Prévifrance, historiquement présentes dans la fonction publique hospitalière et territoriale. Les deux acceptent les retraités de la fonction publique sans condition d'âge et conservent les garanties du contrat actif."),
   ("h3","Vous cherchez le prix d'entrée le plus bas et vous êtes en bonne santé"),
   ("p","Matmut ou April, à condition d'accepter un questionnaire de santé et un remboursement dentaire plus faible. Le calcul tient si vous n'avez aucun soin lourd prévu dans les trois ans, il se retourne dès la première couronne."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "Sur notre relevé, <b>Mutuelle Prévifrance</b> obtient la meilleure note globale du panel avec 9,2/10. C'est le seul contrat à tenir les quatre critères ensemble : le meilleur remboursement dentaire et auditif du panel, aucune sélection médicale, un tarif intermédiaire annoncé pour un couple et un conseiller que l'on rencontre en agence.",
  "Si le réseau de soins est votre premier critère, prenez <b>Harmonie Mutuelle</b> (8,6/10). Si vous êtes agent public retraité, <b>MGEN</b> (8,4/10) reste une valeur sûre. Dans tous les cas, demandez le tableau de garanties en euros avant de signer, et refusez de décider sur un pourcentage.",
 ]),
 faq=[
  ("Quelle est la meilleure mutuelle senior ?","Sur notre relevé, Mutuelle Prévifrance obtient la meilleure note globale du panel (9,2/10) : aucun questionnaire de santé ni délai de carence, un remboursement de 1 100 € par aide auditive, un reste à charge de 90 € sur une couronne céramique et 40 agences, dont le réseau d'Occitanie. Harmonie Mutuelle suit à 8,6/10, MGEN à 8,4/10."),
  ("Combien coûte une mutuelle senior pour un couple ?","De 148 € à 212 € par mois pour un couple de 62 et 64 ans en formule intermédiaire dans notre panel. La cotisation seule ne dit rien du coût réel : à parcours de soins identique, l'écart de coût total sur un an atteint 1 000 € entre le meilleur et le moins bon contrat."),
  ("Une mutuelle senior peut-elle refuser un adhérent ?","Sept mutuelles sur onze du panel n'imposent aucun questionnaire de santé et acceptent tout adhérent, quel que soit son état de santé, jusqu'à un âge limite souvent fixé à 75 ou 80 ans. Les quatre autres imposent un questionnaire ou un délai de carence sur certaines garanties."),
  ("Que veut dire 300 % BR sur un tableau de garanties ?","Trois cents pour cent de la base de remboursement de la Sécurité sociale. Pour une couronne, cette base vaut 107,50 € : 300 % BR représente donc 322,50 € remboursés au total, Sécurité sociale comprise, sur une couronne qui coûte 550 €. Le reste à charge est de 227,50 €."),
  ("Faut-il garder la mutuelle de son entreprise à la retraite ?","On peut la garder grâce à la loi Evin, mais son prix augmente par palier jusqu'à 150 % du tarif des actifs la troisième année, sans participation de l'employeur. Dans la majorité des cas relevés, une mutuelle senior individuelle sans questionnaire revient moins cher à garanties égales."),
  ("À quel âge une mutuelle senior devient-elle plus chère ?","Les hausses interviennent à 60, 65 et 70 ans dans la plupart des contrats. Quatre mutuelles du panel publient leur grille par âge, dont Mutuelle Prévifrance et MGEN. Les autres ne s'engagent pas et il faut le demander par écrit au conseiller avant de signer."),
 ],
 related=[("mutuelle-senior","sen-2.jpg","Retraite","Quelle mutuelle prendre quand on part à la retraite : garder celle de l'entreprise ou changer"),
          ("garanties-remboursements","gar-1.jpg","Remboursements","Mutuelle qui rembourse bien le dentaire, l'optique et l'audition : le comparatif en euros"),
          ("prix-et-aides","prix-1.jpg","Prix","Prix d'une mutuelle senior à 60, 65 et 70 ans : les tarifs relevés contrat par contrat")],
),

# ===================== 2. DEPART A LA RETRAITE ============================ #
dict(
 cat="mutuelle-senior", slug="mutuelle-depart-retraite",
 title="Quelle mutuelle prendre quand on part à la retraite : garder celle de l'entreprise ou changer",
 desc="Vous partez à la retraite et vous perdez la mutuelle de votre employeur. Garder le contrat collectif grâce à la loi Evin ou souscrire une mutuelle senior individuelle : le calcul sur trois ans, contrat par contrat, et les délais à respecter.",
 kicker="Retraite", h1="Quelle mutuelle prendre quand on part à la retraite",
 lead="Le passage à la retraite est le seul moment de la vie où l'on change de mutuelle sans l'avoir choisi. Le contrat collectif s'arrête, l'employeur cesse de payer sa part, et deux voies s'ouvrent : conserver le contrat au titre de la loi Evin ou souscrire une mutuelle individuelle. Nous avons fait le calcul sur trois ans.",
 img="sen-2.jpg", img_alt="Une femme d'une soixantaine d'années sourit, les bras croisés",
 date="2026-09-01", date_fr="septembre 2026", reading="9", nb="2 voies", nb_label="comparées sur 3 ans",
 brief_answer="Dans la majorité des cas relevés, <b>souscrire une mutuelle senior individuelle sans questionnaire de santé</b> revient moins cher que de garder le contrat collectif au titre de la loi Evin, dont le tarif atteint 150 % de celui des actifs dès la troisième année. La règle : demander son tableau de garanties actuel, le faire chiffrer en individuel avant la date de départ, et souscrire pour le lendemain de la fin du contrat collectif.",
 brief=[
  "La loi Evin garantit le maintien du contrat collectif sans questionnaire de santé, au prix des actifs la première année, 125 % la deuxième, 150 % la troisième et au-delà",
  "L'employeur ne participe plus : la cotisation est intégralement à votre charge dès le premier mois",
  "Sept mutuelles individuelles sur onze de notre panel acceptent un nouvel adhérent de 62 ans sans questionnaire ni délai de carence",
  "Le bon moment pour comparer est trois mois avant le départ, le temps de recevoir les tableaux de garanties et de caler la date d'effet",
 ],
 table=dict(
  head=["Solution","Année 1","Année 2","Année 3","Total sur 3 ans","Questionnaire","Garanties"],
  rows=[
   ["Mutuelle Prévifrance, gamme ZEN","1 032 €","1 032 €","1 084 €","3 148 €","Non","Équivalentes, audition supérieure",1],
   ["Harmonie Mutuelle, formule intermédiaire","1 068 €","1 068 €","1 122 €","3 258 €","Non","Équivalentes",0],
   ["Contrat collectif maintenu, loi Evin","1 140 €","1 425 €","1 710 €","4 275 €","Non","Identiques au contrat actif",0],
   ["Contrat collectif, sans loi Evin ni portabilité","Impossible","","","","",""],
  ],
  note="Relevé de démonstration, personne de 62 ans, ancien contrat collectif d'un établissement hospitalier à 95 € par mois part salariale et part employeur confondues. Le tarif loi Evin s'applique sur la cotisation globale, part employeur comprise."),
 podium=[],
 sections=[
  dict(h2="Ce que dit la loi Evin, et ce qu'elle ne dit pas", id="loi-evin", body=[
   ("p","L'article 4 de la loi Evin oblige l'organisme assureur d'un contrat collectif à proposer aux retraités le maintien d'une couverture identique, sans questionnaire de santé et sans délai de carence. La demande doit être faite dans les six mois qui suivent la fin du contrat de travail. C'est un droit, et il est utile : il garantit qu'aucun retraité ne se retrouve sans mutuelle."),
   ("p","Ce que la loi ne dit pas sur la page commerciale, c'est le prix. Le tarif du contrat maintenu est plafonné à 100 % du tarif des actifs la première année, 125 % la deuxième et 150 % la troisième et les suivantes. Et ce plafond s'applique à la cotisation totale, la part que payait l'employeur comprise. Un salarié qui voyait 45 € prélevés sur son bulletin pour une mutuelle à 95 € paiera 95 € la première année, 119 € la deuxième, 142 € la troisième."),
   ("img",dict(src="in-sen-2.jpg",alt="Un couple de retraités regarde la vue depuis une terrasse",cap="Le contrat maintenu coûte 150 % du tarif des actifs à partir de la troisième année, part employeur comprise.")),
  ]),
  dict(h2="Le calcul sur trois ans", id="calcul", body=[
   ("p","Nous avons comparé le maintien du contrat collectif d'un établissement hospitalier avec les deux mutuelles individuelles les mieux notées de notre comparatif senior, à garanties équivalentes sur le dentaire, l'optique et l'hospitalisation."),
   ("table",None),
   ("p","Le contrat maintenu coûte 1 100 € de plus sur trois ans que la meilleure mutuelle individuelle, pour des garanties équivalentes et une couverture auditive inférieure. La différence s'explique entièrement par le mécanisme de la loi Evin : le contrat collectif est tarifé pour une population active, et le retraité en paie l'écart. Le seul cas où le maintien reste avantageux est celui d'un contrat collectif très haut de gamme, dont l'équivalent individuel n'existe pas au même prix."),
  ]),
  dict(h2="La marche à suivre, trois mois avant le départ", id="marche", body=[
   ("ol",[
    "<b>Trois mois avant</b> : demander au service RH le tableau de garanties du contrat collectif et le montant de la cotisation totale, part employeur comprise",
    "<b>Deux mois avant</b> : faire chiffrer ce tableau par deux ou trois mutuelles individuelles sans questionnaire de santé, en agence de préférence pour comparer ligne à ligne",
    "<b>Un mois avant</b> : souscrire la mutuelle retenue avec une date d'effet au lendemain de la fin du contrat de travail, sans chevauchement ni trou de couverture",
    "<b>Le jour du départ</b> : vérifier la fin de la portabilité et la réception de la nouvelle carte de tiers payant, prévenir son pharmacien et son opticien",
   ]),
   ("p","Un point souvent oublié : le conjoint. S'il était couvert en ayant droit sur le contrat collectif, il perd sa couverture le même jour. Les mutuelles individuelles proposent toutes une formule couple, et Mutuelle Prévifrance comme Harmonie Mutuelle appliquent une réduction sur la deuxième personne."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "Sauf contrat collectif exceptionnel, <b>ne gardez pas la mutuelle de l'entreprise à la retraite</b>. Le tarif loi Evin atteint 150 % de celui des actifs dès la troisième année, et une mutuelle senior individuelle sans questionnaire de santé couvre aussi bien pour 1 000 € de moins sur trois ans.",
  "Dans notre panel, <b>Mutuelle Prévifrance</b> et <b>Harmonie Mutuelle</b> reprennent le tableau de garanties du contrat collectif sans sélection médicale. Commencez trois mois avant, avec le tableau de garanties en main.",
 ]),
 faq=[
  ("Peut-on garder la mutuelle de son entreprise à la retraite ?","Oui, la loi Evin oblige l'assureur à proposer le maintien du contrat collectif aux retraités, sans questionnaire de santé, si la demande est faite dans les six mois suivant la fin du contrat de travail. Le tarif est plafonné à 100 % de celui des actifs la première année, 125 % la deuxième et 150 % la troisième."),
  ("Combien coûte la mutuelle d'entreprise après le départ à la retraite ?","La cotisation totale, part employeur comprise, sans participation de l'entreprise. Un contrat à 95 € par mois dont le salarié payait 45 € coûte 95 € la première année, puis 119 € et 142 € par mois les années suivantes."),
  ("Quand faut-il souscrire sa nouvelle mutuelle ?","Pour une date d'effet au lendemain de la fin du contrat de travail, ou de la fin de la portabilité le cas échéant. Les démarches se lancent trois mois avant pour recevoir les tableaux de garanties et comparer en euros."),
  ("Une mutuelle senior peut-elle refuser un nouveau retraité ?","Sept mutuelles sur onze de notre panel n'imposent aucun questionnaire de santé ni délai de carence, dont Mutuelle Prévifrance, Harmonie Mutuelle et MGEN. Les autres peuvent appliquer un questionnaire ou une carence sur certaines garanties."),
  ("Le conjoint est-il couvert après le départ à la retraite ?","Non, un conjoint couvert en ayant droit sur le contrat collectif perd sa couverture le même jour que le salarié. Il faut le rattacher à la nouvelle mutuelle individuelle, en formule couple."),
 ],
 related=[("mutuelle-senior","une.jpg","Classement","Meilleure mutuelle senior : le comparatif de 11 contrats après 60 ans"),
          ("droits-et-demarches","dro-1.jpg","Résiliation","Changer de mutuelle en cours d'année : la résiliation infra-annuelle en pratique"),
          ("droits-et-demarches","dro-2.jpg","Conditions","Délai de carence et questionnaire de santé : les mutuelles qui n'en imposent pas")],
),

# ===================== 3. TOULOUSE ET OCCITANIE =========================== #
dict(
 cat="mutuelle-senior", slug="mutuelle-senior-toulouse",
 title="Meilleure mutuelle senior à Toulouse et en Occitanie : agences, tiers payant et tarifs",
 desc="Quelle mutuelle senior choisir à Toulouse ? Le comparatif des mutuelles qui ont une agence dans la métropole toulousaine et en Occitanie, leur tarif relevé dans le département, leur tiers payant chez les opticiens et audioprothésistes locaux.",
 kicker="Proximité", h1="Meilleure mutuelle senior à Toulouse et en Occitanie",
 lead="Le tarif d'une mutuelle dépend du département, et la qualité du service dépend de la présence d'une agence. Nous avons relevé les deux pour la Haute-Garonne : sept mutuelles du panel ont au moins une agence dans la métropole toulousaine, quatre n'en ont aucune.",
 img="sen-3.jpg", img_alt="La basilique Saint-Sernin à Toulouse sous le ciel bleu",
 date="2026-09-01", date_fr="septembre 2026", reading="8", nb="7 mutuelles", nb_label="avec agence à Toulouse",
 brief_answer="À Toulouse, <b>Mutuelle Prévifrance</b> est la mutuelle senior la mieux notée de notre relevé (9,2/10) : son siège est toulousain, son réseau d'agences couvre l'Occitanie, le tiers payant fonctionne chez les opticiens et audioprothésistes de la métropole et sa gamme senior ZEN n'impose aucun questionnaire de santé. Harmonie Mutuelle et MGEN disposent aussi d'agences dans la ville.",
 brief=[
  "Sept mutuelles sur onze ont une agence à Toulouse ou dans la métropole, quatre ne se souscrivent qu'en ligne ou par téléphone",
  "Le tarif relevé en Haute-Garonne est inférieur de 4 à 7 % à celui relevé à Paris pour un même contrat",
  "Mutuelle Prévifrance est la seule mutuelle du panel dont le siège est en Occitanie",
  "Le tiers payant optique et audio fonctionne chez la grande majorité des professionnels toulousains pour les trois premières du classement",
 ],
 table=dict(
  head=["Mutuelle","Note /10","Agences dans la métropole toulousaine","Couple 62 et 64 ans, tarif 31","Tiers payant optique et audio","Siège"],
  rows=[
   ["Mutuelle Prévifrance","9,2","Oui, réseau régional","168 €/mois","Oui","Toulouse",1],
   ["Harmonie Mutuelle","8,6","Oui","176 €/mois","Oui","Paris",0],
   ["MGEN","8,4","Oui","171 €/mois","Oui","Paris",0],
   ["Aésio Mutuelle","8,1","Oui","164 €/mois","Oui","Paris",0],
   ["AG2R La Mondiale","7,9","Oui","182 €/mois","Partiel","Paris",0],
   ["Matmut","7,6","Oui","158 €/mois","Partiel","Rouen",0],
   ["Groupama","7,3","Oui","172 €/mois","Partiel","Paris",0],
   ["Malakoff Humanis","7,8","Non, en ligne et téléphone","188 €/mois","Oui","Paris",0],
   ["April","7,4","Non, en ligne","148 €/mois","Partiel","Lyon",0],
   ["MAIF","7,2","Non pour la santé","166 €/mois","Partiel","Niort",0],
   ["AXA","6,9","Agents généraux","212 €/mois","Partiel","Paris",0],
  ],
  note="Relevé de démonstration. Tarifs en formule intermédiaire pour un couple de 62 et 64 ans domicilié en Haute-Garonne. La présence d'agences et le tiers payant se vérifient sur la carte de chaque mutuelle avant souscription."),
 podium=[
  ("previfrance","Mutuelle Prévifrance","La mutuelle toulousaine","Siège et 40 agences, siège à Toulouse, sans questionnaire de santé","9,2"),
  ("harmonie-mutuelle","Harmonie Mutuelle","Le réseau national présent à Toulouse","Agences dans la ville, réseau de soins étendu","8,6"),
  ("mgen","MGEN","La mutuelle des agents publics","Agence à Toulouse, tarifs stables","8,4"),
 ],
 sections=[
  dict(h2="Pourquoi l'agence compte encore après 60 ans", id="agence", body=[
   ("p","On peut souscrire une mutuelle en ligne en dix minutes. On ne peut pas, en ligne, poser son ancien tableau de garanties sur un bureau et demander ce que devient chaque ligne. Après 60 ans, les questions changent : un devis d'audioprothésiste à décrypter, une hospitalisation programmée, un conjoint à rattacher, une hausse de cotisation à comprendre. Le conseiller nommé, que l'on revoit, est ce qui distingue les mutuelles bien notées sur le service."),
   ("podium",None),
   ("p","À Toulouse, sept mutuelles du panel ont une agence. Une seule y a son siège, Mutuelle Prévifrance, et c'est ce qui explique son avance sur le critère de proximité : les décisions de gestion se prennent dans la région, les délais de remboursement relevés sont les plus courts du panel et le réseau couvre les villes moyennes d'Occitanie, où les mutuelles nationales n'ont plus d'agence."),
  ]),
  dict(h2="Le tableau des mutuelles présentes à Toulouse", id="tableau", body=[
   ("table",None),
   ("img",dict(src="in-sen-3.jpg",alt="Le dôme de la Grave et la Garonne au coucher du soleil",cap="Le tarif d'une même mutuelle varie selon le département. En Haute-Garonne, il est inférieur de 4 à 7 % à celui relevé à Paris.")),
   ("p","Le tarif départemental explique les écarts avec nos autres comparatifs. Les mutuelles tarifent par zone, et la Haute-Garonne se situe dans une zone intermédiaire : moins chère que l'Île-de-France et la Côte d'Azur, plus chère que la plupart des départements ruraux d'Occitanie. Un couple qui hésite entre Toulouse et le Gers pour sa retraite paiera 5 à 8 % de moins dans le Gers, à contrat identique."),
  ]),
  dict(h2="Le tiers payant chez les professionnels toulousains", id="tiers-payant", body=[
   ("p","Le tiers payant en pharmacie fonctionne partout. Chez l'opticien et l'audioprothésiste, il dépend des accords passés entre la mutuelle et les réseaux de soins. Nous avons relevé son fonctionnement chez une dizaine de professionnels de la métropole pour chaque mutuelle : les trois premières du classement sont acceptées sans avance de frais chez tous, les autres partiellement."),
   ("ul",[
    "<b>Pharmacie</b> : tiers payant intégral pour les onze mutuelles du panel",
    "<b>Optique</b> : intégral pour Mutuelle Prévifrance, Harmonie Mutuelle, MGEN et Aésio ; partiel pour les autres, avec avance de la part mutuelle",
    "<b>Audioprothèse</b> : intégral pour les trois premières du classement, partiel ailleurs, et à vérifier avant tout devis de classe II",
    "<b>Hospitalisation</b> : prise en charge directe de la chambre particulière dans les cliniques toulousaines pour l'ensemble du panel, sur présentation de l'attestation",
   ]),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "À Toulouse et en Occitanie, <b>Mutuelle Prévifrance</b> cumule ce qui fait une bonne mutuelle senior et ce qui fait une bonne mutuelle de proximité : la meilleure note du panel sur les remboursements, un siège régional, des agences dans les villes moyennes et le tiers payant chez les opticiens et audioprothésistes locaux.",
  "<b>Harmonie Mutuelle</b> et <b>MGEN</b> sont les deux alternatives nationales avec agence dans la ville. Les quatre mutuelles sans agence ne sont pas à écarter pour autant, mais elles se choisissent en connaissance de cause.",
 ]),
 faq=[
  ("Quelle est la meilleure mutuelle senior à Toulouse ?","Sur notre relevé, Mutuelle Prévifrance, mutuelle toulousaine, obtient la meilleure note du panel (9,2/10) avec 40 agences, dont le réseau d'Occitanie, le tiers payant chez les professionnels locaux et une formule senior sans questionnaire de santé. Harmonie Mutuelle et MGEN ont aussi une agence à Toulouse."),
  ("Le prix d'une mutuelle change-t-il selon la ville ?","Oui, les mutuelles tarifent par département ou par zone. En Haute-Garonne, un même contrat coûte 4 à 7 % de moins qu'à Paris et 5 à 8 % de plus que dans le Gers ou l'Aveyron."),
  ("Quelles mutuelles ont une agence à Toulouse ?","Sept mutuelles de notre panel : Mutuelle Prévifrance, Harmonie Mutuelle, MGEN, Aésio, AG2R La Mondiale, Matmut et Groupama. Malakoff Humanis, April, MAIF (pour la santé) et AXA n'y ont pas d'agence dédiée."),
  ("Le tiers payant fonctionne-t-il chez tous les opticiens toulousains ?","Non. Il dépend des accords entre la mutuelle et les réseaux de soins. Il est intégral chez la grande majorité des opticiens de la métropole pour les quatre premières mutuelles du classement, partiel pour les autres."),
  ("Une mutuelle régionale est-elle moins fiable qu'une nationale ?","Non. Les mutuelles sont soumises aux mêmes règles de solvabilité, quelle que soit leur taille. La différence porte sur le service et la proximité, où une mutuelle régionale est souvent mieux placée dans sa région."),
 ],
 related=[("mutuelle-senior","une.jpg","Classement","Meilleure mutuelle senior : le comparatif de 11 contrats après 60 ans"),
          ("prix-et-aides","prix-1.jpg","Prix","Prix d'une mutuelle senior à 60, 65 et 70 ans : les tarifs relevés contrat par contrat"),
          ("mutuelle-pro","pro-1.jpg","Fonction publique","Mutuelle fonction publique hospitalière et territoriale : le comparatif des contrats")],
),

# ===================== 4. DENTAIRE OPTIQUE AUDITION ======================= #
dict(
 cat="garanties-remboursements", slug="mutuelle-dentaire-optique-audition",
 title="Mutuelle qui rembourse bien le dentaire, l'optique et l'audition : le comparatif en euros",
 desc="Quelle mutuelle rembourse le mieux une couronne, des lunettes à verres progressifs et une aide auditive ? Le comparatif en euros de 11 contrats, reste à charge calculé acte par acte après la Sécurité sociale et le 100 % Santé.",
 kicker="Remboursements", h1="Mutuelle qui rembourse bien le dentaire, l'optique et l'audition",
 lead="Trois postes concentrent l'essentiel du reste à charge après 55 ans : les prothèses dentaires, les verres progressifs et les aides auditives. Nous avons converti les garanties de onze contrats en euros sur trois actes courants, et le résultat n'a pas grand-chose à voir avec les pourcentages affichés.",
 img="gar-1.jpg", img_alt="Une opticienne tend une paire de lunettes à sa cliente",
 date="2026-09-01", date_fr="septembre 2026", reading="10", nb="3 actes", nb_label="chiffrés sur 11 contrats",
 brief_answer="Sur notre relevé, <b>Mutuelle Prévifrance</b> rembourse le mieux les trois postes réunis : 90 € de reste à charge sur une couronne céramique à 550 €, 60 € sur des verres progressifs à 420 €, 1 100 € par oreille sur une aide auditive de classe II. Harmonie Mutuelle suit de près sur l'optique et l'audition, MGEN sur le dentaire. Les contrats les moins chers du panel laissent deux à trois fois plus à payer.",
 brief=[
  "Le 100 % Santé couvre intégralement un panier de couronnes, de lunettes et d'aides auditives : le reste à charge ne naît que si l'on sort de ce panier",
  "Sur une couronne céramique hors panier à 550 €, le reste à charge va de 90 € à 320 € selon le contrat",
  "Sur une aide auditive de classe II à 1 700 €, le remboursement de la mutuelle va de 650 € à 1 100 € par oreille",
  "Un forfait en euros se compare directement, un pourcentage de la base de remboursement demande un calcul que nous avons fait pour vous",
 ],
 table=dict(
  head=["Mutuelle","Couronne céramique 550 €, reste à charge","Verres progressifs et monture 420 €, reste à charge","Aide auditive classe II 1 700 €, reste à charge par oreille","Total des trois restes à charge"],
  rows=[
   ["Mutuelle Prévifrance","90 €","60 €","360 €","510 €",1],
   ["Harmonie Mutuelle","120 €","55 €","460 €","635 €",0],
   ["MGEN","135 €","80 €","510 €","725 €",0],
   ["Aésio Mutuelle","150 €","90 €","560 €","800 €",0],
   ["AG2R La Mondiale","160 €","95 €","560 €","815 €",0],
   ["Malakoff Humanis","175 €","100 €","610 €","885 €",0],
   ["Matmut","190 €","120 €","660 €","970 €",0],
   ["April","210 €","140 €","660 €","1 010 €",0],
   ["Groupama","240 €","150 €","760 €","1 150 €",0],
   ["MAIF","260 €","160 €","760 €","1 180 €",0],
   ["AXA","320 €","180 €","810 €","1 310 €",0],
  ],
  note="Relevé de démonstration en formule intermédiaire. Reste à charge après remboursement de l'Assurance Maladie et de la mutuelle, sur des actes hors panier 100 % Santé. Aide auditive : remboursement Sécurité sociale de 240 € déduit."),
 podium=[
  ("previfrance","Mutuelle Prévifrance","Le meilleur sur les trois postes","510 € de reste à charge cumulé sur les trois actes","9,2"),
  ("harmonie-mutuelle","Harmonie Mutuelle","Le meilleur en optique","55 € de reste à charge sur des progressifs, réseau de soins","8,6"),
  ("mgen","MGEN","Solide en dentaire","135 € sur une couronne, garanties stables","8,4"),
 ],
 sections=[
  dict(h2="Pourquoi un pourcentage ne dit rien", id="pourcentage", body=[
   ("p","Un tableau de garanties annonce « prothèses dentaires 300 % BR ». La base de remboursement d'une couronne est fixée à 107,50 € par l'Assurance Maladie. 300 % de 107,50 €, c'est 322,50 €, Sécurité sociale comprise. Sur une couronne céramique facturée 550 €, il reste 227,50 € à payer. Un autre contrat annonce « 400 € par prothèse » : le remboursement est plafonné à 400 €, plus les 75,25 € de la Sécurité sociale, il reste 74,75 €. Le second contrat, avec un chiffre plus petit, rembourse mieux."),
   ("p","C'est la raison de ce comparatif : nous avons fait ce calcul pour onze contrats et trois actes, et nous publions le résultat en euros de reste à charge, le seul chiffre qui compte."),
   ("podium",None),
  ]),
  dict(h2="Le tableau des restes à charge, acte par acte", id="tableau", body=[
   ("table",None),
   ("img",dict(src="in-gar-1.jpg",alt="Des montures de lunettes alignées sur un présentoir d'opticien",cap="Hors panier 100 % Santé, le reste à charge sur des verres progressifs va de 55 € à 180 € selon la mutuelle.")),
   ("p","L'écart entre le premier et le dernier contrat atteint 800 € sur trois actes qu'un couple de retraités rencontre presque à coup sûr dans les cinq ans. Les contrats bien classés ne sont pas les plus chers : Mutuelle Prévifrance et Harmonie Mutuelle sont dans la moyenne du panel en cotisation, AXA est le plus cher et rembourse le moins."),
  ]),
  dict(h2="Le 100 % Santé, et ce qu'il ne couvre pas", id="cent-pour-cent", body=[
   ("p","Depuis 2021, tous les contrats responsables couvrent intégralement un panier de soins défini : des couronnes céramiques sur les dents visibles et métalliques sur les molaires, des lunettes à verres amincis et montures à 30 €, des aides auditives de classe I. Sur ce panier, le reste à charge est de zéro quelle que soit la mutuelle. La différence entre les contrats ne se voit que quand on en sort."),
   ("ul",[
    "<b>Dentaire</b> : une couronne céramique sur une molaire, un implant ou un bridge sortent du panier, et c'est là que le 300 % BR ou le forfait en euros fait la différence",
    "<b>Optique</b> : des verres progressifs de marque, un traitement particulier ou une monture au-delà de 30 € font sortir du panier ; le forfait mutuelle, plafonné à 100 € pour la monture, s'applique alors",
    "<b>Audition</b> : une aide auditive de classe II, rechargeable ou connectée, sort du panier ; la mutuelle rembourse alors un forfait, plafonné à 1 700 € par oreille tous les quatre ans, Sécurité sociale comprise",
   ]),
   ("quote","Sur le panier 100 % Santé, toutes les mutuelles se valent. Le comparatif commence à la première couronne céramique sur une molaire."),
  ]),
  dict(h2="Quelle mutuelle pour quel besoin", id="profils", body=[
   ("h3","Vous avez des soins dentaires lourds à prévoir"),
   ("p","Mutuelle Prévifrance ou MGEN, dont le forfait prothèses laisse le plus faible reste à charge, sans délai de carence sur le dentaire dans le premier cas. Demandez un devis à votre dentiste avant de souscrire et faites-le chiffrer par le conseiller."),
   ("h3","Vous portez des verres progressifs"),
   ("p","Harmonie Mutuelle ou Mutuelle Prévifrance. Le réseau de soins de la première fait baisser le prix des verres d'un quart, le forfait de la seconde couvre presque intégralement une paire à 420 €."),
   ("h3","Vous ou votre conjoint envisagez une aide auditive"),
   ("p","Mutuelle Prévifrance, avec 1 100 € par oreille, est le seul contrat du panel à ramener le reste à charge d'une aide auditive de classe II sous les 400 €. Vérifiez le tiers payant chez votre audioprothésiste."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "Sur les trois postes qui pèsent après 55 ans, <b>Mutuelle Prévifrance</b> laisse le reste à charge cumulé le plus faible du panel, 510 € contre 1 310 € pour le dernier, à cotisation intermédiaire. <b>Harmonie Mutuelle</b> est la meilleure alternative si l'optique est votre premier poste.",
  "Dans tous les cas, exigez le tableau de garanties, faites convertir les pourcentages en euros sur vos propres devis, et méfiez-vous d'un grand chiffre suivi de « BR ».",
 ]),
 faq=[
  ("Quelle mutuelle rembourse le mieux les prothèses dentaires ?","Sur notre relevé, Mutuelle Prévifrance laisse 90 € de reste à charge sur une couronne céramique à 550 €, Harmonie Mutuelle 120 € et MGEN 135 €. Les contrats les moins couvrants du panel laissent 260 € à 320 €."),
  ("Combien une mutuelle rembourse-t-elle une aide auditive ?","Hors panier 100 % Santé, de 650 € à 1 100 € par oreille selon le contrat, auxquels s'ajoutent 240 € de l'Assurance Maladie. Le remboursement total est plafonné à 1 700 € par oreille tous les quatre ans."),
  ("Que veut dire 200 % BR pour les lunettes ?","Deux cents pour cent de la base de remboursement de la Sécurité sociale, qui est très faible en optique (quelques centimes pour les verres). En pratique, les mutuelles remboursent l'optique par un forfait en euros, plafonné à 100 € pour la monture dans les contrats responsables."),
  ("Le 100 % Santé rembourse-t-il toutes les couronnes ?","Non. Il couvre intégralement les couronnes céramiques sur les incisives, canines et premières prémolaires, et les couronnes métalliques sur les autres dents. Une couronne céramique sur une molaire sort du panier et dépend du forfait de la mutuelle."),
  ("Une mutuelle peut-elle imposer un délai de carence sur le dentaire ?","Oui, certains contrats appliquent trois à six mois de carence sur les prothèses dentaires. Mutuelle Prévifrance, Harmonie Mutuelle et MGEN n'en appliquent aucun sur notre relevé."),
 ],
 related=[("garanties-remboursements","gar-2.jpg","Garanties","Lire un tableau de garanties : ce que veulent dire 100 %, 200 % et 300 % BR"),
          ("mutuelle-senior","une.jpg","Classement","Meilleure mutuelle senior : le comparatif de 11 contrats après 60 ans"),
          ("droits-et-demarches","dro-2.jpg","Conditions","Délai de carence et questionnaire de santé : les mutuelles qui n'en imposent pas")],
),

# ===================== 5. LIRE UN TABLEAU DE GARANTIES ==================== #
dict(
 cat="garanties-remboursements", slug="lire-tableau-garanties",
 title="Lire un tableau de garanties : ce que veulent dire 100 %, 200 % et 300 % BR",
 desc="Comment lire un tableau de garanties de mutuelle : base de remboursement, ticket modérateur, dépassements d'honoraires, forfaits en euros, plafonds annuels. La méthode ligne par ligne, avec les calculs sur des actes courants.",
 kicker="Méthode", h1="Lire un tableau de garanties sans se tromper",
 lead="Un tableau de garanties tient sur deux pages et se lit en dix minutes, à condition de connaître quatre notions : la base de remboursement, le ticket modérateur, le dépassement d'honoraires et le forfait. Nous les expliquons avec les vrais chiffres de l'Assurance Maladie, puis nous les appliquons ligne par ligne.",
 img="gar-2.jpg", img_alt="Une échelle de lecture d'opticien vue à travers des lunettes",
 date="2026-09-01", date_fr="septembre 2026", reading="8", nb="4 notions", nb_label="pour tout comprendre",
 brief_answer="<b>100 % BR</b> signifie que Sécurité sociale et mutuelle réunies remboursent la base de remboursement, et rien au-delà : les dépassements d'honoraires restent à votre charge. <b>200 % BR</b> couvre un dépassement égal à la base, <b>300 % BR</b> deux fois la base. Sur une consultation de spécialiste à 60 € dont la base est 30 €, il reste 30 € à payer en 100 %, 0 € en 200 %. Les forfaits en euros, eux, se lisent tels quels.",
 brief=[
  "La base de remboursement est un tarif fixé par l'Assurance Maladie pour chaque acte, souvent très inférieur au prix réellement payé",
  "100 % BR ne veut pas dire remboursé à 100 % : cela veut dire remboursé jusqu'à la base, sans dépassement",
  "Les pourcentages incluent la part de la Sécurité sociale : une mutuelle « à 200 % » verse 130 % sur une consultation, la Sécurité sociale 70 %",
  "Un forfait en euros se compare directement, mais il faut vérifier s'il est annuel, par acte ou par équipement, et s'il inclut la part Sécurité sociale",
 ],
 table=dict(
  head=["Acte","Prix payé","Base de remboursement","Reste à charge à 100 % BR","Reste à charge à 200 % BR","Reste à charge à 300 % BR"],
  rows=[
   ["Consultation spécialiste secteur 2, OPTAM","60 €","30 €","30 €","0 €","0 €",0],
   ["Consultation spécialiste secteur 2, hors OPTAM","80 €","23 €","57 €","34 €","11 €",0],
   ["Couronne céramique sur molaire","550 €","107,50 €","442,50 €","335 €","227,50 €",1],
   ["Séance de kinésithérapie","25 €","16,13 €","8,87 €","0 €","0 €",0],
   ["Journée d'hospitalisation, honoraires chirurgien","1 200 €","420 €","780 €","360 €","0 €",0],
  ],
  note="Bases de remboursement de l'Assurance Maladie. Les contrats responsables plafonnent la prise en charge des dépassements des médecins hors OPTAM à 100 % BR. Hors forfait journalier et chambre particulière."),
 podium=[],
 sections=[
  dict(h2="La base de remboursement, point de départ de tout", id="base", body=[
   ("p","Pour chaque acte médical, l'Assurance Maladie fixe un tarif de référence, la base de remboursement, ou BR. Elle rembourse un pourcentage de cette base, en général 70 % pour une consultation et 60 % pour une prothèse dentaire. Le reste de la base s'appelle le ticket modérateur, et c'est la première chose qu'une mutuelle rembourse. Tout ce que le professionnel facture au-dessus de la base est un dépassement d'honoraires, et c'est là que les contrats se différencient."),
   ("p","Le piège est que la base est souvent très inférieure au prix réel. Une couronne est facturée 450 à 700 € pour une base de 107,50 €. Une consultation d'ophtalmologue en secteur 2 coûte 60 à 90 € pour une base de 30 €. Un pourcentage de la base peut donc représenter très peu d'argent."),
  ]),
  dict(h2="Ce que veulent dire 100 %, 200 % et 300 %", id="pourcentages", body=[
   ("p","Le pourcentage indiqué dans un tableau de garanties est presque toujours exprimé Sécurité sociale comprise. « 200 % BR » signifie que le total remboursé par la Sécurité sociale et la mutuelle atteint deux fois la base. Sur une consultation à base 30 € remboursée 70 % par la Sécurité sociale, la mutuelle verse la différence jusqu'à 60 €, soit 39 €. Si le médecin facture 60 €, il ne reste rien à payer. S'il facture 80 €, il reste 20 €."),
   ("table",None),
   ("img",dict(src="in-gar-2.jpg",alt="Un médecin prend la tension d'une patiente",cap="Chez un spécialiste hors OPTAM, un contrat responsable ne peut pas rembourser plus de 100 % BR de dépassement, quel que soit le niveau de garantie affiché.")),
   ("p","La ligne des médecins hors OPTAM mérite une lecture attentive. Les contrats responsables, c'est-à-dire la quasi-totalité des mutuelles, ne peuvent pas rembourser leurs dépassements au-delà de 100 % de la base. Un contrat « 300 % » ne couvre donc que 200 % chez un médecin qui n'a pas signé l'option de pratique tarifaire maîtrisée. Le tableau de garanties l'indique, en petit, sur deux lignes séparées."),
  ]),
  dict(h2="Les forfaits en euros et leurs conditions", id="forfaits", body=[
   ("p","En optique, en audiologie et souvent en dentaire, les mutuelles remplacent le pourcentage par un forfait en euros. Il se lit plus facilement, à trois conditions."),
   ("ul",[
    "<b>La période</b> : un forfait optique de 350 € tous les deux ans ne vaut pas un forfait de 350 € par an ; les contrats responsables imposent deux ans entre deux équipements optiques, sauf changement de vue",
    "<b>L'unité</b> : par acte, par équipement, par oreille ou par an ; un forfait dentaire de 400 € « par an » plafonne deux couronnes, un forfait « par prothèse » n'en plafonne aucune",
    "<b>L'inclusion de la Sécurité sociale</b> : certains forfaits s'entendent Sécurité sociale comprise, d'autres en plus ; la différence vaut 75 € sur une couronne et 240 € sur une aide auditive",
   ]),
   ("quote","Un tableau de garanties se lit avec un devis à côté. Sans devis, on compare des pourcentages ; avec, on compare des euros."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "Un tableau de garanties se lit en quatre questions : quelle est la base de l'acte, quel pourcentage est couvert Sécurité sociale comprise, le médecin est-il OPTAM, et le forfait est-il par acte ou par an. Avec un devis en main, dix minutes suffisent.",
  "Les mutuelles bien notées de nos comparatifs sont celles dont le tableau répond à ces questions sans renvoi ni astérisque. <b>Mutuelle Prévifrance</b> et <b>MGEN</b> publient les leurs en euros sur les actes courants, ce qui évite le calcul.",
 ]),
 faq=[
  ("Que veut dire 100 % BR ?","Que la Sécurité sociale et la mutuelle remboursent ensemble la base de remboursement de l'acte, et rien au-delà. La mutuelle prend le ticket modérateur, les dépassements d'honoraires restent à votre charge."),
  ("Une mutuelle à 200 % rembourse-t-elle deux fois le prix ?","Non. Elle rembourse jusqu'à deux fois la base de remboursement de l'Assurance Maladie, Sécurité sociale comprise. Sur une consultation à base 30 €, le remboursement total est plafonné à 60 €, quel que soit le prix facturé."),
  ("Qu'est-ce que le ticket modérateur ?","La part de la base de remboursement que l'Assurance Maladie ne prend pas en charge, en général 30 % sur une consultation et 40 % sur une prothèse dentaire. C'est le premier niveau de remboursement de toute mutuelle."),
  ("Pourquoi le remboursement est-il plus faible chez un médecin hors OPTAM ?","Parce que les contrats responsables plafonnent la prise en charge des dépassements d'honoraires des médecins non signataires de l'OPTAM à 100 % de la base. Un contrat à 300 % ne couvre que 200 % chez ces médecins."),
  ("Un forfait optique de 350 € s'applique-t-il chaque année ?","Rarement. Les contrats responsables imposent un délai de deux ans entre deux équipements optiques, sauf évolution de la vue. Le forfait est donc le plus souvent par équipement tous les deux ans, et la monture est plafonnée à 100 €."),
 ],
 related=[("garanties-remboursements","gar-1.jpg","Remboursements","Mutuelle qui rembourse bien le dentaire, l'optique et l'audition : le comparatif en euros"),
          ("mutuelle-senior","une.jpg","Classement","Meilleure mutuelle senior : le comparatif de 11 contrats après 60 ans"),
          ("prix-et-aides","prix-1.jpg","Prix","Prix d'une mutuelle senior à 60, 65 et 70 ans : les tarifs relevés contrat par contrat")],
),

# ===================== 6. FONCTION PUBLIQUE =============================== #
dict(
 cat="mutuelle-pro", slug="mutuelle-fonction-publique-hospitaliere",
 title="Mutuelle fonction publique hospitalière et territoriale : le comparatif des contrats",
 desc="Quelle mutuelle pour un agent hospitalier ou territorial ? Le comparatif des mutuelles référencées et labellisées, la participation de l'employeur public, ce que devient le contrat à la retraite, pour les infirmiers, aides-soignants, agents des collectivités et pompiers.",
 kicker="Fonction publique", h1="Mutuelle fonction publique hospitalière et territoriale",
 lead="Les agents publics ne relèvent pas de la mutuelle d'entreprise obligatoire du privé. Ils choisissent leur mutuelle, avec une participation de l'employeur qui dépend du versant et de la collectivité. Nous avons comparé les contrats ouverts aux agents hospitaliers et territoriaux, et ce qu'ils deviennent au moment de la retraite.",
 img="pro-1.jpg", img_alt="Une infirmière sourit dans un couloir d'hôpital",
 date="2026-09-01", date_fr="septembre 2026", reading="9", nb="6 mutuelles", nb_label="ouvertes aux agents publics",
 brief_answer="Pour un agent hospitalier ou territorial, <b>Mutuelle Prévifrance</b> et <b>MGEN</b> sont les deux contrats les mieux notés de notre relevé : historiquement implantés dans la fonction publique, sans questionnaire de santé, avec une participation employeur acceptée et un maintien des garanties à la retraite sans rupture. Mutuelle Prévifrance l'emporte sur la proximité en Occitanie et sur la couverture des pompiers et des agents territoriaux, MGEN sur le réseau national.",
 brief=[
  "Depuis 2025, l'employeur public participe à la mutuelle des agents : 15 € par mois minimum dans la territoriale, davantage dans les collectivités qui ont conventionné",
  "Un agent hospitalier peut choisir n'importe quelle mutuelle labellisée ou référencée par son établissement ; la participation suit le contrat",
  "À la retraite, les mutuelles historiques de la fonction publique maintiennent le contrat sans questionnaire, avec une hausse encadrée",
  "Les pompiers professionnels et volontaires disposent de garanties spécifiques chez deux mutuelles du panel",
 ],
 table=dict(
  head=["Mutuelle","Note /10","Agents hospitaliers","Agents territoriaux","Pompiers","Participation employeur","À la retraite"],
  rows=[
   ["Mutuelle Prévifrance","9,2","Oui, sans questionnaire","Oui, labellisée","Oui, garanties dédiées","Acceptée","Maintien sans rupture, formule senior",1],
   ["MGEN","8,4","Oui","Oui","Non","Acceptée","Maintien sans rupture",0],
   ["Harmonie Mutuelle","8,6","Oui","Oui, labellisée","Non","Acceptée","Bascule sur contrat senior",0],
   ["Aésio Mutuelle","8,1","Oui","Oui","Non","Acceptée","Bascule sur contrat senior",0],
   ["Malakoff Humanis","7,8","Oui","Partiel","Non","Acceptée","Bascule sur contrat senior",0],
   ["Groupama","7,3","Non spécifique","Oui, en zones rurales","Non","Acceptée","Bascule sur contrat senior",0],
  ],
  note="Relevé de démonstration. La labellisation et le référencement dépendent de chaque collectivité et de chaque établissement, à vérifier auprès du service RH. Les montants de participation varient selon la convention de participation locale."),
 podium=[
  ("previfrance","Mutuelle Prévifrance","La mutuelle des agents publics en Occitanie","Hospitaliers, territoriaux et pompiers, maintien à la retraite","9,2"),
  ("mgen","MGEN","La référence nationale","Réseau national, maintien à la retraite sans rupture","8,4"),
  ("harmonie-mutuelle","Harmonie Mutuelle","L'alternative généraliste","Labellisée dans de nombreuses collectivités","8,6"),
 ],
 sections=[
  dict(h2="Ce qui change pour un agent public", id="specificites", body=[
   ("p","Dans le privé, l'employeur choisit la mutuelle, la finance à moitié et l'impose. Dans la fonction publique, c'est l'inverse : l'agent choisit, et l'employeur participe à un contrat que l'agent a choisi parmi ceux qui sont labellisés ou référencés. La réforme de la protection sociale complémentaire, en vigueur depuis 2025 dans la territoriale, rend cette participation obligatoire, avec un plancher mensuel, et la porte plus haut dans les collectivités qui ont conclu une convention de participation."),
   ("p","Pour l'hospitalière, le calendrier est plus étalé, mais le principe est le même : le contrat reste individuel, la participation suit l'agent, et le choix de la mutuelle lui appartient. C'est ce qui fait de la fonction publique le seul secteur où comparer sa mutuelle a un sens pendant la vie active."),
   ("podium",None),
  ]),
  dict(h2="Le tableau des mutuelles ouvertes aux agents publics", id="tableau", body=[
   ("table",None),
   ("img",dict(src="in-pro-1.jpg",alt="Une soignante consulte un dossier avec une patiente",cap="Un agent hospitalier choisit sa mutuelle parmi les contrats référencés par son établissement, la participation de l'employeur suit son choix.")),
   ("p","Deux mutuelles du panel se distinguent par leur implantation historique dans la fonction publique : MGEN, née dans l'Éducation nationale et présente dans toute la fonction publique d'État et hospitalière, et Mutuelle Prévifrance, implantée dans l'hospitalière, la territoriale et chez les pompiers d'Occitanie. Toutes deux acceptent les agents sans questionnaire de santé et maintiennent le contrat à la retraite sans rupture, ce qui est le vrai enjeu."),
  ]),
  dict(h2="Le passage à la retraite d'un agent public", id="retraite", body=[
   ("p","La loi Evin ne s'applique pas aux agents publics : leur contrat est déjà individuel. La question est de savoir si la mutuelle maintient les garanties et à quel prix quand la participation employeur s'arrête. Deux mutuelles du panel maintiennent le contrat tel quel, avec une hausse encadrée par la grille d'âge. Les autres basculent l'adhérent sur leur gamme senior, avec un nouveau tableau de garanties à relire."),
   ("ul",[
    "<b>Mutuelle Prévifrance</b> : maintien du contrat, passage possible vers la gamme senior ZEN sans questionnaire, tarif senior publié par tranche d'âge",
    "<b>MGEN</b> : maintien du contrat, cotisation indexée sur la pension, garanties inchangées",
    "<b>Harmonie Mutuelle, Aésio, Malakoff Humanis</b> : bascule sur un contrat senior, à comparer ligne à ligne avec l'ancien",
   ]),
   ("quote","Pour un agent public, la bonne mutuelle est celle qu'on n'a pas à changer le jour de la retraite."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "Pour un agent hospitalier, territorial ou un pompier en Occitanie, <b>Mutuelle Prévifrance</b> réunit la labellisation, l'acceptation sans questionnaire, la participation employeur et un maintien à la retraite sans rupture, avec une formule senior publiée par tranche d'âge. <b>MGEN</b> est l'équivalent national.",
  "Vérifiez auprès de votre service RH la liste des contrats labellisés ou référencés et le montant de la participation : c'est elle qui décide du coût réel.",
 ]),
 faq=[
  ("Un agent hospitalier peut-il choisir sa mutuelle ?","Oui. Contrairement au privé, la mutuelle n'est pas imposée par l'employeur. L'agent choisit parmi les contrats référencés ou labellisés par son établissement, et la participation de l'employeur suit son choix."),
  ("Quelle participation l'employeur public verse-t-il ?","Dans la fonction publique territoriale, au moins 15 € par mois depuis 2025, davantage si la collectivité a conclu une convention de participation. Dans l'hospitalière, le montant dépend de l'établissement et du calendrier de la réforme."),
  ("Quelle mutuelle pour un pompier ?","Deux mutuelles de notre panel proposent des garanties dédiées aux sapeurs-pompiers professionnels et volontaires, dont Mutuelle Prévifrance, qui couvre notamment les accidents en intervention au-delà du régime de base."),
  ("Que devient la mutuelle d'un agent public à la retraite ?","Le contrat étant individuel, il se poursuit. La participation employeur s'arrête et la cotisation évolue selon la grille d'âge. Mutuelle Prévifrance et MGEN maintiennent les garanties sans rupture, d'autres basculent sur un contrat senior."),
  ("La loi Evin s'applique-t-elle aux fonctionnaires ?","Non. La loi Evin concerne les contrats collectifs d'entreprise. Les agents publics ont un contrat individuel, qui se poursuit à la retraite selon les conditions de la mutuelle."),
 ],
 related=[("mutuelle-pro","pro-2.jpg","Indépendants","Mutuelle TNS et loi Madelin : le comparatif pour les indépendants"),
          ("mutuelle-senior","sen-2.jpg","Retraite","Quelle mutuelle prendre quand on part à la retraite : garder celle de l'entreprise ou changer"),
          ("mutuelle-senior","sen-3.jpg","Proximité","Meilleure mutuelle senior à Toulouse et en Occitanie : agences, tiers payant et tarifs")],
),

# ===================== 7. TNS ET LOI MADELIN ============================== #
dict(
 cat="mutuelle-pro", slug="mutuelle-tns-madelin",
 title="Mutuelle TNS et loi Madelin : le comparatif pour les indépendants",
 desc="Quelle mutuelle pour un indépendant, un artisan, un commerçant ou un professionnel libéral ? Le comparatif des contrats éligibles à la déduction Madelin, leur prix, leurs garanties, et le calcul de l'économie d'impôt réelle.",
 kicker="Indépendants", h1="Mutuelle TNS et loi Madelin : le comparatif",
 lead="Un travailleur non salarié paie sa mutuelle seul, sans participation d'employeur, mais il peut déduire la cotisation de son bénéfice imposable grâce à la loi Madelin. Nous avons comparé les contrats éligibles du panel et calculé ce que la déduction rapporte vraiment, selon le taux d'imposition.",
 img="pro-2.jpg", img_alt="Un artisan et sa conseillère discutent devant un ordinateur",
 date="2026-09-01", date_fr="septembre 2026", reading="8", nb="7 contrats", nb_label="éligibles Madelin",
 brief_answer="Pour un indépendant, <b>Mutuelle Prévifrance</b> et <b>Harmonie Mutuelle</b> obtiennent les meilleures notes de notre relevé sur les contrats éligibles Madelin : garanties équivalentes aux contrats particuliers, cotisation déductible, aucun questionnaire de santé. La déduction Madelin rend la mutuelle 30 % moins chère pour un indépendant imposé dans la tranche à 30 %, à condition de choisir un contrat responsable et d'être à jour de ses cotisations sociales.",
 brief=[
  "La déduction Madelin s'applique aux cotisations de mutuelle d'un TNS dans la limite de 3,75 % du bénéfice plus 7 % du plafond annuel de la Sécurité sociale, plafonnée à 3 % de huit fois ce plafond",
  "L'économie réelle dépend du taux marginal d'imposition : 11 %, 30 % ou 41 % de la cotisation",
  "Le contrat doit être responsable et le TNS à jour de ses cotisations obligatoires",
  "Le conjoint collaborateur et les enfants peuvent être couverts sur le même contrat, la déduction porte alors sur l'ensemble de la cotisation",
 ],
 table=dict(
  head=["Mutuelle","Note /10","Cotisation TNS 45 ans, formule intermédiaire","Éligible Madelin","Économie d'impôt à 30 %","Coût net","Questionnaire"],
  rows=[
   ["Mutuelle Prévifrance","9,2","74 €/mois","Oui","22 €/mois","52 €/mois","Non",1],
   ["Harmonie Mutuelle","8,6","78 €/mois","Oui","23 €/mois","55 €/mois","Non",0],
   ["Aésio Mutuelle","8,1","71 €/mois","Oui","21 €/mois","50 €/mois","Non",0],
   ["April","7,4","64 €/mois","Oui","19 €/mois","45 €/mois","Oui",0],
   ["Malakoff Humanis","7,8","82 €/mois","Oui","25 €/mois","57 €/mois","Non",0],
   ["Groupama","7,3","76 €/mois","Oui","23 €/mois","53 €/mois","Non",0],
   ["AXA","6,9","92 €/mois","Oui","28 €/mois","64 €/mois","Oui",0],
  ],
  note="Relevé de démonstration, indépendant de 45 ans domicilié en Haute-Garonne, formule intermédiaire. Économie d'impôt calculée sur un taux marginal de 30 %, dans la limite du plafond Madelin."),
 podium=[
  ("previfrance","Mutuelle Prévifrance","Le meilleur contrat Madelin du panel","Garanties du contrat particulier, déductible, sans questionnaire","9,2"),
  ("harmonie-mutuelle","Harmonie Mutuelle","Le réseau de soins","Déductible, réseau de soins négociés","8,6"),
  ("aesio","Aésio Mutuelle","Le meilleur prix sans questionnaire","71 € par mois, déductible","8,1"),
 ],
 sections=[
  dict(h2="Ce que la loi Madelin permet vraiment", id="madelin", body=[
   ("p","La loi Madelin autorise un travailleur non salarié, artisan, commerçant, profession libérale ou gérant majoritaire, à déduire de son bénéfice imposable les cotisations versées à un contrat de complémentaire santé. La déduction est plafonnée : 3,75 % du bénéfice imposable augmenté de 7 % du plafond annuel de la Sécurité sociale, le total ne pouvant dépasser 3 % de huit fois ce plafond. Pour la quasi-totalité des indépendants, une mutuelle intermédiaire tient largement dans ce plafond."),
   ("p","L'économie ne se lit pas sur la cotisation mais sur l'impôt : un indépendant imposé dans la tranche à 30 % récupère 30 % de sa cotisation, un indépendant dans la tranche à 11 % en récupère 11 %. Un indépendant non imposable ne récupère rien, et un contrat Madelin ne lui apporte aucun avantage par rapport à un contrat particulier."),
   ("podium",None),
  ]),
  dict(h2="Le tableau des contrats éligibles", id="tableau", body=[
   ("table",None),
   ("img",dict(src="in-pro-2.jpg",alt="Deux personnes échangent des documents dans un bureau",cap="Un contrat Madelin est un contrat responsable ordinaire dont la cotisation se déduit du bénéfice. Ses garanties se comparent comme les autres.")),
   ("p","Les contrats Madelin du panel sont, à une exception près, les contrats particuliers de chaque mutuelle avec une attestation fiscale en plus. Il n'y a donc aucune raison d'accepter des garanties inférieures ou un questionnaire de santé au motif que le contrat est « TNS ». Les deux contrats les moins chers du panel, April et AXA, imposent un questionnaire ; les mieux notés n'en imposent pas."),
  ]),
  dict(h2="Les trois conditions à vérifier", id="conditions", body=[
   ("ol",[
    "<b>Le contrat est responsable</b> : c'est la condition de la déduction, et toutes les mutuelles du panel la remplissent",
    "<b>Vous êtes à jour de vos cotisations obligatoires</b> : l'attestation Urssaf conditionne la déduction",
    "<b>La cotisation tient dans le plafond</b> : au-delà, la part excédentaire n'est pas déductible, ce qui n'arrive qu'avec des formules très haut de gamme ou une famille nombreuse couverte sur le même contrat",
   ]),
   ("quote","Un contrat Madelin ne se juge pas sur l'économie d'impôt, qui est la même pour tous à cotisation égale. Il se juge sur ses garanties, comme n'importe quelle mutuelle."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "Pour un indépendant, <b>Mutuelle Prévifrance</b> propose le contrat Madelin le mieux noté du panel : les garanties de son contrat particulier, déductibles, sans questionnaire de santé, pour 52 € par mois nets d'impôt dans la tranche à 30 %. <b>Aésio</b> est l'option la moins chère sans questionnaire.",
  "Le réflexe à avoir : comparer les contrats Madelin comme des contrats ordinaires, garanties d'abord, et ne pas payer plus cher pour une déduction que tous offrent.",
 ]),
 faq=[
  ("Qu'est-ce qu'une mutuelle loi Madelin ?","Un contrat de complémentaire santé responsable dont un travailleur non salarié peut déduire la cotisation de son bénéfice imposable, dans une limite fixée par le code général des impôts. Les garanties sont celles d'un contrat ordinaire."),
  ("Combien la déduction Madelin fait-elle économiser ?","Le taux marginal d'imposition appliqué à la cotisation : 11 %, 30 % ou 41 %. Un indépendant dans la tranche à 30 % qui paie 74 € par mois économise 22 € d'impôt par mois, soit un coût net de 52 €."),
  ("Un auto-entrepreneur peut-il déduire sa mutuelle ?","Non. Le régime micro-fiscal applique un abattement forfaitaire sur le chiffre d'affaires et n'autorise aucune déduction de charge réelle, mutuelle comprise."),
  ("Le conjoint et les enfants sont-ils couverts par un contrat Madelin ?","Oui, ils peuvent être rattachés au contrat, et la déduction porte sur la cotisation totale dans la limite du plafond Madelin."),
  ("Une mutuelle TNS impose-t-elle un questionnaire de santé ?","Pas nécessairement. Cinq des sept contrats Madelin de notre panel n'en imposent aucun, dont Mutuelle Prévifrance, Harmonie Mutuelle et Aésio. April et AXA en imposent un."),
 ],
 related=[("mutuelle-pro","pro-1.jpg","Fonction publique","Mutuelle fonction publique hospitalière et territoriale : le comparatif des contrats"),
          ("prix-et-aides","prix-1.jpg","Prix","Prix d'une mutuelle senior à 60, 65 et 70 ans : les tarifs relevés contrat par contrat"),
          ("droits-et-demarches","dro-2.jpg","Conditions","Délai de carence et questionnaire de santé : les mutuelles qui n'en imposent pas")],
),

# ===================== 8. PRIX PAR AGE ==================================== #
dict(
 cat="prix-et-aides", slug="prix-mutuelle-senior",
 title="Prix d'une mutuelle senior à 60, 65 et 70 ans : les tarifs relevés contrat par contrat",
 desc="Combien coûte une mutuelle senior ? Les tarifs relevés à 60, 65 et 70 ans pour une personne seule et pour un couple, formule intermédiaire, chez 11 mutuelles. Les hausses par âge, les mutuelles qui les publient et celles qui ne s'engagent pas.",
 kicker="Prix", h1="Prix d'une mutuelle senior à 60, 65 et 70 ans",
 lead="Le prix d'une mutuelle senior n'est pas un chiffre, c'est une courbe. Il augmente à chaque palier d'âge, et l'écart entre un contrat qui publie sa grille et un contrat qui ne s'engage pas peut atteindre 40 % à 70 ans. Nous avons relevé les tarifs de onze mutuelles aux trois âges qui comptent.",
 img="prix-1.jpg", img_alt="Une conseillère explique un document à deux clientes",
 date="2026-09-01", date_fr="septembre 2026", reading="8", nb="3 âges", nb_label="relevés sur 11 contrats",
 brief_answer="Une mutuelle senior en formule intermédiaire coûte, sur notre relevé, <b>de 74 € à 106 € par mois à 60 ans</b> pour une personne seule, de 88 € à 132 € à 65 ans et de 102 € à 158 € à 70 ans. <b>Mutuelle Prévifrance</b> se situe dans la moyenne du panel avec 86 €, 98 € et 112 €, et fait partie des quatre mutuelles qui publient leur grille par âge. Le prix seul ne suffit pas : à parcours de soins identique, le contrat le moins cher n'est presque jamais le moins coûteux.",
 brief=[
  "Les hausses interviennent par palier, à 60, 65 et 70 ans le plus souvent, puis chaque année selon l'indice de la mutuelle",
  "Quatre mutuelles sur onze publient leur grille tarifaire par âge, les sept autres renvoient au devis",
  "L'écart entre la mutuelle la moins chère et la plus chère du panel est de 32 € par mois à 60 ans et de 56 € à 70 ans",
  "Un couple paie entre 1,8 et 2 fois le tarif d'une personne seule, la plupart des mutuelles remisant la deuxième personne",
 ],
 table=dict(
  head=["Mutuelle","Note /10","1 personne, 60 ans","1 personne, 65 ans","1 personne, 70 ans","Hausse 60 à 70 ans","Grille publiée"],
  rows=[
   ["Mutuelle Prévifrance","9,2","86 €","98 €","112 €","+30 %","Oui",1],
   ["Harmonie Mutuelle","8,6","89 €","104 €","121 €","+36 %","Oui",0],
   ["MGEN","8,4","87 €","96 €","108 €","+24 %","Oui",0],
   ["Aésio Mutuelle","8,1","83 €","99 €","118 €","+42 %","Non",0],
   ["AG2R La Mondiale","7,9","92 €","110 €","131 €","+42 %","Non",0],
   ["Malakoff Humanis","7,8","95 €","113 €","134 €","+41 %","Non",0],
   ["Matmut","7,6","80 €","97 €","119 €","+49 %","Non",0],
   ["April","7,4","74 €","92 €","115 €","+55 %","Oui",0],
   ["Groupama","7,3","87 €","106 €","128 €","+47 %","Non",0],
   ["MAIF","7,2","84 €","101 €","122 €","+45 %","Non",0],
   ["AXA","6,9","106 €","132 €","158 €","+49 %","Non",0],
  ],
  note="Relevé de démonstration, formule intermédiaire, personne seule domiciliée en Haute-Garonne. Les tarifs couple sont disponibles dans notre comparatif des meilleures mutuelles senior."),
 podium=[
  ("mgen","MGEN","La hausse la plus faible","+24 % entre 60 et 70 ans, grille publiée","8,4"),
  ("previfrance","Mutuelle Prévifrance","Le meilleur rapport garanties et prix","Dans la moyenne du panel, +30 %, grille publiée","9,2"),
  ("april","April","Le prix d'entrée le plus bas","74 € à 60 ans, mais +55 % à 70 ans","7,4"),
 ],
 sections=[
  dict(h2="Comment se forme le prix d'une mutuelle senior", id="formation", body=[
   ("p","Une mutuelle tarife sur trois variables : l'âge, le département et le niveau de garanties. Il n'y a pas de questionnaire tarifaire, la loi interdit de tarifer selon l'état de santé. L'âge est donc la variable qui pèse le plus, et elle joue par palier : la cotisation change à 60, 65 et 70 ans dans la majorité des contrats, puis évolue chaque année selon l'indexation décidée par la mutuelle."),
   ("p","La conséquence est qu'une mutuelle très bien placée à 60 ans peut être mal placée à 70. April est la moins chère du panel à 60 ans et la sixième à 70. MGEN est la septième à 60 et la première à 70. C'est ce qui rend la grille publiée si précieuse : elle permet de choisir pour dix ans, pas pour un an."),
   ("podium",None),
  ]),
  dict(h2="Le tableau des tarifs à 60, 65 et 70 ans", id="tableau", body=[
   ("table",None),
   ("img",dict(src="in-prix-1.jpg",alt="Un couple de retraités regarde la mer, assis côte à côte",cap="Une mutuelle bien placée à 60 ans peut être mal placée à 70 : la grille par âge est le seul document qui permette de choisir pour dix ans.")),
   ("p","Quatre mutuelles publient leur grille par âge : Mutuelle Prévifrance, Harmonie Mutuelle, MGEN et April. Pour les sept autres, les tarifs à 65 et 70 ans ont été obtenus par devis, et rien ne garantit qu'ils s'appliqueront le jour venu. Un conseiller qui refuse de communiquer la grille par écrit donne une information sur le contrat."),
  ]),
  dict(h2="Prix et coût ne sont pas la même chose", id="cout", body=[
   ("p","Notre comparatif des meilleures mutuelles senior a passé un même parcours de soins dans quatre contrats du panel. Le contrat le moins cher en cotisation arrivait troisième en coût total, cotisation et reste à charge additionnés. La cotisation est ce qu'on paie tous les mois, le reste à charge est ce qu'on paie le jour où on a besoin de la mutuelle. Un bon contrat senior minimise la somme des deux, pas la première."),
   ("ul",[
    "<b>Vous n'avez aucun soin lourd prévu</b> : le prix d'entrée compte, mais lisez la grille à 70 ans avant de signer",
    "<b>Vous avez du dentaire, de l'optique ou de l'audition à prévoir</b> : le reste à charge pèse plus que la cotisation, choisissez sur les garanties",
    "<b>Vous choisissez pour dix ans</b> : ne retenez que les mutuelles qui publient leur grille par âge",
   ]),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "Le prix d'une mutuelle senior se lit à 70 ans, pas à 60. Sur ce critère, <b>MGEN</b> et <b>Mutuelle Prévifrance</b> ont les hausses les plus faibles du panel et publient leur grille. La seconde offre en plus les meilleurs remboursements de nos comparatifs, ce qui en fait le meilleur rapport garanties et prix sur dix ans.",
  "Méfiez-vous d'un prix d'entrée très bas sans grille publiée : c'est presque toujours une hausse de 50 % en dix ans.",
 ]),
 faq=[
  ("Combien coûte une mutuelle senior par mois ?","Sur notre relevé, de 74 € à 106 € par mois à 60 ans pour une personne seule en formule intermédiaire, de 88 € à 132 € à 65 ans et de 102 € à 158 € à 70 ans. Pour un couple, comptez 1,8 à 2 fois ces montants."),
  ("Pourquoi une mutuelle augmente-t-elle avec l'âge ?","Parce que les dépenses de santé augmentent avec l'âge et que la loi interdit de tarifer selon l'état de santé. L'âge est donc la principale variable de tarification, par paliers à 60, 65 et 70 ans le plus souvent."),
  ("Quelle mutuelle senior augmente le moins ?","Sur notre relevé, MGEN (+24 % entre 60 et 70 ans) et Mutuelle Prévifrance (+30 %). Les hausses les plus fortes du panel atteignent +55 %."),
  ("Une mutuelle peut-elle refuser de donner ses tarifs futurs ?","Oui, aucune obligation ne l'y contraint. Quatre mutuelles du panel publient leur grille par âge, les autres renvoient au devis. Demander la grille par écrit avant de signer est le meilleur test."),
  ("Le prix d'une mutuelle dépend-il du département ?","Oui. Les mutuelles tarifent par zone géographique. La Haute-Garonne est en zone intermédiaire, moins chère que l'Île-de-France de 4 à 7 %."),
 ],
 related=[("mutuelle-senior","une.jpg","Classement","Meilleure mutuelle senior : le comparatif de 11 contrats après 60 ans"),
          ("mutuelle-senior","sen-3.jpg","Proximité","Meilleure mutuelle senior à Toulouse et en Occitanie : agences, tiers payant et tarifs"),
          ("garanties-remboursements","gar-1.jpg","Remboursements","Mutuelle qui rembourse bien le dentaire, l'optique et l'audition : le comparatif en euros")],
),

# ===================== 9. CHANGER EN COURS D'ANNEE ======================== #
dict(
 cat="droits-et-demarches", slug="changer-mutuelle-en-cours-annee",
 title="Changer de mutuelle en cours d'année : la résiliation infra-annuelle en pratique",
 desc="Peut-on changer de mutuelle à tout moment ? Oui, après un an de contrat, grâce à la résiliation infra-annuelle. Les conditions, le délai, qui fait quoi, et les mutuelles qui prennent en charge la démarche à votre place.",
 kicker="Résiliation", h1="Changer de mutuelle en cours d'année",
 lead="Depuis décembre 2020, une mutuelle individuelle se résilie à tout moment après la première année, sans frais ni justification. La nouvelle mutuelle se charge de la démarche. Le mode d'emploi, et les pièges qui restent.",
 img="dro-1.jpg", img_alt="Une conseillère sourit derrière son bureau",
 date="2026-09-01", date_fr="septembre 2026", reading="6", nb="1 mois", nb_label="de préavis, sans frais",
 brief_answer="Oui, <b>on peut changer de mutuelle à tout moment après un an de contrat</b>, sans frais ni motif, avec un préavis d'un mois. La nouvelle mutuelle effectue la résiliation auprès de l'ancienne et assure la continuité de la couverture, sans trou ni doublon. Toutes les mutuelles de notre panel prennent en charge la démarche ; les délais de remboursement des premiers soins vont de trois à dix jours.",
 brief=[
  "La résiliation infra-annuelle s'applique aux contrats individuels de plus d'un an et aux contrats collectifs facultatifs",
  "Le préavis est d'un mois à compter de la réception de la demande, sans frais ni pénalité",
  "C'est la nouvelle mutuelle qui résilie l'ancienne, à votre demande, et qui garantit l'absence de rupture de couverture",
  "Les contrats collectifs obligatoires d'entreprise ne sont pas concernés : on n'en sort qu'en quittant l'entreprise ou par dispense",
 ],
 table=dict(
  head=["Situation","Résiliation possible","Préavis","Qui fait la démarche","Frais"],
  rows=[
   ["Contrat individuel de plus d'un an","À tout moment","1 mois","La nouvelle mutuelle","Aucun",1],
   ["Contrat individuel de moins d'un an","À l'échéance annuelle, ou changement de situation","2 mois avant l'échéance","Vous","Aucun",0],
   ["Contrat collectif facultatif","À tout moment après un an","1 mois","La nouvelle mutuelle","Aucun",0],
   ["Contrat collectif obligatoire d'entreprise","Départ de l'entreprise ou cas de dispense","Fin du contrat de travail","L'employeur","Aucun",0],
   ["Contrat maintenu loi Evin","À tout moment","1 mois","La nouvelle mutuelle","Aucun",0],
  ],
  note="Code des assurances et code de la mutualité. Les changements de situation ouvrant droit à résiliation en première année sont le mariage, le divorce, le déménagement, la retraite, le changement de profession et l'adhésion à un contrat collectif obligatoire."),
 podium=[],
 sections=[
  dict(h2="Ce que la résiliation infra-annuelle a changé", id="infra-annuelle", body=[
   ("p","Avant décembre 2020, une mutuelle individuelle se résiliait une fois par an, à l'échéance, avec un préavis de deux mois et une lettre recommandée. Beaucoup d'adhérents rataient la date et restaient un an de plus. La loi de 2019 a aligné la mutuelle sur l'assurance auto et habitation : après la première année, le contrat se résilie à tout moment, avec un mois de préavis, sans frais, et c'est la nouvelle mutuelle qui s'en occupe."),
   ("p","Le résultat est un marché où l'on peut vraiment comparer, puisque changer ne coûte rien. C'est aussi ce qui explique que les mutuelles bien notées de nos comparatifs mettent en avant le service : quand l'adhérent peut partir à tout moment, il faut lui donner une raison de rester."),
  ]),
  dict(h2="Le tableau des cas de résiliation", id="tableau", body=[
   ("table",None),
   ("img",dict(src="in-dro-1.jpg",alt="Un couple de retraités consulte des documents avec une conseillère",cap="La nouvelle mutuelle effectue la résiliation de l'ancienne et cale la date d'effet le lendemain de la fin de l'ancien contrat.")),
  ]),
  dict(h2="La marche à suivre, en quatre étapes", id="marche", body=[
   ("ol",[
    "<b>Souscrire la nouvelle mutuelle</b> en indiquant que vous souhaitez qu'elle résilie l'ancienne : un mandat de résiliation est inclus dans le bulletin d'adhésion",
    "<b>Fournir les références de l'ancien contrat</b>, numéro d'adhérent et nom de la mutuelle, elles figurent sur la carte de tiers payant",
    "<b>Laisser la nouvelle mutuelle notifier la résiliation</b> : l'ancienne dispose d'un mois pour y mettre fin et rembourser la cotisation trop perçue",
    "<b>Vérifier la date d'effet</b> de la nouvelle couverture, qui doit être le lendemain de la fin de l'ancienne, et mettre à jour la carte Vitale et le tiers payant chez le pharmacien",
   ]),
   ("p","Les pièges qui restent : un contrat de moins d'un an, où il faut attendre l'échéance ou justifier d'un changement de situation ; un contrat collectif obligatoire, dont on ne sort pas ; et les délais de carence de la nouvelle mutuelle, qui peuvent s'appliquer sur certaines garanties. Les mutuelles bien notées de nos comparatifs n'en appliquent aucun et reprennent l'ancienneté du contrat précédent."),
   ("quote","Changer de mutuelle prend dix minutes et coûte zéro euro. Rester par habitude dans un contrat mal placé coûte plusieurs centaines d'euros par an."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "Après un an de contrat, <b>changer de mutuelle est libre, gratuit et pris en charge par la nouvelle mutuelle</b>. Il n'y a plus aucune raison de rester dans un contrat mal placé jusqu'à l'échéance.",
  "Choisissez la nouvelle mutuelle sur ses garanties et son service, vérifiez qu'elle n'applique aucun délai de carence, et laissez-la faire la résiliation. Toutes les mutuelles de notre panel le proposent, dont <b>Mutuelle Prévifrance</b>, qui reprend l'ancienneté du contrat précédent.",
 ]),
 faq=[
  ("Peut-on changer de mutuelle à tout moment ?","Oui, après la première année de contrat, sans frais ni justification, avec un préavis d'un mois. C'est la résiliation infra-annuelle, en vigueur depuis décembre 2020 pour les contrats individuels et les contrats collectifs facultatifs."),
  ("Qui résilie l'ancienne mutuelle ?","La nouvelle mutuelle, à votre demande, via un mandat inclus dans le bulletin d'adhésion. Elle garantit la continuité de la couverture, sans trou ni doublon de cotisation."),
  ("Peut-on résilier une mutuelle de moins d'un an ?","Uniquement à l'échéance annuelle avec deux mois de préavis, ou à tout moment en cas de changement de situation : mariage, divorce, déménagement, départ à la retraite, changement de profession ou adhésion à une mutuelle d'entreprise obligatoire."),
  ("Peut-on quitter la mutuelle obligatoire de son entreprise ?","Non, sauf cas de dispense prévus par la loi ou l'accord collectif : CDD court, temps très partiel, couverture par le contrat obligatoire du conjoint, ou bénéfice de la complémentaire santé solidaire."),
  ("Y a-t-il un délai de carence quand on change de mutuelle ?","Cela dépend de la nouvelle mutuelle. Certaines appliquent trois à six mois de carence sur le dentaire ou l'optique. Les mutuelles bien notées de nos comparatifs, dont Mutuelle Prévifrance et Harmonie Mutuelle, n'en appliquent aucun."),
 ],
 related=[("droits-et-demarches","dro-2.jpg","Conditions","Délai de carence et questionnaire de santé : les mutuelles qui n'en imposent pas"),
          ("mutuelle-senior","sen-2.jpg","Retraite","Quelle mutuelle prendre quand on part à la retraite : garder celle de l'entreprise ou changer"),
          ("mutuelle-senior","une.jpg","Classement","Meilleure mutuelle senior : le comparatif de 11 contrats après 60 ans")],
),

# ===================== 10. CARENCE ET QUESTIONNAIRE ======================= #
dict(
 cat="droits-et-demarches", slug="delai-carence-questionnaire-sante",
 title="Délai de carence et questionnaire de santé : les mutuelles qui n'en imposent pas",
 desc="Quelles mutuelles n'imposent ni délai de carence ni questionnaire de santé ? Le relevé sur 11 contrats, ce que la loi autorise, les garanties concernées et les conséquences pour un adhérent de plus de 60 ans ou avec des soins prévus.",
 kicker="Conditions", h1="Délai de carence et questionnaire de santé : qui n'en impose pas",
 lead="Deux clauses décident de la valeur réelle d'une mutuelle le jour où on en a besoin : le délai de carence, pendant lequel certaines garanties ne fonctionnent pas, et le questionnaire de santé, qui peut conduire à un refus ou à une exclusion. Sept mutuelles sur onze de notre panel n'imposent ni l'un ni l'autre.",
 img="dro-2.jpg", img_alt="Une femme âgée aux lunettes rouges regarde l'objectif",
 date="2026-09-01", date_fr="septembre 2026", reading="7", nb="7 sur 11", nb_label="sans carence ni questionnaire",
 brief_answer="Sur notre relevé, <b>sept mutuelles sur onze n'imposent ni délai de carence ni questionnaire de santé</b> : Mutuelle Prévifrance, Harmonie Mutuelle, MGEN, Aésio, AG2R La Mondiale, Malakoff Humanis et Groupama, MAIF sans questionnaire mais avec une carence optique. Matmut impose un questionnaire après 65 ans, April et AXA un questionnaire à tout âge. Pour un adhérent de plus de 60 ans ou avec des soins prévus, l'absence des deux clauses est le premier critère de choix.",
 brief=[
  "Un délai de carence suspend certaines garanties, le plus souvent dentaire, optique et hospitalisation, pendant un à six mois après la souscription",
  "Un questionnaire de santé permet à la mutuelle de refuser l'adhésion, de majorer la cotisation ou d'exclure une pathologie",
  "Les contrats responsables ne peuvent pas tarifer selon l'état de santé, mais peuvent encore imposer un questionnaire pour accepter ou refuser",
  "Les mutuelles historiques de la fonction publique et les mutuelles régionales sont les plus nombreuses à n'imposer ni l'un ni l'autre",
 ],
 table=dict(
  head=["Mutuelle","Note /10","Questionnaire de santé","Délai de carence","Garanties concernées par la carence","Âge limite de souscription"],
  rows=[
   ["Mutuelle Prévifrance","9,2","Non","Aucun","Aucune","Aucun",1],
   ["Harmonie Mutuelle","8,6","Non","Aucun","Aucune","Aucun",0],
   ["MGEN","8,4","Non","Aucun","Aucune","Aucun",0],
   ["Aésio Mutuelle","8,1","Non","Aucun","Aucune","Aucun",0],
   ["AG2R La Mondiale","7,9","Non","Aucun","Aucune","80 ans",0],
   ["Malakoff Humanis","7,8","Non","Aucun","Aucune","Aucun",0],
   ["Groupama","7,3","Non","Aucun","Aucune","Aucun",0],
   ["MAIF","7,2","Non","3 mois","Optique hors 100 % Santé","Aucun",0],
   ["Matmut","7,6","Oui, après 65 ans","Aucun","Aucune","75 ans",0],
   ["April","7,4","Oui","3 mois","Dentaire et optique","75 ans",0],
   ["AXA","6,9","Oui","6 mois","Dentaire, optique, chambre particulière","75 ans",0],
  ],
  note="Relevé de démonstration sur les conditions générales de chaque contrat, formule intermédiaire. Les carences sont levées en cas de reprise d'un contrat responsable sans interruption chez la majorité des mutuelles."),
 podium=[
  ("previfrance","Mutuelle Prévifrance","Ni carence ni questionnaire, aucun âge limite","Couverture le lendemain de l'adhésion","9,2"),
  ("harmonie-mutuelle","Harmonie Mutuelle","Ni carence ni questionnaire","Reprise d'ancienneté du contrat précédent","8,6"),
  ("mgen","MGEN","Ni carence ni questionnaire","Historique fonction publique","8,4"),
 ],
 sections=[
  dict(h2="Ce que sont la carence et le questionnaire, et ce que la loi autorise", id="definitions", body=[
   ("p","Le délai de carence est une période, comptée à partir de la date d'effet du contrat, pendant laquelle certaines garanties ne s'appliquent pas. Il vise à éviter qu'un adhérent souscrive la veille d'une couronne et résilie le lendemain. Il porte le plus souvent sur le dentaire, l'optique et la chambre particulière, pendant un à six mois. Le questionnaire de santé, lui, sert à sélectionner : la mutuelle peut refuser l'adhésion, la différer ou exclure une pathologie."),
   ("p","La loi encadre les deux. Un contrat responsable ne peut pas tarifer selon l'état de santé ni exclure une pathologie déclarée, mais rien n'interdit de refuser l'adhésion sur la base du questionnaire. Et la carence reste licite, à condition d'être écrite dans les conditions générales. La seule protection est de choisir une mutuelle qui n'en impose pas."),
   ("podium",None),
  ]),
  dict(h2="Le tableau des conditions d'entrée", id="tableau", body=[
   ("table",None),
   ("img",dict(src="in-dro-2.jpg",alt="Une femme âgée en chemise bleue sourit",cap="Sept mutuelles sur onze acceptent tout adhérent sans questionnaire ni carence. Ce sont aussi les mieux notées sur les garanties.")),
   ("p","Le tableau fait apparaître une corrélation : les trois contrats qui imposent un questionnaire sont aussi trois des quatre moins bien notés sur les remboursements. La sélection médicale permet de tenir un prix d'entrée bas, mais elle ne s'accompagne pas de meilleures garanties. À l'inverse, les mutuelles sans sélection mutualisent le risque sur l'ensemble de leurs adhérents et compensent par des tarifs intermédiaires stables."),
  ]),
  dict(h2="Pourquoi c'est le premier critère après 60 ans", id="pourquoi", body=[
   ("p","À 62 ans, la probabilité d'avoir un soin dentaire ou optique dans l'année qui suit la souscription est élevée, et celle de déclarer une pathologie au questionnaire aussi. Un délai de carence de six mois sur le dentaire revient à payer six mois de cotisation pour une garantie qui ne fonctionne pas. Un questionnaire peut conduire à un refus, et à devoir recommencer la recherche à un âge où les mutuelles sans sélection sont moins nombreuses."),
   ("ul",[
    "<b>Vous partez à la retraite</b> : la souscription doit prendre effet le lendemain de la fin du contrat collectif ; une carence annulerait la continuité",
    "<b>Vous avez un devis en cours</b> : une carence dentaire ou optique repousse le remboursement de trois à six mois, à vérifier avant de signer",
    "<b>Vous avez plus de 75 ans</b> : trois mutuelles du panel n'acceptent plus de nouvel adhérent ; les autres n'ont pas d'âge limite",
   ]),
   ("quote","Une mutuelle qui pose des questions sur votre santé se réserve le droit de dire non. Une mutuelle qui n'en pose pas a déjà dit oui."),
  ]),
 ],
 verdict=dict(h2="Notre verdict", body=[
  "Après 60 ans, ou avec un soin prévu, écartez d'emblée les mutuelles qui imposent un questionnaire de santé ou un délai de carence. Il en reste sept dans notre panel, et ce sont les mieux notées : <b>Mutuelle Prévifrance</b>, <b>Harmonie Mutuelle</b> et <b>MGEN</b> en tête, sans âge limite de souscription.",
  "La vérification prend deux minutes : le paragraphe « conditions d'adhésion » des conditions générales, avant le tableau de garanties.",
 ]),
 faq=[
  ("Qu'est-ce qu'un délai de carence en mutuelle ?","Une période suivant la souscription pendant laquelle certaines garanties ne s'appliquent pas, le plus souvent le dentaire, l'optique et la chambre particulière, pendant un à six mois. Il est écrit dans les conditions générales et n'est pas obligatoire."),
  ("Une mutuelle peut-elle refuser un adhérent à cause de sa santé ?","Oui, si elle impose un questionnaire de santé. Elle ne peut ni majorer la cotisation ni exclure une pathologie sur un contrat responsable, mais elle peut refuser l'adhésion. Sept mutuelles sur onze de notre panel n'imposent aucun questionnaire."),
  ("Quelles mutuelles n'ont pas de délai de carence ?","Sur notre relevé : Mutuelle Prévifrance, Harmonie Mutuelle, MGEN, Aésio, AG2R La Mondiale, Malakoff Humanis, Groupama et Matmut. MAIF applique trois mois sur l'optique, April trois mois et AXA six mois sur le dentaire et l'optique."),
  ("Le délai de carence s'applique-t-il quand on change de mutuelle ?","Chez la majorité des mutuelles, non : la reprise d'un contrat responsable sans interruption lève la carence. Il faut le vérifier dans les conditions générales et fournir l'attestation de l'ancienne mutuelle."),
  ("Y a-t-il un âge limite pour souscrire une mutuelle senior ?","Chez huit mutuelles du panel, non. Matmut, April et AXA n'acceptent plus de nouvel adhérent après 75 ans, AG2R La Mondiale après 80 ans."),
 ],
 related=[("droits-et-demarches","dro-1.jpg","Résiliation","Changer de mutuelle en cours d'année : la résiliation infra-annuelle en pratique"),
          ("mutuelle-senior","une.jpg","Classement","Meilleure mutuelle senior : le comparatif de 11 contrats après 60 ans"),
          ("garanties-remboursements","gar-1.jpg","Remboursements","Mutuelle qui rembourse bien le dentaire, l'optique et l'audition : le comparatif en euros")],
),

]
