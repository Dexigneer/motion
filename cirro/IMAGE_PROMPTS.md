# Cirro: prompty na generovanie obrázkov

Prompty sú v angličtine, lebo generátory (Midjourney, Flux, Imagen, DALL·E, Firefly) s ňou fungujú najlepšie.
Každý prompt = **scéna + spoločný STYLE blok**. STYLE blok vlož vždy celý, aby mala celá séria rovnaký grading.

## Prečo takto (ladenie k videu)
- Video je **tmavé navy** `#060A12` / `#16233A` s **bledo-modrými** akcentmi `#CFE8FF` / `#8EC5FF`. Fotky preto majú **studené tóny, tiene zdvihnuté do navy (nie do čiernej), stredné až nízke kontrasty a saturáciu okolo 60–70 %**.
- Teplé farby (červené strechy, žltá električka, jedlo) **nevymazávať**, len stlmiť na prachové, pastelové odtiene. Inak by fotky pôsobili ako mrazené.
- **Dolná tretina fotky má byť tmavšia a pokojná.** Ukladá sa tam biely popis karty („IMG 03 · Miradouro da Graça“).
- Svetlo: **modrá hodinka, skoré ráno alebo hmla**, rozptýlené, mäkké tiene, jemný opar. Žiadne tvrdé poludňajšie slnko.
- Žiadne čitateľné texty, logá ani tváre zblízka. Ľudia sú len siluety, zozadu alebo z profilu.

---

## STYLE blok (vlož za každý prompt)

```
cinematic travel photography, cool blue color grade, shadows lifted into deep navy blue (#16233A), highlights soft icy pale blue (#CFE8FF), muted desaturated palette around 65% saturation, warm colors softened to dusty pastel tones, low contrast, soft diffused light, blue hour atmosphere, gentle haze, subtle fine film grain, shallow depth of field, calm darker lower third, editorial, minimal, no text, no logos, no watermark
```

**Negative prompt** (ak ho nástroj podporuje):
```
text, letters, signage, logos, watermark, oversaturated, neon, HDR, harsh midday sun, orange teal look, heavy vignette, faces in close-up, cartoon, illustration, 3d render, frame, border
```

**Midjourney parametre:** `--ar 3:4 --style raw --stylize 150` (pre THUMB `--ar 1:1`)
**Flux / Imagen / DALL·E:** pomer strán nastav v UI; STYLE blok drž na konci promptu.

---

## Scéna 06: 3D stena obrázkov · pomer 3:4 · min. 900×1200 px

**IMG 01 · Alfama · tram 28**
```
A vintage yellow tram climbing a steep narrow cobblestone street in Alfama, Lisbon, shot from below with a telephoto lens, old pastel facades on both sides, laundry on balconies, pale sky at the top of the frame, the tram's yellow softened to a dusty butter tone,
```

**IMG 02 · Pastel de nata**
```
Top-down close-up of three Portuguese custard tarts (pastéis de nata) on a dark slate plate, dusted with cinnamon, a small espresso cup at the edge, cool window light from the side, dark blue-grey table surface, caramelized tops in soft muted amber,
```

**IMG 03 · Miradouro da Graça (HLAVNÁ KARTA, musí byť najkrajšia)**
```
View from a Lisbon viewpoint (miradouro) over a sea of terracotta rooftops down to the wide Tagus river and a long suspension bridge in the distance, just after sunset during blue hour, one or two small silhouettes leaning on an iron railing in the foreground from behind, rooftops in dusty muted rose, the sky a gradient from pale icy blue to deep navy, first city lights turning on,
```

**IMG 04 · Praia da Ursa**
```
Aerial drone view looking down on a wild Atlantic beach with dramatic rock stacks, white foam lines on turquoise-to-deep-blue water, a tiny lone figure on the sand, early morning overcast light, sea mist,
```

**IMG 05 · Azulejo walls**
```
Close-up of a Lisbon building facade covered in traditional blue and white azulejo tiles with an old wooden window and a wrought-iron balcony, soft overcast light, the tiles' cobalt blue harmonizing with the cool grade, slight wear and texture on the tiles,
```

**IMG 06 · Time Out Market**
```
A shared long wooden table at a busy food hall in Lisbon, plates of seafood, bread and glasses of white wine, hands reaching for food, people blurred in the background, shot from a 45-degree angle, cool ambient light with a few soft warm pendant lights, cozy but calm,
```

**IMG 07 · LX Factory**
```
A colorful street-art mural on an old industrial brick wall in Lisbon, a bicycle leaning against it, straight-on graphic composition, the mural's colors muted toward blues and soft pastels, overcast even light,
```

**IMG 08 · Pena Palace**
```
The romantic hilltop Pena Palace in Sintra rising above a forest wrapped in fog, seen from a distance, its painted towers softened into dusty pastel tones, mysterious moody morning mist, layered depth of misty hills,
```

**IMG 09 · Belém tower**
```
The historic Belém Tower in Lisbon standing at the edge of the calm river at dawn, its perfect reflection in still water, pale icy-blue sky, soft low mist over the water, serene and symmetrical,
```

**IMG 10 · Rooftop bar**
```
A rooftop terrace bar overlooking Lisbon at dusk, two cocktail glasses on a small table in the foreground, string lights glowing softly, silhouettes of friends from behind, the city and river below fading into blue haze,
```

**IMG 11 · Grilled sardines**
```
Close-up macro of fresh sardines grilling on a charcoal grill with rising smoke, a halved lemon and rustic bread beside them, dark moody background, cool-toned smoke catching soft light, appetizing but muted,
```

**IMG 12 · Sunset tram**
```
A Lisbon tram passing through a street at blue hour with motion blur, streaks of soft city lights, a pale lavender-to-navy sky, silhouettes of passengers in the windows, dreamy sense of movement,
```

---

## Scéna 07: kocka „Day by day“ · pomer 1:1 · min. 400×400 px

Náhľady sú malé (150 px), preto **jeden jasný motív a jednoduché pozadie**.

**THUMB D1 · Alfama & views**
```
Simple square crop of terracotta Lisbon rooftops and a church dome against a pale icy-blue evening sky, one clear subject, minimal composition,
```

**THUMB D2 · Coast day**
```
Simple square aerial shot of a single white wave breaking on a sandy Atlantic beach near Cascais, deep blue water, minimal composition,
```

**THUMB D3 · Sintra hills**
```
Simple square shot of a pastel palace tower peeking out of thick fog over green forested hills in Sintra, minimal composition,
```

---

## Po vygenerovaní (rýchla kontrola)
1. Daj všetkých 12 fotiek vedľa seba. Ak niektorá vyskakuje (je teplejšia alebo sýtejšia), zníž jej saturáciu a posuň white balance do modra.
2. Spoločná úprava v Lightroome alebo Photoshope: **Temperature −10 až −15**, **Saturation −20**, **Shadows** do modrej (split toning: tiene ~220°, svetlá ~205°), **Blacks +15** (zdvihnuté, aby nič nebolo úplne čierne).
3. Exportuj ako JPG alebo WebP, 3:4 a 1:1, sRGB. Mená súborov podľa ID (`img01.jpg` … `img12.jpg`, `thumb_d1.jpg` …), aby sa dali rovno napojiť do kompozície.
