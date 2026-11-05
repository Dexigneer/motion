"""v3: faster (x1.25 → 28 s), 60 fps, shutter motion blur on the snap beats, and creative additions:
per-character 3D type rise, ink flood 02→03, ink underline + drawn checks on the plan,
stamp camera punches, ripple rings on the endcard.

All GSAP positions stay in authored (35 s) time; a master timeline plays the authored
timeline at 1.25x. Clip and audio attributes are rescaled here so they match.
"""
import re

K = 0.8  # new_time = authored_time * K
p = "index.html"
s = open(p).read()


def R(a, b, count=1):
    global s
    assert s.count(a) >= count, ("MISSING", a[:100])
    s = s.replace(a, b, count)


# ---------------------------------------------------------------- markup additions
# ink flood circle in scene 02 + extra SFX for it
R('        <div class="cursor" id="s2-cur">', '        <div id="s2-flood"></div>\n        <div class="cursor" id="s2-cur" data-hf-motion-blur=\'{"samplesPerFrame": 8}\'>')
R('<div id="s3-blob"></div>', '<div id="s3-flood" class="fill" style="background: var(--seal)"></div>\n        <div id="s3-blob"></div>')
R('<div id="s3-giant">Introducing</div>', '<div id="s3-giant" data-hf-motion-blur=\'{"samplesPerFrame": 8}\'>Introducing</div>')
for c in ("ch1", "ch2", "ch3"):
    R(f'<div class="chev" id="{c}">', f'<div class="chev" id="{c}" data-hf-motion-blur=\'{{"samplesPerFrame": 8}}\'>')
R('<svg id="s11-ball" style="color: var(--ink)">', '<svg id="s11-ball" data-hf-motion-blur=\'{"samplesPerFrame": 8}\' style="color: var(--ink)">')

# plan: brush underline + drawn checks (scene 08 only — first three .chk in the file)
R('<div class="plan-head"><div class="plan-title">Q3 Launch — the plan</div>',
  '<svg id="s8-ul" viewBox="0 0 660 24"><path id="s8-ul-p" d="M4 14 C120 6 260 18 420 10 S600 8 656 12" fill="none" stroke="#e8432a" stroke-width="7" stroke-linecap="round" /></svg>\n          <div class="plan-head"><div class="plan-title">Q3 Launch — the plan</div>')
CHK = '<div class="chk s8c"><svg viewBox="0 0 34 34"><path d="M9 17.5 L14.5 23 L25 11.5" fill="none" stroke="#e8432a" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round" /></svg></div>'
for _ in range(3):
    R('<div class="row s8r"><div class="chk"><b></b></div>', '<div class="row s8r">' + CHK)

# endcard ripples
R('        <div id="s12-row">', '        <div class="ring" id="rg1"></div><div class="ring" id="rg2"></div><div class="ring" id="rg3"></div>\n        <div id="s12-row">')

# ---------------------------------------------------------------- css
R('      /* S1 + S2 */', '''      .ch { display: inline-block; will-change: transform, opacity, filter; }
      #s2-flood { position: absolute; width: 40px; height: 40px; border-radius: 50%; background: var(--seal); opacity: 0; z-index: 5; }
      #s8-ul { position: absolute; left: 60px; top: 122px; width: 660px; height: 24px; overflow: visible; }
      .chk.s8c { border-color: #e9ded2; background: transparent; }
      .chk.s8c svg { width: 30px; height: 30px; }
      .ring { position: absolute; width: 200px; height: 200px; border-radius: 50%; border: 3px solid rgba(245, 241, 234, 0.7); opacity: 0; }

      /* S1 + S2 */''')

# ---------------------------------------------------------------- timing attributes
R('data-duration="35" data-width="1920" data-height="1080"', 'data-duration="35" data-fps="60" data-width="1920" data-height="1080"')
# new flood sfx (authored time; rescaled with everything else below)
R('      <audio id="sfx-wh1"', '      <audio id="sfx-flood" src="assets/sfx/swell.wav" data-start="4.82" data-duration="0.6" data-track-index="12" data-volume="0.7"></audio>\n      <audio id="sfx-wh1"')
R('      <audio id="sfx-ting"', '      <audio id="sfx-ripple" src="assets/sfx/plop.wav" data-start="31.62" data-duration="0.9" data-track-index="11" data-volume="0.5"></audio>\n      <audio id="sfx-ting"')


def scale_tag(m):
    tag = m.group(0)
    is_audio = tag.startswith("<audio")
    tag = re.sub(r'data-start="([\d.]+)"', lambda n: f'data-start="{round(float(n.group(1)) * K, 3):g}"', tag)
    if not is_audio:
        tag = re.sub(r'data-duration="([\d.]+)"', lambda n: f'data-duration="{round(float(n.group(1)) * K, 3):g}"', tag)
    return tag


s = re.sub(r'<(section|svg|div|audio)\b[^>]*data-start="[^"]*"[^>]*>', scale_tag, s)

# ---------------------------------------------------------------- motion-blur component snippet
snippet = open("compositions/components/motion-blur.html").read()
R('    <script>\n      document.fonts.ready.then(() => {', snippet + '\n    <script>\n      document.fonts.ready.then(() => {')

# ---------------------------------------------------------------- js
R('        const tl = gsap.timeline({ paused: true });',
  '''        // master plays the authored (35 s) timeline at 1/K speed → 28 s film
        const SPEED = 1.25;
        const master = gsap.timeline({ paused: true });
        const tl = gsap.timeline();''')
R('''        // layout centre of an element''', '''        // per-character 3D rise (kinetic type)
        const charRise = (el, at, o = {}) => {
          el = typeof el === "string" ? $(el) : el;
          if (!el.dataset.split) {
            const txt = el.textContent; el.textContent = "";
            txt.split("").forEach((c) => { const sp = document.createElement("span"); sp.className = "ch"; sp.textContent = c === " " ? "\\u00a0" : c; el.appendChild(sp); });
            el.dataset.split = "1";
          }
          tl.fromTo(el.children, { opacity: 0, y: o.y ?? 70, rotationX: -85, filter: "blur(10px)", transformPerspective: 700, transformOrigin: "50% 100%" },
            { opacity: 1, y: 0, rotationX: 0, filter: "blur(0px)", duration: o.dur ?? 0.7, ease: "expo.out", stagger: o.stagger ?? 0.03 }, at);
        };
        // layout centre of an element''')

# 01 / 02 / 09 headlines → kinetic per-character rise
R('        blurIn("#s1-a", 0.12);\n        blurIn("#s1-b", 0.45);', '        charRise("#s1-a", 0.05);\n        charRise("#s1-b", 0.3);')
R('''        blurIn("#s2-a", 2.62, { dur: 0.55 });
        blurIn("#s2-b", 2.76, { dur: 0.55 });
        blurIn("#s2-c", 2.9, { dur: 0.55 });''', '''        charRise("#s2-a", 2.62, { stagger: 0.025 });
        charRise("#s2-b", 2.74, { stagger: 0.025 });
        charRise("#s2-c", 2.86, { stagger: 0.025 });''')
R('        blurIn("#s9-a", 22.42);\n        blurIn("#s9-b", 22.6);', '        charRise("#s9-a", 22.42, { stagger: 0.025 });\n        charRise("#s9-b", 22.56, { stagger: 0.022 });')

# 02→03 ink flood from the burst capsule
R('''        tl.to("#s2-line", { x: -420, filter: "blur(24px)", opacity: 0, duration: 0.3, ease: "power3.in" }, 5.1);''',
  '''        tl.to("#s2-line", { x: -420, filter: "blur(24px)", opacity: 0, duration: 0.3, ease: "power3.in" }, 5.0);
        const flood = $("#s2-flood");
        flood.style.left = capC.x - 20 + "px"; flood.style.top = capC.y - 20 + "px";
        tl.fromTo(flood, { scale: 0.2, opacity: 1 }, { scale: 120, duration: 0.55, ease: "power3.in" }, 4.85);''')
R('''        tl.fromTo("#s3-blob", { scale: 0.7, opacity: 0, x: 300 }, { scale: 1, opacity: 1, x: 0, duration: 0.6, ease: "expo.out" }, 5.4);''',
  '''        tl.fromTo("#s3-flood", { opacity: 1 }, { opacity: 0, duration: 0.6, ease: "power2.out" }, 5.45);
        tl.fromTo("#s3-blob", { scale: 1.7, opacity: 1, x: 0 }, { scale: 1, opacity: 1, x: 0, duration: 0.9, ease: "expo.out" }, 5.4);''')

# 08 plan: underline + drawn checks
R('''        tl.fromTo(".s8r .chk b", { scale: 0 }, { scale: 1, duration: 0.3, ease: "back.out(3)", stagger: 0.1 }, 20.2);''',
  '''        const ul = $("#s8-ul-p"), ulLen = ul.getTotalLength();
        tl.fromTo(ul, { strokeDasharray: ulLen, strokeDashoffset: ulLen }, { strokeDashoffset: 0, duration: 0.55, ease: "power2.inOut" }, 19.55);
        $$(".s8c path").forEach((pth, i) => {
          const l = pth.getTotalLength();
          tl.fromTo(pth, { strokeDasharray: l, strokeDashoffset: l }, { strokeDashoffset: 0, duration: 0.28, ease: "power2.out" }, 20.15 + i * 0.12);
          tl.fromTo(pth.parentNode.parentNode, { scale: 1 }, { scale: 1.18, duration: 0.1, yoyo: true, repeat: 1, ease: "power2.out" }, 20.15 + i * 0.12);
        });''')

# 11 stamp punches
R('''          tl.fromTo(words[i], { opacity: 0, scale: 1.35, filter: "blur(8px)", y: -10 }''',
  '''          tl.fromTo("#s11-line", { scale: 1 }, { scale: 1.025, duration: 0.07, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, tLand);
          tl.fromTo(words[i], { opacity: 0, scale: 1.35, filter: "blur(8px)", y: -10 }''')

# 12 ripples where the drop lands
R('''        tl.fromTo(mark12, { rotationY: 180,''', '''        const m12 = centre(mark12);
        ["#rg1", "#rg2", "#rg3"].forEach((r, i) => {
          const el = $(r); el.style.left = m12.x + shift - 100 + "px"; el.style.top = m12.y - 100 + "px";
          tl.fromTo(el, { scale: 0.3, opacity: 0.8 }, { scale: 3.2 + i, opacity: 0, duration: 1.3, ease: "power2.out" }, 31.62 + i * 0.14);
        });
        tl.fromTo(mark12, { rotationY: 180,''')

R('''        window.__timelines["main"] = tl;''', '''        master.add(tl, 0);
        tl.timeScale(SPEED);
        window.__timelines["main"] = master;''')
R('''        const shift = (word12.offsetWidth + 34) / 2;''', '''        const shift = (word12.offsetWidth + 34) / 2; // mark starts centred''')

open(p, "w").write(s)
print("ok", re.search(r'data-duration="([\d.]+)" data-fps', s).group(1))
