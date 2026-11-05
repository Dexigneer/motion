"""v2b: SVG source icons, larger docked icons, carousel cards no longer overlap the shrinking card."""
p = "index.html"
s = open(p).read()


def R(a, b):
    global s
    assert a in s, ("MISSING", a[:90])
    s = s.replace(a, b, 1)


IC = 'viewBox="0 0 24 24" fill="none" stroke="#17161b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
R('<div class="ico">◖</div>', f'<div class="ico"><svg {IC}><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2" /></svg></div>')
R('<div class="ico">#</div>', f'<div class="ico"><svg {IC}><path d="M9 4 7 20M17 4l-2 16M4 9h16M3 15h16" /></svg></div>')
R('<div class="ico">≡</div>', f'<div class="ico"><svg {IC}><path d="M6 3h8l4 4v14H6zM14 3v4h4M9 12h6M9 16h6" /></svg></div>')
R('<div class="ico">∿</div>', f'<div class="ico"><svg {IC}><path d="M4 12v0M8 8v8M12 5v14M16 9v6M20 11v2" /></svg></div>')
R('.tile .ico { position: absolute;', '.tile .ico svg { width: 26px; height: 26px; }\n      .tile .ico { position: absolute;')
R('tl.to(t.querySelector(".ico"), { y: 26, scale: 1.25,', 'tl.to(t.querySelector(".ico"), { y: 26, scale: 1.55,')

# carousel: first card shrinks first, the others follow behind it
R('tl.to("#s9-first", { scale: 0.42, x: -620, duration: 0.6, ease: "expo.inOut" }, 23.85);',
  'tl.to("#s9-first", { scale: 0.42, x: -620, duration: 0.42, ease: "power3.inOut" }, 23.8);')
R('{ x: slots9[i] + 1500, scale: 0.42 }, { x: slots9[i], scale: 0.42, duration: 0.6, ease: "expo.out" }, 23.95 + i * 0.08);',
  '{ x: slots9[i] + 1500, scale: 0.42 }, { x: slots9[i], scale: 0.42, duration: 0.5, ease: "power3.out" }, 24.0 + i * 0.07);')
R('tl.to("#s9-track", { x: -620, duration: 0.45, ease: "expo.inOut" }, 24.1);',
  'tl.to("#s9-track", { x: -620, duration: 0.4, ease: "power3.inOut" }, 24.2);')
open(p, "w").write(s)
print("ok")
