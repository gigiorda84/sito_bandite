#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BANDITE static site generator — trilingual (EN root, IT in /it/, FR in /fr/).
All text content lives in TR below. Run from the repo root:  python3 build.py
"""
import os, html, re, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://bandite.eu"
LANGS = ["en", "it", "fr"]
OG_LOCALE = {"en": "en_GB", "it": "it_IT", "fr": "fr_FR"}
BUILD_DATE = datetime.date.today().isoformat()

ORG_JSONLD = (
    '<script type="application/ld+json">'
    '{"@context":"https://schema.org","@graph":['
    '{"@type":["Organization","PerformingGroup"],"@id":"https://bandite.eu/#org",'
    '"name":"BANDITE","alternateName":"BANDITE \\u2014 artivism","url":"https://bandite.eu",'
    '"logo":"https://bandite.eu/assets/img/bandite-emblem.webp","email":"resonavisse@gmail.com",'
    '"foundingDate":"2023","areaServed":["IT","FR"],'
    '"founder":[{"@type":"Person","name":"Valentina Bosio"},{"@type":"Person","name":"Simona Sala"}],'
    '"sameAs":["https://simonasala.com"]},'
    '{"@type":"WebSite","@id":"https://bandite.eu/#website","name":"BANDITE","url":"https://bandite.eu",'
    '"inLanguage":["en","it","fr"],"publisher":{"@id":"https://bandite.eu/#org"}}'
    ']}</script>'
)

# Pages in the nav: (filename, nav-key)
NAV = [
    ("about.html", "about"),
    ("works.html", "works"),
    ("sonic-walkscape.html", "sonic"),
    ("resonavisse.html", "resonavisse"),
    ("stampa.html", "press"),
    ("collaborations.html", "collaborations"),
    ("contacts.html", "contacts"),
]

# ---------- shared assets (not translated) ----------
PMA_IMGS = ["/assets/img/pma-%d.jpg" % i for i in range(1, 9)]
OV_IMGS = ["/assets/img/ov-%d.jpg" % i for i in range(1, 9)]
LOGOS = [
    ("col-ponte.png", "Ponte tra Culture"),
    ("col-grenoble.png", "Université Grenoble Alpes"),
    ("col-resonavisse.png", "Resonavisse"),
    ("col-poziom.png", "Instytut Grotowskiego"),
    ("col-onborders.png", "On Borders"),
    ("col-sentieri.jpeg", "Sentieri Solidali"),
    ("col-cor.png", "COR"),
]
PRESS = [
    ("Luna nuova", "06.03.2026 / Susanna Torasso", "/assets/docs/lunanuova-6-marzo-2026-1.pdf"),
    ("Altreconomia", "11.02.2026 / Alessia Cesana", "/assets/docs/altreconomia11febr2026.pdf"),
    ("Labex ITTEM", "09.02.2026 / Art and science: a learned jumble", "/assets/docs/art-and-science_-a-learned-jumble-e28093-labex-ittem-eng.pdf"),
    ("Labex ITTEM", "27.01.2026 / Unseen &ndash; Balade sonore &agrave; la fronti&egrave;re", "/assets/docs/unseen-e28093-balade-sonore-a-la-frontiere-e28093-labex-ittem-1.pdf"),
    ("Carnets de g&eacute;ographes 19", "2025 / Cristina Del Biaggio", "/assets/docs/cdg-11060.pdf"),
    ("Pacte &ndash; Laboratoire de sciences sociales", "22.05.2025 / Pushing Border Art&rsquo;s Borders &ndash; session #3", "/assets/docs/pushing-border-arts-borders-session-3-_-pacte-laboratoire-de-sciences-sociales.pdf"),
]

# ============================================================
#  TRANSLATIONS
# ============================================================
TR = {
"en": {
 "name": "English",
 "nav": {"about":"About","works":"Works","sonic":"Sonic WalkScape","resonavisse":"Resonavisse","press":"Press","collaborations":"Collaborations","contacts":"Contacts"},
 "meta_home": "BANDITE is an art-activism collective founded in 2023 by Valentina Bosio and Simona Sala, working at the border between Italy and France through sonic walkscapes, performance and memory.",
 "meta_about": "BANDITE — the art-activism collective of Valentina Bosio and Simona Sala, working across theatre, sound, performance and memory on the Italian–French border.",
 "meta_sonic": "Download BANDITE's Sonic WalkScape app for iPhone and Android and discover how to experience the geolocated immersive soundwalks Unseen and Presenti Mai Assenti.",
 "meta_collab": "The alliances and partners that support BANDITE's work — from Ponte tra Culture to Université Grenoble Alpes and the Grotowski Institute.",
 "meta_contacts": "Get in touch with BANDITE — resonavisse@gmail.com — Turin, Val di Susa, Italy.",
 "foot_loc": "Turin &mdash; Val di Susa",
 "foot_works": "Works", "foot_app": "Sonic WalkScape app", "foot_contacts": "Contacts",
 "foot_credit": "BANDITE &mdash; Valentina Bosio &amp; Simona Sala. Photos by Mauro Ujetto.",
 "cta_works": "Explore the works", "cta_app": "Sonic WalkScape app",
 "news_h": "News", "back_about": "&#8249; Back to About",
 "home_intro": "BANDITE is a collective founded in 2023 by Valentina Bosio and Simona Sala, two artists whose research and creative practices meet at the intersection of art and activism. Their work is rooted in an anthropological approach to physical theatre and moves fluidly across theatre, dance, visual arts, video, and multimedia technologies. Their urgency lies in observing and narrating what remains at the margins: stories and identities rendered invisible or forgotten by dominant narratives.",
 "news": [
   {"date":"3&ndash;5 July 2026","title":"Master Salute Collettiva &ndash; Residenziale Oulx, Val di Susa &ndash; Università di Parma","text":""},
   {"date":"3&ndash;4 October 2026","title":"Rifugiati in rifugio","text":""},
   {"date":"Mar&ndash;Jun 2026","title":"Esistenze Plurali &mdash; intersezioni di cartografie sensibili","text":"A participatory, performative workshop project conceived and curated by BANDITE within Torino Multisemiotica (University of Turin). Addressed to young people aged 18&ndash;25 with migratory backgrounds, it turns multilingualism and cultural difference into generative resources, culminating in a living, multimedia archive."},
   {"date":"13 Nov 2025","title":"Resonavisse&rsquo;s first event: let&rsquo;s party together","text":"To celebrate the birth of RESONAVISSE, an evening at Ramo d&rsquo;Oro (Galleria Umberto I, Turin) between exhibition, immersive installation, electroacoustic live performance and DJ set &mdash; terracotta works by Massimiliano Todisco, <em>Al&egrave;theia || traces</em> by Simona Sala, live music by Mildred and Ansss. Opening 6:30 PM, live 7:30 PM."},
   {"date":"New &middot; 2025","title":"Resonavisse &mdash; our new cultural association","text":"RESONAVISSE &mdash; from the Latin <em>resonare</em>, &ldquo;to resonate&rdquo; &mdash; is now officially active: a cultural and artistic association conceived as a living space for exploration, creation and sharing, where artistic practices, human experiences and different forms of knowledge meet."},
   {"date":"Work in progress","title":"Unseen#1 &mdash; Montgen&egrave;vre &ndash; La Vachette (France)","text":"A new site-specific artwork on the story of Blessing Matthew, co-produced with Universit&eacute; Grenoble Alpes for the DisFrontAlp research by geographer Cristina Del Biaggio, made possible by &ldquo;Soutien aux projets de recherche en cr&eacute;ation 2025&rdquo; from SFR Cr&eacute;ation."},
 ],
 "about_kicker":"The collective", "about_title":"About",
 "about": [
   "BANDITE is a collective founded in 2023 by Valentina Bosio and Simona Sala, two artists whose research and creative practices meet at the intersection of art and activism. Their work is rooted in an anthropological approach to physical theatre and moves fluidly across theatre, dance, visual arts, video, and multimedia technologies. Their aim is to move beyond traditional performative languages by interweaving diverse expressive codes, restoring theatre to its nature as a collective space&mdash;a place for reflection and confrontation with the complexities of the present. Their urgency lies in observing and narrating what remains at the margins: stories and identities rendered invisible or forgotten by dominant narratives.",
   "BANDITE&rsquo;s practice is grounded in an understanding of art as a practice of crossing&mdash;capable of connecting territories, languages, and communities. The collective continuously seeks to build spaces of dialogue between bodies and memories, between the real and the digital, between the present and the ancestral. The objective is not to represent, but to activate: to generate experiences in which the audience becomes part of a collective ritual of listening, awareness, and transmission. Their methodology draws on <em>Witness Action</em>, an interactive and participatory approach to performance developed from 2015 by Simona Sala in collaboration with the director of the Grotowski Institute (PL). This approach moves beyond aesthetics to activate collective witnessing processes, fostering mutual dignity and social engagement through art.",
   "In 2024, BANDITE created <em>Presenti Mai Assenti</em> (&ldquo;Present, Never Absent&rdquo;), a site-specific immersive soundwalk conceived for CommemorAction&mdash;a day of resistance against the deadly regime of borders. The piece unfolds along the migratory route between Claviere (Italy) and Montgen&egrave;vre (France). Participants walk while listening via headphones to an original sound composition blending field recordings, Mediterranean and Chiapas chants, and the poetry of Rahma Nur, layered with the sound of their footsteps and the surrounding landscape. That same year, BANDITE also curated the exhibition <em>Orizzonti Verticali &ndash; Sulle tracce di memorie esuli</em> (<em>Vertical Horizons &ndash; In the Footsteps of Exiled Memories</em>), hosted in the Torre Delfinale in Oulx, a symbolic waypoint on the migratory route to France. The exhibition featured photographs, audiovisual works, drawings, objects and installations by Enrico Carpegna, Beppe Gromi, Fabio Russo and Simona Sala. It explored themes of walking, memory and horizon, functioning as a &ldquo;memory activator&rdquo; that sparked personal recollections among visitors&mdash;often linked to the region&rsquo;s own history of hardship and marginality in the Alpine borderlands.",
   "Continuing this trajectory, BANDITE has developed a new site-specific project, <em>Unseen</em> (2026), set between Montgen&egrave;vre and La Vachette near Brian&ccedil;on (France). Thanks also to the contribution of SFR Cr&eacute;ation, a program run by the University of Grenoble Alpes, they have designed and developed a customized app called Sonic WalkScape, which makes all the immersive walks BANDITE has produced easily accessible to participants. <em>Unseen</em> invites audiences to engage with the story of Blessing Matthew, a young woman who died at this border in May 2018. Her death was investigated by a group of researchers, including Border Forensics and geographer Cristina Del Biaggio, as part of a broader inquiry into the deaths of people on the move at Europe&rsquo;s frontiers. Over the past year, BANDITE has been invited to present its work at various academic conferences intersecting border art, activism, migration and the humanities, contributing to wider conversations on artistic practices as tools of political engagement and collective memory.",
 ],
 "valentina_kicker":"Bandite", "valentina_title":"Valentina Bosio",
 "valentina": [
   "Valentina Bosio is a performer, artivist and community activator. Her authorial research focuses particularly on themes such as body-scape, borders, archive and memory, moving freely between the re-mediation and proposition of a language that intersects the codes of theatre, dance and new media.",
   "Her multidisciplinary background began with a two-year intensive program in physical theatre and performing arts at Philip Radice&rsquo;s Atelier Teatro Fisico in Turin. In 2019/20 she took part in Daniele Ninarello&rsquo;s permanent research and composition laboratory <em>Il Corpo Intuitivo</em>. In 2020 she obtained an Executive Master&rsquo;s degree, with a final project on the valorisation of the landscape and cultural heritage of Alpine cross-border territories through Social and Community Theatre Methodology&mdash;a project that led her to explore the mountain territories between France and Italy for two years. She graduated from the University of Turin in DAMS (Disciplines of Art, Music and Performance) with a research thesis on dance and educational innovation, examining the decolonial practice of artist and choreographer Salvo Lombardo (2023). Significant were her encounters and collaborations with artists such as Virgilio Sieni, Daniele Ninarello, Silvia Gribaudi, Sara Leghissa, Giulia Rae and Davide Enia. Between 2018 and 2020 she was part of the young theatre formation Nouvelle Plague, resident company at the Torino Fringe Festival 2019 with <em>La Semimbecille e altre storie</em>, a work on female hysteria and its interpretation within 19th-century psychology, set against the stigma surrounding people labelled as psychiatrically ill today. In 2021 she founded the trans-media collective Volpi Metropolitane, experimenting with video and digital language, the notion of <em>tiers paysage</em> by Cl&eacute;ment, and the body as landscape in the project <em>erbacce perenni</em>. In 2023 she first joined the international projects of Ponte tra Culture soc.coop. Italia, beginning to collaborate with Gianluca Barbadori and Simona Sala.",
   "She currently works on the Alpine border between Italy and France with the actress and visual artist Simona Sala, with whom she founded the collective BANDITE in 2023. BANDITE aims to transcend purely performative language, developing a fusion of diverse codes and forms of expression that reclaim theatre as a collective space and a privileged observatory for engaging with and comprehending the contemporary. Their latest projects explore memory, witnessing and cross-border migratory movements, culminating in site-specific works on the territory between Italy and France. Their work involves numerous collaborations, especially with the community and local realities, and partnerships with entities including Ponte tra Culture soc.coop. Italia, the Grotowski Institute in Wroc&lstrok;aw, Universit&eacute; Grenoble Alpes and the Pacte social science laboratory in Grenoble.",
 ],
 "simona_kicker":"Bandite", "simona_title":"Simona Sala",
 "simona": [
   "Simona Sala is a visual artist, actress and performer.",
   "In 2006 she founded the performing arts company Sineglossa. Since 2011 she has worked at the Grotowski Institute in Wroclaw (PL) within the company Teatr Zar, in the performances <em>Armine, Sister</em> and <em>Medea / On Getting Across</em>, taking part in numerous festivals including the San Francisco International Arts Festival and the Th&eacute;&acirc;tre de la Temp&ecirc;te in Paris. In 2011 she collaborated with Fundacja Jubilo on the three-year project <em>Unlocking</em> in Wroclaw Penitentiary No.1 with long-sentence inmates. Between 2015 and 2018 she organised field travels to Salvador de Bahia to research Candombl&eacute; rituals and to southern Iran (Abadan) for possession rituals. In those years she collaborated with Jaros&lstrok;aw Fret, director of Teatr Zar, on the creation of <em>Witness Action</em>, a new interactive and participatory approach to performance aimed at moving beyond the merely aesthetic experience towards one linked to personal identity and dignity. Between 2015 and 2017 she organised conferences and public actions in which audiences and artists discussed how art and artists can witness and act, through a new rituality of participation. In 2019 she began her latest work <em>Al&egrave;theia</em>, creating site-specific installations around the theme of what cannot be hidden and the relationship with memory and witness. In 2022 she made a field trip to Chiapas, Mexico, with Giovanna Maroccolo&rsquo;s Fusion Art Center, following a political and social engagement within Zapatista communities.",
   "Since 2023 she has been collaborating with the association On Borders, an ethnographic research laboratory on border crossings, on a field project between Italy and France.",
 ],
 "simona_link":"www.simonasala.com",
 "works_kicker":"Projects", "works_title":"Works",
 "works_sub":"Site-specific sonic walkscapes, exhibitions and immersive installations along the Italian&ndash;French Alpine border.",
 "work_unseen_meta":"Montgen&egrave;vre &middot; 2026", "work_ov_meta":"Oulx &middot; 2024", "work_pma_meta":"Claviere &middot; 2024",
 # UNSEEN
 "unseen_tag":"Montgen&egrave;vre &mdash; La Vachette (FR) &middot; 2026",
 "unseen_h2":"Sonic WalkScape at the border",
 "unseen": [
   "<strong>UNSEEN</strong> was created to remember Blessing Matthew and all those who have lost their lives crossing borders. This sonic walkscape is dedicated to them&mdash;an immersive walk that seeks to restore voice to stories forced into invisibility.",
   "This Sonic WalkScape follows the paths between Montgen&egrave;vre and La Vachette through a journey of listening and participation, as an act of collective memory. An immersive sonic narrative composed of voices, sounds, and landscapes, it is presented on the occasion of Commemor-Action 2026, the international day of struggle against the regime of death and violence at borders. The score is made up of testimonies from activists and volunteers, field recordings, sounds and original music, together with data on the case of Blessing Matthew gathered by geographer Cristina Del Biaggio&mdash;who took part in the counter-investigation alongside Border Forensics and the association Toutes et Tous Migrants.",
   "Sonic WalkScape is a format conceived by BANDITE that brings together artistic and sonic practice, fieldwork, and the active involvement of local communities. Developed through a custom app, it takes shape as a site-specific and participatory work that weaves together territory, memory, and community through storytelling and walking. It functions as a mobile sound installation in which participants, equipped with smartphones and headphones, are guided along a route via a map with geolocated points, where original audio content activates&mdash;voices, testimonies, songs, field recordings and environmental sounds.",
 ],
 "unseen_cta":"Download the app &amp; how to walk",
 # OV
 "ov_kicker":"Exhibition / immersive installation", "ov_title":"Orizzonti Verticali",
 "ov_sub":"Sulle tracce di memorie esuli &middot; Oulx (IT) &middot; 2024",
 "ov": [
   "<em>Orizzonti Verticali &ndash; sulle tracce di memorie esuli</em> is an exhibition conceived as an immersive installation, the result of the synergy of a local community in dialogue with the territory. The common vision aims to catch what often remains invisible, giving voice to the exiles of the past and present, men and women determined to project their stories &ndash; and desires &ndash; forward.",
   "The idea is to shift the perspective on the world we know and rethink the journey: the one taken by thousands of people driven to escape a ruined world in an attempt to create other possible futures. The exhibition is evoked in a liminal place, setting our gaze on interstitial spaces as spaces that are, also, generative &mdash; to pierce our own horizons and take flight into new perspectives.",
 ],
 # PMA
 "pma_kicker":"Sonic WalkScape", "pma_title":"Presenti Mai Assenti",
 "pma_sub":"Claviere &mdash; Montgen&egrave;vre &middot; 2024",
 "pma": [
   "Site-specific sonic walkscape created in Claviere, the last Italian village on the border with France.",
   "Using a simple smartphone app, participants follow geolocated points on a map along an easy stretch of a migration route travelled by thousands of illegalised people every year. The walk is an immersive experience, composed of sounds, field recordings, Mediterranean songs and poems by Rahma Nur, overlapping with the sound of one&rsquo;s footsteps and the surrounding landscape.",
   "The intent of this soundwalk is to engage participants in an active process of witnessing and memorisation, ensuring that the stories and voices of people compelled to migrate in search of freedom remain ever present, never absent.",
 ],
 # SONIC
 "sonic_kicker":"The app", "sonic_title":"Sonic WalkScape",
 "sonic_sub":"Download BANDITE&rsquo;s <em>Sonic WalkScape</em> app",
 "sonic_iphone":"Download for iPhone", "sonic_android":"Download for Android",
 "sonic_need_h":"WHAT YOU NEED",
 "sonic_need":"<strong>Headphones</strong> or <strong>earphones</strong> for your smartphone. A <strong>phone</strong> with a charged battery. <strong>Shoes and clothing</strong> suitable for a <strong>mountain</strong> itinerary: always check the <strong>weather</strong> before setting out, and the avalanche bulletin; in case of snow make sure you have high boots and, if needed, poles and snowshoes.",
 "sonic_how_h":"HOW TO DO A SONIC WALKSCAPE",
 "sonic_how":"&ndash; <strong>Download the Sonic WalkScape app</strong>: scan the QR code on the first sign at Montgen&egrave;vre, or tap the buttons above.<br>&ndash; Open the app, go to <strong>settings</strong> (top-right), choose your <strong>language</strong> and <strong>enable geolocation</strong>.<br>&ndash; Back on the home page, <strong>start exploring</strong>: select from the map the Sonic WalkScape you want, tapping UNSEEN or PRESENTI MAI ASSENTI.<br>&ndash; <strong>Start the tour</strong> &ndash; choose language and subtitles (recordings available in Italian, French and English) and <strong>download the tour</strong> (also for offline use).<br>&ndash; Allow the use of your location data (GPS): tap <strong>always allow</strong>.<br>&ndash; Reach the <strong>starting point</strong>: for Unseen, reach the <strong>Chalmettes</strong> car park, then walk on to the <em>Games in forest</em> adventure park, watching for the crossing over the ski slopes. Follow the route to the reach the points on the map, up to the village of La Vachette.",
 "sonic_end":"At the end of the Sonic WalkScape the app shows the buses back to Montgen&egrave;vre (tickets on board, &euro;2.20). You can leave feedback on the app, follow us on our social channels, or subscribe to our newsletter.",
 # RESONAVISSE
 "reso_title":"Resonavisse",
 "reso": [
   "<strong>Resonavisse</strong> &ndash; from the Latin <em>resonare</em>, <em>to have resounded</em> &ndash; is a cultural and artistic association born from the desire to create a living space for exploration, creation, and sharing: a space for encounters and creative contamination between art, human experience, and multiple knowledges.",
   "The association pursues cultural, artistic, and social aims, placing at its core the experimentation with artistic languages as a means to express one&rsquo;s presence in the world, to awaken critical awareness, and to foster consciousness and transformation. We believe in art as a relational practice and a tool to engage, awaken, and activate those who encounter it. We support both practical and theoretical research, and we nurture the meeting of bodies, stories, and visions through expressive forms ranging from performance to theatre, from sculpture to voice, from sound to audiovisual creations.",
 ],
 # STAMPA
 "press_kicker":"Press", "press_title":"Press review",
 "press_sub":"Articles, reviews and academic contributions on BANDITE&rsquo;s work.",
 "press_open":"Open PDF &#8594;",
 # CONTACTS
 "contacts_kicker":"Get in touch", "contacts_title":"Contacts",
 "contacts_meta":"Turin &mdash; Val di Susa, Italy",
 "contacts_app":"Get the app",
 # 404
 "nf_kicker":"Error 404", "nf_title":"Page not found",
 "nf_sub":"The page you are looking for does not exist or has moved.",
 "nf_home":"Back home",
},

"it": {
 "name": "Italiano",
 "nav": {"about":"Chi siamo","works":"Opere","sonic":"Sonic WalkScape","resonavisse":"Resonavisse","press":"Stampa","collaborations":"Collaborazioni","contacts":"Contatti"},
 "meta_home": "BANDITE è un collettivo di art-activism fondato nel 2023 da Valentina Bosio e Simona Sala, attivo sul confine tra Italia e Francia attraverso sonic walkscape, performance e memoria.",
 "meta_about": "BANDITE — il collettivo di art-activism di Valentina Bosio e Simona Sala, tra teatro, suono, performance e memoria sul confine italo-francese.",
 "meta_sonic": "Scarica l'app Sonic WalkScape di BANDITE per iPhone e Android e scopri come vivere le camminate sonore immersive geolocalizzate Unseen e Presenti Mai Assenti.",
 "meta_collab": "Le alleanze e i partner che sostengono il lavoro di BANDITE — da Ponte tra Culture all'Université Grenoble Alpes e all'Istituto Grotowski.",
 "meta_contacts": "Contatta BANDITE — resonavisse@gmail.com — Torino, Val di Susa, Italia.",
 "foot_loc": "Torino &mdash; Val di Susa",
 "foot_works": "Opere", "foot_app": "App Sonic WalkScape", "foot_contacts": "Contatti",
 "foot_credit": "BANDITE &mdash; Valentina Bosio &amp; Simona Sala. Foto di Mauro Ujetto.",
 "cta_works": "Scopri le opere", "cta_app": "App Sonic WalkScape",
 "news_h": "Novit&agrave;", "back_about": "&#8249; Torna a Chi siamo",
 "home_intro": "BANDITE è un collettivo fondato nel 2023 da Valentina Bosio e Simona Sala, due artiste la cui ricerca e pratica creativa si incontrano all&rsquo;intersezione tra arte e attivismo. Il loro lavoro affonda le radici in un approccio antropologico al teatro fisico e si muove fluidamente tra teatro, danza, arti visive, video e tecnologie multimediali. La loro urgenza sta nell&rsquo;osservare e raccontare ciò che resta ai margini: storie e identità rese invisibili o dimenticate dalle narrazioni dominanti.",
 "news": [
   {"date":"3&ndash;5 luglio 2026","title":"Master Salute Collettiva &ndash; Residenziale Oulx, Val di Susa &ndash; Università di Parma","text":""},
   {"date":"3&ndash;4 ottobre 2026","title":"Rifugiati in rifugio","text":""},
   {"date":"Mar&ndash;Giu 2026","title":"Esistenze Plurali &mdash; intersezioni di cartografie sensibili","text":"Un progetto laboratoriale partecipativo e performativo ideato e curato dal collettivo BANDITE nell&rsquo;ambito di Torino Multisemiotica (Università di Torino). Rivolto a giovani tra i 18 e i 25 anni con background migratorio, trasforma multilinguismo e differenze culturali in risorse generative, culminando in un archivio vivente e multimediale."},
   {"date":"13 nov 2025","title":"Il primo evento di Resonavisse: festeggiamo insieme","text":"Per celebrare la nascita di RESONAVISSE, una serata al Ramo d&rsquo;Oro (Galleria Umberto I, Torino) tra esposizione, installazione immersiva, live elettroacustico e DJ set &mdash; terrecotte di Massimiliano Todisco, <em>Al&egrave;theia || traces</em> di Simona Sala, musica live di Mildred e Ansss. Apertura 18:30, live 19:30."},
   {"date":"Novit&agrave; &middot; 2025","title":"Resonavisse &mdash; la nostra nuova associazione culturale","text":"RESONAVISSE &mdash; dal latino <em>resonare</em>, &ldquo;essere risuonato&rdquo; &mdash; è ora ufficialmente attiva: un&rsquo;associazione culturale e artistica immaginata come spazio vivo di esplorazione, creazione e condivisione, dove pratiche artistiche, esperienze umane e saperi diversi si incontrano."},
   {"date":"Work in progress","title":"Unseen#1 &mdash; Montgen&egrave;vre &ndash; La Vachette (Francia)","text":"Una nuova opera site-specific sulla storia di Blessing Matthew, coproduzione dell&rsquo;Universit&eacute; Grenoble Alpes per la ricerca DisFrontAlp della geografa Cristina Del Biaggio, resa possibile dal contributo &ldquo;Soutien aux projets de recherche en cr&eacute;ation 2025&rdquo; di SFR Cr&eacute;ation."},
 ],
 "about_kicker":"Il collettivo", "about_title":"Chi siamo",
 "about": [
   "BANDITE è un collettivo fondato nel 2023 da Valentina Bosio e Simona Sala, due artiste la cui ricerca e pratica creativa si incontrano all&rsquo;intersezione tra arte e attivismo. Il loro lavoro affonda le radici in un approccio antropologico al teatro fisico e si muove tra teatro, danza, arti visive, video e tecnologie multimediali. L&rsquo;obiettivo è superare i linguaggi performativi tradizionali intrecciando codici espressivi diversi, restituendo al teatro la sua natura di spazio collettivo&mdash;luogo di riflessione e confronto con le complessità del presente. La loro urgenza sta nell&rsquo;osservare e raccontare ciò che resta ai margini: storie e identità rese invisibili o dimenticate dalle narrazioni dominanti.",
   "La pratica di BANDITE si fonda su una concezione dell&rsquo;arte come pratica di attraversamento&mdash;capace di connettere territori, lingue e comunità. Il collettivo cerca continuamente di costruire spazi di dialogo tra corpi e memorie, tra reale e digitale, tra presente e ancestrale. L&rsquo;obiettivo non è rappresentare, ma attivare: generare esperienze in cui il pubblico diventa parte di un rito collettivo di ascolto, consapevolezza e trasmissione. La metodologia attinge a <em>Witness Action</em>, un approccio interattivo e partecipativo alla performance sviluppato dal 2015 da Simona Sala in collaborazione con il direttore dell&rsquo;Istituto Grotowski (PL).",
   "Nel 2024 BANDITE ha creato <em>Presenti Mai Assenti</em>, un&rsquo;immersiva passeggiata sonora site-specific concepita per la CommemorAction&mdash;una giornata di resistenza contro il regime mortale delle frontiere. L&rsquo;opera si sviluppa lungo la rotta migratoria tra Claviere (Italia) e Montgen&egrave;vre (Francia). Le persone partecipanti camminano ascoltando in cuffia una composizione sonora originale che intreccia field recordings, canti mediterranei e del Chiapas e la poesia di Rahma Nur, sovrapposti al suono dei propri passi e al paesaggio circostante. Lo stesso anno il collettivo ha curato la mostra <em>Orizzonti Verticali &ndash; sulle tracce di memorie esuli</em>, ospitata nella Torre Delfinale di Oulx, tappa simbolica sulla rotta migratoria verso la Francia. La mostra presentava fotografie, opere audiovisive, disegni, oggetti e installazioni di Enrico Carpegna, Beppe Gromi, Fabio Russo e Simona Sala, esplorando i temi del camminare, della memoria e dell&rsquo;orizzonte e funzionando come un &laquo;attivatore di memoria&raquo; capace di risvegliare ricordi personali nei visitatori&mdash;spesso legati alla storia di fatica e marginalità di queste terre di confine alpine.",
   "Proseguendo questa traiettoria, BANDITE ha sviluppato un nuovo progetto site-specific, <em>Unseen</em> (2026), tra Montgen&egrave;vre e La Vachette presso Brian&ccedil;on (Francia). Grazie anche al contributo di SFR Cr&eacute;ation, programma dell&rsquo;Università di Grenoble Alpes, il collettivo ha progettato e sviluppato un&rsquo;app personalizzata, Sonic WalkScape, che rende facilmente accessibili tutte le camminate immersive prodotte. <em>Unseen</em> invita il pubblico a confrontarsi con la storia di Blessing Matthew, giovane donna morta a questo confine nel maggio 2018. La sua morte è stata indagata da un gruppo di ricercatori, tra cui Border Forensics e la geografa Cristina Del Biaggio, nell&rsquo;ambito di un&rsquo;inchiesta più ampia sulle morti delle persone in movimento alle frontiere d&rsquo;Europa. Nell&rsquo;ultimo anno BANDITE è stata invitata a presentare il proprio lavoro in diverse conferenze accademiche all&rsquo;incrocio tra arte di frontiera, attivismo, migrazioni e scienze umane, contribuendo a un dibattito più ampio sulle pratiche artistiche come strumenti di impegno politico e memoria collettiva.",
 ],
 "valentina_kicker":"Bandite", "valentina_title":"Valentina Bosio",
 "valentina": [
   "Valentina Bosio è performer, artivista e attivatrice di comunità. La sua ricerca autoriale si concentra in particolare su temi come body-scape, confini, archivio e memoria, muovendosi liberamente tra la ri-mediazione e la proposta di un linguaggio che interseca i codici del teatro, della danza e dei new media.",
   "La sua formazione multidisciplinare inizia con un biennio intensivo di teatro fisico e arti performative all&rsquo;Atelier Teatro Fisico di Philip Radice a Torino. Nel 2019/20 partecipa al laboratorio permanente di ricerca e composizione <em>Il Corpo Intuitivo</em> di Daniele Ninarello. Nel 2020 consegue un Master Executive con un progetto sulla valorizzazione del paesaggio e del patrimonio culturale dei territori transfrontalieri alpini attraverso la metodologia del Teatro Sociale e di Comunità&mdash;progetto che la porta a esplorare per due anni i territori montani tra Francia e Italia. Si laurea all&rsquo;Università di Torino in DAMS (Discipline delle Arti, della Musica e dello Spettacolo) con una tesi di ricerca su danza e innovazione educativa, esaminando la pratica decoloniale dell&rsquo;artista e coreografo Salvo Lombardo (2023). Significativi gli incontri e le collaborazioni con artisti come Virgilio Sieni, Daniele Ninarello, Silvia Gribaudi, Sara Leghissa, Giulia Rae e Davide Enia. Tra il 2018 e il 2020 fa parte della giovane formazione teatrale Nouvelle Plague, compagnia residente al Torino Fringe Festival 2019 con <em>La Semimbecille e altre storie</em>, un lavoro sullo studio dell&rsquo;isteria femminile e sulla sua interpretazione nella psicologia ottocentesca, in rapporto allo stigma verso le persone etichettate come malate psichiatriche oggi. Nel 2021 fonda il collettivo trans-media Volpi Metropolitane, sperimentando anche il linguaggio video e digitale, il concetto di <em>tiers paysage</em> di Cl&eacute;ment e il corpo come paesaggio nel progetto <em>erbacce perenni</em>. Nel 2023 entra per la prima volta nei progetti internazionali di Ponte tra Culture soc.coop. Italia, iniziando a collaborare con Gianluca Barbadori e Simona Sala.",
   "Attualmente lavora sul confine alpino tra Italia e Francia con l&rsquo;attrice e artista visiva Simona Sala, con cui nel 2023 fonda il collettivo BANDITE. BANDITE mira a trascendere il linguaggio puramente performativo, sviluppando una fusione di codici e forme espressive diverse che reclamano il teatro come spazio collettivo e osservatorio privilegiato per interrogare e comprendere la contemporaneità. I loro ultimi progetti esplorano memoria, testimonianza e movimenti migratori transfrontalieri, culminando in opere site-specific sul territorio tra Italia e Francia. Il loro lavoro coinvolge numerose collaborazioni, soprattutto con la comunità e le realtà locali, e partnership con enti come Ponte tra Culture soc.coop. Italia, l&rsquo;Istituto Grotowski di Wroc&lstrok;aw, l&rsquo;Universit&eacute; Grenoble Alpes e il laboratorio di scienze sociali Pacte di Grenoble.",
 ],
 "simona_kicker":"Bandite", "simona_title":"Simona Sala",
 "simona": [
   "Simona Sala è artista visiva, attrice e performer.",
   "Nel 2006 fonda la compagnia di arti performative Sineglossa. Dal 2011 lavora all&rsquo;Istituto Grotowski di Wroclaw (PL) all&rsquo;interno della compagnia Teatr Zar, negli spettacoli <em>Armine, Sister</em> e <em>Medea / On Getting Across</em>, con cui partecipa a numerosi festival, tra cui il San Francisco International Arts Festival e il Th&eacute;&acirc;tre de la Temp&ecirc;te di Parigi. Nel 2011 collabora con la Fundacja Jubilo al progetto triennale <em>Unlocking</em> nel Penitenziario n.1 di Wroclaw con detenuti con lunghe condanne. Tra il 2015 e il 2018 organizza viaggi sul campo a Salvador de Bahia per studiare i rituali del Candombl&eacute; e nel sud dell&rsquo;Iran (Abadan) per i rituali di possessione. In quegli anni collabora con Jaros&lstrok;aw Fret, direttore del Teatr Zar, alla creazione di <em>Witness Action</em>, un nuovo approccio interattivo e partecipativo alla performance volto a superare l&rsquo;esperienza puramente estetica per attivarne una legata all&rsquo;identità e alla dignità personale. Tra il 2015 e il 2017 organizza conferenze e azioni pubbliche in cui pubblico e artisti discutono di come l&rsquo;arte e gli artisti possano testimoniare e agire, attraverso una nuova ritualità della partecipazione. Nel 2019 inizia il suo ultimo lavoro <em>Al&egrave;theia</em>, creando installazioni site-specific attorno al tema di ciò che non può essere nascosto e al rapporto con la memoria e la testimonianza. Nel 2022 compie un viaggio sul campo in Chiapas, Messico, con il Fusion Art Center di Giovanna Maroccolo, seguendo un&rsquo;istanza politica e sociale all&rsquo;interno delle comunità zapatiste.",
   "Dal 2023 collabora con l&rsquo;associazione On Borders, laboratorio di ricerca etnografica sugli attraversamenti di frontiera, a un progetto sul campo tra Italia e Francia.",
 ],
 "simona_link":"www.simonasala.com",
 "works_kicker":"Progetti", "works_title":"Opere",
 "works_sub":"Sonic walkscape site-specific, mostre e installazioni immersive lungo il confine alpino tra Italia e Francia.",
 "work_unseen_meta":"Montgen&egrave;vre &middot; 2026", "work_ov_meta":"Oulx &middot; 2024", "work_pma_meta":"Claviere &middot; 2024",
 "unseen_tag":"Montgen&egrave;vre &mdash; La Vachette (FR) &middot; 2026",
 "unseen_h2":"Sonic WalkScape alla frontiera",
 "unseen": [
   "<strong>UNSEEN</strong> nasce per ricordare Blessing Matthew e tutte le persone che hanno perso la vita attraversando le frontiere. A loro è dedicata questa sonic walkscape, una camminata sonora che vuole restituire voce alle storie costrette all&rsquo;invisibilità.",
   "Questa Sonic WalkScape attraversa i sentieri tra Montgen&egrave;vre e La Vachette in un viaggio d&rsquo;ascolto e partecipazione, in un atto di memoria collettiva. Un racconto sonoro immersivo fatto di voci, suoni e paesaggi, presentato in occasione della Commemor-Action 2026, la giornata internazionale di lotta contro il regime di morte e violenza delle frontiere. La partitura è composta da testimonianze di attivistě e volontariě, field recordings, suoni e musiche originali, uniti ai dati sul caso di Blessing Matthew raccolti dalla geografa Cristina Del Biaggio&mdash;che ha partecipato alla contro-inchiesta insieme a Border Forensics e a Toutes et Tous Migrants.",
   "Sonic WalkScape è un format ideato da BANDITE che unisce pratica artistica e sonora, lavoro sul campo e coinvolgimento attivo delle comunità locali. Sviluppata attraverso un&rsquo;app personalizzata, prende forma come opera site-specific e partecipativa che intreccia territorio, memoria e comunità attraverso il racconto e il camminare. Funziona come un&rsquo;installazione sonora mobile in cui i partecipanti, dotati di smartphone e cuffie, sono guidati lungo un percorso tramite una mappa con punti geolocalizzati, in cui si attivano contenuti audio originali&mdash;voci, testimonianze, canti, field recordings e suoni ambientali.",
 ],
 "unseen_cta":"Scarica l&rsquo;app e come camminare",
 "ov_kicker":"Mostra / installazione immersiva", "ov_title":"Orizzonti Verticali",
 "ov_sub":"Sulle tracce di memorie esuli &middot; Oulx (IT) &middot; 2024",
 "ov": [
   "<em>Orizzonti Verticali &ndash; sulle tracce di memorie esuli</em> è una mostra concepita come installazione immersiva, frutto della sinergia di una comunità locale in dialogo con il territorio. La visione comune punta a cogliere ciò che spesso resta invisibile, dando voce agli esuli del passato e del presente, uomini e donne determinati a proiettare in avanti le proprie storie &ndash; e i propri desideri.",
   "L&rsquo;idea è spostare la prospettiva sul mondo che conosciamo e ripensare il viaggio: quello di migliaia di persone spinte a fuggire da un mondo in rovina nel tentativo di creare altri futuri possibili. La mostra è evocata in un luogo liminale, posando lo sguardo sugli spazi interstiziali come spazi anche generativi &mdash; per bucare i nostri orizzonti e spiccare il volo verso nuove prospettive.",
 ],
 "pma_kicker":"Sonic WalkScape", "pma_title":"Presenti Mai Assenti",
 "pma_sub":"Claviere &mdash; Montgen&egrave;vre &middot; 2024",
 "pma": [
   "Sonic walkscape site-specific creata a Claviere, l&rsquo;ultimo villaggio italiano sul confine con la Francia.",
   "Con una semplice app per smartphone, i partecipanti seguono punti geolocalizzati su una mappa lungo un tratto facile di una rotta migratoria percorsa ogni anno da migliaia di persone illegalizzate. La camminata è un&rsquo;esperienza immersiva, fatta di suoni, field recordings, canti mediterranei e poesie di Rahma Nur, che si sovrappongono al suono dei propri passi e al paesaggio circostante.",
   "L&rsquo;intento di questa passeggiata sonora è coinvolgere i partecipanti in un processo attivo di testimonianza e memorizzazione, affinché le storie e le voci di chi è costretto a migrare in cerca di libertà restino sempre presenti, mai assenti.",
 ],
 "sonic_kicker":"L&rsquo;app", "sonic_title":"Sonic WalkScape",
 "sonic_sub":"Scarica l&rsquo;app <em>Sonic WalkScape</em> di BANDITE",
 "sonic_iphone":"Scarica per iPhone", "sonic_android":"Scarica per Android",
 "sonic_need_h":"COSA TI SERVE?",
 "sonic_need":"<strong>Cuffie</strong> o <strong>auricolari</strong> da collegare al tuo smartphone. <strong>Telefono</strong> con batteria carica. <strong>Scarpe e abiti</strong> adatti per un itinerario di <strong>montagna</strong>: controlla sempre il <strong>meteo</strong> prima di partire e il bollettino delle allerte valanghe; in caso di neve assicurati di avere scarpe alte ed eventualmente bacchette e ciaspole.",
 "sonic_how_h":"COME FARE UNA SONIC WALKSCAPE?",
 "sonic_how":"&ndash; <strong>Scarica l&rsquo;app Sonic WalkScape</strong>: scannerizza il QR code sul primo cartello a Monginevro o clicca sui pulsanti qui sopra.<br>&ndash; Entra nell&rsquo;app, vai nelle <strong>impostazioni</strong> (in alto a destra), seleziona la <strong>lingua</strong> e <strong>attiva la geolocalizzazione</strong>.<br>&ndash; Torna alla homepage e <strong>inizia ad esplorare</strong>: seleziona dalla mappa la Sonic WalkScape che vuoi fare, cliccando su UNSEEN o PRESENTI MAI ASSENTI.<br>&ndash; <strong>Inizia Tour</strong> &ndash; seleziona lingua e sottotitoli (registrazioni in italiano, francese e inglese) e fai il <strong>download del tour</strong> (anche offline).<br>&ndash; Consenti l&rsquo;uso dei dati di posizione (gps): clicca su <strong>consenti sempre</strong>.<br>&ndash; Raggiungi il <strong>punto di partenza</strong>: per Unseen arriva al parcheggio <strong>Chalmettes</strong>, poi cammina fino al parco avventure <em>Games in forest</em>, attento al passaggio che attraversa le piste da sci. Segui il percorso fino al villaggio di La Vachette.",
 "sonic_end":"Al termine della Sonic WalkScape l&rsquo;app indica i bus per tornare a Monginevro (biglietto a bordo, 2,20&euro;). Puoi lasciare un feedback sull&rsquo;app, seguirci sui social o iscriverti alla newsletter.",
 "reso_title":"Resonavisse",
 "reso": [
   "<strong>Resonavisse</strong> &ndash; dal latino <em>resonare</em>, <em>essere risuonato</em> &ndash; è un&rsquo;associazione culturale e artistica nata con l&rsquo;intento di creare uno spazio vivo di esplorazione, creazione e condivisione: un luogo di incontro e contaminazione creativa tra arte, esperienza umana e saperi molteplici.",
   "L&rsquo;associazione persegue finalità culturali, artistiche e sociali, mettendo al centro la sperimentazione dei linguaggi dell&rsquo;arte come veicolo per esprimere la propria presenza nel mondo, attivare lo sguardo critico e generare consapevolezza e trasformazione. Crediamo nell&rsquo;arte come pratica relazionale e strumento per sensibilizzare e attivare chi la incontra. Promuoviamo la ricerca pratica e teorica e coltiviamo l&rsquo;incontro tra corpi, storie e visioni attraverso forme espressive che spaziano dalla performance al teatro, dalla scultura alla voce, dal suono alle creazioni audiovisive.",
 ],
 "press_kicker":"Stampa", "press_title":"Rassegna stampa",
 "press_sub":"Articoli, recensioni e contributi accademici sul lavoro di BANDITE.",
 "press_open":"Apri PDF &#8594;",
 "contacts_kicker":"Scrivici", "contacts_title":"Contatti",
 "contacts_meta":"Torino &mdash; Val di Susa, Italia",
 "contacts_app":"Scarica l&rsquo;app",
 "nf_kicker":"Errore 404", "nf_title":"Pagina non trovata",
 "nf_sub":"La pagina che cerchi non esiste o è stata spostata.",
 "nf_home":"Torna alla home",
},

"fr": {
 "name": "Français",
 "nav": {"about":"À propos","works":"Œuvres","sonic":"Sonic WalkScape","resonavisse":"Resonavisse","press":"Presse","collaborations":"Collaborations","contacts":"Contacts"},
 "meta_home": "BANDITE est un collectif d&rsquo;art-activisme fondé en 2023 par Valentina Bosio et Simona Sala, actif à la frontière entre l&rsquo;Italie et la France à travers des sonic walkscapes, la performance et la mémoire.",
 "meta_about": "BANDITE — le collectif d'art-activisme de Valentina Bosio et Simona Sala, entre théâtre, son, performance et mémoire à la frontière italo-française.",
 "meta_sonic": "Téléchargez l'appli Sonic WalkScape de BANDITE pour iPhone et Android et découvrez comment vivre les marches sonores immersives géolocalisées Unseen et Presenti Mai Assenti.",
 "meta_collab": "Les alliances et partenaires qui soutiennent le travail de BANDITE — de Ponte tra Culture à l'Université Grenoble Alpes et l'Institut Grotowski.",
 "meta_contacts": "Contactez BANDITE — resonavisse@gmail.com — Turin, Vallée de Suse, Italie.",
 "foot_loc": "Turin &mdash; Vallée de Suse",
 "foot_works": "Œuvres", "foot_app": "Appli Sonic WalkScape", "foot_contacts": "Contacts",
 "foot_credit": "BANDITE &mdash; Valentina Bosio &amp; Simona Sala. Photos de Mauro Ujetto.",
 "cta_works": "Découvrir les œuvres", "cta_app": "Appli Sonic WalkScape",
 "news_h": "Actualités", "back_about": "&#8249; Retour à À propos",
 "home_intro": "BANDITE est un collectif fondé en 2023 par Valentina Bosio et Simona Sala, deux artistes dont la recherche et la pratique créative se rejoignent à l&rsquo;intersection de l&rsquo;art et de l&rsquo;activisme. Leur travail s&rsquo;enracine dans une approche anthropologique du théâtre physique et circule librement entre théâtre, danse, arts visuels, vidéo et technologies multimédia. Leur urgence : observer et raconter ce qui demeure aux marges, ces histoires et identités rendues invisibles ou oubliées par les récits dominants.",
 "news": [
   {"date":"3&ndash;5 juillet 2026","title":"Master Salute Collettiva &ndash; Residenziale Oulx, Val di Susa &ndash; Università di Parma","text":""},
   {"date":"3&ndash;4 octobre 2026","title":"Rifugiati in rifugio","text":""},
   {"date":"Mars&ndash;Juin 2026","title":"Esistenze Plurali &mdash; intersezioni di cartografie sensibili","text":"Un projet d&rsquo;atelier participatif et performatif conçu et organisé par le collectif BANDITE dans le cadre de Torino Multisemiotica (Université de Turin). Destiné aux jeunes de 18 à 25 ans issus de parcours migratoires, il transforme le plurilinguisme et la différence culturelle en ressources génératives, aboutissant à une archive vivante et multimédia."},
   {"date":"13 nov. 2025","title":"Le premier événement de Resonavisse : fêtons ensemble","text":"Pour célébrer la naissance de RESONAVISSE, une soirée au Ramo d&rsquo;Oro (Galleria Umberto I, Turin) entre exposition, installation immersive, performance live électroacoustique et DJ set &mdash; terres cuites de Massimiliano Todisco, <em>Al&egrave;theia || traces</em> de Simona Sala, musique live de Mildred et Ansss. Ouverture 18h30, live 19h30."},
   {"date":"Nouveau &middot; 2025","title":"Resonavisse &mdash; notre nouvelle association culturelle","text":"RESONAVISSE &mdash; du latin <em>resonare</em>, &laquo;&nbsp;avoir résonné&nbsp;&raquo; &mdash; est désormais officiellement active : une association culturelle et artistique conçue comme un espace vivant d&rsquo;exploration, de création et de partage, où se rencontrent pratiques artistiques, expériences humaines et savoirs multiples."},
   {"date":"En cours","title":"Unseen#1 &mdash; Montgen&egrave;vre &ndash; La Vachette (France)","text":"Une nouvelle œuvre in situ sur l&rsquo;histoire de Blessing Matthew, coproduite par l&rsquo;Université Grenoble Alpes pour la recherche DisFrontAlp de la géographe Cristina Del Biaggio, rendue possible par le &laquo;&nbsp;Soutien aux projets de recherche en création 2025&nbsp;&raquo; de la SFR Création."},
 ],
 "about_kicker":"Le collectif", "about_title":"À propos",
 "about": [
   "BANDITE est un collectif fondé en 2023 par Valentina Bosio et Simona Sala, deux artistes dont la recherche et la pratique créative se rejoignent à l&rsquo;intersection de l&rsquo;art et de l&rsquo;activisme. Leur travail s&rsquo;enracine dans une approche anthropologique du théâtre physique et circule entre théâtre, danse, arts visuels, vidéo et technologies multimédia. L&rsquo;objectif est de dépasser les langages performatifs traditionnels en entrelaçant des codes expressifs divers, rendant au théâtre sa nature d&rsquo;espace collectif&mdash;lieu de réflexion et de confrontation avec les complexités du présent. Leur urgence : observer et raconter ce qui reste aux marges, ces histoires et identités rendues invisibles par les récits dominants.",
   "La pratique de BANDITE repose sur une conception de l&rsquo;art comme pratique de la traversée&mdash;capable de relier territoires, langues et communautés. Le collectif cherche sans cesse à construire des espaces de dialogue entre corps et mémoires, entre le réel et le numérique, entre le présent et l&rsquo;ancestral. L&rsquo;objectif n&rsquo;est pas de représenter, mais d&rsquo;activer : générer des expériences où le public devient partie d&rsquo;un rituel collectif d&rsquo;écoute, de conscience et de transmission. La méthodologie puise dans <em>Witness Action</em>, une approche interactive et participative de la performance développée dès 2015 par Simona Sala avec le directeur de l&rsquo;Institut Grotowski (PL).",
   "En 2024, BANDITE a créé <em>Presenti Mai Assenti</em>, une marche sonore immersive in situ conçue pour la CommemorAction&mdash;une journée de résistance contre le régime mortel des frontières. L&rsquo;œuvre se déploie le long de la route migratoire entre Claviere (Italie) et Montgen&egrave;vre (France). Les participant·es marchent en écoutant au casque une composition sonore originale mêlant field recordings, chants méditerranéens et du Chiapas et la poésie de Rahma Nur, superposés au bruit de leurs pas et au paysage environnant. La même année, le collectif a organisé l&rsquo;exposition <em>Orizzonti Verticali &ndash; sulle tracce di memorie esuli</em>, accueillie dans la Torre Delfinale d&rsquo;Oulx, étape symbolique sur la route migratoire vers la France. L&rsquo;exposition réunissait photographies, œuvres audiovisuelles, dessins, objets et installations d&rsquo;Enrico Carpegna, Beppe Gromi, Fabio Russo et Simona Sala, explorant les thèmes de la marche, de la mémoire et de l&rsquo;horizon et fonctionnant comme un &laquo;&nbsp;activateur de mémoire&nbsp;&raquo; éveillant des souvenirs personnels chez les visiteur·ses&mdash;souvent liés à l&rsquo;histoire de difficulté et de marginalité de ces terres frontalières alpines.",
   "Dans cette continuité, BANDITE a développé un nouveau projet in situ, <em>Unseen</em> (2026), entre Montgen&egrave;vre et La Vachette près de Brian&ccedil;on (France). Grâce aussi au soutien de la SFR Création, programme de l&rsquo;Université Grenoble Alpes, le collectif a conçu et développé une application dédiée, Sonic WalkScape, qui rend accessibles toutes les marches immersives produites. <em>Unseen</em> invite le public à se confronter à l&rsquo;histoire de Blessing Matthew, jeune femme morte à cette frontière en mai 2018. Sa mort a fait l&rsquo;objet d&rsquo;une enquête menée par un groupe de chercheur·ses, dont Border Forensics et la géographe Cristina Del Biaggio, dans le cadre d&rsquo;une investigation plus large sur les morts des personnes en mouvement aux frontières de l&rsquo;Europe. Au cours de l&rsquo;année écoulée, BANDITE a été invité à présenter son travail dans diverses conférences académiques au croisement de l&rsquo;art de la frontière, de l&rsquo;activisme, des migrations et des sciences humaines, contribuant à un débat plus vaste sur les pratiques artistiques comme outils d&rsquo;engagement politique et de mémoire collective.",
 ],
 "valentina_kicker":"Bandite", "valentina_title":"Valentina Bosio",
 "valentina": [
   "Valentina Bosio est performeuse, artiviste et activatrice de communauté. Sa recherche d&rsquo;auteure porte en particulier sur des thèmes tels que le body-scape, les frontières, l&rsquo;archive et la mémoire, se mouvant librement entre la re-médiation et la proposition d&rsquo;un langage qui croise les codes du théâtre, de la danse et des nouveaux médias.",
   "Sa formation pluridisciplinaire débute par un cursus intensif de deux ans en théâtre physique et arts vivants à l&rsquo;Atelier Teatro Fisico de Philip Radice à Turin. En 2019/20, elle participe au laboratoire permanent de recherche et de composition <em>Il Corpo Intuitivo</em> de Daniele Ninarello. En 2020, elle obtient un Master Executive avec un projet sur la valorisation du paysage et du patrimoine culturel des territoires transfrontaliers alpins par la méthodologie du Théâtre Social et de Communauté&mdash;projet qui l&rsquo;amène à explorer pendant deux ans les territoires de montagne entre la France et l&rsquo;Italie. Elle est diplômée de l&rsquo;Université de Turin en DAMS (Disciplines des Arts, de la Musique et du Spectacle) avec une thèse de recherche sur la danse et l&rsquo;innovation éducative, examinant la pratique décoloniale de l&rsquo;artiste et chorégraphe Salvo Lombardo (2023). Marquantes furent ses rencontres et collaborations avec des artistes tels que Virgilio Sieni, Daniele Ninarello, Silvia Gribaudi, Sara Leghissa, Giulia Rae et Davide Enia. Entre 2018 et 2020, elle fait partie de la jeune formation théâtrale Nouvelle Plague, compagnie en résidence au Torino Fringe Festival 2019 avec <em>La Semimbecille e altre storie</em>, un travail sur l&rsquo;hystérie féminine et son interprétation dans la psychologie du XIXe siècle, mis en regard de la stigmatisation des personnes étiquetées aujourd&rsquo;hui comme malades psychiatriques. En 2021, elle fonde le collectif trans-média Volpi Metropolitane, expérimentant aussi le langage vidéo et numérique, la notion de <em>tiers paysage</em> de Clément et le corps comme paysage dans le projet <em>erbacce perenni</em>. En 2023, elle rejoint pour la première fois les projets internationaux de Ponte tra Culture soc.coop. Italia, commençant à collaborer avec Gianluca Barbadori et Simona Sala.",
   "Elle travaille actuellement sur la frontière alpine entre l&rsquo;Italie et la France avec l&rsquo;actrice et artiste visuelle Simona Sala, avec qui elle fonde le collectif BANDITE en 2023. BANDITE entend dépasser le langage purement performatif, en développant une fusion de codes et de formes d&rsquo;expression divers qui revendiquent le théâtre comme espace collectif et observatoire privilégié pour interroger et comprendre la contemporanéité. Leurs derniers projets explorent la mémoire, le témoignage et les mouvements migratoires transfrontaliers, aboutissant à des œuvres in situ sur le territoire entre l&rsquo;Italie et la France. Leur travail implique de nombreuses collaborations, en particulier avec la communauté et les acteurs locaux, et des partenariats avec des entités telles que Ponte tra Culture soc.coop. Italia, l&rsquo;Institut Grotowski de Wroc&lstrok;aw, l&rsquo;Université Grenoble Alpes et le laboratoire de sciences sociales Pacte de Grenoble.",
 ],
 "simona_kicker":"Bandite", "simona_title":"Simona Sala",
 "simona": [
   "Simona Sala est artiste visuelle, actrice et performeuse.",
   "En 2006, elle fonde la compagnie d&rsquo;arts vivants Sineglossa. Depuis 2011, elle travaille à l&rsquo;Institut Grotowski de Wroclaw (PL) au sein de la compagnie Teatr Zar, dans les spectacles <em>Armine, Sister</em> et <em>Medea / On Getting Across</em>, avec lesquels elle participe à de nombreux festivals, dont le San Francisco International Arts Festival et le Th&eacute;&acirc;tre de la Temp&ecirc;te à Paris. En 2011, elle collabore avec la Fundacja Jubilo au projet triennal <em>Unlocking</em> à la maison d&rsquo;arrêt n°1 de Wroclaw, auprès de détenus à longues peines. Entre 2015 et 2018, elle organise des voyages de terrain à Salvador de Bahia pour étudier les rituels du Candomblé et dans le sud de l&rsquo;Iran (Abadan) pour les rituels de possession. Durant ces années, elle collabore avec Jaros&lstrok;aw Fret, directeur du Teatr Zar, à la création de <em>Witness Action</em>, une nouvelle approche interactive et participative de la performance visant à dépasser l&rsquo;expérience purement esthétique pour en activer une liée à l&rsquo;identité et à la dignité personnelles. Entre 2015 et 2017, elle organise des conférences et des actions publiques où public et artistes débattent de la manière dont l&rsquo;art et les artistes peuvent témoigner et agir, à travers une nouvelle ritualité de la participation. En 2019, elle commence son dernier travail <em>Al&egrave;theia</em>, créant des installations in situ autour du thème de ce qui ne peut être caché et du rapport à la mémoire et au témoignage. En 2022, elle effectue un voyage de terrain au Chiapas, au Mexique, avec le Fusion Art Center de Giovanna Maroccolo, suivant un engagement politique et social au sein des communautés zapatistes.",
   "Depuis 2023, elle collabore avec l&rsquo;association On Borders, laboratoire de recherche ethnographique sur les passages de frontière, pour un projet de terrain entre l&rsquo;Italie et la France.",
 ],
 "simona_link":"www.simonasala.com",
 "works_kicker":"Projets", "works_title":"Œuvres",
 "works_sub":"Sonic walkscapes in situ, expositions et installations immersives le long de la frontière alpine italo-française.",
 "work_unseen_meta":"Montgen&egrave;vre &middot; 2026", "work_ov_meta":"Oulx &middot; 2024", "work_pma_meta":"Claviere &middot; 2024",
 "unseen_tag":"Montgen&egrave;vre &mdash; La Vachette (FR) &middot; 2026",
 "unseen_h2":"Sonic WalkScape à la frontière",
 "unseen": [
   "<strong>UNSEEN</strong> est née pour se souvenir de Blessing Matthew et de toutes les personnes ayant perdu la vie en traversant les frontières. Cette sonic walkscape leur est dédiée&mdash;une marche sonore qui cherche à redonner voix aux histoires contraintes à l&rsquo;invisibilité.",
   "Cette Sonic WalkScape parcourt les sentiers entre Montgen&egrave;vre et La Vachette dans un voyage d&rsquo;écoute et de participation, comme un acte de mémoire collective. Un récit sonore immersif fait de voix, de sons et de paysages, présenté à l&rsquo;occasion de la Commemor-Action 2026, journée internationale de lutte contre le régime de mort et de violence aux frontières. La partition se compose de témoignages de militant·es et de bénévoles, de field recordings, de sons et de musiques originales, avec les données sur le cas de Blessing Matthew recueillies par la géographe Cristina Del Biaggio&mdash;qui a participé à la contre-enquête aux côtés de Border Forensics et de l&rsquo;association Toutes et Tous Migrants.",
   "Sonic WalkScape est un format conçu par BANDITE qui réunit pratique artistique et sonore, travail de terrain et implication active des communautés locales. Développée via une application dédiée, elle prend la forme d&rsquo;une œuvre in situ et participative qui tisse ensemble territoire, mémoire et communauté par le récit et la marche. Elle fonctionne comme une installation sonore mobile où les participant·es, muni·es d&rsquo;un smartphone et d&rsquo;écouteurs, sont guidé·es le long d&rsquo;un parcours via une carte à points géolocalisés, où s&rsquo;activent des contenus audio originaux&mdash;voix, témoignages, chants, field recordings et sons d&rsquo;ambiance.",
 ],
 "unseen_cta":"Télécharger l&rsquo;appli &amp; comment marcher",
 "ov_kicker":"Exposition / installation immersive", "ov_title":"Orizzonti Verticali",
 "ov_sub":"Sulle tracce di memorie esuli &middot; Oulx (IT) &middot; 2024",
 "ov": [
   "<em>Orizzonti Verticali &ndash; sulle tracce di memorie esuli</em> est une exposition conçue comme une installation immersive, fruit de la synergie d&rsquo;une communauté locale en dialogue avec le territoire. La vision commune cherche à saisir ce qui demeure souvent invisible, en donnant voix aux exilés du passé et du présent, hommes et femmes déterminés à projeter en avant leurs histoires &ndash; et leurs désirs.",
   "L&rsquo;idée est de déplacer le regard sur le monde que nous connaissons et de repenser le voyage : celui de milliers de personnes poussées à fuir un monde en ruine pour tenter de créer d&rsquo;autres futurs possibles. L&rsquo;exposition est évoquée dans un lieu liminal, posant le regard sur les espaces interstitiels comme des espaces aussi génératifs &mdash; pour percer nos propres horizons et nous élancer vers de nouvelles perspectives.",
 ],
 "pma_kicker":"Sonic WalkScape", "pma_title":"Presenti Mai Assenti",
 "pma_sub":"Claviere &mdash; Montgen&egrave;vre &middot; 2024",
 "pma": [
   "Sonic walkscape in situ créée à Claviere, le dernier village italien à la frontière avec la France.",
   "Avec une simple application pour smartphone, les participant·es suivent des points géolocalisés sur une carte le long d&rsquo;un tronçon facile d&rsquo;une route migratoire empruntée chaque année par des milliers de personnes illégalisées. La marche est une expérience immersive, faite de sons, de field recordings, de chants méditerranéens et de poèmes de Rahma Nur, qui se superposent au bruit des pas et au paysage environnant.",
   "L&rsquo;intention de cette marche sonore est d&rsquo;engager les participant·es dans un processus actif de témoignage et de mémorisation, afin que les histoires et les voix de celles et ceux contraints de migrer en quête de liberté restent toujours présentes, jamais absentes.",
 ],
 "sonic_kicker":"L&rsquo;application", "sonic_title":"Sonic WalkScape",
 "sonic_sub":"Téléchargez l&rsquo;appli <em>Sonic WalkScape</em> de BANDITE",
 "sonic_iphone":"Télécharger pour iPhone", "sonic_android":"Télécharger pour Android",
 "sonic_need_h":"DE QUOI AVEZ-VOUS BESOIN ?",
 "sonic_need":"Un <strong>casque</strong> ou des <strong>écouteurs</strong> à brancher sur votre smartphone. Un <strong>téléphone</strong> chargé. Des <strong>chaussures et vêtements</strong> adaptés à un itinéraire de <strong>montagne</strong> : vérifiez toujours la <strong>météo</strong> avant de partir et le bulletin d&rsquo;avalanches ; en cas de neige, prévoyez des chaussures montantes et, si besoin, bâtons et raquettes.",
 "sonic_how_h":"COMMENT FAIRE UNE SONIC WALKSCAPE ?",
 "sonic_how":"&ndash; <strong>Téléchargez l&rsquo;appli Sonic WalkScape</strong> : scannez le QR code du premier panneau à Montgen&egrave;vre, ou appuyez sur les boutons ci-dessus.<br>&ndash; Ouvrez l&rsquo;appli, allez dans les <strong>réglages</strong> (en haut à droite), choisissez la <strong>langue</strong> et <strong>activez la géolocalisation</strong>.<br>&ndash; De retour à l&rsquo;accueil, <strong>explorez</strong> : sélectionnez sur la carte la Sonic WalkScape souhaitée, en touchant UNSEEN ou PRESENTI MAI ASSENTI.<br>&ndash; <strong>Démarrez le tour</strong> &ndash; choisissez langue et sous-titres (enregistrements en italien, français et anglais) et <strong>téléchargez le tour</strong> (aussi hors ligne).<br>&ndash; Autorisez l&rsquo;utilisation de votre position (GPS) : appuyez sur <strong>toujours autoriser</strong>.<br>&ndash; Rejoignez le <strong>point de départ</strong> : pour Unseen, gagnez le parking des <strong>Chalmettes</strong>, puis marchez jusqu&rsquo;au parc aventure <em>Games in forest</em>, attentif au passage qui traverse les pistes de ski. Suivez le parcours jusqu&rsquo;au village de La Vachette.",
 "sonic_end":"À la fin de la Sonic WalkScape, l&rsquo;appli indique les bus pour revenir à Montgen&egrave;vre (billet à bord, 2,20&euro;). Vous pouvez laisser un avis sur l&rsquo;appli, nous suivre sur nos réseaux ou vous abonner à la newsletter.",
 "reso_title":"Resonavisse",
 "reso": [
   "<strong>Resonavisse</strong> &ndash; du latin <em>resonare</em>, <em>avoir résonné</em> &ndash; est une association culturelle et artistique née du désir de créer un espace vivant d&rsquo;exploration, de création et de partage : un lieu de rencontre et de contamination créative entre l&rsquo;art, l&rsquo;expérience humaine et les savoirs multiples.",
   "L&rsquo;association poursuit des finalités culturelles, artistiques et sociales, en plaçant au cœur l&rsquo;expérimentation des langages de l&rsquo;art comme moyen d&rsquo;exprimer sa présence au monde, d&rsquo;éveiller le regard critique et de susciter conscience et transformation. Nous croyons en l&rsquo;art comme pratique relationnelle et outil pour sensibiliser et activer celles et ceux qui le rencontrent. Nous soutenons la recherche pratique et théorique et cultivons la rencontre entre corps, histoires et visions à travers des formes allant de la performance au théâtre, de la sculpture à la voix, du son aux créations audiovisuelles.",
 ],
 "press_kicker":"Presse", "press_title":"Revue de presse",
 "press_sub":"Articles, comptes rendus et contributions académiques sur le travail de BANDITE.",
 "press_open":"Ouvrir le PDF &#8594;",
 "contacts_kicker":"Écrivez-nous", "contacts_title":"Contacts",
 "contacts_meta":"Turin &mdash; Vallée de Suse, Italie",
 "contacts_app":"Obtenir l&rsquo;appli",
 "nf_kicker":"Erreur 404", "nf_title":"Page introuvable",
 "nf_sub":"La page que vous cherchez n&rsquo;existe pas ou a été déplacée.",
 "nf_home":"Retour à l&rsquo;accueil",
},
}

# ============================================================
#  HELPERS
# ============================================================
def url(lang, file):
    prefix = "/" if lang == "en" else "/%s/" % lang
    if file == "index.html":
        return prefix
    return prefix + file

def outpath(lang, filename):
    if lang == "en":
        return os.path.join(ROOT, filename)
    d = os.path.join(ROOT, lang)
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, filename)

def head(lang, filename, title, desc, og_image="/assets/img/hero-home.jpg"):
    L = TR[lang]
    nav = "\n".join(
        '      <a href="{href}"{cur}>{label}</a>'.format(
            href=url(lang, f), label=html.escape(L["nav"][k]),
            cur=' aria-current="page"' if f == filename else "")
        for f, k in NAV
    )
    switch = "\n".join(
        '        <a href="{href}"{cur} hreflang="{lg}">{lab}</a>'.format(
            href=url(lg, filename), lg=lg, lab=lg.upper(),
            cur=' aria-current="page"' if lg == lang else "")
        for lg in LANGS
    )
    alt = "\n".join(
        '  <link rel="alternate" hreflang="{lg}" href="{u}">'.format(lg=lg, u=SITE_URL + url(lg, filename))
        for lg in LANGS
    ) + '\n  <link rel="alternate" hreflang="x-default" href="{u}">'.format(u=SITE_URL + url("en", filename))
    og_loc = '  <meta property="og:locale" content="%s">\n' % OG_LOCALE[lang]
    og_loc += "\n".join('  <meta property="og:locale:alternate" content="%s">' % OG_LOCALE[lg] for lg in LANGS if lg != lang)
    # clean + truncate the meta description (strip tags, decode entities)
    d = html.unescape(re.sub(r"<[^>]+>", "", desc)).strip()
    if len(d) > 160:
        d = d[:157].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    desc = html.escape(d)
    return """<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#fafafa">
  <link rel="canonical" href="{site}{canon}">
{alt}
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="BANDITE">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="{site}{og}">
  <meta property="og:url" content="{site}{canon}">
{og_loc}
  <meta name="twitter:card" content="summary_large_image">
  {jsonld}
  <link rel="icon" type="image/png" href="/assets/img/favicon.png">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <link rel="preload" href="/assets/fonts/roboto-condensed.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/handelson-five.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
  <header class="site-header">
    <div class="wrap site-header__inner">
      <a class="brand" href="{home}" aria-label="BANDITE — artivism"><img src="/assets/img/bandite-wordmark.svg" alt="BANDITE — artivism" width="118" height="66"></a>
      <button class="nav-toggle" aria-label="Menu" aria-controls="nav" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
      <nav class="nav" id="nav">
{nav}
        <span class="lang-switch">
{switch}
        </span>
      </nav>
    </div>
  </header>
  <main>
""".format(lang=lang, title=html.escape(title), desc=desc,
           site=SITE_URL, canon=url(lang, filename), og=og_image,
           alt=alt, og_loc=og_loc, jsonld=ORG_JSONLD,
           nav=nav, switch=switch, home=url(lang, "index.html"))

def foot(lang):
    L = TR[lang]
    return """
  </main>
  <footer class="site-footer">
    <div class="wrap site-footer__inner">
      <div>
        <img class="fbrand" src="/assets/img/bandite-wordmark.svg" alt="BANDITE — artivism" width="150" height="84">
        <p style="margin:.8em 0 0">{loc}</p>
      </div>
      <div class="cols">
        <div>
          <a href="{c_contacts}">{contacts}</a><br>
          <a href="mailto:resonavisse@gmail.com">resonavisse@gmail.com</a>
        </div>
        <div>
          <a href="{c_works}">{works}</a><br>
          <a href="{c_sonic}">{app}</a>
        </div>
      </div>
    </div>
    <div class="wrap" style="margin-top:28px;font-size:.8rem;opacity:.7">
      © <span id="yr">2026</span> {credit}
    </div>
  </footer>
  <script src="/assets/js/main.js"></script>
  <script>document.getElementById('yr').textContent=new Date().getFullYear();</script>
</body>
</html>
""".format(loc=L["foot_loc"], contacts=L["foot_contacts"], works=L["foot_works"], app=L["foot_app"],
           credit=L["foot_credit"],
           c_contacts=url(lang, "contacts.html"), c_works=url(lang, "works.html"), c_sonic=url(lang, "sonic-walkscape.html"))

def write(lang, filename, title, desc, body, og_image="/assets/img/hero-home.jpg"):
    out = head(lang, filename, title, desc, og_image) + body + foot(lang)
    with open(outpath(lang, filename), "w", encoding="utf-8") as f:
        f.write(out)

def slideshow(images, alt):
    slides = "".join('<div class="slide"><img src="%s" alt="%s" loading="lazy"></div>' % (s, html.escape(alt)) for s in images)
    return """<div class="gallery">
  <div class="slides">
    <div class="slides__track">%s</div>
    <button class="slides__btn slides__btn--prev" aria-label="Previous">&#8249;</button>
    <button class="slides__btn slides__btn--next" aria-label="Next">&#8250;</button>
  </div>
  <div class="slides__dots"></div>
</div>""" % slides

def paras(items, cls="prose justify"):
    return "\n".join("      <p>%s</p>" % p for p in items)

# ============================================================
#  PAGE BUILDERS  (per language)
# ============================================================
def build_all(lang):
    L = TR[lang]
    BR = "BANDITE"

    # ---- HOME ----
    _news = []
    for n in L["news"]:
        if n.get("text"):
            _news.append(
                '<details class="news-item"><summary class="news-summary">'
                '<time class="news-date">{d}</time><span class="news-title">{t}</span>'
                '<span class="news-toggle" aria-hidden="true"></span></summary>'
                '<div class="news-content"><p class="news-text">{x}</p></div></details>'.format(d=n["date"], t=n["title"], x=n["text"]))
        else:
            _news.append(
                '<div class="news-item news-static"><div class="news-summary">'
                '<time class="news-date">{d}</time><span class="news-title">{t}</span>'
                '</div></div>'.format(d=n["date"], t=n["title"]))
    news = "\n        ".join(_news)
    home = """
  <section class="hero hero--home" style="background-image:url('/assets/img/hero-home.jpg')">
    <h1 class="sr-only">BANDITE &mdash; artivism</h1>
  </section>

  <section class="section">
    <div class="wrap read prose justify">
      <p>{intro}</p>
      <div class="btn-row">
        <a class="btn btn--accent" href="{works}">{cta_works}</a>
        <a class="btn" href="{sonic}">{cta_app}</a>
      </div>
    </div>
  </section>

  <section class="section news" id="news">
    <div class="wrap">
      <h2 class="news-heading">{news_h}</h2>
      <div class="news-list">
        {news}
      </div>
    </div>
  </section>
""".format(intro=L["home_intro"], works=url(lang, "works.html"), sonic=url(lang, "sonic-walkscape.html"),
           cta_works=L["cta_works"], cta_app=L["cta_app"], news_h=L["news_h"], news=news)
    write(lang, "index.html", "BANDITE — artivism", L["meta_home"], home)

    # ---- ABOUT ----
    about = """
  <div class="wrap page-head read">
    <div class="kicker">{kicker}</div>
    <h1>{title}</h1>
  </div>
  <div class="wrap">
    <figure class="emblem"><img src="/assets/img/bandite-emblem.webp" alt="BANDITE" width="440" height="440" loading="lazy"></figure>
  </div>
  <section class="section--tight">
    <div class="wrap read prose justify">
{p}
      <div class="btn-row">
        <a class="btn" href="{simona}">Simona Sala</a>
        <a class="btn" href="{valentina}">Valentina Bosio</a>
      </div>
    </div>
  </section>
""".format(kicker=L["about_kicker"], title=L["about_title"], p=paras(L["about"]),
           simona=url(lang, "simona-sala.html"), valentina=url(lang, "valentina-bosio.html"))
    write(lang, "about.html", "%s — BANDITE" % L["about_title"], L["meta_about"], about)

    # ---- VALENTINA ----
    val = """
  <div class="wrap page-head read"><div class="kicker">{k}</div><h1>{t}</h1></div>
  <section class="section--tight"><div class="wrap read prose justify">
{p}
    <div class="btn-row"><a class="btn" href="{about}">{back}</a></div>
  </div></section>
""".format(k=L["valentina_kicker"], t=L["valentina_title"], p=paras(L["valentina"]),
           about=url(lang, "about.html"), back=L["back_about"])
    write(lang, "valentina-bosio.html", "Valentina Bosio — BANDITE", L["valentina"][0], val)

    # ---- SIMONA ----
    sim = """
  <div class="wrap page-head read"><div class="kicker">{k}</div><h1>{t}</h1></div>
  <section class="section--tight"><div class="wrap read prose justify">
{p}
    <p><a href="https://simonasala.com/" target="_blank" rel="noopener">{link}</a></p>
    <div class="btn-row"><a class="btn" href="{about}">{back}</a></div>
  </div></section>
""".format(k=L["simona_kicker"], t=L["simona_title"], p=paras(L["simona"]), link=L["simona_link"],
           about=url(lang, "about.html"), back=L["back_about"])
    write(lang, "simona-sala.html", "Simona Sala — BANDITE", L["simona"][0], sim)

    # ---- WORKS ----
    works = """
  <div class="wrap page-head read">
    <div class="kicker">{kicker}</div><h1>{title}</h1>
    <p class="sub">{sub}</p>
  </div>
  <section class="section--tight"><div class="wrap read">
    <div class="work-list">
      <a class="work-item" href="{u_unseen}"><h3>Unseen</h3><span class="meta">{m_unseen}</span><span class="arrow">&#8594;</span></a>
      <a class="work-item" href="{u_ov}"><h3>Orizzonti Verticali</h3><span class="meta">{m_ov}</span><span class="arrow">&#8594;</span></a>
      <a class="work-item" href="{u_pma}"><h3>Presenti Mai Assenti</h3><span class="meta">{m_pma}</span><span class="arrow">&#8594;</span></a>
    </div>
  </div></section>
""".format(kicker=L["works_kicker"], title=L["works_title"], sub=L["works_sub"],
           u_unseen=url(lang, "unseen.html"), u_ov=url(lang, "orizzonti-verticali.html"), u_pma=url(lang, "presenti-mai-assenti.html"),
           m_unseen=L["work_unseen_meta"], m_ov=L["work_ov_meta"], m_pma=L["work_pma_meta"])
    write(lang, "works.html", "%s — BANDITE" % L["works_title"], L["works_sub"], works)

    # ---- UNSEEN ----
    unseen = """
  <section class="hero hero--page" style="background-image:url('/assets/img/unseen-hero.jpg')">
    <div class="wrap hero__inner"><h1 class="hero__title">Unseen</h1><p class="hero__tag">{tag}</p></div>
  </section>
  <section class="section--tight"><div class="wrap read prose justify">
    <h2 style="text-align:left">{h2}</h2>
{p}
    <div class="btn-row"><a class="btn btn--accent" href="{sonic}">{cta}</a></div>
  </div>
  <div class="wrap read"><div class="figure"><img src="/assets/img/unseen-info.jpg" alt="UNSEEN" loading="lazy"></div></div>
  </section>
""".format(tag=L["unseen_tag"], h2=L["unseen_h2"], p=paras(L["unseen"]), sonic=url(lang, "sonic-walkscape.html"), cta=L["unseen_cta"])
    write(lang, "unseen.html", "Unseen — BANDITE", L["unseen"][0], unseen, og_image="/assets/img/unseen-hero.jpg")

    # ---- ORIZZONTI VERTICALI ----
    ov = """
  <div class="wrap page-head read"><div class="kicker">{k}</div><h1>{t}</h1><p class="sub">{sub}</p></div>
  <section class="section--tight"><div class="wrap read prose justify">
{p}
  </div>
  <div class="wrap">{slide}</div>
  </section>
""".format(k=L["ov_kicker"], t=L["ov_title"], sub=L["ov_sub"], p=paras(L["ov"]), slide=slideshow(OV_IMGS, "Orizzonti Verticali"))
    write(lang, "orizzonti-verticali.html", "Orizzonti Verticali — BANDITE", L["ov_sub"], ov, og_image="/assets/img/ov-1.jpg")

    # ---- PRESENTI MAI ASSENTI ----
    pma = """
  <div class="wrap page-head read"><div class="kicker">{k}</div><h1>{t}</h1><p class="sub">{sub}</p></div>
  <section class="section--tight"><div class="wrap read prose justify">
{p}
  </div>
  <div class="wrap">{slide}</div>
  </section>
""".format(k=L["pma_kicker"], t=L["pma_title"], sub=L["pma_sub"], p=paras(L["pma"]), slide=slideshow(PMA_IMGS, "Presenti Mai Assenti"))
    write(lang, "presenti-mai-assenti.html", "Presenti Mai Assenti — BANDITE", L["pma_sub"], pma, og_image="/assets/img/pma-1.jpg")

    # ---- SONIC WALKSCAPE ----
    sonic = """
  <div class="wrap page-head read"><div class="kicker">{k}</div><h1>{t}</h1><p class="sub">{sub}</p></div>
  <section class="section--tight"><div class="wrap read">
    <div class="btn-row">
      <a class="btn btn--accent" href="https://apps.apple.com/it/app/sonicwalkscape/id6757606425?l=en-GB" target="_blank" rel="noopener">{iphone}</a>
      <a class="btn btn--accent" href="https://play.google.com/store/apps/details?id=com.bandite.sonicwalkscape" target="_blank" rel="noopener">{android}</a>
    </div>
    <div class="figure"><img src="/assets/img/sonic-dossier.png" alt="Sonic WalkScape" loading="lazy"></div>
    <div class="prose">
      <h3 style="color:#b8860b">{need_h}</h3>
      <p>{need}</p>
      <h3 style="color:#b8860b">{how_h}</h3>
      <p>{how}</p>
      <p>{end}</p>
    </div>
  </div></section>
""".format(k=L["sonic_kicker"], t=L["sonic_title"], sub=L["sonic_sub"], iphone=L["sonic_iphone"], android=L["sonic_android"],
           need_h=L["sonic_need_h"], need=L["sonic_need"], how_h=L["sonic_how_h"], how=L["sonic_how"], end=L["sonic_end"])
    write(lang, "sonic-walkscape.html", "Sonic WalkScape — BANDITE", L["meta_sonic"], sonic)

    # ---- RESONAVISSE ----
    reso = """
  <section class="hero hero--page" style="background-image:url('/assets/img/resonavisse-hero.jpg')">
    <div class="wrap hero__inner"><h1 class="hero__title">{t}</h1></div>
  </section>
  <section class="section--tight"><div class="wrap read prose justify">
{p}
  </div>
  <div class="wrap read"><div class="figure figure--center"><img src="/assets/img/resonavisse-logo.png" alt="Resonavisse" loading="lazy"></div></div>
  </section>
""".format(t=L["reso_title"], p=paras(L["reso"]))
    write(lang, "resonavisse.html", "Resonavisse — BANDITE", L["reso"][0], reso, og_image="/assets/img/resonavisse-hero.jpg")

    # ---- STAMPA ----
    press_items = "\n".join(
        '        <a href="{h}" target="_blank" rel="noopener"><span><span class="src">{s}</span><br><span class="who">{w}</span></span><span class="dl">{open}</span></a>'.format(
            h=h, s=s, w=w, open=L["press_open"]) for s, w, h in PRESS)
    press = """
  <div class="wrap page-head read"><div class="kicker">{k}</div><h1>{t}</h1><p class="sub">{sub}</p></div>
  <section class="section--tight"><div class="wrap read"><div class="press">
{items}
  </div></div></section>
""".format(k=L["press_kicker"], t=L["press_title"], sub=L["press_sub"], items=press_items)
    write(lang, "stampa.html", "%s — BANDITE" % L["press_title"], L["press_sub"], press)

    # ---- COLLABORATIONS ----
    logo_items = "\n".join('        <figure><img src="/assets/img/%s" alt="%s" loading="lazy"></figure>' % (s, html.escape(a)) for s, a in LOGOS)
    collab = """
  <div class="wrap page-head read"><div class="kicker">{k}</div><h1>{t}</h1></div>
  <section class="section--tight"><div class="wrap"><div class="logos">
{items}
  </div></div></section>
""".format(k=("Network" if lang=="en" else ("Rete" if lang=="it" else "Réseau")), t=L["nav"]["collaborations"], items=logo_items)
    write(lang, "collaborations.html", "%s — BANDITE" % L["nav"]["collaborations"], L["meta_collab"], collab)

    # ---- CONTACTS ----
    contacts = """
  <div class="wrap page-head read"><div class="kicker">{k}</div><h1>{t}</h1></div>
  <section class="section--tight"><div class="wrap read">
    <p class="contact-big"><a href="mailto:resonavisse@gmail.com">resonavisse@gmail.com</a></p>
    <p class="contact-meta">{meta}</p>
    <div class="btn-row" style="margin-top:2em">
      <a class="btn" href="https://simonasala.com/" target="_blank" rel="noopener">simonasala.com</a>
      <a class="btn" href="{sonic}">{app}</a>
    </div>
  </div></section>
""".format(k=L["contacts_kicker"], t=L["contacts_title"], meta=L["contacts_meta"], sonic=url(lang, "sonic-walkscape.html"), app=L["contacts_app"])
    write(lang, "contacts.html", "%s — BANDITE" % L["contacts_title"], L["meta_contacts"], contacts)

    # ---- 404 ----
    nf = """
  <section class="section" style="text-align:center"><div class="wrap read">
    <div class="kicker" style="color:var(--accent);text-transform:uppercase;letter-spacing:.18em;font-size:.78rem;font-weight:600">{k}</div>
    <h1>{t}</h1>
    <p class="sub" style="color:var(--muted)">{sub}</p>
    <div class="btn-row" style="justify-content:center"><a class="btn btn--accent" href="{home}">{home_l}</a></div>
  </div></section>
""".format(k=L["nf_kicker"], t=L["nf_title"], sub=L["nf_sub"], home=url(lang, "index.html"), home_l=L["nf_home"])
    write(lang, "404.html", "%s — BANDITE" % L["nf_title"], L["nf_sub"], nf)


for lg in LANGS:
    build_all(lg)
    print("built:", lg)

# sitemap (all languages, with hreflang alternates + lastmod)
pages = ["index.html","about.html","works.html","sonic-walkscape.html","resonavisse.html",
         "stampa.html","collaborations.html","contacts.html","unseen.html",
         "orizzonti-verticali.html","presenti-mai-assenti.html","valentina-bosio.html","simona-sala.html"]
urls = ""
for p in pages:
    alts = "".join(
        '    <xhtml:link rel="alternate" hreflang="%s" href="%s%s"/>\n' % (lg, SITE_URL, url(lg, p))
        for lg in LANGS
    ) + '    <xhtml:link rel="alternate" hreflang="x-default" href="%s%s"/>\n' % (SITE_URL, url("en", p))
    for lg in LANGS:
        urls += '  <url>\n    <loc>%s%s</loc>\n    <lastmod>%s</lastmod>\n%s  </url>\n' % (
            SITE_URL, url(lg, p), BUILD_DATE, alts)
with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + '</urlset>\n')

print("\nDone — EN at root, IT in /it/, FR in /fr/.")
