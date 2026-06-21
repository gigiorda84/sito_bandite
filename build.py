#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANDITE static site generator.
Regenerates all HTML pages in this directory from the content defined below.
Run from the repository root:  python3 build.py
"""
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://bandite.eu"

# Navigation: (file, label)
NAV = [
    ("about.html", "About"),
    ("works.html", "Works"),
    ("sonic-walkscape.html", "Sonic WalkScape"),
    ("resonavisse.html", "Resonavisse"),
    ("stampa.html", "Stampa"),
    ("collaborations.html", "Collaborations"),
    ("contacts.html", "Contacts"),
]

def head(title, desc, current, og_image="assets/img/hero-home.jpg"):
    nav = "\n".join(
        '      <a href="{f}"{cur}>{l}</a>'.format(
            f=f, l=html.escape(l),
            cur=' aria-current="page"' if f == current else "")
        for f, l in NAV
    )
    return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{site}/{current}">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{site}/{og}">
  <meta property="og:url" content="{site}/{current}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/png" href="assets/img/favicon.png">
  <link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">
  <link rel="preload" href="assets/fonts/handelson-five.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/fonts/sailors.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <header class="site-header">
    <div class="wrap site-header__inner">
      <a class="brand" href="index.html" aria-label="BANDITE — artivism"><img src="assets/img/bandite-wordmark.svg" alt="BANDITE — artivism" width="118" height="66"></a>
      <button class="nav-toggle" aria-label="Menu" aria-controls="nav" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
      <nav class="nav" id="nav">
{nav}
      </nav>
    </div>
  </header>
""".format(title=html.escape(title), desc=html.escape(desc), current=current,
           site=SITE_URL, og=og_image, nav=nav)

FOOT = """
  <footer class="site-footer">
    <div class="wrap site-footer__inner">
      <div>
        <img class="fbrand" src="assets/img/bandite-wordmark.svg" alt="BANDITE — artivism" width="150" height="84">
        <p style="margin:.8em 0 0">Turin — Val di Susa</p>
      </div>
      <div class="cols">
        <div>
          <a href="contacts.html">Contacts</a><br>
          <a href="mailto:resonavisse@gmail.com">resonavisse@gmail.com</a>
        </div>
        <div>
          <a href="works.html">Works</a><br>
          <a href="sonic-walkscape.html">Sonic WalkScape app</a>
        </div>
      </div>
    </div>
    <div class="wrap" style="margin-top:28px;font-size:.8rem;opacity:.7">
      © <span id="yr">2026</span> BANDITE — Valentina Bosio &amp; Simona Sala. Photos by Mauro Ujetto.
    </div>
  </footer>
  <script src="assets/js/main.js"></script>
  <script>document.getElementById('yr').textContent=new Date().getFullYear();</script>
</body>
</html>
"""

def page(filename, title, desc, body, current=None, og_image="assets/img/hero-home.jpg"):
    cur = current if current is not None else filename
    htmlout = head(title, desc, cur, og_image) + body + FOOT
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(htmlout)
    print("wrote", filename)

def slideshow(images, alt="BANDITE"):
    slides = "".join(
        '<div class="slide"><img src="{0}" alt="{1}" loading="lazy"></div>'.format(src, html.escape(alt))
        for src in images
    )
    return """<div class="gallery">
  <div class="slides">
    <div class="slides__track">{slides}</div>
    <button class="slides__btn slides__btn--prev" aria-label="Previous">&#8249;</button>
    <button class="slides__btn slides__btn--next" aria-label="Next">&#8250;</button>
  </div>
  <div class="slides__dots"></div>
</div>""".format(slides=slides)

# ============================================================
# HOME
# ============================================================
# News items (newest / featured first). href=None -> not linked.
NEWS = [
    {
        "date": "Mar&ndash;Jun 2026",
        "title": "Esistenze Plurali &mdash; intersezioni di cartografie sensibili",
        "text": "A participatory, performative workshop project conceived and curated by BANDITE within Torino Multisemiotica (University of Turin). Addressed to young people aged 18&ndash;25 with migratory backgrounds, it turns multilingualism and cultural difference into generative resources, culminating in a living, multimedia archive.",
        "href": None,
    },
    {
        "date": "13 Nov 2025",
        "title": "Resonavisse&rsquo;s first event: let&rsquo;s party together",
        "text": "To celebrate the birth of RESONAVISSE, an evening at Ramo d&rsquo;Oro (Galleria Umberto I, Turin) between exhibition, immersive installation, electroacoustic live performance and DJ set &mdash; terracotta works by Massimiliano Todisco, <em>Al&egrave;theia || traces</em> by Simona Sala, live music by Mildred and Ansss. Opening 6:30 PM, live 7:30 PM.",
        "href": "resonavisse.html",
    },
    {
        "date": "New &middot; 2025",
        "title": "Resonavisse &mdash; our new cultural association",
        "text": "RESONAVISSE &mdash; from the Latin <em>resonare</em>, &ldquo;to resonate&rdquo; &mdash; is now officially active: a cultural and artistic association conceived as a living space for exploration, creation and sharing, where artistic practices, human experiences and different forms of knowledge meet.",
        "href": "resonavisse.html",
    },
    {
        "date": "Work in progress",
        "title": "Unseen#1 &mdash; Montgen&egrave;vre &ndash; La Vachette (France)",
        "text": "A new site-specific artwork on the story of Blessing Matthew, co-produced with Universit&eacute; Grenoble Alpes for the DisFrontAlp research by geographer Cristina Del Biaggio, made possible by &ldquo;Soutien aux projets de recherche en cr&eacute;ation 2025&rdquo; from SFR Cr&eacute;ation.",
        "href": "unseen.html",
    },
]

def news_items():
    out = []
    for n in NEWS:
        tag = "a" if n["href"] else "div"
        href = ' href="%s"' % n["href"] if n["href"] else ""
        arrow = '<span class="news-arrow" aria-hidden="true">&#8594;</span>' if n["href"] else ""
        out.append(
            '<{tag} class="news-item"{href}>'
            '<time class="news-date">{date}</time>'
            '<div class="news-main"><h3 class="news-title">{title}{arrow}</h3>'
            '<p class="news-text">{text}</p></div>'
            '</{tag}>'.format(tag=tag, href=href, date=n["date"], title=n["title"],
                              arrow=arrow, text=n["text"])
        )
    return "\n        ".join(out)

home_body = """
  <section class="hero" style="background-image:url('assets/img/hero-home.jpg')">
    <div class="wrap hero__inner">
      <h1 class="hero__title">Bandite</h1>
      <p class="hero__tag">artivism</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap read prose justify">
      <p>BANDITE is a collective founded in 2023 by Valentina Bosio and Simona Sala, two artists whose research and creative practices meet at the intersection of art and activism. Their work is rooted in an anthropological approach to physical theatre and moves fluidly across theatre, dance, visual arts, video, and multimedia technologies. Their urgency lies in observing and narrating what remains at the margins: stories and identities rendered invisible or forgotten by dominant narratives.</p>
      <div class="btn-row">
        <a class="btn btn--accent" href="works.html">Explore the works</a>
        <a class="btn" href="sonic-walkscape.html">Sonic WalkScape app</a>
      </div>
    </div>
  </section>

  <section class="section news" id="news">
    <div class="wrap">
      <h2 class="news-heading">News</h2>
      <div class="news-list">
        __NEWS__
      </div>
    </div>
  </section>
""".replace("__NEWS__", news_items())
page("index.html", "BANDITE — artivism",
     "BANDITE is an art-activism collective founded in 2023 by Valentina Bosio and Simona Sala, working at the border between Italy and France through sonic walkscapes, performance and memory.",
     home_body, current="index.html")

# ============================================================
# ABOUT
# ============================================================
about_body = """
  <div class="wrap page-head read">
    <div class="kicker">The collective</div>
    <h1>About</h1>
  </div>
  <div class="wrap">
    <figure class="emblem"><img src="assets/img/bandite-emblem.webp" alt="BANDITE — illustration of the collective" width="440" height="440" loading="lazy"></figure>
  </div>
  <section class="section--tight">
    <div class="wrap read prose justify">
      <p>BANDITE is a collective founded in 2023 by Valentina Bosio and Simona Sala, two artists whose research and creative practices meet at the intersection of art and activism. Their work is rooted in an anthropological approach to physical theatre and moves fluidly across theatre, dance, visual arts, video, and multimedia technologies. Their aim is to move beyond traditional performative languages by interweaving diverse expressive codes, restoring theatre to its nature as a collective space&mdash;a place for reflection and confrontation with the complexities of the present. Their urgency lies in observing and narrating what remains at the margins: stories and identities rendered invisible or forgotten by dominant narratives.</p>
      <p>BANDITE&rsquo;s practice is grounded in an understanding of art as a practice of crossing&mdash;capable of connecting territories, languages, and communities. The collective continuously seeks to build spaces of dialogue between bodies and memories, between the real and the digital, between the present and the ancestral. The objective is not to represent, but to activate: to generate experiences in which the audience becomes part of a collective ritual of listening, awareness, and transmission. Their methodology draws on <em>Witness Action</em>, an interactive and participatory approach to performance developed from 2015 by Simona Sala in collaboration with the director of the Grotowski Institute (PL). This approach moves beyond aesthetics to activate collective witnessing processes, fostering mutual dignity and social engagement through art.</p>
      <p>In 2024, BANDITE created <em>Presenti Mai Assenti</em> (&ldquo;Present, Never Absent&rdquo;), a site-specific immersive soundwalk conceived for CommemorAction&mdash;a day of resistance against the deadly regime of borders. The piece unfolds along the migratory route between Claviere (Italy) and Montgen&egrave;vre (France). Participants walk while listening via headphones to an original sound composition blending field recordings, Mediterranean and Chiapas chants, and the poetry of Rahma Nur, layered with the sound of their footsteps and the surrounding landscape. That same year, BANDITE also curated the exhibition <em>Orizzonti Verticali &ndash; Sulle tracce di memorie esuli</em> (<em>Vertical Horizons &ndash; In the Footsteps of Exiled Memories</em>), hosted in the Torre Delfinale in Oulx, a symbolic waypoint on the migratory route to France. The exhibition featured photographs, audiovisual works, drawings, objects, and installations by Enrico Carpegna, Beppe Gromi, Fabio Russo, and Simona Sala. It explored themes of walking, memory, and horizon, functioning as a &ldquo;memory activator&rdquo; that sparked personal recollections among visitors&mdash;often linked to the region&rsquo;s own history of hardship and marginality in the Alpine borderlands.</p>
      <p>Continuing this trajectory, BANDITE has developed a new site-specific project, <em>Unseen</em> (2026), set between Montgen&egrave;vre and La Vachette near Brian&ccedil;on (France). Thanks also to the contribution of SFR Cr&eacute;ation, a program run by the University of Grenoble Alpes, in this project they have designed and developed a customized app called Sonic WalkScape, which makes all the immersive walks BANDITE has produced easily accessible to participants. <em>Unseen</em> invites audiences to engage with the story of Blessing Matthew, a young woman who died at this border in May 2018. Her death was investigated by a group of researchers, including Border Forensics and geographer Cristina Del Biaggio, as part of a broader inquiry into the deaths of people on the move at Europe&rsquo;s frontiers. In the past year, BANDITE has been invited to present their work at various academic conferences intersecting the fields of border art, activism, migration, and the humanities, contributing to broader conversations around artistic practices as tools of political engagement and collective memory.</p>
      <div class="btn-row">
        <a class="btn" href="simona-sala.html">Simona Sala</a>
        <a class="btn" href="valentina-bosio.html">Valentina Bosio</a>
      </div>
    </div>
  </section>
"""
page("about.html", "About — BANDITE",
     "BANDITE is a collective founded in 2023 by Valentina Bosio and Simona Sala, working at the intersection of art and activism.",
     about_body)

# ============================================================
# VALENTINA BOSIO
# ============================================================
valentina_body = """
  <div class="wrap page-head read">
    <div class="kicker">Bandite</div>
    <h1>Valentina Bosio</h1>
  </div>
  <section class="section--tight">
    <div class="wrap read prose justify">
      <p>Valentina Bosio is a performer, artivist and community activator. Her authorial research focuses particularly on themes such as body-scape, borders, archive and memory, moving freely between the re-mediation and proposition of a language that intersects codes of theatre, dance and new media.</p>
      <p>Her multidisciplinary background began with a two-year intensive program in physical theatre and performing arts at Philip Radice&rsquo;s Atelier Teatro Fisico in Turin. In 2019/20, she participated in Daniele Ninarello&rsquo;s permanent research and composition laboratory Il Corpo Intuitivo. In 2020, she obtained an Executive Master&rsquo;s degree, completing a final project focused on the valorisation of the landscape and cultural heritage of Alpine cross-border territories through Social and Community Theatre Methodology. This project led her to explore the mountain territories between France and Italy for two years. Valentina graduated from the University of Turin in DAMS &ndash; Disciplines of Art, Music, and Performance &ndash; with a research thesis on dance and educational innovation, specifically examining the decolonial practice of the Italian artist and choreographer Salvo Lombardo (2023). Significant were the gatherings and collaborations with artists such as Virgilio Sieni, Daniele Ninarello, Silvia Gribaudi, Sara Leghissa, Giulia Rae and Davide Enia. Between 2018 and 2020, she was part of the young theatre formation Nouvelle Plague, which also participated as a resident company at the Torino Fringe Festival 2019 with La Semimbecille e altre storie, a theatre work concerning the study of female hysteria, its interpretation in the context of 19th century psychology, in comparison with the stigma of people stigmatized as psychiatrically ill nowadays. In 2021 she founded the collective Volpi Metropolitane, a trans-media performing arts project, with which she experimented also video and digital language, especially related to the concept of tiers paysage proposed by Cl&eacute;ment, and the body as landscape with the project erbacce perenni. In 2023 she first joined the international projects of Ponte tra Culture soc.coop. Italia, beginning to collaborate together with Gianluca Barbadori and Simona Sala.</p>
      <p>Currently she&rsquo;s working in the Alps border between Italy and France with the actress and visual artist Simona Sala, with whom she founded the collective BANDITE in 2023. Bandite aims to transcend purely performative language, developing a fusion of diverse codes and forms of expression that reclaim theatre as a collective space and a privileged observatory for engaging with and comprehending contemporaneity. Their latest projects explored themes such as memory, witnessing, cross-border migratory movements, and culminate in site-specific works on the cross-border territory between Italy and France. Their work involves numerous collaborations, especially with the community and local realities, and partnerships with entities including Ponte tra Culture soc.coop. Italia, the Grotowski Institute in Wroc&lstrok;aw, Universit&eacute; Grenoble Alpes and Pacte social science laboratory in Grenoble.</p>
      <div class="btn-row"><a class="btn" href="about.html">&#8249; Back to About</a></div>
    </div>
  </section>
"""
page("valentina-bosio.html", "Valentina Bosio — BANDITE",
     "Valentina Bosio is a performer, artivist and community activator, co-founder of BANDITE.",
     valentina_body, current="about.html")

# ============================================================
# SIMONA SALA
# ============================================================
simona_body = """
  <div class="wrap page-head read">
    <div class="kicker">Bandite</div>
    <h1>Simona Sala</h1>
  </div>
  <section class="section--tight">
    <div class="wrap read prose justify">
      <p>Simona Sala is a visual artist, actress and performer.</p>
      <p>In 2006 she founded the performing arts company Sineglossa. Since 2011 she has been working at the Grotowski Institute in Wroclaw (PL) within the company Teatr Zar in the performances Armine, sister and Medee On getting Across, with which she participates in numerous festivals including San Francisco International Arts Festival and Paris Th&eacute;&acirc;tre de la Temp&ecirc;te. In 2011 she collaborates with Fundacja Jubilo with the 3-year project Unlocking in Wroclaw Penitentiary No.1 with long-sentence inmates. Between 2015 and 2018 she organized field travels to Salvador de Bahia to study and research Candombl&eacute; rituals and to southern Iran (Abadan) for possession rituals. In the same years she collaborated with Jaros&lstrok;aw Fret, director of Teatr Zar, on the creation of Witness Action, a new interactive and participatory approach to performance, with the aim of moving beyond the artistic experience that is proposed as aesthetic, with a view to activating an approach linked instead to personal identity and dignity. Between 2015 and 2017 she organizes conferences and public actions in which audiences and artists discuss how art and artists can witness and act in the sphere of action, through a new rituality of participation. In 2019 she starts working on her latest work Al&egrave;theia, creating site-specific installations around the theme of what cannot be hidden and on the relationship with memory and witness. In 2022 she makes a field trip to Chiapas, Mexico with Giovanna Maroccolo&rsquo;s Fusion Art Center following a political and social instance within Zapatista communities.</p>
      <p>Since 2023 she has been collaborating with the association On Borders, an ethnographic research laboratory on border crossings, on a field project between Italy and France.</p>
      <p><a href="https://simonasala.com/" target="_blank" rel="noopener">www.simonasala.com</a></p>
      <div class="btn-row"><a class="btn" href="about.html">&#8249; Back to About</a></div>
    </div>
  </section>
"""
page("simona-sala.html", "Simona Sala — BANDITE",
     "Simona Sala is a visual artist, actress and performer, co-founder of BANDITE.",
     simona_body, current="about.html")

# ============================================================
# WORKS
# ============================================================
works_body = """
  <div class="wrap page-head read">
    <div class="kicker">Projects</div>
    <h1>Works</h1>
    <p class="sub">Site-specific sonic walkscapes, exhibitions and immersive installations along the Italian&ndash;French Alpine border.</p>
  </div>
  <section class="section--tight">
    <div class="wrap read">
      <div class="work-list">
        <a class="work-item" href="unseen.html">
          <h3>Unseen</h3><span class="meta">Montgen&egrave;vre &middot; 2026</span><span class="arrow">&#8594;</span>
        </a>
        <a class="work-item" href="orizzonti-verticali.html">
          <h3>Orizzonti Verticali</h3><span class="meta">Oulx &middot; 2024</span><span class="arrow">&#8594;</span>
        </a>
        <a class="work-item" href="presenti-mai-assenti.html">
          <h3>Presenti Mai Assenti</h3><span class="meta">Claviere &middot; 2024</span><span class="arrow">&#8594;</span>
        </a>
      </div>
    </div>
  </section>
"""
page("works.html", "Works — BANDITE",
     "The works of BANDITE: Unseen, Orizzonti Verticali and Presenti Mai Assenti — sonic walkscapes and immersive installations on the Alpine border.",
     works_body)

# ============================================================
# UNSEEN
# ============================================================
unseen_body = """
  <section class="hero hero--page" style="background-image:url('assets/img/unseen-hero.jpg')">
    <div class="wrap hero__inner">
      <h1 class="hero__title">Unseen</h1>
      <p class="hero__tag">Montgen&egrave;vre &mdash; La Vachette (FR) &middot; 2026</p>
    </div>
  </section>
  <section class="section--tight">
    <div class="wrap read prose justify">
      <h2 style="text-align:left">Sonic WalkScape at the border</h2>
      <p><strong>UNSEEN</strong> was created to remember Blessing Matthew and all those who have lost their lives crossing borders. This sonic walkscape is dedicated to them&mdash;an immersive walk that seeks to restore voice to stories forced into invisibility.</p>
      <p>This Sonic WalkScape follows the paths between Montgen&egrave;vre and La Vachette through a journey of listening and, at the same time, participation, as an act of collective memory. An immersive sonic narrative composed of voices, sounds, and landscapes, it is presented on the occasion of Commemor-Action 2026, the international day of struggle against the regime of death and violence at borders and in remembrance of the victims of border policies. The score is made up of testimonies from activists and volunteers, field recordings, sounds and original music, together with data on the case of Blessing Matthew gathered by geographer and researcher Cristina Del Biaggio&mdash;who took part in the counter-investigation alongside Border Forensics and the association Toutes et Tous Migrants. Through a custom app developed by BANDITE, the public is invited to walk along the mapped route, with an invitation to immerse themselves in the sounds and in the traversal of the Alpine border landscape.</p>
      <p>Sonic WalkScape is a format conceived by the collective BANDITE that brings together artistic and sonic practice, fieldwork, and the active involvement of local communities. Developed through a custom app, it takes shape as a site-specific and participatory work capable of weaving together territory, memory, and community through storytelling and walking. Each Sonic WalkScape is reworked and reconfigured according to the context in which it emerges. It functions as a mobile sound installation in which participants, equipped with smartphones and headphones, are guided along a defined route via a map with geolocated points. At each point, original audio content&mdash;voices, testimonies, songs, field recordings, and environmental sounds&mdash;activates, gathered and composed during fieldwork or created specifically for the piece. The walk thus becomes an in/visible itinerary made of layered sonic and narrative traces, offering a sensitive and plural reading of the place.</p>
      <hr>
      <p>UNSEEN nasce per ricordare <strong>Blessing Matthew</strong> e tutte le persone che hanno perso la vita attraversando le frontiere. <em>A loro &egrave; dedicata questa sonic walkscape, una cammino sonora che vuole restituire voce alle storie che vengono costrette all&rsquo;invisibilit&agrave;.</em></p>
      <p>Questa <strong>Sonic WalkScape</strong> attraversa i sentieri tra Montgen&egrave;vre e La Vachette attraverso un viaggio d&rsquo;ascolto, e al tempo stesso partecipazione, in un atto di memoria collettiva. Un racconto sonoro immersivo fatto di voci, suoni e paesaggi, presentato in occasione della Commemor-Action 2026, la giornata internazionale di lotta contro il regime di morte e violenza delle frontiere, e ricordo delle vittime delle politiche di frontiera. La partitura &egrave; composta da testimonianze di attivist&euml; e volontari&euml;, field recordings, suoni e musiche originali, uniti ai dati sul caso di Blessing Matthew raccolti dalla geografa e ricercatrice Cristina Del Biaggio &ndash; che ha partecipato alla contro-inchiesta insieme a Border Forensics e all&rsquo;associazione Toutes et Tous Migrants. Attraverso un&rsquo;app personalizzata e sviluppata da BANDITE, il pubblico &egrave; invitato a camminare seguendo il percorso indicato da una mappa, con l&rsquo;invito ad immergersi nei suoni e nell&rsquo;attraversamento del paesaggio alpino frontaliero.</p>
      <div class="credits">
        Creazione e drammaturgia <em>Bandite</em><br>
        Montaggio audio, sound design, mix <em>Valeria Miracapillo</em><br>
        Voci <em>Cristina Del Biaggio, Simona Sala, Alice Ruotolo &ndash; Gruppo Abele, Silvia Massara &ndash; Sentieri Solidali, Davide Rostan, Nicolas Toselli, Michel Rousseau &ndash; Toutes et Tous Migrants, Theo, Ana&iuml;s Leduc, Herv&eacute;, Christiana Obie</em><br>
        Canti <em>Jean-Fran&ccedil;ois Favreau, Aleksandra Kotecka, Collectif f&eacute;ministe du Brian&ccedil;onnais</em><br>
        Beat in traccia &ldquo;Il caso&rdquo; <em>Calogero Dario Bufalino Maranella</em><br>
        Sviluppo app <em>Giuseppe Giordano</em><br>
        Valorizzazione della ricerca &laquo;La mort de Blessing Matthew &ndash; Une contre-enqu&ecirc;te sur la violence aux fronti&egrave;res alpines&raquo; (2022), <em>Border Forensics, Toutes et Tous Migrants</em><br>
        Progetto vincitore del bando <em>SFR Cr&eacute;ation &ndash; Arts in the Alps, Universit&eacute; Grenoble Alpes</em><br>
        Produzione <em>BANDITE</em><br>
        Con il contributo di <em>Maison de la Cr&eacute;ation et de l&rsquo;Innovation (MaCI), Pacte &ndash; Laboratoire de sciences sociales, Universit&eacute; Grenoble Alpes</em><br>
        Foto <em>Mauro Ujetto</em>
      </div>
      <div class="btn-row"><a class="btn btn--accent" href="sonic-walkscape.html">Download the app &amp; how to walk</a></div>
    </div>
  </section>
  <div class="wrap read">
    <div class="figure"><img src="assets/img/unseen-info.jpg" alt="UNSEEN — practical information" loading="lazy"></div>
  </div>
"""
page("unseen.html", "Unseen — BANDITE",
     "UNSEEN (2026) is a sonic walkscape between Montgenèvre and La Vachette, created to remember Blessing Matthew and all those who lost their lives crossing borders.",
     unseen_body, current="works.html", og_image="assets/img/unseen-hero.jpg")

# ============================================================
# ORIZZONTI VERTICALI
# ============================================================
ov_imgs = ["assets/img/ov-%d.jpg" % i for i in range(1, 9)]
ov_body = """
  <div class="wrap page-head read">
    <div class="kicker">Exhibition / immersive installation</div>
    <h1>Orizzonti Verticali</h1>
    <p class="sub">Sulle tracce di memorie esuli &middot; Oulx (IT) &middot; 2024</p>
  </div>
  <section class="section--tight">
    <div class="wrap read prose justify">
      <p><em>orizzonti verticali_sulle tracce di memorie esuli</em> is an exhibition conceived as an immersive installation, the result of the synergy of a local community in dialogue with the territory, joined in the aim of elevating itself from the dimension it inhabits and lives everyday toward a multifaceted and hybrid horizon. The common vision aims to catch what often remains invisible or poorly concealed, giving voice to the exiles of the past and present, men and women determined to project their stories &ndash; and desires &ndash; forward.</p>
      <p>The idea is to shift the perspective on the world we know and rethink the journey: the one taken by thousands of people driven to escape a ruined world in an attempt to create other possible futures. Vertical horizons was born, then, to look up and tear apart the veil of what is familiar and known to us; to do so, first of all, there is also a need to stumble. The fall, in fact, represents a necessary condition without which the rise could not take place. It is the stumbling that we never consider steps backward, but rather that movement of retreating backwardness that &ndash; like the waves of the sea &ndash; retreats to gain impetus and move forward with stubborn determination. This exhibition is evoked in a liminal place, with the aim of setting our gaze on interstitial spaces as spaces that are, also, generative. To pierce, first and foremost, our own horizons and take flight into new perspectives.</p>
      <div class="credits">
        <em>production and artistic direction</em> BANDITE<br>
        <em>exhibition by</em> Enrico Carpegna, Beppe Gromi and Fabio Russo, Simona Sala<br>
        <em>organization</em> Valentina Bosio, Martina Pasqualetto, Simona Sala<br>
        <em>texts and research consultancy</em> Valentina Bosio, Piero Gorza, Martina Pasqualetto<br>
        <em>photo</em> Mauro Ujetto<br>
        <em>under the patronage of</em> the Municipality of Oulx<br>
        <em>with the support of</em> Abb&agrave; SAS, Action For odv, Recycle For Refugees Campaign, Clarea Wines of Chiomonte, Associazione Liberamente Insieme of Bardonecchia, On Borders, Sentieri Solidali
      </div>
    </div>
    <div class="wrap">
      __SLIDESHOW__
    </div>
  </section>
""".replace("__SLIDESHOW__", slideshow(ov_imgs, "Orizzonti Verticali — exhibition"))
page("orizzonti-verticali.html", "Orizzonti Verticali — BANDITE",
     "Orizzonti Verticali — sulle tracce di memorie esuli: an immersive exhibition by BANDITE in Oulx (2024).",
     ov_body, current="works.html", og_image="assets/img/ov-1.jpg")

# ============================================================
# PRESENTI MAI ASSENTI
# ============================================================
pma_imgs = ["assets/img/pma-%d.jpg" % i for i in range(1, 9)]
pma_body = """
  <div class="wrap page-head read">
    <div class="kicker">Sonic WalkScape</div>
    <h1>Presenti Mai Assenti</h1>
    <p class="sub">Claviere &mdash; Montgen&egrave;vre &middot; 2024</p>
  </div>
  <section class="section--tight">
    <div class="wrap read prose justify">
      <p>Site-specific sonic walkscape created in Claviere, the last Italian village on the border with France.</p>
      <p>Using a simple smartphone app, participants are invited to follow geolocated points on a map that lead along an easy stretch of a migration route travelled by thousands of illegalised people every year. The walk is an immersive experience, composed of sounds, field recordings, Mediterranean songs, and poems by Rahma Nur, all of which overlap with the sounds of one&rsquo;s footsteps and the surrounding landscape. This experience &ndash; which can be shared collectively and enjoyed at any time &ndash; constitutes a profoundly personal and introspective moment, where voice and sound dialogue with silences, an integral part of the soundscape. By prompting reflection on the challenges faced by people on the move every day along migratory routes, it seeks to pay tribute to those who have lost their lives attempting to cross these mountains.</p>
      <p>The intent of this soundwalk is to engage participants/travellers in an active process of witnessing and memorisation, ensuring that the stories and voices of people compelled to migrate in search of freedom and improved living conditions remain ever present, never absent.</p>
      <div class="credits">
        <em>Sound installation and field recordings</em> BANDITE &ndash; Valentina Bosio, Simona Sala<br>
        <em>Sound editing</em> Giuseppe Giordano, Jacopo Salvatore<br>
        <em>Songs</em> Marjan Vahdat, Selda &Ouml;zturk<br>
        <em>Poems</em> Rahma Nur / from <em>The Cry and the Whisper</em> &ndash; Capovolte editrice<br>
        <em>In collaboration with</em> Sentieri Solidali, On Borders<br>
        <em>Photo credits</em> Mauro Ujetto<br>
        <em>Video</em> Francesco Arrigoni
      </div>
    </div>
    <div class="wrap">
      __SLIDESHOW__
    </div>
  </section>
""".replace("__SLIDESHOW__", slideshow(pma_imgs, "Presenti Mai Assenti — Claviere"))
page("presenti-mai-assenti.html", "Presenti Mai Assenti — BANDITE",
     "Presenti Mai Assenti — a site-specific sonic walkscape created by BANDITE in Claviere on the Italian–French border (2024).",
     pma_body, current="works.html", og_image="assets/img/pma-1.jpg")

# ============================================================
# SONIC WALKSCAPE (download)
# ============================================================
sonic_body = """
  <div class="wrap page-head read">
    <div class="kicker">The app</div>
    <h1>Sonic WalkScape</h1>
    <p class="sub">Click to download BANDITE&rsquo;s app <em>Sonic WalkScape</em> &middot; Scarica l&rsquo;app di Bandite</p>
  </div>
  <section class="section--tight">
    <div class="wrap read">
      <div class="btn-row">
        <a class="btn btn--accent" href="https://apps.apple.com/it/app/sonicwalkscape/id6757606425?l=en-GB" target="_blank" rel="noopener">Download for iPhone</a>
        <a class="btn btn--accent" href="https://play.google.com/store/apps/details?id=com.bandite.sonicwalkscape" target="_blank" rel="noopener">Download for Android</a>
      </div>
      <div class="figure"><img src="assets/img/sonic-dossier.png" alt="Sonic WalkScape — UNSEEN" loading="lazy"></div>
      <div class="prose">
        <h3 style="color:#b8860b">COSA TI SERVE?</h3>
        <p><strong>Cuffie</strong> o <strong>auricolari</strong> da collegare al tuo smartphone.<br>
        <strong>Telefono</strong> con batteria carica.<br>
        <strong>Scarpe e abiti</strong> adatti per un itinerario di <strong>montagna</strong>: controlla sempre il <strong>meteo</strong> prima di partire, il bollettino delle allerte valanghe, e in caso di neve assicurati di avere scarpe alte ed eventualmente bacchette e ciaspole.</p>
        <h3 style="color:#b8860b">COME FARE UNA SONIC WALKSCAPE?</h3>
        <p>&ndash; <strong>Scarica l&rsquo;app Sonic WalkScape</strong>: scannerizza il QR code che trovi sul primo cartello a Monginevro o clicca sui pulsanti qui sopra per accedere al tuo Apple Store o Play Store.<br>
        &ndash; Entra nell&rsquo;app e accedi alle <strong>impostazioni</strong> cliccando sulla rotellina in alto a destra: seleziona la <strong>lingua</strong> di preferenza, e <strong>attiva</strong> la <strong>geolocalizzazione</strong> del tuo dispositivo.<br>
        &ndash; Torna all&rsquo;homepage e <strong>inizia ad esplorare</strong>: cerca e seleziona dalla mappa la Sonic WalkScape che vuoi fare, cliccando su UNSEEN o PRESENTI MAI ASSENTI.<br>
        &ndash; Ora <strong>Inizia Tour</strong> &ndash; seleziona lingua, sottotitoli (sono presenti registrazioni in lingua italiana, francese e inglese), e fai il <strong>download del tour</strong> (per l&rsquo;uso anche offline).<br>
        &ndash; Prima di iniziare &egrave; importante cliccare sulle finestre di autorizzazione per l&rsquo;uso dei dati di posizione del tuo telefono (gps): clicca su <strong>consenti sempre</strong>.<br>
        &ndash; Vai vicino al <strong>punto di partenza</strong> del tour: per Unseen arriva al parcheggio <strong>Chalmettes</strong>, poi continua a camminare fino al parco avventure <em>Games in forest</em>, facendo attenzione al passaggio che attraversa le piste da sci. Assicurati di seguire il percorso e raggiungere i punti indicati sulla mappa, fino alla conclusione dell&rsquo;itinerario presso il villaggio di La Vachette.</p>
        <p>Al termine della Sonic WalkScape troverai sull&rsquo;app le indicazioni per i bus che ti riportano a Monginevro (&egrave; possibile fare il biglietto a bordo &ndash; costo di 2,20&euro;).<br>
        Puoi lasciare un feedback sull&rsquo;app e seguirci sui nostri canali social, o iscriverti alla nostra newsletter.</p>
      </div>
    </div>
  </section>
"""
page("sonic-walkscape.html", "Sonic WalkScape — BANDITE",
     "Download BANDITE's Sonic WalkScape app for iPhone and Android, and learn how to experience the immersive geolocated soundwalks.",
     sonic_body)

# ============================================================
# RESONAVISSE
# ============================================================
resonavisse_body = """
  <section class="hero hero--page" style="background-image:url('assets/img/resonavisse-hero.jpg')">
    <div class="wrap hero__inner">
      <h1 class="hero__title">Resonavisse</h1>
    </div>
  </section>
  <section class="section--tight">
    <div class="wrap read prose justify">
      <p><strong>Resonavisse</strong> &ndash; from the Latin <em>resonare</em>, <em>to have resounded</em> &ndash; is a cultural and artistic association born from the desire to create a living space for exploration, creation, and sharing: a space for encounters and creative contamination between art, human experience, and multiple knowledges.</p>
      <p>The association pursues cultural, artistic, and social aims, placing at its core the experimentation with artistic languages as a means to express one&rsquo;s presence in the world, to awaken critical awareness, and to foster consciousness and transformation. We believe in art as a relational practice and a tool to engage, awaken, and activate those who encounter it. We support both practical and theoretical research, and we nurture the meeting of bodies, stories, and visions through expressive forms ranging from performance to theatre, from sculpture to voice, from sound to audiovisual creations.</p>
      <hr>
      <p><strong>Resonavisse</strong> &ndash; dal latino <em>resonare</em>, <em>essere risuonato</em> &ndash; &egrave; un&rsquo;associazione culturale e artistica nata con l&rsquo;intento di creare uno spazio vivo di esplorazione, creazione e condivisione, un luogo dove possono incontrarsi e contaminarsi pratiche artistiche, esperienze umane e saperi diversi.</p>
      <p>L&rsquo;associazione persegue finalit&agrave; culturali, artistiche e sociali, mettendo al centro la sperimentazione dei linguaggi dell&rsquo;arte come veicolo per esprimere la propria presenza nel mondo, attivare lo sguardo critico, generare consapevolezza e trasformazione. Crediamo nell&rsquo;arte come pratica relazionale e strumento per sensibilizzare e attivare chi la incontra. Promuoviamo la ricerca pratica e teorica, e coltiviamo l&rsquo;incontro tra corpi, storie e visioni attraverso forme espressive che spaziano dalla performance al teatro, dalla scultura alla voce, dal suono alle creazioni audiovisive.</p>
    </div>
    <div class="wrap read">
      <div class="figure figure--center"><img src="assets/img/resonavisse-logo.png" alt="Resonavisse" loading="lazy"></div>
    </div>
  </section>
"""
page("resonavisse.html", "Resonavisse — BANDITE",
     "Resonavisse is a cultural and artistic association — a living space for exploration, creation and sharing between art, human experience and multiple knowledges.",
     resonavisse_body, og_image="assets/img/resonavisse-hero.jpg")

# ============================================================
# STAMPA (press)
# ============================================================
press = [
    ("Luna nuova", "06.03.2026 / Susanna Torasso", "assets/docs/lunanuova-6-marzo-2026-1.pdf"),
    ("Altreconomia", "11.02.2026 / Alessia Cesana", "assets/docs/altreconomia11febr2026.pdf"),
    ("Labex ITTEM", "09.02.2026 / Art and science: a learned jumble", "assets/docs/art-and-science_-a-learned-jumble-e28093-labex-ittem-eng.pdf"),
    ("Labex ITTEM", "27.01.2026 / Unseen &ndash; Balade sonore &agrave; la fronti&egrave;re", "assets/docs/unseen-e28093-balade-sonore-a-la-frontiere-e28093-labex-ittem-1.pdf"),
    ("Carnets de g&eacute;ographes 19", "2025 / Cristina Del Biaggio", "assets/docs/cdg-11060.pdf"),
    ("Pacte &ndash; Laboratoire de sciences sociales", "22.05.2025 / Pushing Border Art&rsquo;s Borders &ndash; session #3", "assets/docs/pushing-border-arts-borders-session-3-_-pacte-laboratoire-de-sciences-sociales.pdf"),
]
press_items = "\n".join(
    '        <a href="{href}" target="_blank" rel="noopener"><span><span class="src">{src}</span><br><span class="who">{who}</span></span><span class="dl">Open PDF &#8594;</span></a>'.format(
        href=href, src=src, who=who)
    for src, who, href in press
)
stampa_body = """
  <div class="wrap page-head read">
    <div class="kicker">Press</div>
    <h1>Rassegna stampa</h1>
    <p class="sub">Articles, reviews and academic contributions on BANDITE&rsquo;s work.</p>
  </div>
  <section class="section--tight">
    <div class="wrap read">
      <div class="press">
__ITEMS__
      </div>
    </div>
  </section>
""".replace("__ITEMS__", press_items)
page("stampa.html", "Stampa — BANDITE",
     "Press review: articles, reviews and academic contributions on BANDITE's work.",
     stampa_body)

# ============================================================
# COLLABORATIONS
# ============================================================
logos = [
    ("col-ponte.png", "Ponte tra Culture"),
    ("col-grenoble.png", "Université Grenoble Alpes"),
    ("col-resonavisse.png", "Resonavisse"),
    ("col-poziom.png", "Instytut Grotowskiego"),
    ("col-onborders.png", "On Borders"),
    ("col-sentieri.jpeg", "Sentieri Solidali"),
    ("col-cor.png", "COR"),
]
logo_items = "\n".join(
    '        <figure><img src="assets/img/{src}" alt="{alt}" loading="lazy"></figure>'.format(
        src=src, alt=html.escape(alt))
    for src, alt in logos
)
collab_body = """
  <div class="wrap page-head read">
    <div class="kicker">Network</div>
    <h1>Collaborations</h1>
    <p class="sub">Alliances and collaborations established over these years.</p>
  </div>
  <section class="section--tight">
    <div class="wrap">
      <div class="logos">
__ITEMS__
      </div>
    </div>
  </section>
""".replace("__ITEMS__", logo_items)
page("collaborations.html", "Collaborations — BANDITE",
     "The alliances and collaborations that support BANDITE's work.",
     collab_body)

# ============================================================
# CONTACTS
# ============================================================
contacts_body = """
  <div class="wrap page-head read">
    <div class="kicker">Get in touch</div>
    <h1>Contacts</h1>
  </div>
  <section class="section--tight">
    <div class="wrap read">
      <p class="contact-big"><a href="mailto:resonavisse@gmail.com">resonavisse@gmail.com</a></p>
      <p class="contact-meta">Turin &mdash; Val di Susa, Italy</p>
      <div class="btn-row" style="margin-top:2em">
        <a class="btn" href="https://simonasala.com/" target="_blank" rel="noopener">simonasala.com</a>
        <a class="btn" href="sonic-walkscape.html">Get the app</a>
      </div>
    </div>
  </section>
"""
page("contacts.html", "Contacts — BANDITE",
     "Contact BANDITE — resonavisse@gmail.com — Turin, Val di Susa, Italy.",
     contacts_body)

# ============================================================
# 404
# ============================================================
nf_body = """
  <section class="section" style="text-align:center">
    <div class="wrap read">
      <div class="kicker" style="color:var(--accent);text-transform:uppercase;letter-spacing:.18em;font-size:.78rem;font-weight:600">Error 404</div>
      <h1>Page not found</h1>
      <p class="sub" style="color:var(--muted)">The page you are looking for does not exist or has moved.</p>
      <div class="btn-row" style="justify-content:center"><a class="btn btn--accent" href="index.html">Back home</a></div>
    </div>
  </section>
"""
page("404.html", "Page not found — BANDITE", "Page not found.", nf_body, current="index.html")

print("\nDone. Pages written to", OUT)
