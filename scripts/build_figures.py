#!/usr/bin/env python3
from pathlib import Path
import shutil

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
SRC = ROOT / "paperII_submission_source" / "figures"


def add_box(ax, x, y, w, h, text, color):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.015,rounding_size=0.015",
        linewidth=1.3, edgecolor="#263238", facecolor=color
    ))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=8.5)


def add_arrow(ax, a, b, label=""):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=12,
                                 linewidth=1.3, color="#263238"))
    if label:
        ax.text((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + 0.045,
                label, ha="center", fontsize=7.5)


def signature_pipeline(path):
    fig, ax = plt.subplots(figsize=(7.5, 3.1))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    add_box(ax, .03, .38, .18, .24, "typed primitive\nsource roles", "#dceef8")
    add_box(ax, .29, .38, .19, .24, "joint source algebra\nand faithful state", "#dff3e4")
    add_box(ax, .56, .38, .17, .24, "structured\nGNS signature", "#eef0fa")
    add_box(ax, .81, .64, .16, .22, "unique minimal\ncyclic realization", "#eef6d8")
    add_box(ax, .81, .13, .16, .22, "unselected\nphysical occupation", "#f7dfdf")
    add_arrow(ax, (.21, .50), (.29, .50), "joint incidence")
    add_arrow(ax, (.48, .50), (.56, .50), "deduplicate")
    add_arrow(ax, (.73, .54), (.81, .73), "if complete")
    add_arrow(ax, (.73, .46), (.81, .24), "nature gap")
    ax.set_title("Finite source-signature logic", fontsize=12, fontweight="bold")
    fig.tight_layout(); fig.savefig(path, bbox_inches="tight"); plt.close(fig)


def marginal_dimensions(path):
    labels = ["weight 1", "weight 2", "weight 3", "weight 4\n(hidden from proper marginals)"]
    values = [12, 54, 108, 81]
    colors = ["#9ecae1", "#74c476", "#bcbddc", "#e34a33"]
    fig, ax = plt.subplots(figsize=(7.2, 3.7))
    bars = ax.bar(labels, values, color=colors, edgecolor="#263238", linewidth=.8)
    ax.set_ylabel("Pauli-word directions")
    ax.set_title("Four-qubit traceless source algebra: 255 directions")
    ax.spines[["top", "right"]].set_visible(False)
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, value + 3, str(value), ha="center", fontsize=9)
    ax.set_ylim(0, 125)
    fig.tight_layout(); fig.savefig(path, bbox_inches="tight"); plt.close(fig)


def selection_and_stability(path):
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.8), gridspec_kw={"width_ratios": [1.15, 1]})
    ax = axes[0]
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ys = [.77, .55, .33, .11]
    labels = [
        ("existence", "an explicit realization"),
        ("uniqueness", "typed GNS orbit"),
        ("identifiability", "descriptor rank"),
        ("physical selection", "base-seed law / experiment"),
    ]
    colors = ["#dceef8", "#dff3e4", "#eef0fa", "#f7dfdf"]
    for y, (title, sub), color in zip(ys, labels, colors):
        add_box(ax, .08, y, .78, .15, f"{title}\n{sub}", color)
    for y0, y1 in zip(ys[:-1], ys[1:]):
        ax.annotate("", xy=(.92, y1 + .075), xytext=(.92, y0 + .075),
                    arrowprops={"arrowstyle": "-[,widthB=2.8", "lw": 1.1, "color": "#7f8c8d"})
    ax.text(.95, .5, "separate\naudits", rotation=90, ha="center", va="center", fontsize=8)
    ax.set_title("Logical levels are not interchangeable", fontsize=10.5, fontweight="bold")

    ax = axes[1]
    delta = np.logspace(-2, 0, 200)
    condition = delta ** -2
    ax.loglog(delta, condition, color="#c0392b", lw=2.2)
    ax.axhline(1, color="#607d8b", lw=1, ls="--")
    ax.set_xlabel(r"small incidence singular value $\delta$")
    ax.set_ylabel(r"$\kappa(G_J)=\delta^{-2}$")
    ax.set_title("Faithful but unstable before rank loss", fontsize=10.5, fontweight="bold")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(True, which="both", alpha=.22)
    fig.tight_layout(); fig.savefig(path, bbox_inches="tight"); plt.close(fig)


def foundation_series_map(path):
    fig, ax = plt.subplots(figsize=(8.2, 3.0))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    add_box(ax, .03, .52, .27, .20, "Paper I\narchitecture + conditional completion", "#eaf4ea")
    add_box(ax, .365, .52, .27, .20, "Paper II\nfinite source sufficiency + incidence", "#f3efff")
    add_box(ax, .70, .52, .27, .20, "Paper III\nrecord transport + recovery", "#eaf2ff")
    add_arrow(ax, (.30, .62), (.365, .62))
    add_arrow(ax, (.635, .62), (.70, .62))
    add_box(ax, .19, .18, .62, .15,
            "shared open arrow: physical base--seed selection and occupation", "#f7dfdf")
    ax.text(.5, .93, "Foundation sequence and dependency direction",
            ha="center", fontsize=11.5, fontweight="bold")
    ax.text(.5, .08, "Later papers refine sufficient internal conditions; they do not prove nature-level selection.",
            ha="center", fontsize=7.8)
    fig.tight_layout(); fig.savefig(path, bbox_inches="tight"); plt.close(fig)


def main():
    OUT.mkdir(parents=True, exist_ok=True); SRC.mkdir(parents=True, exist_ok=True)
    paths = [OUT / "fig_source_signature_pipeline.pdf", OUT / "fig_pauli_dimension_audit.pdf",
             OUT / "fig_selection_stability.pdf", OUT / "fig_foundation_series_map.pdf"]
    signature_pipeline(paths[0]); marginal_dimensions(paths[1]); selection_and_stability(paths[2])
    foundation_series_map(paths[3])
    for path in paths:
        shutil.copy2(path, SRC / path.name)
    print("WROTE", *paths)


if __name__ == "__main__":
    main()
