"""Synthesize the temporary SFX set for the Sumi promo (deterministic, license-free).

Usage: python3 tools/make_sfx.py assets/sfx
Every sound is placeholder quality by design; swap any file 1:1 later.
"""
import sys, os, wave
import numpy as np

SR = 48000
rng = np.random.default_rng(7)
OUT = sys.argv[1] if len(sys.argv) > 1 else "assets/sfx"
os.makedirs(OUT, exist_ok=True)


def t(d):
    return np.arange(int(SR * d)) / SR


def env(n, a=0.002, d=0.1, curve=4.0):
    x = np.arange(n) / SR
    att = np.clip(x / max(a, 1e-4), 0, 1)
    dec = np.exp(-np.clip(x - a, 0, None) * curve / max(d, 1e-4))
    return att * dec


def band(sig, lo, hi):
    f = np.fft.rfft(sig)
    fr = np.fft.rfftfreq(len(sig), 1 / SR)
    m = ((fr >= lo) & (fr <= hi)).astype(float)
    # soft edges
    m = np.convolve(m, np.hanning(41) / np.hanning(41).sum(), mode="same")
    return np.fft.irfft(f * m, len(sig))


def sweep_noise(d, f0, f1, width=0.6, shape=None):
    """Noise whose band centre glides f0->f1 (whoosh). Processed in short blocks."""
    n = int(SR * d)
    noise = rng.standard_normal(n)
    out = np.zeros(n)
    blk = 1024
    win = np.hanning(blk * 2)
    for i in range(0, n, blk):
        seg = noise[max(0, i - blk // 2): i - blk // 2 + blk * 2]
        if len(seg) < blk * 2:
            seg = np.pad(seg, (0, blk * 2 - len(seg)))
        p = min(1, i / n)
        fc = f0 * (f1 / f0) ** p
        y = band(seg * win, fc * (1 - width), fc * (1 + width))
        s = max(0, i - blk // 2)
        e = min(n, s + blk * 2)
        out[s:e] += y[: e - s]
    if shape is None:
        x = np.linspace(0, 1, n)
        shape = np.sin(np.pi * x) ** 1.5
    return out * shape


def tone(d, f0, f1=None, kind="sine"):
    x = t(d)
    f1 = f0 if f1 is None else f1
    freq = f0 * (f1 / f0) ** (x / d)
    ph = 2 * np.pi * np.cumsum(freq) / SR
    return np.sin(ph) if kind == "sine" else np.sign(np.sin(ph)) * 0.3


def norm(s, peak=0.85):
    m = np.max(np.abs(s)) or 1
    return s / m * peak


def save(name, s, peak=0.85):
    s = norm(s, peak)
    fade = min(len(s), int(SR * 0.004))
    s[-fade:] *= np.linspace(1, 0, fade)
    data = (np.stack([s, s], 1) * 32767).astype(np.int16)
    with wave.open(os.path.join(OUT, name + ".wav"), "w") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())


def click(d=0.05, lo=2000, hi=9000, decay=0.012):
    n = int(SR * d)
    return band(rng.standard_normal(n), lo, hi) * env(n, 0.0005, decay)


# --- the set ---------------------------------------------------------------
save("tick", click(0.06, 3000, 12000, 0.008) + 0.5 * tone(0.06, 2400) * env(int(SR * .06), .0005, .01), 0.45)

blop = tone(0.22, 180, 620) * env(int(SR * .22), .003, .12)
save("blop", blop, 0.8)

mclick = click(0.08, 1500, 7000, 0.01)
mclick[int(SR * .03):] += click(0.05, 1200, 5000, 0.008)[: len(mclick) - int(SR * .03)]
save("mouse_click", mclick, 0.7)

n = int(SR * .35)
splat = band(rng.standard_normal(n), 300, 4000) * env(n, .002, .12) + 0.6 * tone(.35, 300, 90) * env(n, .001, .08)
save("splat", splat, 0.8)

save("whoosh_short", sweep_noise(0.32, 600, 3500, 0.5), 0.7)
lw = sweep_noise(0.7, 200, 1400, 0.6) + 0.5 * tone(.7, 70, 45) * np.sin(np.pi * np.linspace(0, 1, int(SR * .7)))
save("whoosh_low", lw, 0.85)

n = int(SR * .25)
save("thup", tone(.25, 140, 60) * env(n, .002, .09) + 0.3 * click(.25, 200, 2000, .02), 0.85)

n = int(SR * .9)
plop = tone(.9, 520, 260) * env(n, .002, .35) + 0.4 * tone(.9, 1040, 520) * env(n, .002, .2)
save("plop", plop, 0.75)

save("snap", click(0.05, 2500, 10000, 0.006) + 0.4 * tone(.05, 1800) * env(int(SR * .05), .0005, .008), 0.5)

n = int(SR * .12)
save("tok", tone(.12, 420, 300) * env(n, .001, .045) + 0.3 * click(.12, 800, 4000, .01), 0.6)

n = int(SR * .5)
save("whump", tone(.5, 110, 50) * env(n, .01, .2) + 0.4 * band(rng.standard_normal(n), 80, 600) * env(n, .01, .15), 0.85)

n = int(SR * .6)
rus = band(rng.standard_normal(n), 1500, 9000) * (0.5 + 0.5 * np.abs(np.sin(np.linspace(0, 18, n)))) * np.sin(np.pi * np.linspace(0, 1, n))
save("rustle", rus, 0.5)

for i, f in enumerate([520, 620, 740, 880]):
    n = int(SR * .18)
    save(f"pop_{i+1}", tone(.18, f * .7, f * 1.5) * env(n, .002, .06), 0.6)

save("zoom_whoosh", sweep_noise(0.55, 300, 6000, 0.45), 0.75)

# typing: individual key, combined later via many short clicks
key_n = int(SR * .045)
save("key", click(.045, 1800, 8000, .007) + 0.3 * tone(.045, 900) * env(key_n, .0005, .01), 0.45)


def typing(chars, rate=14.0, seed=3):
    r = np.random.default_rng(seed)
    d = chars / rate + 0.1
    out = np.zeros(int(SR * d))
    for c in range(chars):
        st = int(SR * (c / rate + r.uniform(-0.012, 0.012)))
        k = click(.045, 1600 + r.uniform(0, 800), 8000, .006 + r.uniform(0, .003)) * r.uniform(.6, 1)
        st = max(0, st)
        out[st: st + len(k)] += k[: len(out) - st]
    return out


save("typing_23", typing(23), 0.5)
save("typing_20", typing(20, 16, 5), 0.5)

x = np.linspace(0, 1, int(SR * .6))
save("swell", sweep_noise(0.6, 300, 4000, 0.5, x ** 2.2), 0.8)

save("scan", sweep_noise(0.7, 2500, 7000, 0.35), 0.4)
save("fwip", sweep_noise(0.18, 1500, 6000, 0.4), 0.55)
save("swoosh_soft", sweep_noise(0.45, 400, 1800, 0.5), 0.5)
n = int(SR * .2)
save("thock", tone(.2, 240, 160) * env(n, .001, .06) + 0.4 * click(.2, 500, 3000, .015), 0.65)

n = int(SR * .5)
mk = band(rng.standard_normal(n), 2500, 8000) * (0.7 + 0.3 * np.sin(np.linspace(0, 60, n))) * np.sin(np.pi * np.linspace(0, 1, n)) ** .5
save("marker", mk, 0.45)

n = int(SR * .3)
stamp = tone(.3, 160, 70) * env(n, .001, .07) + 0.7 * band(rng.standard_normal(n), 200, 3500) * env(n, .001, .03)
save("stamp", stamp, 0.85)

dw = sweep_noise(0.8, 150, 2500, 0.6) + 0.6 * tone(.8, 60, 35) * np.sin(np.pi * np.linspace(0, 1, int(SR * .8)))
save("whoosh_deep", dw, 0.85)

n = int(SR * 2.6)
ting = sum(a * tone(2.6, f) * env(n, .002, dd) for f, a, dd in [(1318.5, 1, 1.6), (2637, .35, .9), (1975.5, .25, 1.2), (3951, .1, .4)])
save("ting", ting, 0.6)

n = int(SR * 1.2)
chord = sum(tone(1.2, f) * env(n, .01, .9, 3) for f in [220, 277.2, 329.6, 415.3])
save("rhodes", chord, 0.5)
print("ok", len(os.listdir(OUT)))
