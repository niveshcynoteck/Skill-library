import matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import to_hex

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "svg.fonttype": "none",
    "figure.facecolor": "white",
})

OUT = "/media/cynoteckdell/data/Documents/FastAPI practice/analysis_report_inbox-curator (sonnet)/testing/coverage_visuals"

TOTAL_STMTS = 665
TOTAL_MISSING = 187
TOTAL_COVERED = 478
TOTAL_PCT = 72

def cov_color(pct):
    pct = max(0.0, min(1.0, pct))
    cmap = plt.get_cmap("RdYlGn")
    return to_hex(cmap(pct))

# ---------------------------------------------------------------
# 1. Overall donut
# ---------------------------------------------------------------
covered_pct = TOTAL_COVERED / TOTAL_STMTS * 100
missing_pct = 100 - covered_pct

fig, ax = plt.subplots(figsize=(7, 5))
fig.suptitle("Inbox-Curator — Overall Test Coverage", fontsize=16, fontweight="bold", y=0.96)
ax.pie(
    [covered_pct, missing_pct],
    colors=[cov_color(0.72), "#d9d9d9"],
    startangle=90,
    counterclock=False,
    wedgeprops=dict(width=0.38, edgecolor="white", linewidth=2),
)
ax.text(0, 0.12, "72%", ha="center", va="center", fontsize=44, fontweight="bold", color=cov_color(0.72))
ax.text(0, -0.18, "478 / 665 statements\ncovered", ha="center", va="center", fontsize=13, color="#333333")
ax.text(0, -0.42, "coverage.py v7.15.3 · 2026-08-07", ha="center", va="center", fontsize=9, color="#888888")

legend = [
    mpatches.Patch(color=cov_color(0.72), label=f"Covered — {covered_pct:.0f}%  ({TOTAL_COVERED} stmts)"),
    mpatches.Patch(color="#d9d9d9", label=f"Missing — {missing_pct:.0f}%  ({TOTAL_MISSING} stmts)"),
]
ax.legend(handles=legend, loc="lower center", bbox_to_anchor=(0.5, -0.12), frameon=False, fontsize=11, ncol=2)

plt.tight_layout()
plt.savefig(f"{OUT}/1_overall_donut.svg", bbox_inches="tight", facecolor="white")
plt.close()

# ---------------------------------------------------------------
# 2. Module coverage (bar)
# ---------------------------------------------------------------
modules = [
    ("Config", 28, 0),
    ("EmailCurator", 36, 1),
    ("EmailFetcher", 70, 13),
    ("Scheduler", 34, 7),
    ("Utilities", 39, 9),
    ("TokenRefresher", 82, 20),
    ("EmailFilter", 241, 74),
    ("Root src\n(app / delete_api / logger)", 135, 63),
]
modules = sorted(modules, key=lambda m: (m[1] - m[2]) / m[1])

names = [m[0] for m in modules]
stmts = [m[1] for m in modules]
miss = [m[2] for m in modules]
pcts = [(c - m) / c * 100 for c, m in zip(stmts, miss)]

fig, ax = plt.subplots(figsize=(10.5, 5.4))
fig.suptitle("Coverage by Module", fontsize=16, fontweight="bold")
bars = ax.barh(names, pcts, color=[cov_color(p / 100) for p in pcts], edgecolor="white", height=0.62)
ax.set_xlim(0, 100)
ax.set_xlabel("Coverage (%)")
ax.set_ylabel("")
ax.xaxis.grid(True, linestyle="--", alpha=0.4)
ax.set_axisbelow(True)
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)

for bar, p, c, m in zip(bars, pcts, stmts, miss):
    ax.text(bar.get_width() + 1.5, bar.get_y() + bar.get_height() / 2,
            f"{p:.0f}%   ({c - m}/{c})", va="center", ha="left", fontsize=11,
            fontweight="bold" if p < 70 else "normal", color="#333333")

plt.tight_layout()
plt.savefig(f"{OUT}/2_module_coverage.svg", bbox_inches="tight", facecolor="white")
plt.close()

# ---------------------------------------------------------------
# 3. File coverage (bar, worst first)
# ---------------------------------------------------------------
files = [
    ("src/app.py", 22, 22),
    ("src/delete_api.py", 29, 29),
    ("src/Utilities/getfilters.py", 13, 8),
    ("src/EmailFilter/GroupingHandler.py", 107, 43),
    ("src/EmailFilter/DeleteHandler.py", 57, 19),
    ("src/EmailFilter/BaseHandler.py", 32, 8),
    ("src/TokenRefresher/TokenRefresher.py", 82, 20),
    ("src/Scheduler/scheduler.py", 34, 7),
    ("src/EmailFetcher/EmailFetcher.py", 70, 13),
    ("src/logger.py", 84, 12),
    ("src/EmailFilter/BounceHandler.py", 45, 4),
    ("src/Utilities/text_processing.py", 13, 1),
    ("src/EmailCurator/EmailCurator.py", 36, 1),
    ("src/Utilities/pathmaker.py", 7, 0),
    ("src/Utilities/isotimestamp.py", 6, 0),
    ("src/Config/redis_config.py", 2, 0),
    ("src/Config/env.py", 26, 0),
]
files = sorted(files, key=lambda f: (f[1] - f[2]) / f[1])

fnames = [f[0].replace("src/", "") for f in files]
fstmts = [f[1] for f in files]
fmiss = [f[2] for f in files]
fpcts = [(c - m) / c * 100 for c, m in zip(fstmts, fmiss)]

fig, ax = plt.subplots(figsize=(11, 8.6))
fig.suptitle("Coverage by File (worst → best)", fontsize=16, fontweight="bold")
bars = ax.barh(fnames, fpcts, color=[cov_color(p / 100) for p in fpcts], edgecolor="white", height=0.68)
ax.set_xlim(0, 108)
ax.set_xlabel("Coverage (%)")
ax.xaxis.grid(True, linestyle="--", alpha=0.4)
ax.set_axisbelow(True)
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)
ax.tick_params(axis="y", labelsize=10)

for bar, p, c, m in zip(bars, fpcts, fstmts, fmiss):
    ax.text(bar.get_width() + 1.0, bar.get_y() + bar.get_height() / 2,
            f"{p:.0f}% · {m} of {c} stmts missing", va="center", ha="left", fontsize=10,
            fontweight="bold" if p < 70 else "normal", color="#333333")

note = "0-statement __init__.py files excluded (shown as 100% in the raw report)."
ax.text(0, -0.4, note, transform=ax.transAxes, fontsize=9, color="#888888")

plt.tight_layout()
plt.savefig(f"{OUT}/3_file_coverage.svg", bbox_inches="tight", facecolor="white")
plt.close()

# ---------------------------------------------------------------
# 4. Module treemap (statements size, coverage color) — manual squarify
# ---------------------------------------------------------------
import math

def squarify_rects(sizes, x, y, w, h):
    if not sizes:
        return []
    total = sum(sizes)
    norm = [(s / total) * w * h for s in sizes]
    rects = []
    area = w * h
    items = list(zip(norm, range(len(norm))))
    idx = 0
    # sorted-layout squarify (row-based)
    # Simple slice-and-dice fallback to guarantee correctness:
    def slice_and_dice(items, x, y, w, h, out):
        if not items:
            return
        total = sum(a for a, _ in items)
        if w >= h:
            cw = w * (items[0][0] / total)
            out.append((x, y, cw, h, items[0][1]))
            slice_and_dice(items[1:], x + cw, y, w - cw, h, out)
        else:
            ch = h * (items[0][0] / total)
            out.append((x, y, w, ch, items[0][1]))
            slice_and_dice(items[1:], x, y + ch, w, h - ch, out)
    slice_and_dice(sorted(items, key=lambda t: -t[0]), x, y, w, h, rects)
    return rects

tm_names = [m[0].replace("\n", " ") for m in modules]
tm_stmts = stmts
tm_pcts = pcts
tm_miss = miss

fig, ax = plt.subplots(figsize=(11, 6.4))
fig.suptitle("Statement Share by Module — Sized by Statements, Colored by Coverage",
             fontsize=14, fontweight="bold")

rects = squarify_rects(tm_stmts, 0, 0, 1, 1)
for (rx, ry, rw, rh, i) in rects:
    p = tm_pcts[i]
    color = cov_color(p / 100)
    ax.add_patch(mpatches.Rectangle((rx, ry), rw, rh, facecolor=color, edgecolor="white", linewidth=2))
    label = f"{tm_names[i]}\n{tm_stmts[i]} stmts · {p:.0f}%"
    ax.text(rx + rw / 2, ry + rh / 2, label, ha="center", va="center",
            fontsize=10 if rw > 0.18 and rh > 0.18 else 9,
            fontweight="bold", color="white", linespacing=1.4)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")
ax.set_facecolor("white")
fig.patch.set_facecolor("white")

plt.tight_layout()
plt.savefig(f"{OUT}/4_module_treemap.svg", bbox_inches="tight", facecolor="white")
plt.close()

print("Done.")
