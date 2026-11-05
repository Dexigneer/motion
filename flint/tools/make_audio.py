"""Synthesize the temporary SFX set + a 128 BPM temp beat for the FLINT promo.

Deterministic and license-free. Usage: python3 tools/make_audio.py
Writes assets/sfx/*.wav and assets/music/temp_beat.wav. Swap any file 1:1 later.
"""
import os, wave
import numpy as np

SR = 48000
rng = np.random.default_rng(21)
HERE = os.path.dirname(os.path.abspath(__file__))
SFX = os.path.join(HERE, "..", "assets", "sfx")
MUS = os.path.join(HERE, "..", "assets", "music")
os.makedirs(SFX, exist_ok=True)
os.makedirs(MUS, exist_ok=True)


def n_(d):
    return int(SR * d)


def t(d):
    return np.arange(n_(d)) / SR


def env(n, a=0.002, d=0.1, curve=4.0):
    x = np.arange(n) / SR
    return np.clip(x / max(a, 1e-4), 0, 1) * np.exp(-np.clip(x - a, 0, None) * curve / max(d, 1e-4))


def band(sig, lo, hi):
    f = np.fft.rfft(sig)
    fr = np.fft.rfftfreq(len(sig), 1 / SR)
    m = ((fr >= lo) & (fr <= hi)).astype(float)
    m = np.convolve(m, np.hanning(41) / np.hanning(41).sum(), mode="same")
    return np.fft.irfft(f * m, len(sig))


def noise(d):
    return rng.standard_normal(n_(d))


def sweep_noise(d, f0, f1, width=0.5, shape=None):
    n = n_(d)
    src = rng.standard_normal(n)
    out = np.zeros(n)
    blk = 1024
    win = np.hanning(blk * 2)
    for i in range(0, n, blk):
        s = max(0, i - blk // 2)
        seg = src[s: s + blk * 2]
        if len(seg) < blk * 2:
            seg = np.pad(seg, (0, blk * 2 - len(seg)))
        fc = f0 * (f1 / f0) ** min(1, i / n)
        y = band(seg * win, fc * (1 - width), fc * (1 + width))
        e = min(n, s + blk * 2)
        out[s:e] += y[: e - s]
    if shape is None:
        shape = np.sin(np.pi * np.linspace(0, 1, n)) ** 1.5
    return out * shape


def tone(d, f0, f1=None, kind="sine", vib=0.0, vibf=0.0):
    x = t(d)
    f1 = f0 if f1 is None else f1
    freq = f0 * (f1 / f0) ** (x / d)
    if vib:
        freq = freq * (1 + vib * np.sin(2 * np.pi * vibf * x))
    ph = 2 * np.pi * np.cumsum(freq) / SR
    if kind == "saw":
        return 2 * ((ph / (2 * np.pi)) % 1) - 1
    if kind == "sq":
        return np.sign(np.sin(ph))
    return np.sin(ph)


def norm(s, peak=0.85):
    m = np.max(np.abs(s)) or 1
    return s / m * peak


def write(path, s, peak=0.85):
    s = norm(np.asarray(s, float), peak)
    f = min(len(s), n_(0.004))
    s[-f:] *= np.linspace(1, 0, f)
    data = (np.stack([s, s], 1) * 32767).astype(np.int16)
    with wave.open(path, "w") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())


def save(name, s, peak=0.85):
    write(os.path.join(SFX, name + ".wav"), s, peak)


def click(d=0.05, lo=2000, hi=9000, decay=0.012):
    return band(noise(d), lo, hi) * env(n_(d), 0.0005, decay)


def mix(*parts):
    L = max(len(p) for p in parts)
    out = np.zeros(L)
    for p in parts:
        out[: len(p)] += p
    return out


# --- SFX ----------------------------------------------------------------------
save("tick", click(0.05, 3000, 12000, 0.006) + 0.5 * tone(0.05, 2600) * env(n_(.05), .0005, .008), 0.5)
save("thud", tone(.35, 120, 45) * env(n_(.35), .001, .12) + 0.5 * click(.35, 100, 1500, .03), 0.95)
save("schwip", sweep_noise(0.22, 1500, 9000, 0.35, np.linspace(0, 1, n_(.22)) ** 0.6 * np.linspace(1, 0, n_(.22)) ** 0.3), 0.75)
save("clack", click(.05, 1200, 7000, .008) + 0.4 * tone(.05, 900, 600) * env(n_(.05), .0005, .01), 0.5)
save("boing", tone(.5, 180, 420, vib=0.12, vibf=18) * env(n_(.5), .002, .3), 0.7)
save("boing_lo", tone(.45, 110, 240, vib=0.15, vibf=14) * env(n_(.45), .002, .25), 0.8)
flap = np.zeros(n_(.32))
for i in range(5):
    c = click(.04, 600, 5000, .01)
    st = n_(i * 0.055)
    flap[st: st + len(c)] += c[: len(flap) - st] * (1 - i * 0.12)
save("flap", flap, 0.6)
save("riser", sweep_noise(0.5, 300, 8000, 0.4, np.linspace(0, 1, n_(.5)) ** 2.5), 0.6)
x = t(.7)
bwamp = tone(.7, 90, 40) * env(n_(.7), .002, .35) + 0.4 * tone(.7, 180, 80, "saw") * env(n_(.7), .002, .12)
save("bwamp", bwamp, 0.95)
save("wub", tone(.55, 70, 140, "saw", vib=0.3, vibf=9) * env(n_(.55), .01, .4) * 0.6 + band(noise(.55), 60, 600) * env(n_(.55), .01, .2) * .2, 0.6)
# strike: hard click + metallic ring + crackle
strike = mix(click(.08, 3000, 14000, .01) * 1.5, 0.3 * (tone(.6, 3100) + tone(.6, 4870)) * env(n_(.6), .0005, .15))
crk = np.zeros(n_(.7))
for i in range(40):
    st = int(rng.uniform(0, 0.6) * SR)
    c = click(.01, 2500, 12000, .002) * rng.uniform(.2, 1) * (1 - st / len(crk))
    crk[st: st + len(c)] += c[: len(crk) - st]
save("strike", mix(strike, crk * 0.8), 0.9)
save("whomp", tone(.6, 160, 38) * env(n_(.6), .005, .25) + 0.5 * sweep_noise(.6, 900, 150, .6), 0.95)
save("tok", tone(.12, 520, 360) * env(n_(.12), .001, .04) + 0.3 * click(.12, 800, 4000, .01), 0.6)
ping = sum(a * tone(1.0, f) * env(n_(1.0), .001, dd) for f, a, dd in [(1760, 1, .5), (3520, .3, .25), (2637, .2, .35)])
save("ping", ping, 0.45)
save("whoosh_in", sweep_noise(0.4, 300, 6000, 0.45, np.linspace(0, 1, n_(.4)) ** 1.8), 0.8)
save("whoosh", sweep_noise(0.35, 500, 3000, 0.5), 0.7)
for i, f in enumerate([520, 600, 690, 790, 900, 1030]):
    save(f"pop_{i+1}", tone(.16, f * .7, f * 1.6) * env(n_(.16), .002, .05), 0.6)
save("click", click(.06, 1500, 7000, .008) + 0.3 * click(.06, 1000, 4000, .01), 0.7)
save("zip", sweep_noise(0.3, 800, 5000, 0.3) * (0.6 + 0.4 * np.sign(np.sin(np.linspace(0, 90, n_(.3))))), 0.6)
snip = mix(click(.04, 3000, 12000, .005), np.pad(click(.04, 4000, 12000, .004), (n_(.035), 0)))
save("snip", snip, 0.6)
save("fwip", sweep_noise(0.16, 1800, 7000, 0.4), 0.55)
crunch = band(noise(.25), 300, 5000) * env(n_(.25), .002, .08) * (0.5 + 0.5 * np.abs(np.sin(np.linspace(0, 60, n_(.25)))))
save("crunch", crunch, 0.7)
save("slam", tone(.45, 100, 40) * env(n_(.45), .001, .16) + 0.7 * band(noise(.45), 200, 6000) * env(n_(.45), .001, .05), 0.95)
save("schwing", sweep_noise(0.3, 2500, 9000, 0.25) + 0.25 * tone(.3, 2400, 3600) * env(n_(.3), .01, .15), 0.7)
save("wobble", tone(.6, 300, 300, vib=0.25, vibf=11) * env(n_(.6), .005, .35), 0.5)
ding = sum(a * tone(1.6, f) * env(n_(1.6), .001, dd) for f, a, dd in [(1318.5, 1, .9), (2637, .35, .5), (1975.5, .3, .7)])
save("ding", ding, 0.55)
save("kachunk", mix(click(.06, 400, 4000, .012) * 1.2, np.pad(tone(.25, 140, 60) * env(n_(.25), .001, .08), (n_(.05), 0)), np.pad(click(.05, 1500, 8000, .006), (n_(.09), 0))), 0.9)
save("stretch", tone(.45, 200, 700, "saw") * env(n_(.45), .02, .5) * 0.4 + band(noise(.45), 400, 3000) * 0.1, 0.5)
save("sup", sweep_noise(.25, 5000, 400, .4, np.linspace(1, 0, n_(.25)) ** 0.5), 0.6)
save("zap", mix(tone(.35, 2400, 200, "sq") * env(n_(.35), .001, .12) * .4, click(.35, 2000, 12000, .05) * .5), 0.7)
save("tiktok", mix(click(.04, 3000, 9000, .006), np.pad(click(.04, 1500, 5000, .006), (n_(.17), 0))), 0.45)
save("cascade", mix(*[np.pad(click(.03, 2500, 9000, .004) * (1 - i / 26), (n_(i * .012), 0)) for i in range(26)]), 0.5)

# --- Temp music: 128 BPM, 24 s -------------------------------------------------
BPM = 128
B = 60 / BPM
DUR = 24.5
song = np.zeros(n_(DUR))


def put(sig, at, g=1.0):
    st = n_(at)
    if st >= len(song):
        return
    e = min(len(song), st + len(sig))
    song[st:e] += sig[: e - st] * g


kick = tone(.35, 150, 42) * env(n_(.35), .001, .16) + 0.25 * click(.35, 1000, 5000, .004)
clap = mix(*[np.pad(band(noise(.18), 900, 6000) * env(n_(.18), .001, .05), (n_(k * .011), 0)) for k in range(3)])
hat = band(noise(.05), 7000, 16000) * env(n_(.05), .0005, .015)
ohat = band(noise(.18), 6000, 16000) * env(n_(.18), .001, .07)
root = [55.0, 55.0, 65.4, 49.0]  # A1, A1, C2, G1 per bar


def bass(f, d):
    s = tone(d, f, kind="saw") * 0.6 + tone(d, f * 2, kind="sq") * 0.15 + tone(d, f / 2) * 0.6
    return band(s, 30, 900) * env(n_(d), .004, d * .8, 2.5)


def stab(f, d=0.22):
    s = sum(tone(d, f * r, kind="saw") for r in (1, 1.189, 1.498, 2))
    return band(s, 200, 4000) * env(n_(d), .002, .12)


DROP = 8 * B          # 3.75
BREAK = 34 * B        # 15.94
END = 44 * B          # 20.625
nbeats = int(DUR / B)
for b in range(nbeats):
    at = b * B
    if at >= END + 0.01:
        break
    in_break = BREAK - 0.01 <= at < BREAK + B - 0.01
    if in_break:
        continue
    put(kick, at, 1.0 if at >= DROP else 0.8)
    put(hat, at + B / 2, 0.35)
    if at >= DROP:
        if b % 2 == 1:
            put(clap, at, 0.55)
        put(hat, at + B / 4, 0.18)
        put(hat, at + 3 * B / 4, 0.18)
        if b % 4 == 3:
            put(ohat, at + B / 2, 0.25)
        bar = int((at - DROP) / (4 * B)) % 4
        f = root[bar]
        put(bass(f, B * 0.45), at + B / 2, 0.55)
        if b % 4 == 0:
            put(bass(f, B * 0.35), at, 0.4)
        if b % 8 in (0, 3, 6):
            put(stab(f * 4), at + (B / 2 if b % 8 == 3 else 0), 0.16)
# intro riser into the drop
put(sweep_noise(1.6, 300, 9000, 0.4, np.linspace(0, 1, n_(1.6)) ** 3), DROP - 1.6, 0.35)
# riser into the break & the end
put(sweep_noise(0.9, 400, 7000, 0.4, np.linspace(0, 1, n_(.9)) ** 3), BREAK - 0.9, 0.25)
# final hit with tail
tail = n_(3.2)
put(kick, END, 1.1)
put(sum(tone(3.2, f, kind="saw") for f in (220, 261.6, 329.6, 440)) * env(tail, .005, 1.6, 3) * 0.08, END, 1)
put(tone(3.2, 55) * env(tail, .003, 1.4, 3) * 0.5, END, 1)
write(os.path.join(MUS, "temp_beat.wav"), song, 0.8)
print("ok", len(os.listdir(SFX)), "sfx + temp_beat")
