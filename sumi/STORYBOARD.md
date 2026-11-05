---
format: 1920x1080
duration: 35s
message: "Every meeting ends with one clear plan."
arc: Pain → Turn (Introducing) → Show (sources → ask → plan → fix) → Payoff → Logo
audience: team leads, founders, PMs who live in back-to-back calls
mode: collaborative
version: v1
---

# SUMI — promo (storyboard + scenár) · v1

## Rozhodnutia

- **Firma (fiktívna):** **Sumi** — AI, ktorá z hovorov, chatov a poznámok spraví jeden jasný plán: rozhodnutia, úlohy, kto a dokedy. Názov podľa japonského atramentu *sumi* → celá vizuálna identita je „atrament na papieri“.
- **Message:** Every meeting ends with one clear plan.
- **Formát:** 16:9 · 1920×1080 · 30 fps · ~35 s · **bez voiceoveru**, hudba + SFX. Text na obrazovke v angličtine (zmena na slovenčinu = len výmena textov).
- **Chrbtica (spine):** **atramentová kvapka/pečať** Sumi. Je to bodka, z ktorej vyrastie kapsula (01–02), logo (04), kurzorový „klik“ (06–07), sken odhalenia (08), zvýrazňovač (10) a nakoniec odrážajúce sa logo (11–12). Jeden objekt, ktorý vedie každý prechod.
- **Paleta:** papier `#F5F1EA` · atrament `#17161B` · pečatná červená (akcent) `#E8432A` · tieňový sivý `#8C877F` · jemný teplý gradient (červená → marhuľová → papier) iba v úsekoch 03 a 06 namiesto fialovej aurory.
- **Typografia:** display serif *Instrument Serif* (akcentové slová, kurzíva) + grotesk *Inter Tight* (všetko ostatné), mono *JetBrains Mono* iba v UI. Nadpisy ≥ 72 px, UI ≥ 22 px.
- **Pohyb:** všetky prechody s rozmazaním v smere pohybu; vstupy `expo.out` 0,5–0,7 s, odchody `power3.in` 0,3 s. **Jeden smer: doľava** (whipy, karusel, posun kamery).
- **Čitateľnosť:** každý text stojí hotový min. **1,2 s**; max. 5 slov na obrazovke naraz.
- **Statický záber (held frame):** 08, plán je hotový a 1 s sa nehýbe nič okrem jemného dýchania pozadia.
- **Zákazy:** žiadny fialový/modrý gradient, žiadny neon, žiadne fullscreen fotky, žiadne prázdne „karty v mriežke“, žiadny čierny/čisto biely `#000/#fff` (okrem endcardu, ten je atrament `#17161B`). Žiadna prezentácia (každý beat nová karta) ani šetrič obrazovky (pohyb bez významu).
- **Placeholdery:** malé obrázky (zdroje, avatary) = šrafované dlaždice s popisom, doplníme neskôr.

## Prehľad beatov

| # | Beat | Čas | Na obrazovke | Prečo |
|---|---|---|---|---|
| 01 | Hook | 0,0–2,6 | „Great meeting.“ | Pozná to každý: stretnutie bolo fajn… |
| 02 | Háčik | 2,6–5,4 | „So… who does [?]“ → klik → pop | …ale nikto nevie, čo ďalej. Bolesť. |
| 03 | Zvrat | 5,4–7,2 | obrie „Introducing“ → malé | Ohlásenie riešenia |
| 04 | Logo | 7,2–10,0 | písmená obiehajú kvapku → „sumi“ | Meno + značka |
| 05 | Remix | 10,0–11,4 | 6 rýchlych štýlov loga | Energia, značka je hravá |
| 06 | Zdroje | 11,4–15,4 | UI: 4 zdroje sa ukotvia do baru | Ako to funguje 1: všetko na jedno miesto |
| 07 | Požiadavka | 15,4–19,0 | „Turn it into one plan.“ → odoslať → burst | Ako to funguje 2: jedna veta |
| 08 | Plán | 19,0–22,4 | hotový plán: 3 úlohy, mená, termíny | **Dôkaz = message** |
| 09 | Zmena? | 22,4–24,8 | „Missed something?“ → karta → karusel | Otvára úpravy |
| 10 | Označ | 24,8–28,6 | zvýrazňovač na prepise, čip „add deadlines“ | Úpravy sú triviálne |
| 11 | Payoff | 28,6–31,6 | iris → logo sa odráža: „Less recap. More done.“ | Tagline |
| 12 | Endcard | 31,6–35,0 | atrament, flip, „sumi“ + sumi.app | Zapamätanie |

**Súčet:** 2,6+2,8+1,8+2,8+1,4+4,0+3,6+3,4+2,4+3,8+3,0+3,4 = **35,0 s** ✔

**Rytmus:** pomaly-pomaly · BUM (03) · ťah (04) · **rýchle strihy** (05) · stredné tempo UI (06–07) · **STOP** (08) · stredné (09–10) · zrýchlenie (11) · ticho (12).

**Nové poradie oproti referencii:** kapsula + kurzor sa spájajú do jedného gagu (02); písací stroj a burst sú až po UI; „text → karta“ prichádza až po výsledku; odrážajúce sa logo je tagline; iris je pred taglinom, nie pred montážou; depth-map sken je nahradený „atramentovým skenom“.

## Hudba a zvuk

- **Hudba:** teplý, ľahko funky lo-fi / minimal house, **104 BPM** (1 dob = 0,577 s), čistý bubon + Rhodes + mäkký bas. Bez vokálu. Zdroj: licencovaná knižnica alebo AI hudba s komerčnou licenciou. −16 LUFS pod SFX.
  - 0,0–5,4: iba Rhodes + jemný hi-hat (zvedavosť) · **5,4 drop** (celý beat nastúpi s „Introducing“) · 19,0–20,0 hudba sa stlmí (low-pass) pre held frame · 20,0 späť · 31,4 hudba utíchne s dozvukom → endcard v takmer tichu.
- **SFX (prehľad):** klávesnica, mäkký klik myši, „pop“ bubliny, krátke whooshe, papierový šuchot, ťah fixky, „stamp“ pečiatky, jemný zvonček na koniec. Konkrétne časy pri každom beate (riadok *Zvuk*).

---

## Frame 1 — Great meeting

- duration: 2.6s
- start: 0.0
- transition_in: cut
- scene: Papierové pozadie, uprostred „Great meeting.“ slovo po slove z rozmazania
- voiceover: onscreen
- status: outline

**Na obrazovke:** „Great meeting.“ (Inter Tight 88 px, atrament; „meeting.“ v Instrument Serif kurzíve).
**Pohyb:** 0,15 s „Great“ príde z blur 24 px → 0, scale 1,08 → 1, `expo.out` 0,6 s. 0,45 s „meeting.“ rovnako. Pozadie: veľmi jemné papierové zrno + pomaly dýchajúci teplý kruh vpravo dole (opacity 6 %).
**Výstup:** 2,3–2,6 text sa zmenší na 0,9 a rozmaže (pripraví sa na ďalšiu vetu na tom istom mieste).
**Zvuk:** 0,0 Rhodes akord (hudba štartuje) · 0,15 a 0,45 jemné „tick“ pri slovách.
**Nie:** žiadny gradient, žiadne logo na začiatku.

## Frame 2 — Who does what?

- duration: 2.8s
- start: 2.6
- transition_in: blur-crossfade
- scene: „So… who does [?]“, kapsula vyrastie z bodky, kurzor ju ťukne a praskne
- voiceover: onscreen
- status: outline

**Na obrazovke:** „So… who does“ + **kapsula** (zaoblená, 140×88 px, pečatná červená) s bielym „?“, ktorý jemne pulzuje.
**Pohyb:** 2,6 slová blur-in po 0,12 s. 3,3 medzi „does“ a koncom sa objaví **atramentová bodka**, vyrastie do kapsuly (`back.out(1.6)`, 0,45 s), slová sa odsunú doľava. 4,2 **3D kurzor** vletí sprava zdola (`power3.out` 0,5 s), 4,75 klik: kurzor sa zmačkne (scale 0,85), kapsula sa **rozprskne na 6 kvapiek** atramentu, ktoré odletia.
**Výstup:** 5,1–5,4 **whip doľava** (x −400, blur 24 px, `power3.in` 0,3 s).
**Zvuk:** 3,3 „blop“ kvapky · 4,75 klik myši + mokrý „splat“ · 5,1 krátky whoosh doľava.
**Nie:** kurzor nie je štandardná šípka, je to mäkká 3D ruka v atramentových tónoch.

## Frame 3 — Introducing

- duration: 1.8s
- start: 5.4
- transition_in: whip-left
- scene: Obrie orezané „Introducing“ letí doľava cez teplý atramentový gradient, potom skok na malý nápis
- voiceover: onscreen
- status: outline

**Na obrazovke:** „Introducing“ v Instrument Serif **640 px** (orezané okrajmi), papierová farba na teplej škvrne (pečatná červená → marhuľová → papier, rozmazaná 120 px).
**Pohyb:** 5,4 text prichádza sprava, x +900 → −300 počas 0,9 s, motion blur 30 → 8 px. 6,3 **zoom-out snap**: škvrna sa stiahne do rohu, text skočí na 64 px do stredu, farba atrament (`expo.out` 0,5 s).
**Výstup:** 6,9–7,2 písmená sa začnú **kývať** každé zvlášť (rotácia ±8°, y ±6 px, stagger 0,03 s).
**Zvuk:** 5,4 **DROP** (nastúpi celý beat) + nízky whoosh · 6,3 krátky „thup“.
**Nie:** žiadny fialový ani modrý tón v gradiente.

## Frame 4 — Sumi

- duration: 2.8s
- start: 7.2
- transition_in: continuous
- scene: Písmená „Introducing“ sa rozletia, štyri z nich (s-u-m-i) obiehajú atramentovú kvapku, ktorá sa zmení na logo; zložia wordmark „sumi“
- voiceover: onscreen
- status: outline

**Na obrazovke:** logo = **atramentová kvapka s vyrezaným „ťahom štetca“** (placeholder vektor, 160 px) + wordmark „sumi“ (Inter Tight 120 px, rozostup −2 %). Pod ním po 9,2 s malé „meeting notes that act.“ (Instrument Serif kurzíva 40 px, sivá).
**Pohyb:** 7,2 nepotrebné písmená odfúknu a zmiznú; s-u-m-i **obiehajú po elipse** okolo stredu (1 obeh, 1,2 s, 3D perspektíva, písmená vzadu menšie a rozmazané). 7,4 kvapka dopadne do stredu (scale 0 → 1,15 → 1, `elastic.out(1, .6)`), raz sa otočí. 8,5 písmená sa **zacvaknú** vedľa loga do wordmarku (stagger 0,06 s, `expo.out`). 9,2 podtitulok blur-in.
**Výstup:** 9,8–10,0 wordmark sa zasunie **za logo** (mask), ostane samotné logo.
**Zvuk:** 7,4 kvapka „plop“ s dozvukom · 8,5–8,7 štyri jemné „click“ pri zacvaknutí písmen.
**Nie:** žiadne „2.0“ ani verzia.

## Frame 5 — Mark remix

- duration: 1.4s
- start: 10.0
- transition_in: cut
- scene: Logo v 6 štýloch, tvrdé strihy na dobu hudby
- voiceover: onscreen
- status: outline

**Na obrazovke:** logo vždy v strede, 6 štýlov (CSS/SVG, bez fotiek): 1) **pečiatka** (červená, zrnitý odtlačok) 2) **kontúra** tenkou linkou 3) **papierový výrez** s tieňom 4) **halftone** bodky 5) **štetcový ťah** (neúplný, suchý) 6) **sklo** (rozmazané pozadie, svetlý okraj). Každý štýl má vlastné pozadie z palety.
**Pohyb:** strih každých **0,23 s** (≈ 1/2 doby pri 104 BPM); logo pri každom strihu jemne „pumpne“ (scale 0,96 → 1).
**Výstup:** posledný (sklo) sa zmenší do **bodky** a padne dole.
**Zvuk:** každý strih = tlmený perkusívny „tok“ v rytme hudby.
**Nie:** nie dlhšie ako 1,4 s. Pozn.: chceš tu namiesto štýlov loga radšej **placeholdery** (napr. budúce vizuály)? Dá sa vymeniť 1:1.

## Frame 6 — Sources

- duration: 4.0s
- start: 11.4
- transition_in: drop
- scene: UI scéna: vstupný bar Sumi v strede, 4 zdroje plávajú v rohoch, kurzor ich ťahá do baru
- voiceover: onscreen
- status: outline

**Na obrazovke:** papier s teplým gradientom v hornom a dolnom okraji. V strede **vstupný bar** (920×132 px, radius 28, mäkký tieň): placeholder „Ask Sumi…“ (sivá), vľavo ikony +/⇄, vpravo čip „Sumi ✕“ a tlačidlo ▶. V rohoch 4 **dlaždice zdrojov** (112 px, radius 24, mierne natočené, plávajú): „Call · 48 min“, „Slack thread“, „Doc“, „Voice memo“ — **placeholdery** (šrafa + ikona + popis).
**Pohyb:** 11,4 bodka z 05 dopadne a rozleje sa do baru (scale-in z bodky, `expo.out` 0,6 s). Dlaždice vplávajú z rohov (stagger 0,1 s) a ďalej sa vznášajú (y ±8 px, 3 s sínus). 12,3 kurzor chytí 1. dlaždicu a **odtiahne ju do baru**; ostatné 3 nasledujú samy ako magnet (stagger 0,25 s). Pri ukotvení sa každá **naklopí v 3D** (rotateX 25° → 0) a zmenší na 56 px. Bar sa pritom roztiahne nahor (výška 132 → 190).
**Výstup:** 15,0–15,4 kamera **pricestuje do baru** (zoom 1 → 3 do textového poľa, blur), plocha sa vybieli.
**Zvuk:** 11,4 mäkký „whump“ · 12,3 papierový šuchot (ťahanie) · každé ukotvenie „pop“ (4×, stúpajúca výška tónu).
**Nie:** nevymýšľať reálne logá Zoom/Slack — iba generické ikony + popis.

## Frame 7 — The ask

- duration: 3.6s
- start: 15.4
- transition_in: zoom-through
- scene: Biela plocha, písací stroj „Turn it into one plan.“, odoslanie, burst šípok
- voiceover: onscreen
- status: outline

**Na obrazovke:** „Turn it into one **plan.**“ (Inter Tight 72 px; „plan.“ v serife kurzíve, pečatná červená), blikajúci textový kurzor.
**Pohyb:** 15,4 kurzor bliká 2× (0,5 s). 15,9 písanie **~14 znakov/s** (≈1,6 s pre 23 znakov), počas písania kamera mierne ide doľava, aby text ostal v strede. 17,5 text hotový, stojí 0,6 s. 18,1 vpravo sa objaví **tlačidlo ▶**, kurzor-ruka naň klikne. 18,4 ▶ sa **zmnoží na 3 chevrony**, ktoré rastú a letia doľava cez celú plochu (`power2.in` 0,6 s) → **tlačia** scénu preč.
**Zvuk:** 15,9–17,5 jemná klávesnica (synchronizovaná so znakmi) · 18,2 klik · 18,4 rastúci „whoosh-swell“.
**Nie:** text sa nezmenšuje pod 72 px.

## Frame 8 — The plan (held frame)

- duration: 3.4s
- start: 19.0
- transition_in: chevron-push
- scene: Atramentový sken odhalí hotový plán: názov, 3 úlohy s menom a termínom
- voiceover: onscreen
- status: outline

**Na obrazovke:** karta plánu (1100×640, radius 28, tieň):
„**Q3 Launch — the plan**“ (serif 56 px)
☐ „Final pricing page“ · **Ava** · *Fri*
☐ „Beta invite email“ · **Leo** · *Tue*
☐ „Fix onboarding step 2“ · **Mia** · *Thu*
Avatary = kruhové **placeholdery** s iniciálami. Malý štítok vpravo hore „from 4 sources“.
**Pohyb:** 19,0 chevrony odídu, zostane **atramentová vlna** (červená → atrament), ktorá prejde zľava doprava ako sken (0,7 s) a za sebou nechá hotovú kartu. Riadky sa dopisujú zhora (stagger 0,15 s, y 12 → 0, blur 8 → 0). 20,2 tri **zaškrtávacie políčka** sa ťuknú do stavu „assigned“ (krátka červená bodka). **20,4–22,0 held frame:** nič sa nehýbe, iba pozadie dýcha.
**Výstup:** 22,0–22,4 karta sa zmenší na 0,92 a rozmaže sa (pripravuje text 09).
**Zvuk:** 19,0 hudba stlmená (low-pass) · 19,0 „shhh“ skenu · 20,2 tri tiché „tick“ · 20,4 ticho/tlmená hudba · 22,0 filter sa otvorí.
**Nie:** nie viac ako 3 úlohy; žiadne grafy.

## Frame 9 — Missed something?

- duration: 2.4s
- start: 22.4
- transition_in: blur-crossfade
- scene: „Missed something?“ → text sa stane kartou → karta sa zmenší a z pravej strany príde karusel ďalších plánov
- voiceover: onscreen
- status: outline

**Na obrazovke:** „Missed **something?**“ (Inter Tight 80 px, „something?“ serif kurzíva červená). Potom karta s tým istým textom; karusel 3 kariet: „Weekly sync“, „Client call · Acme“ (fiktívne), „Q3 Launch“.
**Pohyb:** 22,4 text blur-in po slovách. 23,4 okolo textu vyrastie **biela karta** (od okrajov textu von, `expo.out` 0,5 s). 23,9 karta sa **zmenší na 40 %** a posunie doľava, zprava **prichádza karusel** (push doľava, stagger 0,08 s). 24,5 karusel zastaví na karte „Q3 Launch“.
**Výstup:** 24,5–24,8 karta „Q3 Launch“ sa **zväčší na celú plochu** (zoom do karty).
**Zvuk:** 22,4 jemný „tick“ · 23,4 papier „fwip“ · 23,9 kĺzanie kariet (soft swoosh) · 24,5 „thock“ zastavenia.

## Frame 10 — Mark it

- duration: 3.8s
- start: 24.8
- transition_in: zoom-into-card
- scene: Prepis hovoru, zvýrazňovač označí 2 vety, do baru príde čip „Add deadlines“, sken a plán sa aktualizuje
- voiceover: onscreen
- status: outline

**Na obrazovke:** vľavo **prepis hovoru** (5 riadkov, mono 24 px, sivá), vpravo plán z 08 (zmenšený). Dole vstupný bar z 06.
Riadky prepisu (fiktívne):
„Leo: we should probably email the beta list…“ · „Mia: step two is still confusing.“ · „Ava: pricing by Friday?“ · „Leo: and invite the Acme team too.“ · „Mia: let's keep it simple.“
**Pohyb:** 25,0 **zvýrazňovač** (pečatná červená, 35 % opacity, ručne kreslený okraj) prejde cez riadok „…invite the Acme team too.“ (ťah 0,5 s `power2.inOut`). 25,7 druhý ťah krúžkom okolo „Friday?“. 26,3 do baru sa **napíše** „Add the Acme invite.“ a pribudne čip. 27,2 klik ▶. 27,4 **atramentový sken** prejde plánom → pribudne **4. riadok** „Invite Acme team · Leo · Wed“ s červenou bodkou „new“ (pop).
**Výstup:** 28,3–28,6 **iris zatvorenie** do kruhu okolo novej bodky.
**Zvuk:** 25,0 a 25,7 ťah fixkou (2×) · 26,3 klávesnica · 27,2 klik · 27,4 sken „shhh“ · 27,8 pozitívny „pop“.
**Nie:** maximálne 2 ťahy; zvýrazňovač nesmie prekryť čitateľnosť textu.

## Frame 11 — Less recap. More done.

- duration: 3.0s
- start: 28.6
- transition_in: iris-close
- scene: Z kruhu sa stane malé logo, ktoré sa odráža po ploche a pri každom dopade zostane slovo
- voiceover: onscreen
- status: outline

**Na obrazovke:** papier, finálne „Less recap. More **done.**“ (Inter Tight 84 px, „done.“ serif kurzíva červená).
**Pohyb:** 28,6 iris sa stiahne na **logo-kvapku** (64 px). Logo sa **odrazí** 4× po dráhe s motion blur (každý odraz `power2.out`, 0,35 s); kde dopadne, tam **vyrazí slovo ako pečiatka** (scale 1,2 → 1, blur 6 → 0): „Less“ · „recap.“ · „More“ · „done.“. 30,2 celý riadok hotový a stojí **1,2 s**. 31,2 logo **letí do kamery** (scale 1 → 30, blur), plocha sa zaleje atramentom.
**Zvuk:** 4 odrazy = 4 pečiatky „stamp“ v rytme hudby (dobu 0,58 s) · 31,2 hlboký whoosh do kamery · 31,4 hudba doznie.
**Nie:** nie 3 slová s bodkami (ako „Type. Transform. Done“) — dve kontrastné frázy.

## Frame 12 — Endcard

- duration: 3.4s
- start: 31.6
- transition_in: ink-flood
- scene: Atramentová plocha, logo sa preklopí, wordmark „sumi“ sa zúži z roztiahnutých písmen, pod ním sumi.app
- voiceover: onscreen
- status: outline

**Na obrazovke:** pozadie atrament `#17161B`, logo v papierovej farbe (120 px) + „sumi“ (Inter Tight 96 px), pod tým „sumi.app“ (mono 28 px, sivá 60 %).
**Pohyb:** 31,6 logo sa **preklopí** (rotateY 180° → 0, `expo.out` 0,8 s). 32,2 písmená „s u m i“ sa objavia s rozostupom 60 px a **zúžia sa** na −2 % (`expo.out` 0,9 s) a logo sa posunie doľava. 33,2 „sumi.app“ fade-in. 33,4–35,0 statické.
**Zvuk:** 31,6 jemný zvonček / „ting“ s dlhým dozvukom, potom ticho.

---

## SFX — kompletný zoznam (cue sheet)

| Čas (s) | Zvuk | Beat |
|---|---|---|
| 0,00 | Rhodes akord (štart hudby) | 01 |
| 0,15 / 0,45 | jemné „tick“ | 01 |
| 3,30 | „blop“ kvapky | 02 |
| 4,75 | klik myši + mokrý „splat“ | 02 |
| 5,10 | krátky whoosh doľava | 02→03 |
| 5,40 | **DROP** hudby + nízky whoosh | 03 |
| 6,30 | „thup“ | 03 |
| 7,40 | „plop“ s dozvukom | 04 |
| 8,50–8,70 | 4× „click“ | 04 |
| 10,00–11,15 | 6× perkusívny „tok“ | 05 |
| 11,40 | mäkký „whump“ | 06 |
| 12,30 | papierový šuchot | 06 |
| 12,5–13,3 | 4× „pop“ (stúpajúci) | 06 |
| 15,0 | zoom whoosh | 06→07 |
| 15,9–17,5 | klávesnica | 07 |
| 18,2 | klik | 07 |
| 18,4 | whoosh-swell | 07→08 |
| 19,0 | sken „shhh“ + low-pass hudby | 08 |
| 20,2 | 3× „tick“ | 08 |
| 22,0 | filter sa otvára | 08→09 |
| 23,4 / 23,9 / 24,5 | „fwip“ · swoosh · „thock“ | 09 |
| 25,0 / 25,7 | ťah fixkou | 10 |
| 26,3 | klávesnica | 10 |
| 27,2 / 27,4 / 27,8 | klik · sken · „pop“ | 10 |
| 28,6–30,2 | 4× „stamp“ | 11 |
| 31,2 | hlboký whoosh | 11→12 |
| 31,6 | „ting“ + ticho | 12 |
