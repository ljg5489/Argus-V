"""Architecture figure of Argus-V-emp (PNG + SVG, English only). Draws only; reads no data and fits nothing.

Every number in the figure is taken from the code and the saved model folder:
  argus_v_emp_model.py / argus_v_emp.py      the mix (36 Argus-V-em models + P3 + P5, shares against validation, 1/3 each)
  argus_v_em.py, argus_v_em_epochs.py        LearnedEmbedding / LinearScorer, robust_scale (clip 5), full-batch AdamW
  resplit_run01.py                           4 architectures x 3 weights x 3 seeds, 5,360 sampled rows per seed
  argus_v_emp_export.py, argus_v_p.py        P3 / P5: median-IQR scaling (clip 3), PCA, three linear members, random forest
  artifacts/.../argus_v_emp/*.pt, manifest   pos_weight 14.32 / 54.21 / 300, cut-offs 0.864 / 0.932, 3,217 validation calls

Usage: py -3.11 experiments/risk_loop/argus_loop/argus_v_emp_architecture.py
Output: reports/risk-loop/argus-v-emp/architecture/argus_v_emp_architecture.png and .svg
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
matplotlib.rcParams["svg.fonttype"] = "none"
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "reports" / "risk-loop" / "argus-v-emp" / "architecture"
W, H = 2400, 1820

# face colour, edge colour
GRAY = ("#dfe3e8", "#59626e")      # frozen LLM hidden states
ORANGE = ("#f8cfa6", "#b85c12")    # pooling over positions
PURPLE = ("#dccdf1", "#6a3da0")    # robust scaling + clipping
BLUE = ("#bcd9f3", "#1d5ea8")      # trained linear layer
TEAL = ("#b9e5de", "#17786c")      # LayerNorm + GELU
RED = ("#f5bcbc", "#b53030")       # PCA
GREEN = ("#c3e7b8", "#2d7a31")     # random forest
AMBER = ("#f8e3a0", "#9c7500")     # percentile among the member's own train scores
PINK = ("#f6c1dc", "#ab2d76")      # share of validation calls scored lower
CONCAT = ("#ffffff", "#59626e")    # concatenation, no parameters
INK = "#22262b"
SOFT = "#5a6068"
HEAD = "#1b8a8f"
ALARM = "#b53030"
VEC = "#8a9099"                    # a vector inside one model
C23 = "#1d5ea8"                    # line colour of x23
C16 = "#a8581a"                    # line colour of x16
V23 = ("#ffffff", C23)             # pooled vector x23 (not trained)
V16 = ("#ffffff", C16)             # pooled vector x16 (not trained)
GAP = 7                            # half-width of a line jump


def mix(c: str, other: str, t: float) -> str:
    a = [int(c[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(other[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * t):02x}" for x, y in zip(a, b))


def box(ax, x, yc, w, h, col, d=10, z=3, lw=1.1):
    """A 3-D slab: front face x..x+w, centred at yc, depth d going up-right."""
    face, edge = col
    y0, y1 = yc - h / 2, yc + h / 2
    top = mix(face, "#ffffff", 0.45) if face != "#ffffff" else "#f4f5f7"
    side = mix(face, "#000000", 0.12) if face != "#ffffff" else "#e6e8eb"
    ax.add_patch(Polygon([(x, y0), (x + d, y0 - d), (x + w + d, y0 - d), (x + w, y0)], closed=True, fc=top, ec=edge, lw=lw, zorder=z, joinstyle="round"))
    ax.add_patch(Polygon([(x + w, y0), (x + w + d, y0 - d), (x + w + d, y1 - d), (x + w, y1)], closed=True, fc=side, ec=edge, lw=lw, zorder=z, joinstyle="round"))
    ax.add_patch(Rectangle((x, y0), w, h, fc=face, ec=edge, lw=lw, zorder=z, joinstyle="round"))


def line(ax, pts, color=INK, lw=1.5, head=True, z=1):
    """Polyline through pts; the last segment ends in an arrow head."""
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    if head:
        ax.plot(xs[:-1], ys[:-1], color=color, lw=lw, zorder=z, solid_capstyle="butt")
        ax.add_patch(FancyArrowPatch(pts[-2], pts[-1], arrowstyle="-|>", mutation_scale=11, shrinkA=0, shrinkB=0, color=color, lw=lw, zorder=z))
    else:
        ax.plot(xs, ys, color=color, lw=lw, zorder=z, solid_capstyle="butt")


def hline(ax, x0, x1, y, color, gaps=(), head=False):
    """Horizontal line from x0 to x1 that is broken (passes under) at each x in gaps."""
    cuts = sorted(g for g in gaps if min(x0, x1) < g < max(x0, x1))
    pts, start = [], x0
    for g in cuts:
        pts.append((start, g - GAP))
        start = g + GAP
    pts.append((start, x1))
    for i, (a, b) in enumerate(pts):
        line(ax, [(a, y), (b, y)], color=color, head=head and i == len(pts) - 1)


def vline(ax, x, y0, y1, color, gaps=()):
    cuts = sorted(g for g in gaps if min(y0, y1) < g < max(y0, y1))
    start = y0
    for g in cuts:
        line(ax, [(x, start), (x, g - GAP)], color=color, head=False)
        start = g + GAP
    line(ax, [(x, start), (x, y1)], color=color, head=False)


def dot(ax, x, y, color):
    ax.add_patch(Circle((x, y), 4.5, fc=color, ec=color, zorder=2))


def txt(ax, x, y, s, size=9.5, ha="center", va="center", color=INK, weight="normal", style="normal"):
    ax.text(x, y, s, fontsize=size, ha=ha, va=va, color=color, fontweight=weight, fontstyle=style, zorder=6, linespacing=1.3)


def node(ax, x, y, label, r=24, size=9):
    ax.add_patch(Circle((x, y), r, fc="#3f454d", ec="#1c1f23", lw=1.1, zorder=4))
    txt(ax, x, y, label, size=size, color="#ffffff", weight="bold")


def panel(ax, x, y, w, h, title, subs=()):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=14", fc="#fafbfc", ec="#c5cbd3", lw=1.2, zorder=0))
    txt(ax, x + 16, y + 22, title, size=13, ha="left", weight="bold", color=HEAD)
    for i, s in enumerate(subs):
        txt(ax, x + 16, y + 46 + 19 * i, s, size=9.2, ha="left", color=SOFT)


def member(ax, x, y, lines):
    """Three lines of text sitting just above the output line of a member."""
    txt(ax, x, y - 6, "\n".join(lines[1:]), size=8.4, ha="left", va="bottom", color=SOFT)
    txt(ax, x, y - 6 - 15 * (len(lines) - 1) - 3, lines[0], size=9, ha="left", va="bottom")


def p_branch(ax, top, name, subs, k23, k16_store, k16_used, cs, rf):
    """One Argus-V-p setting. top = y of the panel top. Returns (y of x23 input, y of x16 input, y of output)."""
    hp = {128: 92, 32: 50}                      # PCA box heights
    hm = {128: 60, 32: 36, 10: 22}              # member box heights
    panel(ax, 610, top, 1080, 570 if rf else 460, name, subs)
    y23, y16 = top + 210, top + 370
    m1, m3 = y23 - 50, y16
    m2 = (m1 + m3) / 2
    tap_rf = (805, 823) if rf else ()
    for y, col, vcol, k, used in ((y23, C23, PURPLE, k23, k23), (y16, C16, PURPLE, k16_store, k16_used)):
        box(ax, 650, y, 15, 110, vcol)
        txt(ax, 657, y + 62, "2,880", size=8.5, color=SOFT, va="top")
        line(ax, [(665, y), (735, y)], color=col)
        box(ax, 735, y, 28, hp[k], RED)
        txt(ax, 749, y + hp[k] / 2 + 8, f"PCA {k}" + ("" if used == k else f"\n(first {used} used)"), size=8.8, color=RED[1], va="top")
    lab = {m1: ("Member 1 · logistic regression on single calls", f"score = w · z,  z = PCA values 1–{k23},  C = {cs[0]}", "equal total weight per period × class; then the normals", "in tool × period cells holding a violation get half of it"),
           m2: ("Member 2 · pairwise ranking inside one rollout", f"score = w · z,  z = PCA values 1–{k23},  C = {cs[1]}", "fitted on (violation, normal) pairs of one rollout", "(same trajectory); each violation's pairs weigh the same"),
           m3: ("Member 3 · pairwise ranking inside one rollout", f"score = w · z,  z = PCA values 1–{k16_used},  C = {cs[2]}", "fitted on (violation, normal) pairs of one rollout", "(same trajectory); each violation's pairs weigh the same")}
    ks = {m1: k23, m2: k23, m3: k16_used}
    # inputs of the members
    vline(ax, 850, m1, m2, C23)
    line(ax, [(763, y23), (850, y23)], color=C23, head=False)
    dot(ax, 850, y23, C23)
    line(ax, [(850, m1), (890, m1)], color=C23)
    line(ax, [(850, m2), (890, m2)], color=C23)
    hline(ax, 763, 890, m3, C16, gaps=tap_rf[:1], head=True)
    for ym in (m1, m2, m3):
        box(ax, 890, ym, 20, hm[ks[ym]], BLUE, d=8)
        member(ax, 932, ym, lab[ym])
        line(ax, [(918, ym), (1290, ym)])
        box(ax, 1290, ym, 16, 34, AMBER, d=7)
    ymean = (m1 + m3) / 2
    for ym in (m1, m2, m3):
        line(ax, [(1313, ym), (1350, ym), (1350, ymean), (1394, ymean)])
    dot(ax, 1350, ymean, INK)
    node(ax, 1420, ymean, "mean\nof 3", r=26, size=8.5)
    yout = ymean
    if rf:
        yrf = top + 505
        xa, xb = tap_rf
        vline(ax, xa, y23, yrf - 16, C23)
        line(ax, [(xa, yrf - 16), (890, yrf - 16)], color=C23)
        vline(ax, xb, y16, yrf + 16, C16, gaps=(yrf - 16,))
        line(ax, [(xb, yrf + 16), (890, yrf + 16)], color=C16)
        dot(ax, xa, y23, C23)
        dot(ax, xb, y16, C16)
        box(ax, 890, yrf, 20, 62, CONCAT, d=8)
        txt(ax, 900, yrf + 40, "concat 42 = 32 + 10", size=8.6, color=SOFT, va="top")
        line(ax, [(918, yrf), (970, yrf)], color=VEC)
        box(ax, 970, yrf, 70, 62, GREEN, d=10)
        txt(ax, 1005, yrf, "500\ntrees", size=9, weight="bold", color=GREEN[1])
        member(ax, 1062, yrf, ("Random forest · output P(violation)", "min leaf 10 · sqrt features · bootstrap", "row weights as in member 1"))
        line(ax, [(1050, yrf), (1290, yrf)])
        box(ax, 1290, yrf, 16, 34, AMBER, d=7)
        ymix = (ymean + yrf) / 2
        line(ax, [(1446, ymean), (1500, ymean), (1500, ymix - 24)])
        line(ax, [(1313, yrf), (1500, yrf), (1500, ymix + 24)])
        txt(ax, 1512, ymean + 30, "× 0.75", size=9, ha="left", weight="bold")
        txt(ax, 1512, yrf - 24, "× 0.25", size=9, ha="left", weight="bold")
        node(ax, 1500, ymix, "sum", r=24, size=9)
        line(ax, [(1524, ymix), (1572, ymix)])
        yout = ymix
    else:
        line(ax, [(1446, ymean), (1572, ymean)])
    box(ax, 1572, yout, 18, 44, PINK, d=8)
    txt(ax, 1585, yout + 32, "share vs\nvalidation", size=8.4, color=PINK[1], va="top")
    if rf:
        txt(ax, 1538, yout - 36, f"{name.split()[-1]}\nscore", size=8.4, color=SOFT)
    else:
        txt(ax, 1500, yout - 22, f"{name.split()[-1]} score\nin [0, 1]", size=8.4, color=SOFT)
    return y23, y16, yout


def draw():
    fig = plt.figure(figsize=(24, 18.2))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")
    fig.patch.set_facecolor("#ffffff")

    # ------------------------------------------------------------------ title
    txt(ax, 2370, 48, "Argus-V-emp Architecture", size=27, ha="right", weight="bold")
    txt(ax, 2370, 90, "A risk score for one tool call, read from the hidden states of a frozen LLM.", size=11.5, ha="right", color=SOFT)
    txt(ax, 2370, 114, "38 small models; each score becomes a share of validation calls. Weights: the 36 Argus-V-em shares together 1/3, P3 1/3, P5 1/3.", size=11.5, ha="right", color=SOFT)

    T2, T3 = 640, 1120                         # panel tops of parts 2 and 3
    Y23, Y16 = 570, 880                        # input rows
    E23, E16 = 310, 430                        # part 1 input rows

    # ------------------------------------------------------------------ input: frozen LLM and pooling
    txt(ax, 30, 388, "Input", size=13, ha="left", weight="bold", color=HEAD)
    ax.add_patch(FancyBboxPatch((30, 410), 204, 62, boxstyle="round,pad=0,rounding_size=10", fc="#ffffff", ec="#59626e", lw=1.2, zorder=3))
    txt(ax, 132, 441, "One agent step:\ncontext → reasoning → tool call", size=8.8)
    line(ax, [(132, 472), (132, 546)], color=SOFT)
    box(ax, 30, 725, 190, 330, GRAY, d=14)
    txt(ax, 125, 700, "gpt-oss-20b", size=12.5, weight="bold")
    txt(ax, 125, 748, "frozen, never trained\nresidual stream\nwidth 2,880", size=9.2, color=SOFT)
    for y, blk, vec in ((Y23, 23, V23), (Y16, 16, V16)):
        col = vec[1]
        line(ax, [(234, y), (272, y)], color=col)
        for k in (2, 1, 0):
            box(ax, 272 + 7 * k, y - 7 * k, 12, 150, GRAY, d=6)
        txt(ax, 286, y + 84, f"block {blk} output\nn_obs × 2,880", size=8.8, color=SOFT, va="top")
        line(ax, [(304, y), (366, y)], color=col)
        box(ax, 366, y, 16, 150, ORANGE)
        line(ax, [(392, y), (446, y)], color=col)
        box(ax, 446, y, 14, 150, vec, lw=1.6)
        txt(ax, 458, y + 84, f"x{blk}\n1 × 2,880", size=9.2, weight="bold", color=col, va="top")
    txt(ax, 378, Y23 - 108, "max over the\nobservation positions", size=8.8, color=ORANGE[1])
    txt(ax, 378, Y16 - 118, "pre_action row\n(last position\nbefore the action)", size=8.8, color=ORANGE[1])
    txt(ax, 30, 1030, "n_obs = observation positions of the step: the points where\nhidden states were recorded (start of reasoning, every 32\nreasoning tokens, end of reasoning, just before the action).\nIf a step has no pre_action row, x16 takes its last row.", size=8.6, ha="left", color=SOFT, va="top")
    txt(ax, 30, 1120, "Not read when scoring: tool name, step number, prompt\nlength, collection period, scenario id. (Period, tool ×\nperiod cell and rollout are used only to sample, weight\nand pair the training rows.)", size=8.6, ha="left", color=SOFT, va="top")

    # buses: x23 at x = 520, x16 at x = 560 (lines going under a crossing are broken)
    p2_23, p2_16, p3_23, p3_16 = T2 + 210, T2 + 370, T3 + 210, T3 + 370
    line(ax, [(470, Y23), (520, Y23)], color=C23, head=False)
    vline(ax, 520, E23, p3_23, C23)
    hline(ax, 470, 560, Y16, C16, gaps=(520,))
    vline(ax, 560, E16, p3_16, C16, gaps=(p2_23, p3_23))
    dot(ax, 520, Y23, C23)
    dot(ax, 560, Y16, C16)
    for y in (p2_23, p3_23):
        line(ax, [(520, y), (650, y)], color=C23)
    for y in (p2_16, p3_16):
        line(ax, [(560, y), (650, y)], color=C16)
    dot(ax, 520, p2_23, C23)
    dot(ax, 560, p2_16, C16)

    # ------------------------------------------------------------------ part 1: Argus-V-em x 36
    panel(ax, 610, 135, 1080, 485, "Part 1 · Argus-V-em  × 36",
          ("4 architectures × 3 violation weights (BCE pos_weight 14.3, 54.2, 300) × 3 seeds, all read at epoch 67.",
           "Each seed: 5,360 train calls (26 visible violations + sampled normals). Full batch: epoch 67 = 67 AdamW steps, lr 1e-3, weight decay 1e-2."))
    line(ax, [(520, E23), (640, E23)], color=C23)
    line(ax, [(560, E16), (640, E16)], color=C16)
    box(ax, 640, E23, 13, 100, V23, lw=1.6, d=8)
    box(ax, 640, E16, 13, 100, V16, lw=1.6, d=8)
    ym = (E23 + E16) / 2
    line(ax, [(653, E23), (690, E23)], color=C23)
    line(ax, [(653, E16), (690, E16)], color=C16)
    box(ax, 690, ym, 15, 210, CONCAT, lw=1.4)
    txt(ax, 697, 492, "concat\n5,760", size=8.8, color=SOFT, va="top")
    line(ax, [(705, ym), (745, ym)], color=VEC)
    box(ax, 745, ym, 15, 206, PURPLE)
    txt(ax, 757, 492, "scaled\n5,760", size=8.8, color=SOFT, va="top")
    rows = ((300, "EM128", 128, 92, "737,793"), (400, "EM64", 64, 62, "368,897"), (478, "EM32", 32, 42, "184,449"))
    YL = 548
    line(ax, [(760, ym), (810, ym)], head=False, color=VEC)
    line(ax, [(810, 300), (810, YL)], head=False, color=VEC)
    dot(ax, 810, ym, VEC)
    dot(ax, 810, 400, VEC)
    dot(ax, 810, 478, VEC)
    txt(ax, 893, 228, "Linear\n5,760 → width", size=7.6, color=BLUE[1])
    txt(ax, 975, 228, "LayerNorm\n+ GELU", size=7.6, color=TEAL[1])
    txt(ax, 1050, 228, "Linear\nwidth → 1", size=7.6, color=BLUE[1])
    for y, name, w, h, n in rows:
        line(ax, [(810, y), (890, y)], color=VEC)
        box(ax, 890, y, 22, h, BLUE, d=9)
        line(ax, [(921, y), (960, y)], color=VEC)
        box(ax, 960, y, 22, h, TEAL, d=9)
        line(ax, [(991, y), (1030, y)], color=VEC)
        box(ax, 1030, y, 12, 16, BLUE, d=6)
        txt(ax, 1072, y - 24, f"{name}  × 9      width {w}", size=10, ha="left", weight="bold", va="bottom")
        txt(ax, 1072, y - 6, f"{n} trained values each", size=8.6, ha="left", color=SOFT, va="bottom")
        line(ax, [(1048, y), (1330, y)])
    line(ax, [(810, YL), (890, YL)], color=VEC)
    box(ax, 890, YL, 12, 16, BLUE, d=6)
    txt(ax, 896, YL + 22, "Linear 5,760 → 1  (no hidden layer, no dropout)", size=8.4, color=BLUE[1], ha="left")
    txt(ax, 1072, YL - 24, "LINEAR  × 9", size=10, ha="left", weight="bold", va="bottom")
    txt(ax, 1072, YL - 6, "5,761 trained values each · linear control", size=8.6, ha="left", color=SOFT, va="bottom")
    line(ax, [(908, YL), (1330, YL)])
    YP = 424
    box(ax, 1330, YP, 18, 300, PINK)
    txt(ax, 1365, 247, "36 logits  →  36 shares vs validation", size=8.8, color=SOFT)
    line(ax, [(1358, YP), (1394, YP)])
    node(ax, 1420, YP, "mean\nof 36", r=26, size=8.5)
    txt(ax, 650, 588, "Dropout 0.15 after GELU (EM models only) is active only in training.   Each seed has its own median / IQR scaling (shared by its 12 models).",
        size=8.4, color=SOFT, style="italic", ha="left")
    txt(ax, 650, 606, "36 networks = 11,672,100 trained values.   Visible violation = the fact that makes the call a violation was in the context before the call.",
        size=8.4, color=SOFT, style="italic", ha="left")

    # ------------------------------------------------------------------ parts 2 and 3: Argus-V-p
    _, _, y_p3 = p_branch(ax, T2, "Part 2 · Argus-V-p  P3",
                          ("Setting P3 of the Argus-V-p family: PCA + three linear members, weaker regularisation than P5 (PCA 128 instead of 32, C × 10).",
                           "C = inverse strength of the L2 penalty of a logistic regression (larger C = weaker). Fitted on all 9,653 train calls (77 violations)."),
                          128, 128, 32, ("1.0", "0.01", "0.1"), rf=False)
    _, _, y_p5 = p_branch(ax, T3, "Part 3 · Argus-V-p  P5",
                          ("Setting P5 of the Argus-V-p family: PCA + three linear members + a random forest (weight 1/4).",
                           "Fitted on all 9,653 train calls (77 violations)."),
                          32, 32, 10, ("0.1", "0.001", "0.01"), rf=True)

    # ------------------------------------------------------------------ the mix and the decision
    NX, NY, R = 1840, y_p3, 34
    line(ax, [(1446, YP), (NX, YP), (NX, NY - R)])
    txt(ax, 1600, YP - 16, "part 1  in [0, 1]", size=9.2, weight="bold")
    line(ax, [(1590, y_p3), (NX - R, y_p3)])
    txt(ax, 1748, y_p3 - 16, "part 2", size=9.2, weight="bold")
    line(ax, [(1590, y_p5), (NX, y_p5), (NX, NY + R)])
    txt(ax, 1748, y_p5 - 16, "part 3", size=9.2, weight="bold")
    node(ax, NX, NY, "mean\nof 3", r=R, size=10)
    txt(ax, NX - 14, NY - 50, "each input × 1/3", size=9, color=SOFT, ha="right")
    line(ax, [(NX + R, NY), (1920, NY)])
    ax.add_patch(FancyBboxPatch((1920, NY - 30), 110, 60, boxstyle="round,pad=0,rounding_size=10", fc="#fff6e0", ec=INK, lw=2.0, zorder=3))
    txt(ax, 1975, NY, "score\nin [0, 1]", size=10, weight="bold")
    txt(ax, 1975, NY + 44, "Argus-V-emp score\nrank-type, not a probability", size=9, color=SOFT, va="top")
    line(ax, [(2030, NY), (2080, NY)])
    ax.add_patch(Polygon([(2080, NY), (2160, NY - 48), (2240, NY), (2160, NY + 48)], closed=True, fc="#ffffff", ec=INK, lw=1.4, zorder=3))
    txt(ax, 2160, NY, "score >\ncut-off ?", size=9.5, weight="bold")
    txt(ax, 2160, NY - 62, "cut-off 0.864: 5% of the validation\nnormal calls score above it (0.932 for 1%)", size=8.8, color=SOFT, va="bottom")
    line(ax, [(2240, NY), (2288, NY)])
    txt(ax, 2294, NY - 10, "yes", size=9, ha="left", weight="bold", color=ALARM, va="bottom")
    txt(ax, 2294, NY + 2, "violation\n(alarm)", size=9.5, ha="left", weight="bold", color=ALARM, va="top")
    line(ax, [(2160, NY + 48), (2160, NY + 92)])
    txt(ax, 2160, NY + 106, "no → normal", size=9.5, weight="bold")

    # ------------------------------------------------------------------ legend
    lx, ly = 1905, 1075
    ax.add_patch(FancyBboxPatch((lx - 20, ly - 42), 505, 725, boxstyle="round,pad=0,rounding_size=14", fc="#ffffff", ec="#c5cbd3", lw=1.2, zorder=0))
    txt(ax, lx, ly - 14, "Legend", size=13, ha="left", weight="bold", color=HEAD)
    items = ((GRAY, "frozen LLM hidden states (gpt-oss-20b)"),
             (ORANGE, "max (x23) or row choice (x16) over the positions"),
             ("POOLED", "pooled vector x23 / x16 (1 × 2,880, not trained)"),
             (CONCAT, "concatenation (no parameters)"),
             (PURPLE, "robust scaling + clipping, median and IQR of the\nrows each model was fitted on\nArgus-V-em: (x − median) / IQR, clip ±5\nArgus-V-p: (x − median) / (IQR / 1.349), clip ±3"),
             (RED, "PCA fitted on the 9,653 train calls (fixed)"),
             (BLUE, "trained linear layer / linear scorer"),
             (TEAL, "LayerNorm + GELU"),
             (GREEN, "random forest (500 trees)"),
             (AMBER, "percentile of the score among that member's\nscores of the 9,653 train calls  → [0, 1]"),
             (PINK, "share of the 3,217 validation calls this model\nscored lower (ties count half, no label)  → [0, 1]"))
    y = ly + 26
    for col, lab in items:
        n = lab.count("\n")
        if col == "POOLED":
            box(ax, lx - 4, y, 12, 22, V23, d=5, lw=1.4)
            box(ax, lx + 16, y, 12, 22, V16, d=5, lw=1.4)
        else:
            box(ax, lx, y + 7.5 * n, 26, 22, col, d=7, lw=1.4 if col == CONCAT else 1.1)
        txt(ax, lx + 50, y + 7.5 * n, lab, size=9, ha="left")
        y += 38 + 15 * n
    ax.add_patch(Circle((lx + 13, y + 2), 14, fc="#3f454d", ec="#1c1f23", zorder=4))
    txt(ax, lx + 50, y + 2, "average / weighted sum of the incoming values", size=9, ha="left")
    y += 34
    line(ax, [(lx - 4, y), (lx + 30, y)], color=C23, lw=2)
    txt(ax, lx + 50, y, "x23 path: block 23 → max → x23, and values from it", size=9, ha="left")
    y += 26
    line(ax, [(lx - 4, y), (lx + 30, y)], color=C16, lw=2)
    txt(ax, lx + 50, y, "x16 path: block 16 → pre_action row → x16, and values from it", size=9, ha="left")
    y += 26
    ax.plot([lx - 4, lx + 9], [y, y], color=C16, lw=1.5)
    ax.plot([lx + 23, lx + 30], [y, y], color=C16, lw=1.5)
    ax.plot([lx + 16, lx + 16], [y - 12, y + 12], color=C23, lw=1.5)
    txt(ax, lx + 50, y, "broken line = passes under (not connected)", size=9, ha="left")
    y += 26
    line(ax, [(lx - 4, y), (lx + 30, y)], color=INK, lw=2)
    txt(ax, lx + 50, y, "black line = a score or a decision (one per call)", size=9, ha="left")
    y += 26
    line(ax, [(lx - 4, y), (lx + 30, y)], color=VEC, lw=2)
    txt(ax, lx + 50, y, "gray line = a vector mixing x23 and x16 (Part 1, forest)", size=9, ha="left")

    txt(ax, 30, 1740, "Training data = train part of the 17 Nov train / validation / test split only. P3 and P5: all 9,653 train calls (77 violations).",
        size=9.2, ha="left", color=SOFT)
    txt(ax, 30, 1762, "Each Argus-V-em network: 5,360 calls drawn per seed = the 26 visible violations + at most max(30, 20 × that cell's visible violations) normal calls per tool × period cell;",
        size=9.2, ha="left", color=SOFT)
    txt(ax, 30, 1784, "the other 51 violations are not used. The mix fits nothing; the shares use no label; the cut-off uses the validation normal calls. Test calls are only scored.",
        size=9.2, ha="left", color=SOFT)

    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "argus_v_emp_architecture.png", dpi=150, facecolor="#ffffff")
    fig.savefig(OUT / "argus_v_emp_architecture.svg", facecolor="#ffffff")
    plt.close(fig)
    print("saved", OUT / "argus_v_emp_architecture.png")
    print("saved", OUT / "argus_v_emp_architecture.svg")


if __name__ == "__main__":
    draw()
