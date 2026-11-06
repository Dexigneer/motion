---
format: 1920x1080
fps: 60
duration: 24.4s
tempo: 128 BPM (1 doba = 0,469 s) — každý strih sedí na dobu
message: "Trips that plan themselves."
arc: Chaos (tabs, appky) → Implózia do nuly → Meet cirro → Ako to funguje (vibe → spoty → itinerár → book) → Tagline → Endcard
audience: 22–40, cestujú často, nenávidia plánovanie v 37 taboch
version: v2
---

# CIRRO — promo (storyboard + scenár) · v2

## Rozhodnutia

- **Firma (fiktívna):** **Cirro** — AI plánovač ciest. Napíšeš „vibe“ (kam, koľko dní, čo máš rád) a Cirro nájde miesta, poskladá itinerár po dňoch a zabookuje všetko jedným ťuknutím. Názov podľa oblakov *cirrus* → svetlo-modrá, vzdušná, „high-altitude“ identita.
- **Message:** Trips that plan themselves. · Tagline: **Less planning. More going.**
- **Formát:** 16:9 · 1920×1080 · **60 fps** · **24,4 s** (Sumi malo 28 s) · bez voiceoveru · vlastný syntetizovaný **128 BPM** hudobný podklad + SFX.
- **Chrbtica (spine):** **bledo-modrý KRUH / prstenec (ring).** Narodí sa z „0“ v „0 plan.“ (02), skáče so squash & stretch (03), stane sa písmenom „o“ v logu (04), cez neho **preletíme ako cez portál** (04→05), z neho vyletí burst (05), mení sa na **map pin** (07), na **tlačidlo** (08) a na konci znova na „o“ v logu (10). Jeden objekt vedie každý prechod.
- **Paleta (tmavá + bledo-modrá):** noc `#060A12` (pozadie) · hlboká `#0C1424` (panely) · navy `#16233A` · linka `#24344D` · **ľad `#CFE8FF` (hlavný akcent)** · **obloha `#8EC5FF`** · mráz `#EEF6FF` (text) · hmla `#7189A8` (sekundárny text). Jediný „flash“ inverzie: scéna 04 (ľadové pozadie, tmavý text) — vizuálny drop.
- **Typografia:** jediný font **Space Grotesk** (variabilná hrúbka 300–700). Žiadne iné fonty. Font je súčasťou animácie — slová sa **nafukujú hrúbkou** a „slamujú“ rozostupom písmen (tracking).
- **Pohyb (úplne iný ako Sumi):** žiadne blur-iny, žiadne whipy doľava, žiadny atrament, žiadny kurzor-ruka, žiadny iris. Namiesto toho:
  - **pružiny a squash & stretch** (`elastic.out`, `back.out(3)`), všetko pristáva s odskokom,
  - **odometer / rolujúce čísla**, **scramble/decode text**, **maska-reveal zdola**,
  - **gravitácia** (taby padajú), **implózia** (appky sa vcucnú do bodu),
  - **venetian slices** (pásy sa rozídu striedavo doľava/doprava),
  - **portálový zoom cez písmeno „o“**,
  - **3D paralaxná stena** obrázkov, **FLIP** karty na pin, **3D kocka** dní,
  - **orbit ikon** okolo tlačidla, **flip mriežky dlaždíc** (wave), **echo-stack** textu s obrysmi,
  - variabilný font: **šírka/hrúbka ako animácia**.
- **Tempo:** každý beat 1–3 s, strih na dobu hudby, vždy niečo odskakuje. Text stojí hotový min. ~0,7 s (krátke frázy 1–3 slová).
- **Ikonky:** vlastné SVG line-ikony (lietadlo, posteľ, vidlička+nôž, mapa, kalendár, karta, chat, foto, lístok, vlak, auto, slnko, pin, srdce, check).
- **Placeholdery obrázkov:** tmavé karty s bledo-modrou šrafou, ikonou obrázka a popisom „IMG 01 · …“ (zoznam na konci).

## Prehľad beatov (128 BPM)

| # | Beat | Čas (s) | Doby | Na obrazovke | Prechod von |
|---|---|---|---|---|---|
| 01 | 37 tabs | 0,00–1,41 | 0–3 | odometer 1→37, mriežka tabov vypučí zo stredu | **gravitácia** – taby padnú |
| 02 | 12 apps. 0 plan. | 1,41–3,28 | 3–7 | 12 ikon obieha text, potom **implózia** → „0 plan.“ | „0“ sa odlepí ako kruh |
| 03 | Bounce → Meet | 3,28–4,69 | 7–10 | kruh skáče (squash), „Meet“ maska-reveal | **venetian slices** |
| 04 | Logo (DROP) | 4,69–7,03 | 10–15 | ľadové pozadie, písmená c-i-r-r-o padajú s odskokom, „o“ = kruh, podtitul scramble | **portál cez „o“** |
| 05 | Vibe | 7,03–9,84 | 15–21 | sklenený bar s rotujúcim okrajom, rýchle písanie, 3 čipy pop, odoslanie | **burst + bar vystrelí hore** |
| 06 | Spots | 9,84–12,66 | 21–27 | 3D paralaxná stena obrázkov, „It finds the spots.“ | **FLIP** karta → pin |
| 07 | Itinerár | 12,66–15,94 | 27–34 | mapa, piny padajú, trasa sa kreslí, **3D kocka** Day 1→2→3 | mapa sa zroluje do kruhu |
| 08 | Book | 15,94–18,28 | 34–39 | tlačidlo „Book trip“, 3 ikony obiehajú a zacvaknú, cena roluje | **flip mriežky dlaždíc** |
| 09 | Tagline | 18,28–21,09 | 39–45 | echo-stack „Less planning.“ → slam „More going.“ | text sa stiahne (wdth) do kruhu |
| 10 | Endcard | 21,09–24,40 | 45–52 | kruh → „o“, wordmark vlna hrúbky, cirro.travel, 2 badge | hold |

**Rytmus:** chaos-chaos (01–02) · napätie (03) · **DROP** (04) · groove UI (05–08) · slam (09) · výdych (10).

---

## Frame 01 — 37 tabs open. (tab hell)
- 0,00–1,41 · prechod in: cut zo tmy
- **Na obrazovke:** veľké **okno prehliadača** (tmavé, 1420×780) s lištou tabov a adresným riadkom. V tele okna obrovské číslo (330 px, ľad) + „tabs open.“
- **Pohyb:** okno vyskočí (`back.out`). Taby pribúdajú **zrýchľujúcim sa tempom** — prvé sú čitateľné („Cheap flights to Lisbon“, „Hotel Alfama – reviews“, „r/lisbon · 5 day itinerary?“…), potom sa **sťahujú, až ostanú len ikonky** (ako v skutočnom prehliadači). Každý nový tab krátko zasvieti, **číslo sa prepne** (1 → 37) a **adresný riadok prepíše** na nové hľadanie. Od 0,26 s sa za oknom **vejárom rozložia 3 ďalšie preplnené okná**. Celá scéna sa pomaly tlačí ku kamere; pri 37 **otras**.
- **Výstup:** 1,02–1,41 všetky taby **vypadnú z lišty gravitáciou**, okná sa zrútia dole.
- **Zvuk:** 0,0 hudba · bliky pri taboch · 0,9 „thock“ · 1,1 „whump“ pádu.

## Frame 02 — 12 apps. 0 plan.
- 1,41–3,28
- **Na obrazovke:** „12 apps.“ (180 px) + 12 ikoniek v dlaždiciach (96 px, radius 28, navy) na **elipse okolo textu**.
- **Pohyb:** ikony vystrelia zo stredu na elipsu (`elastic.out`) a celý prstenec **rotuje v 3D** (perspektíva, zadné menšie/tmavšie). Text „dýcha“ šírkou 75 → 100. 2,35 **implózia**: ikony sa vcucnú do stredu (scale 0, `back.in`), text sa vymení za **„0 plan.“** (slam: scale 1,4 → 1, roztras ±8 px).
- **Výstup:** 2,9–3,28 „plan.“ odpadne, „0“ sa nafúkne a premení na **kruh** (prstenec, ľad).
- **Zvuk:** 1,41 swoosh · orbit „tick-tick“ · 2,35 „thup“ implózie + „snap“.

## Frame 03 — Bounce → Meet
- 3,28–4,69
- **Pohyb:** kruh **3× odskočí** po dobách (squash 1,35/0,7 pri dopade, stretch 0,8/1,25 v letoch), každým skokom sa zmenší. Pri 2. dopade vyrazí **„Meet“** (maska zdola, hrúbka 200 → 800). 4,4 obrazovka sa rozreže na **12 horizontálnych pásov**, ktoré odletia striedavo doľava/doprava a odhalia ľadovú plochu.
- **Zvuk:** 3× „boing“ na dobách · 4,4 swoosh pásov · **riser** do dropu.

## Frame 04 — cirro (DROP)
- 4,69–7,03 · **inverzia:** ľadové pozadie `#CFE8FF`, tmavé písmo `#060A12`
- **Na obrazovke:** wordmark **„cirro“** (300 px, 800, šírka 85), „o“ je **kruh-prstenec** z 03 (tmavý). Nad „i“ je bodka ako malý oblak. Pod tým „trips that plan themselves.“ (42 px).
- **Pohyb:** 4,69 kruh dopadne na pozíciu „o“ (squash). Písmená **c-i-r-r** padajú zhora jedno po druhom na dobu (`bounce.out`, squash pri dopade). 5,9 podtitul **scramble/decode** (náhodné znaky → text). Wordmark celý „dýcha“ hrúbkou.
- **Výstup:** 6,55–7,03 **zoom cez „o“** (scale 1 → 60, origin = stred o), vnútro „o“ je tmavé → sme v ďalšej scéne.
- **Zvuk:** 4,69 **DROP** (kick + bas) · 4× „plop“ písmen · 5,9 „scan“ scramblu · 6,55 zoom whoosh.

## Frame 05 — Describe the vibe
- 7,03–9,84
- **Na obrazovke:** label „Describe the vibe.“ (84 px) **tesne nad barom**. V strede **sklenený bar** (1180×140, radius 70) s **rotujúcim bledo-modrým okrajom** (conic gradient), ikona iskry vľavo, tlačidlo šípky vpravo. Text: „5 days in Lisbon. Food, sun, no museums.“ Pod barom 3 čipy s ikonami: **☀ 5 days** · **🍴 Food** · **📍 Lisbon** (SVG ikony, nie emoji).
- **Pohyb:** bar sa **roztiahne z kruhu** (šírka 140 → 1180, `elastic.out`). Písanie ~30 znakov/s s kurzorom. Čipy **vyskočia** spod baru (y 60 → 0, `back.out(3)`, rotácia ±6° → 0). 9,2 stlačenie šípky (squash), bar sa stiahne späť do kruhu.
- **Výstup:** 9,45–9,84 kruh **vystrelí hore** + **burst** 16 bodiek do strán.
- **Zvuk:** písanie · 3× pop čipov · klik · „fwip“ výstrelu.

## Frame 06 — It finds the spots.
- 9,84–12,66
- **Na obrazovke:** **3D stena** zo 4 stĺpcov obrázkových kariet (rotateX 24°, rotateZ −10°), stĺpce sa posúvajú **rôznou rýchlosťou a smerom** (paralaxa). Cez ňu tmavý gradient a nadpis **„It finds the spots.“** (120 px).
- **Pohyb:** stena vyjde zdola (push hore). Nadpis slovo po slove maskou. 11,7 jedna karta („IMG 03 · Miradouro“) **vyletí dopredu** do stredu (stena sa rozostrí a stmavne), ťuk **♥ Saved** čip pop.
- **Výstup:** 12,3–12,66 karta sa **FLIP-ne a zmenší do pinu** na mape.
- **Zvuk:** 9,84 swoosh hore · 11,7 „zoom“ · 12,0 pop „saved“.

## Frame 07 — Day by day
- 12,66–15,94
- **Na obrazovke:** vľavo **štylizovaná mapa** (tmavá, bledo-modrá mriežka, pobrežie), 4 piny s číslami; vpravo **3D kocka** s kartami **Day 1 / Day 2 / Day 3** (každá: 3 riadky čas · ikona · miesto + malý obrázkový placeholder).
- **Pohyb:** piny **padajú** s odskokom (stagger na dobu), **trasa sa kreslí** medzi nimi (stroke-dash) s bodkou, ktorá po nej beží. Kocka sa **otočí o 90°** na každú 2. dobu (Day 1 → 2 → 3), pri každom otočení riadky novej karty vyskočia.
- **Výstup:** 15,5–15,94 všetko sa zroluje do **kruhu** v strede.
- **Zvuk:** piny „tok“ · kreslenie „scan“ · 2× „thock“ otočenia kocky.

## Frame 08 — Book it. One tap.
- 15,94–18,28
- **Na obrazovke:** „One tap.“ hore; v strede tlačidlo **„Book trip“** (pilulka 520×132, ľad, tmavý text); **3 ikony** (lietadlo, posteľ, vidlička+nôž) v dlaždiciach **obiehajú tlačidlo** v 3D elipse. Pod ním cena **€ 1 284** a čip **„saved € 312“**.
- **Pohyb:** kruh sa roztiahne do tlačidla (squash-stretch). Ikony obiehajú, potom **jedna po druhej zacvaknú** do tlačidla (každá ho pumpne). 17,3 ťuk (ripple krúžky), tlačidlo sa zmení na **✓ Booked**, cena roluje odometrom, čip vyskočí.
- **Výstup:** 17,9–18,28 **flip mriežky dlaždíc** (16×9) diagonálnou vlnou → nová scéna.
- **Zvuk:** 3× „snap“ · klik + „ting“ · rustle tile flipu.

## Frame 09 — Less planning. More going.
- 18,28–21,09
- **Na obrazovke:** **„Less planning.“** — 5 obrysových kópií nad a pod (echo-stack), ktoré sa zosypú do jednej plnej. Potom **„More going.“** (220 px), „going.“ v bledo-modrej.
- **Pohyb:** echo kópie sa roztiahnu vertikálne ako slot-machine a zacvaknú (stagger). 19,7 strih na dobu: **„More going.“ slam** — šírka 75 → 100 a hrúbka 300 → 800 s prestrelením, ľahké roztrasenie kamery.
- **Výstup:** 20,7–21,09 text sa **stiahne na šírku** do bodky → kruh.
- **Zvuk:** 18,28 swell · 19,7 „stamp“ slam · 20,7 fwip.

## Frame 10 — Endcard
- 21,09–24,40
- **Na obrazovke:** „cirro“ (220 px, mráz, „o“ = ľadový kruh), pod ním **cirro.travel** (40 px, hmla) a 2 placeholder badge **„iOS“ / „Android“** (ikona + text). Okolo „o“ pomaly obiehajú 3 malé bodky (oblaky).
- **Pohyb:** kruh dopadne, písmená vyskočia z „o“ doľava (stagger, `back.out`), **vlna hrúbky** 200 → 800 → 600 prejde wordmarkom. URL maska, badge pop. 22,9–24,4 hold, iba pomalý orbit bodiek.
- **Zvuk:** posledný akord + „ting“, potom doznieva.

---

## Placeholdery obrázkov (čo doplniť)

**Spoločný štýl pre všetky:** chladný, modrastý grade (zdvihnuté tiene do navy, potlačené žlté/oranžové, jemné zrno). Svetlé oblohy a more pomôžu, aby fotky ladili s bledo-modrou paletou. Žiadne logá ani čitateľné značky. Ak je na fotke človek, tak zozadu alebo z profilu.

### Scéna 06 — 3D stena „It finds the spots.“ (12 fotiek, pomer **3:4**, min. 900×1200 px)
| ID | Popis v karte | Čo na fotke | Tip na záber |
|---|---|---|---|
| IMG 01 | Alfama · tram 28 | Žltá električka 28 v úzkej strmej uličke Alfamy | Teleobjektív zdola do kopca, električka v strede, modrá obloha |
| IMG 02 | Pastel de nata | Pastéis de nata zblízka na tanieri, škorica | Top-down, studené svetlo z okna, tmavý stôl |
| **IMG 03** | **Miradouro da Graça** | **Hlavná karta** (vyletí dopredu, dostane ♥ Saved): výhľad z vyhliadky na červené strechy a rieku Tejo | Modrá hodinka / tesne po západe, silueta 1–2 ľudí pri zábradlí |
| IMG 04 | Praia da Ursa | Divoká pláž so skalami, more zhora | Dron alebo útes, tyrkysová voda, biela pena |
| IMG 05 | Azulejo walls | Fasáda s modro-bielymi kachličkami (azulejos) | Detail vzoru + kúsok okna, ideálne aj s balkónom |
| IMG 06 | Time Out Market | Jedlo na spoločnom stole, ruky, poháre | Uhol 45°, plytká hĺbka ostrosti, ľudia rozmazaní |
| IMG 07 | LX Factory | Street art / farebná stena, bicykel | Frontálne, grafická kompozícia |
| IMG 08 | Pena Palace | Palác Pena v Sintre v hmle alebo nad lesom | Ďaleký záber, hmla = mysteriózne, chladné tóny |
| IMG 09 | Belém tower | Veža Belém pri rieke | Odraz vo vode, ranné modré svetlo |
| IMG 10 | Rooftop bar | Strešný bar, drinky, mesto pod nimi | Pri západe, svetelné reťaze, siluety |
| IMG 11 | Grilled sardines | Sardinky na grile, citrón, chlieb | Dym z grilu, makro, tmavé pozadie |
| IMG 12 | Sunset tram | Električka / mesto pri západe slnka | Pohyb, rozmazané svetlá, fialovo-modrá obloha |

### Scéna 07 — kocka „Day by day“ (3 malé náhľady, pomer **1:1**, min. 400×400 px)
| ID | Deň | Čo na fotke |
|---|---|---|
| THUMB D1 | Day 1 · Alfama & views | Strechy Alfamy z vyhliadky (môže byť výrez z IMG 03) |
| THUMB D2 | Day 2 · Coast day | Pobrežie Cascais / vlna / pláž zhora |
| THUMB D3 | Day 3 · Sintra hills | Pena Palace alebo zelené kopce Sintry v hmle |

### Scéna 10 — endcard
| ID | Čo tam dať |
|---|---|
| BADGE iOS | Oficiálny „Download on the App Store“ badge (biela/čierna verzia) |
| BADGE Android | Oficiálny „Get it on Google Play“ badge |

**Voliteľné:** logo/ikona appky Cirro, ak vznikne. Teraz je logo čisto typografické („cirro“ s kruhom ako „o“).

## Build notes (v1)

- Celé video je v `index.html` — jedna GSAP časová os, 24,4 s, **60 fps**, strihy na doby 128 BPM (konštanta `B = 60/128`).
- Font: `assets/fonts/SpaceGrotesk.woff2` — variabilná verzia Space Grotesk (OFL, hrúbka 300–700; dodaný rez Medium = 500 je v nej). Hrúbka sa animuje cez CSS premennú `--wg`.
- Hudba: `assets/music/cirro_bed.wav` je **dočasný** syntetizovaný 128 BPM podklad (`tools/make_audio.py`), drop presne na 4,6875 s. Výmena = rovnaký súbor s licencovanou skladbou 128 BPM s dropom na dobe 10.
- SFX: dočasné (`tools/make_sfx.py` zo Sumi + `boing`, `riser`, `blip`, `slam` z `tools/make_audio.py`), každý zvuk je samostatná `<audio id="sfx-*">` stopa.
- Motion blur (shutter) je na skákajúcom kruhu (03), padajúcich písmenách loga (04), výstrele kruhu (05) a hero karte (06).
- Badge na endcarde sú **placeholdery** (prerušovaný okraj) — nahradiť oficiálnymi App Store / Google Play badge.
- Render: `npx hyperframes@0.9.13 render -o renders/cirro_v2.mp4 --quality delivery`.

## Changes from v1

- Font → **Space Grotesk** (jediný).
- „Tell it the vibe.“ → **„Describe the vibe.“**, posunuté tesne nad bar.
- Scéna 01 prerobená: namiesto mriežky rovnakých pilulek je to **okno prehliadača s množiacimi sa a sťahujúcimi sa tabmi**, meniacim sa adresným riadkom a vejárom ďalších okien.

## Changes from v2 (fotky)

- Všetkých 15 fotiek je zapojených (`assets/images/img01–12.webp`, `thumb_d1–d3.webp`).
- Karty majú namiesto „IMG 0x“ krátky popis kategórie (ALFAMA, EAT, VIEWPOINT, BEACH, WALK, ART, DAY TRIP, BELÉM, NIGHT, RIDE) a názov miesta. Spodok karty má tmavý prechod, aby bol text čitateľný.
- Fotky na šírku (07–12) sú orezané cez `background-position` na hlavný motív: mural s tvárou a kvetom, palác, veža, drinky s výhľadom, sardinky, električka.
- Stena: stĺpec `c`, riadok `r` → fotka `(7c + r) mod 12`, takže sú viditeľné všetky a rovnaké fotky nie sú vedľa seba.
