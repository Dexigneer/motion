---
format: 1920x1080
duration: 24s
fps: 60
tempo: 128 BPM (1 doba = 0,469 s · 1 takt = 1,875 s) — každý strih sedí na dobu
message: "Raw clips in. Fire reels out."
arc: Bolesť (400 klipov, 0 reels) → Chaos → ÚDER (Meet FLINT) → Ako to funguje (drop → cut → features) → Výsledok → Tagline → Endcard
audience: tvorcovia, malé značky, social media manažéri
version: v1
---

# FLINT — promo (storyboard + scenár) · v1

## Rozhodnutia

- **Firma (fiktívna):** **FLINT** — AI strihač do mobilu. Hodíš doň surové klipy z galérie a za pár sekúnd máš hotový reel: strih na beat, titulky, preformátovanie na 9:16, silný „hook“. Názov = *kresadlo* → celá identita je **iskra**: dva kamene sa zrazia, vyletí iskra, z nej je logo.
- **Message:** Raw clips in. Fire reels out.
- **Formát:** 16:9 · 1920×1080 · **60 fps** · **24 s** (Sumi 28 s) · bez voiceoveru · dočasná hudba 128 BPM + SFX (syntetizované, dajú sa vymeniť 1:1). Texty v angličtine.
- **Paleta (tmavá + červená):** uhoľ `#0B0A0D` (pozadie) · grafit `#16131A` (panely) · linka `#2A2430` · **žeravá červená `#FF2A3D`** (hlavný akcent) · tmavá karmínová `#B0101F` · pahreba `#FF6B4A` (iba iskry) · kosť `#F5EEEE` (text) · popol `#8D8592`. Žiadne fialové, modré ani neónové gradienty.
- **Typografia:** **jediný font — Archivo (variabilný)**, osi *wght 100–900* + *wdth 62–125*. Expresivita sa robí **iba osami toho istého písma**: úzke+čierne (Condensed Black) pre nárazy, široké (Expanded) pre značku, stredné pre UI. Písmo sa v animácii **naťahuje ako guma** (tween `font-variation-settings`).
- **Spine (vodiaca línia):** **iskra / červená bodka**. Bodka je odometer kurzor (01), zadná strana dlaždíc (02), iskra zo zrážky (03), bodka nad „i“ v logu, do ktorej letíme (03→04), playhead (05), skóre (06c), srdiečka (07) a nakoniec skákajúca loptička, z ktorej je logo (09).
- **Pohybový jazyk (úplne iný ako Sumi):**
  - Sumi = mäkké blur-iny, smer doľava, papier. **FLINT = gumené squash & stretch, elastické prestrely, tvrdé snapy, vertikálny smer (hore/dole) a masky.**
  - Žiadne „blur-in“ textov. Text vstupuje cez **masky, sloty (slot machine), pády so sploštením, rozťahovanie šírky písma.**
  - Easingy: vstupy `back.out(2–3)` / `elastic.out(1, .45)` 0,35–0,6 s · odchody `power4.in` 0,18–0,25 s · motion blur iba na rýchlych snapoch.
  - Všetko „dýcha na beat“: na každú dobu malý pump (scale 1,04 → 1) v pozadí.
- **Prechody (každý iný):** horizontálny rez (01→02) · 3D otočenie dlaždíc na červenú (02→03) · zrážka kameňov + kruhový výbuch (03) · zoom do bodky nad „i“ (03→04) · žalúzie (04) · prelet cez telefón (04→05) · diagonálny rez (06a) · žalúzie z bodu (06b) · iris z ikony (06c) · 3D vejár (07) · slot-machine roll (08) · kolaps do loptičky (08→09).
- **Čitateľnosť:** aj pri tempe každý text stojí hotový **≥ 0,6 s**; kľúčové vety ≥ 1 s. Max. 4 slová naraz.
- **Placeholdery obrázkov:** tmavé šrafované dlaždice s ikonkou fotoaparátu + kódom (`CR-01`, `CLIP-1`, `CAP`, `RF`, `REEL-A`, `FIRE`). Zoznam na konci.

## Prehľad beatov

| # | Beat | Čas (s) | Doby | Na obrazovke | Prečo |
|---|---|---|---|---|---|
| 01 | Hook | 0,00–1,88 | 4 | „400 clips.“ (odometer) → „0 reels.“ | Bolesť v dvoch číslach |
| 02 | Chaos | 1,88–3,75 | 4 | galéria 24 klipov sa trasie · „Still editing?“ · hodiny | Strih trvá večnosť |
| 03 | Úder | 3,75–6,56 | 6 | „Meet“ guma → dva kamene → ISKRA → logo **flint** | DROP hudby, meno |
| 04 | Drop | 6,56–9,38 | 6 | telefón vyskočí, 6 klipov doň vletí po oblúkoch | Ako to funguje 1 |
| 05 | Cut | 9,38–13,13 | 8 | timeline: playhead, nožnice, výmena klipov, waveform | Ako to funguje 2 |
| 06 | Features | 13,13–15,94 | 6 | 3× rýchlo: Captions · Reframe · Hook score | Čo všetko vie |
| 07 | Výsledok | 15,94–18,75 | 6 | 3 reels vo vejári, srdiečka, „Ready in 12 s“ | Dôkaz |
| 08 | Tagline | 18,75–20,63 | 4 | „Raw clips in.“ ⟶ slot ⟶ „Fire reels out.“ | Message |
| 09 | Endcard | 20,63–24,00 | 7 | loptička skáče → iskra → **flint** · flint.video · CTA | Zapamätanie |

**Rytmus:** rýchlo (01) · nervózne (02) · **BUM + ticho na 1 dobu (03)** · pružne (04) · mechanicky na beat (05) · **najrýchlejšie** (06) · rozlet (07) · dva údery (08) · doskok a pokoj (09).

## Hudba a zvuk

- **Hudba (dočasná, `assets/music/temp_beat.wav`):** 128 BPM, 0–3,75 len kick + hi-hat + stúpajúci riser, **3,75 drop** (clap, bas, stab), 15,94 krátky break (1 doba ticho pred výsledkom), 20,63 finálny úder a doznenie. Odporúčanie pre finál: licencovaný energický *phonk / UK garage / hyperpop beat* 125–130 BPM bez vokálu, −14 LUFS pod SFX.
- **SFX:** tiky odometra, „thud“ sploštenia, mechanické klik-klak dlaždíc, kresanie kameňov + iskry (crackle), pružinové „boing“, cvaknutia nožníc, whoosh pri preletoch, popy čipov, ťuk srdiečok, cinknutie na konci.

---

## Frame 01 — 400 clips. 0 reels.

- start 0,00 · duration 1,88 · transition_in: cut from black
- **Na obrazovke:** uprostred „**400** clips.“ (Archivo wght 900 / wdth 62, 230 px, kosť). Pod tým „**0** reels.“ — nula v červenej.
- **Pohyb:** 0,05 každá číslica „4 0 0“ je **valček odometra** — rolujú zdola (0→9→cieľ), každý valček zastaví o 0,06 s neskôr s prestrelom (`back.out(3)`). „clips.“ sa vysúva spod masky zdola. 0,94 (doba 3) „0 reels.“ **padne zhora**, pri dopade sa sploští (scaleY 0,6 / scaleX 1,3 → 1, `elastic.out`), horný riadok sa od nárazu nadhodí (y −30 → 0). Červená nula pulzuje na dobu.
- **Výstup:** 1,70 **horizontálny rez**: obrazovka sa rozdelí v strede, horná polovica letí hore, dolná dole (`power4.in` 0,18 s, motion blur) → odhalí galériu.
- **Zvuk:** 0,05–0,3 rýchle tiky odometra · 0,94 hlboký „thud“ · 1,70 ostrý „schwip“.

## Frame 02 — Still editing?

- start 1,88 · duration 1,88 · transition_in: split-slice
- **Na obrazovke:** mriežka **6×4 = 24 dlaždíc** (placeholder `CR-01…CR-24`, 200×200, radius 26, mierne pootočené), cez ne veľký pill „**Still editing?**“ (wdth 125 / wght 800, 120 px) a vedľa **ikona hodín** (čiara, ručičky sa točia rýchlo).
- **Pohyb:** 1,88 dlaždice **vyskakujú od stredu von** (domino, scale 0 → 1, `back.out(2.6)`, stagger podľa vzdialenosti 0,012 s). Hneď potom sa celá mriežka **nervózne trasie** (deterministický šum ±6 px, ±2°). 2,35 pill vletí zdola s pružinou; ručičky hodín sa otočia 3× za sekundu.
- **Výstup:** 3,28 všetkých 24 dlaždíc sa **3D otočí** (rotateY 180°) od stredu — zadné strany sú **červené** → 3,60 dlaždice sa zväčšia a zlejú do súvislej červenej plochy.
- **Zvuk:** 1,88 kaskáda drobných klikov · 2,35 „boing“ · tik-tak · 3,28 rýchle „flap-flap-flap“ (otočenie) · 3,4 riser.

## Frame 03 — Meet FLINT

- start 3,75 · duration 2,81 · transition_in: tile-flip to red
- **Na obrazovke:** červená plocha → čierne „**Meet**“ (wght 900) · dva čierne **kamene** (polygóny) · **iskra** · logo: ikona iskry (štvorcípa hviezda s odrezaným rohom) + wordmark „**flint**“ (wdth 125, wght 900, 250 px, kosť; bodka nad „i“ je červený štvorček) · podtitul „AI that cuts your reels.“ (wght 500, 44 px, popol).
- **Pohyb:** 3,75 **DROP**. „Meet“ sa **naťahuje ako guma**: wdth 62 → 125 → 80 → 110 (elastic), zároveň skáče (y −40/0). 4,45 „Meet“ sa stiahne (scaleX 0) a zľava + sprava **vletia dva kamene** a narazia do seba v strede (4,69 = doba 3). **Zrážka:** biely záblesk (1 frame), 16 iskier sa rozprskne (balistické dráhy s gravitáciou), z bodu nárazu **expanduje čierny kruh** cez celú obrazovku (clip-path circle) → pozadie je čierne. 4,75 ikona iskry vyskočí (`elastic.out`, rotácia −90 → 0) a za ňou sa točia **lúče** (sunburst, 12 lúčov, opacity 8 %). 5,0 písmená „f l i n t“ **padajú zhora** po jednom, každé sa pri dopade sploští a odrazí; bodka nad i dopadne posledná s „ping“. 5,5 podtitul sa odhalí maskou po slovách.
- **Výstup:** 6,20 kamera **letí do červenej bodky nad „i“** (scale 1 → 60 so stredom na bodke, `power3.in` 0,36 s) → celá obrazovka je červená.
- **Zvuk:** 3,75 DROP + „bwamp“ · 3,8–4,3 gumové „wub“ · 4,69 **kresnutie + crackle iskier** · 4,75 „whomp“ · 5,0–5,4 päť „tok“ dopadov · 5,4 „ping“ · 6,2 whoosh dnu.

## Frame 04 — Drop your clips.

- start 6,56 · duration 2,81 · transition_in: zoom-through-dot
- **Na obrazovke:** vpravo **telefón** (grafit, 430×860, radius 64, notch) s UI FLINT: hore „New reel“, uprostred zásobník klipov, dole červené tlačidlo „Cut it ✦“. Vľavo nadpis „**Drop your**“ / „**clips.**“ (wght 900, wdth 75, 150 px; „clips.“ červené) + čip s ikonou upload „6 clips added“.
- **Pohyb:** 6,56 červená plocha sa rozpadne na **8 horizontálnych žalúzií**, ktoré sa otočia (rotateX 90°) a odhalia čierne pozadie. Telefón **vyskočí zdola** (y 900 → 0, `back.out(1.8)`, so squash pri dopade). Nadpis: slová **padnú** s odrazom. 7,2–8,4 šesť klipov `CLIP-1…6` (dlaždice 220×160) priletí z ľavého horného rohu po **parabolických oblúkoch** (rotujú), každý dopadne do telefónu na kôpku; telefón sa pri každom chytení **zatrasie ako želé** (scaleX/scaleY 1,04/0,96). Čip počíta 1→6 (číslo sa preklopí).
- **Výstup:** 8,9 tlačidlo „Cut it“ sa stlačí (squash), 9,05 kamera **preletí cez displej telefónu** (telefón scale 1 → 8, motion blur).
- **Zvuk:** 6,56 „flap“ žalúzií · 6,7 „boing“ telefónu · 7,2–8,4 šesť „fwip+pop“ (stúpajúca výška) · 8,9 klik · 9,05 whoosh.

## Frame 05 — Cuts on the beat.

- start 9,38 · duration 3,75 · transition_in: fly-through-phone
- **Na obrazovke:** hore nadpis „Cuts **on the beat.**“ (wdth 110, wght 800, 96 px). V strede **timeline**: rad 6 klipov `CLIP-1…6` (180×120, radius 18) na stope, pod ním **waveform** (48 stĺpikov), **červený playhead** s trojuholníkom. Nad stopou sa objavujú **čipy s ikonami**: ♪ „Beat sync“ · ✂ „Smart cuts“ · CC „Captions“.
- **Pohyb:** 9,38 stopa sa **rozbalí zo stredu** (klipy vystrelia do strán ako harmonika, `back.out`). Waveform stĺpiky **skáču na dobu** (každá doba nový „úder“, stĺpiky padajú `power2.out`). Slová nadpisu menia hrúbku na dobu (wght 300 ↔ 900). 9,9 playhead prebehne stopou; na **každej dobe**: ikona nožníc cvakne (čepele sa zavrú) a klip sa **rozreže** (medzera sa otvorí s pružinou). 11,3 klipy 2 a 5 si **vymenia miesto skokom po oblúku**, klip 4 sa **zmačká** (scaleX 0) — vystrihnutý. Čipy vyskakujú `elastic.out` na doby 10,3 / 10,8 / 11,25.
- **Výstup:** 12,7 všetky klipy sa **zrazia do jedného** v strede (stack), ktorý sa preklopí na výšku 9:16 a pokračuje ako diagonálny rez do 06.
- **Zvuk:** 9,38 „zip“ rozbalenia · každé strihnutie „snip“ (4×) · 11,3 dva „fwip“ + „crunch“ · čipy „pop“ · 12,7 „slam“.

## Frame 06 — Features (rapid fire)

- start 13,13 · duration 2,81 · 3 × 0,94 s · každý panel iný prechod
- **06a Captions (13,13–14,06)** · in: **diagonálny rez** (červený klin preletí šikmo a za sebou nechá panel). Placeholder `CAP` (osoba hovorí do kamery, 16:9 celoplošne, stmavené). Titulky „**this** **is** **actually** **insane**“ (wght 900, 110 px) — aktívne slovo dostane **červený box, ktorý skáče** zo slova na slovo (FLIP), každé slovo pri aktivácii pumpne. Ikona CC + štítok „Auto captions“ vľavo hore.
- **06b Reframe (14,06–15,00)** · in: **žalúzie (vertikálne pásy) zo stredu**. Placeholder `RF` (široký záber 16:9). Rámik 16:9 sa **elasticky stiahne na 9:16** (clip-path) a sleduje osobu (malé dorovnanie); okolie stmavne. Ikona crop + „Auto reframe“.
- **06c Hook score (15,00–15,94)** · in: **iris z ikony plamienka**. Polkruhový **meter**, ručička sa rozkýve (elastic) a zastaví na **98**; číslo sa točí odometrom; plamienok bliká. Štítok „Hook score“.
- **Zvuk:** 13,13 „schwing“ · každé slovo titulku „tick“ · 14,06 „flap“ · 14,3 „boing“ · 15,0 „whomp“ · ručička „wobble“ · 15,7 „ding“.

## Frame 07 — Ready in 12 seconds.

- start 15,94 · duration 2,81 · transition_in: 3D fan
- **Na obrazovke:** tri reels 9:16 (`REEL-A`, `REEL-B`, `REEL-C`, 360×640, radius 40) vo **vejári v 3D** (rotateY −28° / 0 / 28°, krajné vzadu). Vľavo dole veľké „**12 s**“ odometer + „to a ready reel“; vpravo hore čip „**+3.4×** views“. Okolo stredného reelu vyskakujú **srdiečka, komentáre, šípky „share“** (ikony v červenej a kosťovej) a stúpajú s kývaním.
- **Pohyb:** 15,94 break (1 doba ticho) — reels **vyletia zo stredu** a rozložia sa do vejára (`back.out(1.6)`, stagger 0,05). Stredný sa „hrá“ — **progress bar** na spodku beží. 16,6 ikony praskajú v rytme (6×, scale 0 → 1,3 → 1, potom y −300 so sínusovým kývaním). Čísla rolujú.
- **Výstup:** 18,55 vejár sa **zloží** (krajné zajdú za stredný), stredný sa sploští na čiaru → slot.
- **Zvuk:** 15,94 ticho + „whoosh“ rozletu · 16,6–17,8 šesť „pop/ťuk“ · číselné tiky · 18,55 „thwip“.

## Frame 08 — Raw clips in. Fire reels out.

- start 18,75 · duration 1,88 · transition_in: slot
- **Na obrazovke:** obrovský text vo **výreze/okne** (slot machine): riadok 1 „**Raw clips in.**“ (kosť, wdth 62, wght 900, 200 px) → riadok 2 „**Fire reels out.**“ — slovo „Fire“ je vyplnené obrázkom `FIRE` (placeholder textúry; v placeholderi červený gradient).
- **Pohyb:** 18,75 riadok 1 sa **pretočí** zdola (slot roll s prestrelom a motion blur). 19,69 (doba 3) **slot roll** → riadok 2; „out.“ sa **naťahuje do šírky** (wdth 62 → 125) a vytlačí ostatné; celé to na dobu pumpuje.
- **Výstup:** 20,45 text sa **zrúti do červenej loptičky** (všetko scale → 0 do stredu, loptička vznikne z bodky za „out.“).
- **Zvuk:** 18,75 „ka-chunk“ · 19,69 „ka-chunk“ + stretch „wuuup“ · 20,45 „sup“.

## Frame 09 — Endcard

- start 20,63 · duration 3,37 · transition_in: collapse-to-ball
- **Na obrazovke:** čierne pozadie, logo (ikona iskry 150 px, červená) + „**flint**“ (wdth 125, wght 900, 200 px) · pod tým „flint.video“ (wght 500, 36 px, popol) · CTA pill „**Try it free** →“ (červená, 34 px).
- **Pohyb:** 20,63 červená loptička **skáče 2×** (squash pri dopade, stretch vo vzduchu, `power2.out/in`), pri 2. dopade **vystrelí iskru** — loptička sa premení na ikonu iskry (rotácia 90° + elastic). 21,6 wordmark sa **vysunie spoza ikony** (maska, písmená so staggerom a jemným prestrelom šírky). 22,1 URL + CTA vyskočia; okolo CTA **2 pulzujúce kruhy**. 22,6–24,0 **pokoj** (len jemné dýchanie lúčov a pulz CTA).
- **Zvuk:** 20,63 dva „boing/thud“ · 21,1 „zap“ · 21,6 „swish“ · 22,1 „pop“ · záverečné „ding“ s dozvukom.

---

## Placeholdery obrázkov — čo doplniť

| Kód | Kde | Formát | Čo tam dať |
|---|---|---|---|
| `CR-01…CR-24` | 02 galéria | 1:1, min. 400×400 | 24 rôznych „náhodných“ záberov z mobilnej galérie: jedlo, západ slnka, pes, kamaráti, koncert, výlet, posilňovňa, mesto v noci… (pokojne neostré/amatérske — má to pôsobiť chaoticky) |
| `CLIP-1…CLIP-6` | 04 telefón, 05 timeline | 3:2, min. 600×400 | 6 surových klipov jedného príbehu (napr. víkend na skate/bike výlete): príchod · trik · pád · smiech · západ slnka · skupinová fotka |
| `CAP` | 06a Captions | 16:9, 1920×1080 | človek hovorí do kamery (vlog / talking head), tvár v strede |
| `RF` | 06b Reframe | 16:9, 1920×1080 | široký záber s jednou osobou mierne vľavo od stredu (napr. tanečník, športovec) |
| `REEL-A/B/C` | 07 výsledok | 9:16, 1080×1920 | 3 hotové reels (screeny z appky / výsledné vertikálne videá), stredný = najlepší |
| `FIRE` | 08 výplň slova „Fire“ | 16:9 | textúra / záber s ohňom, iskrami alebo červeným svetlom (vyplní písmená) |

## SFX — cue sheet

| Čas (s) | Zvuk | Beat |
|---|---|---|
| 0,05–0,30 | tiky odometra | 01 |
| 0,94 | thud | 01 |
| 1,70 | schwip (rez) | 01→02 |
| 1,88 | kaskáda klikov | 02 |
| 2,35 | boing | 02 |
| 3,28 | flap ×3 | 02→03 |
| 3,75 | DROP / bwamp | 03 |
| 4,69 | kresnutie + crackle | 03 |
| 5,0–5,4 | 5× tok · ping | 03 |
| 6,20 | whoosh dnu | 03→04 |
| 6,56 / 6,70 | flap · boing | 04 |
| 7,2–8,4 | 6× pop (stúpajúci) | 04 |
| 8,90 / 9,05 | klik · whoosh | 04→05 |
| 9,9–11,3 | 4× snip · fwip · crunch | 05 |
| 10,3 / 10,8 / 11,25 | 3× pop | 05 |
| 12,70 | slam | 05→06 |
| 13,13 / 14,06 / 15,0 | schwing · flap · whomp | 06 |
| 15,70 | ding | 06 |
| 15,94 | whoosh | 07 |
| 16,6–17,8 | 6× pop | 07 |
| 18,75 / 19,69 | ka-chunk ×2 | 08 |
| 20,63–21,1 | 2× boing · zap | 09 |
| 22,1 / 22,6 | pop · ding | 09 |

## Build notes (v1)

- Celé video je v `index.html` (jedna časová os GSAP, 24 s, 60 fps). Motion blur (shutter) je v `assets/vendor/motion-blur.js`, zapnutý len na rýchlych snapoch: rez 01, kamene 03, lietajúce klipy 04, slot 08.
- Font: Archivo variabilný (`assets/fonts/Archivo.woff2`, OFL) — osi `wdth` 62–125 a `wght` 100–900 sa animujú priamo (`font-variation-settings`).
- Hudba aj SFX sú **dočasné**, syntetizované skriptom `tools/make_audio.py` (`python3 tools/make_audio.py`). Každý zvuk je samostatná stopa `sfx-NN-názov` — dá sa vymeniť 1:1 alebo posunúť v Studiu. Strihy sedia na mriežku 128 BPM (doba 0,469 s); pri inej hudbe treba časy prepočítať.
- Placeholdery sú `.ph` dlaždice s kódom; výmena = nahradiť `<div class="ph">…</div>` za `<img src="assets/img/…">` s rovnakými rozmermi (`object-fit: cover`). „Fire“ v 08 = `background-image` na `.fire`.
- Render: `npm run render` → `renders/`.

## Changes from v1 (spätná väzba)

> „Príliš generické tlačidlá, zaoblené rohy, search bar… glassmorphism, zmeň pozadie, nech je to prémiové a unique.“

- **Pozadie „obsidián + roztavený hodváb“:** namiesto plochého tmavého gradientu tmavý obsidián, cez ktorý tečú dve rozmazané stuhy červeného svetla (karmín → žeravá → pahreba) s ostrou svetelnou hranou. Stuhy sa pomaly prelievajú (morph tvaru), pod nimi driftujú tri svetelné jadrá; na každú dobu svetlo zadýcha. Šumová textúra (grain) odstránená.
- **Glassmorphism:** lišta „Still editing?“ (teraz príkazová lišta s časovačom a REC počítadlom), štítok „clips added“, čipy funkcií, panel timeline, štítky v 06, meter skóre a reakcie v 07 sú matné sklo — rozmazávajú svetlo za sebou, majú jemný tónovaný odraz a gradientový okraj (biela → červená).
- **Tvarový jazyk = úlomok kresadla:** žiadne „pilulky“. Všetky tlačidlá, lišty a štítky majú **zrezané protiľahlé rohy** (facety), ikony sedia v malých zrezaných červených dlaždiciach. Titulkový box je šikmý „highlighter“.
- **Tlačidlá:** „Cut it“ a „Try it free“ sú červené sklo s vnútorným svetlom, prebehnutým odleskom (sheen), žiarou pod sebou; CTA má šípku vo vlastnom zrezanom okne a pulzujúce facetové obrysy.
- **Placeholdery:** tmavé šošovkové karty s **rohmi hľadáčika** a jemným červeným svetlom namiesto pruhov.
- **Svetelné efekty namiesto lúčov:** šoková vlna (tenký žiariaci prstenec), anamorfný horizontálny odlesk a bloom pri náraze (01, 03, 09). Prechod z červenej na tmu v 03 je teraz „diera“, ktorá sa roztvára zo stredu a odhalí svetelné pozadie.
- **Detaily:** kamene z obsidiánu s červeným okrajovým svetlom, wordmark s jemným kovovým prechodom, bodka nad „i“ je kosoštvorcová faseta, telefón má titánový rám a sklenený displej, meter má stupnicu, lopta je lesklá guľa, linky sú svetelné čepele.
