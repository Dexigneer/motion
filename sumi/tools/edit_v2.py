"""v2 edits: single font (Inter Tight), no image mark in the sumi scene, re-gridded input bar."""
p = "index.html"
s = open(p).read()


def R(a, b):
    global s
    assert a in s, ("MISSING", a[:90])
    s = s.replace(a, b, 1)


# ---- 1) one font family ----------------------------------------------------
R('''      @font-face { font-family: "Instrument Serif"; src: url("assets/fonts/InstrumentSerif-Regular.woff2") format("woff2"); font-weight: 400; font-style: normal; }
      @font-face { font-family: "Instrument Serif"; src: url("assets/fonts/InstrumentSerif-Italic.woff2") format("woff2"); font-weight: 400; font-style: italic; }
      @font-face { font-family: "JetBrains Mono"; src: url("assets/fonts/JetBrainsMono.woff2") format("woff2"); font-weight: 100 800; font-style: normal; }
''', '')
R('''        --serif: "Instrument Serif", serif;
        --mono: "JetBrains Mono", monospace;''', '''        --serif: var(--sans);
        --mono: var(--sans);''')
R('.serif-i { font-family: var(--serif); font-style: italic; font-weight: 400; }',
  '.serif-i { font-family: var(--sans); font-style: normal; font-weight: 650; letter-spacing: -0.03em; }')
R('.line .serif-i { font-size: 118px; letter-spacing: 0; }', '')
R('#s2-q { font-family: var(--serif); font-style: italic; font-size: 92px;',
  '#s2-q { font-family: var(--sans); font-weight: 600; font-size: 76px;')
R('white-space: nowrap; font-family: var(--serif); font-size: 640px;',
  'white-space: nowrap; font-family: var(--sans); font-weight: 600; letter-spacing: -0.04em; font-size: 560px;')
R('justify-content: center; font-family: var(--serif); font-size: 104px; }',
  'justify-content: center; font-family: var(--sans); font-weight: 500; letter-spacing: -0.02em; font-size: 96px; }')
R('#s4-sub { position: absolute; left: 0; right: 0; top: 690px; text-align: center; font-family: var(--serif); font-style: italic; font-size: 52px; color: var(--ash); }',
  '#s4-sub { position: absolute; left: 0; right: 0; top: 680px; text-align: center; font-family: var(--sans); font-weight: 400; font-size: 44px; color: var(--ash); }')
R('#s7-line .c.it { font-family: var(--serif); font-style: italic; font-weight: 400; color: var(--seal); font-size: 108px; letter-spacing: 0; }',
  '#s7-line .c.it { font-weight: 650; color: var(--seal); }')
R('.plan-tag { font: 500 28px var(--mono);', '.plan-tag { font: 500 26px var(--sans);')
R('.plan-title { font-family: var(--serif); font-size: 76px; line-height: 1; }',
  '.plan-title { font-family: var(--sans); font-weight: 600; letter-spacing: -0.025em; font-size: 60px; line-height: 1; }')
R('.day { font-family: var(--serif); font-style: italic; color: var(--seal); font-size: 44px; font-weight: 400; text-align: right; }',
  '.day { font-family: var(--sans); color: var(--seal); font-size: 34px; font-weight: 600; text-align: right; }')
R('top: 70px; font-family: var(--serif); font-size: 84px; line-height: 1; }',
  'top: 70px; font-family: var(--sans); font-weight: 600; letter-spacing: -0.025em; font-size: 72px; line-height: 1; }')
R('#s9-text .serif-i { font-size: 98px; letter-spacing: 0; }', '')
R('.tr-h { font: 500 22px var(--mono);', '.tr-h { font: 500 24px var(--sans);')
R('.tl-row { position: relative; font: 400 27px var(--mono);', '.tl-row { position: relative; font: 400 30px var(--sans);')
R('#s10-plan .plan-title { font-size: 58px; }', '#s10-plan .plan-title { font-size: 50px; }')
R('#s10-plan .day { font-size: 34px; }', '#s10-plan .day { font-size: 28px; }')
R('#s11-line .serif-i { font-size: 128px; letter-spacing: 0; }', '')
R('text-align: center; font: 400 34px var(--mono);', 'text-align: center; font: 500 34px var(--sans);')
R('.tile .lab { font: 500 17px var(--mono);', '.tile .lab { font: 500 18px var(--sans);')

# ---- 2) scene 4 without the image mark -------------------------------------
R('          <svg id="s4-mark" class="mark" style="color: var(--ink)"><use href="#mark" fill="currentColor" /></svg>\n', '')
a = s.index('        const mark4 = $("#s4-mark");')
b = s.index('        // orbit (seek-safe')
s = s[:a] + '''        const L = $$(".s4-l");
        const lC = L.map(centre);
        const wordC = { x: (lC[0].x + lC[3].x) / 2, y: lC[0].y };
''' + s[b:]
R('        tl.to(mark4, { x: 0, y: 0, duration: 0.6, ease: "expo.inOut" }, 8.45);\n', '')
a = s.index('        // tuck the wordmark behind the mark')
b = s.index('        // 05 MARK REMIX')
s = s[:a] + '''        // collapse the wordmark into one ink point → hard cut into the remix
        L.forEach((l, i) => tl.to(l, { x: wordC.x - lC[i].x, scale: 0.2, opacity: 0, filter: "blur(6px)", duration: 0.32, ease: "power3.in" }, 9.66 + (i === 0 || i === 3 ? 0 : 0.04)));
        tl.to("#s4-sub", { opacity: 0, y: 10, duration: 0.2 }, 9.8);

''' + s[b:]
R('const R = 380, rY = 130,', 'const R = 420, rY = 150,')

# ---- 3) input bar on an exact grid ------------------------------------------
# bar: x 500..1420. Closed 156 high (462..618). Open 244 high (418..662), stays centred.
# inside (padding 24/28): sources row 442..506 · placeholder 530..566 · controls 582..638
R('#s6-bar { position: absolute; left: 500px; top: 474px; width: 920px; height: 132px; padding: 0 28px 22px; display: flex; flex-direction: column; justify-content: flex-end; }',
  '#s6-bar { position: absolute; left: 500px; top: 462px; width: 920px; height: 156px; padding: 24px 28px; display: flex; flex-direction: column; justify-content: flex-end; }')
R('#s6-ask { font-size: 32px; color: #a39d93; margin-bottom: 18px; padding-left: 6px; }',
  '#s6-ask { font-size: 30px; line-height: 36px; height: 36px; color: #a39d93; margin-bottom: 16px; padding-left: 4px; }\n      .bar-row { height: 56px; }')
R('.bar-row .left { display: flex; align-items: center; gap: 18px; font: 400 28px var(--mono); color: var(--ash); }',
  '.bar-row .left { display: flex; align-items: center; gap: 12px; }\n      .ib { width: 52px; height: 52px; border-radius: 50%; border: 2px solid var(--hair); display: flex; align-items: center; justify-content: center; color: var(--ash); }\n      .ib svg { width: 22px; height: 22px; }')
R('<div class="left"><span>+</span><span>⇄</span><span class="chip">',
  '<div class="left"><span class="ib"><svg viewBox="0 0 22 22"><path d="M11 3v16M3 11h16" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" /></svg></span><span class="ib"><svg viewBox="0 0 22 22"><path d="M4 7h13l-3-3M18 15H5l3 3" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" /></svg></span><span class="chip" style="margin-left: 4px">')
# tile internals: icon top-centred, label pinned bottom → icon recentres when docked
R('.tile { position: absolute; width: 150px; height: 150px; border-radius: 32px; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px;',
  '.tile { position: absolute; width: 150px; height: 150px; border-radius: 32px;')
R('.tile .ico { width: 46px; height: 46px;', '.tile .ico { position: absolute; left: 52px; top: 26px; width: 46px; height: 46px;')
R('.tile .lab { font: 500 18px var(--sans); color: #5d584f; text-align: center; line-height: 1.2; padding: 0 10px; }',
  '.tile .lab { position: absolute; left: 0; right: 0; bottom: 20px; font: 500 18px var(--sans); color: #5d584f; text-align: center; line-height: 22px; padding: 0 10px; }')
R('tl.to("#s6-bar", { height: 244, y: -56, duration', 'tl.to("#s6-bar", { height: 244, y: -44, duration')
R('const slot = (i) => ({ x: 500 + 28 + 32 + i * 80, y: 418 + 26 + 32 });',
  'const slot = (i) => ({ x: 500 + 28 + 32 + i * 76, y: 442 + 32 });')
R('''          tl.to(t, { x: s.x - c.x, y: s.y - c.y, scale: 64 / 150, rotation: 0, duration: 0.55, ease: "power3.inOut" }, at);''',
  '''          tl.to(t, { x: s.x - c.x, y: s.y - c.y, scale: 64 / 150, rotation: 0, borderRadius: 40, duration: 0.55, ease: "power3.inOut" }, at);
          tl.to(t.querySelector(".lab"), { opacity: 0, duration: 0.2 }, at + 0.1);
          tl.to(t.querySelector(".ico"), { y: 26, scale: 1.25, duration: 0.45, ease: "power3.inOut" }, at + 0.1);''')
R('transformOrigin: "760px 560px"', 'transformOrigin: "640px 548px"')

open(p, "w").write(s)
print("ok")
