---
format: 1920x1080
fps: 60
duration: 24.4s
tempo: 128 BPM (1 doba = 0,469 s) — každý strih sedí na dobu
message: "Trips that plan themselves."
arc: Chaos (tabs, appky) → Implózia do nuly → Meet cirro → Ako to funguje (vibe → spoty → itinerár → book) → Tagline → Endcard
audience: 22–40, cestujú často, nenávidia plánovanie v 37 taboch
version: v1
---

# CIRRO — promo (storyboard + scenár) · v1

## Rozhodnutia

- **Firma (fiktívna):** **Cirro** — AI plánovač ciest. Napíšeš „vibe“ (kam, koľko dní, čo máš rád) a Cirro nájde miesta, poskladá itinerár po dňoch a zabookuje všetko jedným ťuknutím. Názov podľa oblakov *cirrus* → svetlo-modrá, vzdušná, „high-altitude“ identita.
- **Message:** Trips that plan themselves. · Tagline: **Less planning. More going.**
- **Formát:** 16:9 · 1920×1080 · **60 fps** · **24,4 s** (Sumi malo 28 s) · bez voiceoveru · vlastný syntetizovaný **128 BPM** hudobný podklad + SFX.
- **Chrbtica (spine):** **bledo-modrý KRUH / prstenec (ring).** Narodí sa z „0“ v „0 plan.“ (02), skáče so squash & stretch (03), stane sa písmenom „o“ v logu (04), cez neho **preletíme ako cez portál** (04→05), z neho vyletí burst (05), mení sa na **map pin** (07), na **tlačidlo** (08) a na konci znova na „o“ v logu (10). Jeden objekt vedie každý prechod.
- **Paleta (tmavá + bledo-modrá):** noc `#060A12` (pozadie) · hlboká `#0C1424` (panely) · navy `#16233A` · linka `#24344D` · **ľad `#CFE8FF` (hlavný akcent)** · **obloha `#8EC5FF`** · mráz `#EEF6FF` (text) · hmla `#7189A8` (sekundárny text). Jediný „flash“ inverzie: scéna 04 (ľadové pozadie, tmavý text) — vizuálny drop.
- **Typografia:** jediný font **Bricolage Grotesque** (variabilný: šírka 75–100, hrúbka 200–800). Žiadne iné fonty. Font je súčasťou animácie — písmená **dýchajú šírkou a hrúbkou** (wdth/wght), slová sa „nafukujú“ a „sťahujú“.
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

## Frame 01 — 37 tabs
- 0,00–1,41 · prechod in: cut zo tmy
- **Na obrazovke:** obrovské rolujúce číslo **„37“** (260 px, 800, ľad) + „tabs.“ (mráz). Za ním mriežka 12×9 „browser tabov“ (pilulky 128×40 s favicon štvorčekom a sivou čiarkou).
- **Pohyb:** 0,05 prvý tab vypučí v strede (`back.out(3)`), potom mriežka **vypučí zo stredu von** (stagger podľa vzdialenosti). Odometer cifier roluje 01→37 s prestrelením (každá cifra je stĺpec 0–9 vo vertikálnej maske). „tabs.“ príde maskou zdola. Číslo pri dopade **pumpne** (scale 1.15 → 1).
- **Výstup:** 1,10–1,41 taby **padnú gravitáciou** (y +1200, rotácia ±, `power2.in`, stagger), číslo sa stlačí (scaleY 0,2) a zmizne.
- **Zvuk:** 0,0 hudba (hi-hat + bas pulz) · pop-y pri vypučaní · 1,1 „whump“ pádu.

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

## Frame 05 — Tell it the vibe
- 7,03–9,84
- **Na obrazovke:** label „Tell it the vibe.“ hore (64 px). V strede **sklenený bar** (1180×140, radius 70) s **rotujúcim bledo-modrým okrajom** (conic gradient), ikona iskry vľavo, tlačidlo šípky vpravo. Text: „5 days in Lisbon. Food, sun, no museums.“ Pod barom 3 čipy s ikonami: **☀ 5 days** · **🍴 Food** · **📍 Lisbon** (SVG ikony, nie emoji).
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

| ID | Scéna | Čo tam dať (odporúčaný záber) | Pomer |
|---|---|---|---|
| IMG 01 | 06 | Lisabon – Alfama, úzka ulička so žltou električkou 28 | 3:4 |
| IMG 02 | 06 | Pastel de nata zblízka (top-down) | 3:4 |
| IMG 03 | 06 + 07 | Miradouro (vyhliadka) nad strechami pri západe slnka – **hlavná karta** | 3:4 |
| IMG 04 | 06 | Pláž Praia da Ursa / Cascais, more zhora | 3:4 |
| IMG 05 | 06 | Azulejos – modré kachličky na fasáde | 3:4 |
| IMG 06 | 06 | Time Out Market / jedlo na stole s priateľmi | 3:4 |
| IMG 07 | 06 | LX Factory / street art | 3:4 |
| IMG 08 | 06 | Sintra – Palácio da Pena | 3:4 |
| IMG 09 | 06 | Belém – veža pri rieke | 3:4 |
| IMG 10 | 06 | Rooftop bar s výhľadom | 3:4 |
| IMG 11 | 06 | Sardinky na grile / street food | 3:4 |
| IMG 12 | 06 | Ľudia na električke / cestovanie | 3:4 |
| THUMB D1–D3 | 07 | malé náhľady pre každý deň (Alfama, Cascais, Sintra) | 1:1 |

Všetky obrázky ideálne s **chladným/modrým gradingom** (alebo tmavé s modrým nádychom), aby sedeli k palete.

## Build notes (v1)

- Celé video je v `index.html` — jedna GSAP časová os, 24,4 s, **60 fps**, strihy na doby 128 BPM (konštanta `B = 60/128`).
- Font: `assets/fonts/BricolageGrotesque.woff2` (OFL, variabilné osi `wdth` + `wght`, licencia vedľa). Šírka a hrúbka sa animujú cez CSS premenné `--wd` / `--wg`.
- Hudba: `assets/music/cirro_bed.wav` je **dočasný** syntetizovaný 128 BPM podklad (`tools/make_audio.py`), drop presne na 4,6875 s. Výmena = rovnaký súbor s licencovanou skladbou 128 BPM s dropom na dobe 10.
- SFX: dočasné (`tools/make_sfx.py` zo Sumi + `boing`, `riser`, `blip`, `slam` z `tools/make_audio.py`), každý zvuk je samostatná `<audio id="sfx-*">` stopa.
- Motion blur (shutter) je na skákajúcom kruhu (03), padajúcich písmenách loga (04), výstrele kruhu (05) a hero karte (06).
- Badge na endcarde sú **placeholdery** (prerušovaný okraj) — nahradiť oficiálnymi App Store / Google Play badge.
- Render: `npx hyperframes@0.9.13 render -o renders/cirro_v1.mp4 --quality delivery`.
