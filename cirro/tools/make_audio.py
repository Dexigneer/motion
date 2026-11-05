"""Synthesize the temporary music bed + extra SFX for the Cirro promo (deterministic, license-free).

Usage: python3 tools/make_audio.py
  -> assets/music/cirro_bed.wav   (128 BPM, 24.4 s, drop on beat 10 = 4.6875 s)
  -> assets/sfx/boing.wav, riser.wav, blip.wav, slam.wav, chord_end.wav
Placeholder quality by design; replace the bed with a licensed 128 BPM track 1:1.
"""
import os, wave
import numpy as np

SR = 48000
BPM = 128
BEAT = 60 / BPM
DUR = 24.4
rng = np.random.default_rng(23)
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def write(path, sig, stereo=None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if stereo is None:
        stereo = np.stack([sig, sig], 1)
    peak = np.max(np.abs(stereo)) or 1
    stereo = stereo / peak * 0.89
    data = (stereo * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(data.tobytes())


def tt(d):
    return np.arange(int(SR * d)) / SR


def band(sig, lo, hi):
    f = np.fft.rfft(sig)
    fr = np.fft.rfftfreq(len(sig), 1 / SR)
    m = ((fr >= lo) & (fr <= hi)).astype(float)
    k = np.hanning(61); k /= k.sum()
    m = np.convolve(m, k, mode="same")
    return np.fft.irfft(f * m, len(sig))


def conv(a, b):
    n = len(a) + len(b) - 1
    N = 1 << (n - 1).bit_length()
    return np.fft.irfft(np.fft.rfft(a, N) * np.fft.rfft(b, N), N)[:n]


def reverb_ir(d=1.6, decay=3.2, seed=1):
    r = np.random.default_rng(seed)
    x = tt(d)
    ir = r.standard_normal(len(x)) * np.exp(-x * decay)
    ir = band(ir, 200, 9000)
    return ir / np.sqrt(np.sum(ir ** 2))


def note(n):  # midi -> Hz
    return 440 * 2 ** ((n - 69) / 12)


# ---- instruments -----------------------------------------------------------
def kick():
    x = tt(0.42)
    f = 46 + 110 * np.exp(-x * 28)
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * np.exp(-x * 7.5)
    click = band(rng.standard_normal(len(x)), 2000, 8000) * np.exp(-x * 220) * 0.35
    return np.tanh((body + click) * 1.6)


def clap():
    x = tt(0.3)
    n = band(rng.standard_normal(len(x)), 900, 5200)
    e = np.zeros_like(x)
    for o in (0, 0.011, 0.022):
        e += (x >= o) * np.exp(-np.clip(x - o, 0, None) * 60)
    e += np.exp(-x * 14) * 0.4
    return n * e * 0.8


def hat(open_=False):
    x = tt(0.25 if open_ else 0.06)
    n = band(rng.standard_normal(len(x)), 7000, 16000)
    return n * np.exp(-x * (16 if open_ else 90)) * 0.5


def pluck(freqs, d=0.42, bright=1.0):
    x = tt(d)
    s = np.zeros_like(x)
    for f in freqs:
        for det in (-0.12, 0.12):
            ff = f * 2 ** (det / 12)
            # soft saw from 6 harmonics, brightness decays (pluck)
            for h in range(1, 7):
                s += np.sin(2 * np.pi * ff * h * x) / h * np.exp(-x * (3 + h * 4 / bright))
    return s * np.exp(-x * 5.5) / (len(freqs) * 4)


def bass(f, d):
    x = tt(d)
    s = np.sin(2 * np.pi * f * x) + 0.35 * np.sin(2 * np.pi * 2 * f * x) + 0.12 * np.sin(2 * np.pi * 3 * f * x)
    env = np.minimum(1, x / 0.008) * np.exp(-x * 2.2)
    return np.tanh(s * 1.3) * env * 0.6


def pad(freqs, d):
    x = tt(d)
    s = np.zeros_like(x)
    for f in freqs:
        for det in (-0.08, 0, 0.08):
            s += np.sin(2 * np.pi * f * 2 ** (det / 12) * x + det * 40)
    env = np.minimum(1, x / 0.6) * np.minimum(1, (d - x) / 0.4)
    return s * env / (len(freqs) * 3)


# ---- arrangement -------------------------------------------------------------
N = int(SR * (DUR + 2.0))
drums = np.zeros(N); music = np.zeros(N); low = np.zeros(N); duck = np.ones(N)


def put(buf, sig, t, g=1.0):
    i = int(round(t * SR))
    if i >= len(buf):
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i] * g


K, C, H, HO = kick(), clap(), hat(), hat(True)
# progression per bar (4 beats): Fmaj7 · Am7 · Cmaj7 · G6  (airy, bright)
prog = [
    (53, [65, 69, 72, 76]),
    (57, [64, 67, 69, 72]),
    (48, [64, 67, 71, 72]),
    (55, [62, 67, 71, 74]),
]
DROP = 10
END = 45  # endcard beat -> final hit
total_beats = int(DUR / BEAT) + 1

for b in range(total_beats):
    t = b * BEAT
    bar = (b // 4) % 4
    root, chord = prog[bar]
    fr = [note(n) for n in chord]
    if b < END:
        # hats: 8ths before the drop, 16ths after
        steps = 4 if b >= DROP else 2
        for s in range(steps):
            st = t + s * BEAT / steps
            g = 0.55 if (s % 2) else 0.32
            put(drums, H, st, g * (0.7 if b < DROP else 1.0))
        if b >= DROP:
            put(drums, HO, t + BEAT / 2, 0.35)
            put(drums, K, t, 1.0)
            dk = np.ones(int(BEAT * SR))
            xx = np.arange(len(dk)) / SR
            dk = 1 - 0.7 * np.exp(-xx * 11)
            i = int(t * SR); duck[i:i + len(dk)] = np.minimum(duck[i:i + len(dk)], dk)
            if b % 2 == 1:
                put(drums, C, t, 0.75)
            # offbeat bass
            put(low, bass(note(root - 12), BEAT * 0.45), t + BEAT / 2, 1.0)
            if b % 4 == 3:
                put(low, bass(note(root - 12 + 7), BEAT * 0.2), t + BEAT * 0.75, 0.7)
        elif b >= 3:
            # pre-drop pulse bass, soft
            put(low, bass(note(root - 12), BEAT * 0.3), t, 0.45)
        # plucks: syncopated 3-3-2 pattern
        for off in (0, 0.75):
            if b >= 1:
                put(music, pluck(fr, bright=0.6 if b < DROP else 1.2), t + off * BEAT, 0.55 if b < DROP else 0.8)
        if b % 4 == 0 and b >= DROP:
            put(music, pad([f / 2 for f in fr], BEAT * 4), t, 0.5)
    # build: snare roll beats 7–10
    if 7 <= b < DROP:
        n = 4 if b < 9 else 8
        for s in range(n):
            put(drums, C, t + s * BEAT / n, 0.18 + 0.35 * ((b - 7) * n + s) / (3 * 8))

# final hit at the endcard
tf = END * BEAT
put(drums, K, tf, 1.0)
put(music, pad([note(n) for n in (53, 65, 69, 72, 76, 79)], 3.6), tf, 1.3)
put(music, pluck([note(n) for n in (77, 81, 84)], d=1.6, bright=2), tf, 0.8)
put(low, bass(note(41), 2.4), tf, 1.0)

# riser into the drop
rx = tt(DROP * BEAT - 3.0 * BEAT)
rs = band(rng.standard_normal(len(rx)), 1500, 9000) * (rx / rx[-1]) ** 2 * 0.25
put(music, rs, 3.0 * BEAT, 1.0)

mix_music = music * (0.55 + 0.45 * duck)
ir = reverb_ir()
wet = conv(mix_music, ir)[:N] * 0.22
low *= duck
L = drums + mix_music + wet * 1.0 + low
R = drums * 0.96 + mix_music * 0.98 + np.roll(wet, 480) + low
st = np.stack([L, R], 1)[: int(SR * DUR)]
fade = int(SR * 1.2)
st[-fade:] *= np.linspace(1, 0, fade)[:, None]
st = np.tanh(st / (np.max(np.abs(st)) or 1) * 1.4)
write(os.path.join(ROOT, "assets/music/cirro_bed.wav"), None, st)

# ---- extra SFX -------------------------------------------------------------
SFX = os.path.join(ROOT, "assets/sfx")
x = tt(0.38)  # boing: pitch-wobbling spring
f = 180 + 260 * np.exp(-x * 9) * (1 + 0.35 * np.sin(2 * np.pi * 22 * x))
s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-x * 8)
write(os.path.join(SFX, "boing.wav"), s * 0.8)

x = tt(1.4)  # riser
s = band(rng.standard_normal(len(x)), 800, 10000) * (x / x[-1]) ** 2.5
s += np.sin(2 * np.pi * np.cumsum(200 + 900 * (x / x[-1]) ** 2) / SR) * (x / x[-1]) ** 2 * 0.3
write(os.path.join(SFX, "riser.wav"), s)

x = tt(0.09)  # blip: tiny UI tick, pitched
s = np.sin(2 * np.pi * 1760 * x) * np.exp(-x * 60)
write(os.path.join(SFX, "blip.wav"), s)

x = tt(0.5)  # slam: low thump + noise crack
s = np.sin(2 * np.pi * np.cumsum(40 + 90 * np.exp(-x * 30)) / SR) * np.exp(-x * 7)
s += band(rng.standard_normal(len(x)), 1500, 7000) * np.exp(-x * 40) * 0.5
write(os.path.join(SFX, "slam.wav"), np.tanh(s * 1.8))
print("ok")
