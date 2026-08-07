from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon


OUTPUT_DIR = Path(__file__).resolve().parent


def add_box(ax, x, y, width, height, text, color, edge="#183153", size=10):
    box = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        linewidth=1.8,
        edgecolor=edge,
        facecolor=color,
    )
    ax.add_patch(box)
    ax.text(
        x + width / 2,
        y + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=size,
        color="#10243e",
        weight="semibold",
        wrap=True,
    )


def add_arrow(ax, start, end, label=None, dashed=False):
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops={
            "arrowstyle": "-|>",
            "color": "#46647f",
            "linewidth": 1.7,
            "linestyle": "--" if dashed else "-",
            "shrinkA": 2,
            "shrinkB": 2,
        },
    )
    if label:
        ax.text(
            (start[0] + end[0]) / 2,
            (start[1] + end[1]) / 2 + 0.017,
            label,
            ha="center",
            va="bottom",
            fontsize=8,
            color="#314b63",
            bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.5},
        )


def architecture_diagram():
    fig, ax = plt.subplots(figsize=(16, 10))
    fig.patch.set_facecolor("#f7fafc")
    ax.set_facecolor("#f7fafc")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(
        0.04,
        0.95,
        "Petofy Chat Bot: Observed Architecture",
        fontsize=22,
        weight="bold",
        color="#10243e",
    )
    ax.text(
        0.04,
        0.91,
        "Solid arrows show executable data flow; dashed arrows show files expected by scripts but absent from the repository.",
        fontsize=10,
        color="#46647f",
    )

    ax.text(0.04, 0.855, "Query path (main.py)", fontsize=14, weight="bold", color="#0b6e69")
    add_box(ax, 0.04, 0.68, 0.11, 0.09, "Fixed user\nquery", "#dff4f1")
    add_box(ax, 0.20, 0.68, 0.14, 0.09, "main.py\norchestration", "#dcecff")
    add_box(ax, 0.40, 0.79, 0.16, 0.09, "Azure OpenAI\nembeddings", "#fbe7bb")
    add_box(ax, 0.62, 0.79, 0.13, 0.09, "Pinecone\nvector query", "#eadfff")
    add_box(ax, 0.40, 0.61, 0.16, 0.09, "Metadata + prompt\nassembly", "#dcecff")
    add_box(ax, 0.62, 0.61, 0.15, 0.09, "Azure OpenAI\nchat completion", "#fbe7bb")
    add_box(ax, 0.84, 0.61, 0.11, 0.09, "Answer to\nstdout", "#dff4f1")
    add_box(ax, 0.62, 0.44, 0.15, 0.09, "Azure AI Search\ndata source", "#ffe2df")

    add_arrow(ax, (0.15, 0.725), (0.20, 0.725))
    add_arrow(ax, (0.34, 0.74), (0.40, 0.83), "embed")
    add_arrow(ax, (0.56, 0.835), (0.62, 0.835), "vector")
    add_arrow(ax, (0.685, 0.79), (0.56, 0.68), "matches")
    add_arrow(ax, (0.34, 0.70), (0.40, 0.655), "query")
    add_arrow(ax, (0.56, 0.655), (0.62, 0.655), "prompt")
    add_arrow(ax, (0.77, 0.655), (0.84, 0.655))
    add_arrow(ax, (0.695, 0.53), (0.695, 0.61), "second retrieval")

    ax.plot([0.04, 0.96], [0.38, 0.38], color="#c7d4df", linewidth=1.5)
    ax.text(0.04, 0.34, "Offline ingestion scripts", fontsize=14, weight="bold", color="#0b6e69")

    add_box(ax, 0.04, 0.20, 0.12, 0.08, "dataset/data\nJSON files", "#f3f6f8")
    add_box(ax, 0.21, 0.20, 0.14, 0.08, "loader.py +\nvectorcopy.py", "#dcecff")
    add_box(ax, 0.40, 0.20, 0.15, 0.08, "Azure OpenAI\nembeddings", "#fbe7bb")
    add_box(ax, 0.61, 0.20, 0.14, 0.08, "Pinecone vector\nJSON file", "#f3f6f8")
    add_box(ax, 0.81, 0.20, 0.14, 0.08, "pinecone_upsert.py\n-> Pinecone", "#eadfff")

    add_box(ax, 0.21, 0.06, 0.14, 0.08, "vector_data.json", "#f3f6f8")
    add_box(ax, 0.43, 0.06, 0.14, 0.08, "index.py", "#dcecff")
    add_box(ax, 0.65, 0.06, 0.16, 0.08, "Azure AI Search\nindex + documents", "#ffe2df")

    add_arrow(ax, (0.16, 0.24), (0.21, 0.24), dashed=True)
    add_arrow(ax, (0.35, 0.24), (0.40, 0.24))
    add_arrow(ax, (0.55, 0.24), (0.61, 0.24), "write disabled", dashed=True)
    add_arrow(ax, (0.75, 0.24), (0.81, 0.24), dashed=True)
    add_arrow(ax, (0.35, 0.10), (0.43, 0.10), dashed=True)
    add_arrow(ax, (0.57, 0.10), (0.65, 0.10), "create + upload")

    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "architecture.png", dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def testing_strategy_diagram():
    fig, ax = plt.subplots(figsize=(13, 9))
    fig.patch.set_facecolor("#f7fafc")
    ax.set_facecolor("#f7fafc")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(
        0.05,
        0.94,
        "Recommended Testing Strategy",
        fontsize=22,
        weight="bold",
        color="#10243e",
    )
    ax.text(
        0.05,
        0.90,
        "No tests currently exist. Build confidence from deterministic units upward, keeping paid live calls opt-in.",
        fontsize=10,
        color="#46647f",
    )

    layers = [
        (0.38, 0.76, 0.24, 0.10, "4. Opt-in live smoke", "One guarded query against test resources", "#ffe2df"),
        (0.29, 0.60, 0.42, 0.11, "3. Service integration", "Test indexes, schema compatibility, embedding dimensions", "#fbe7bb"),
        (0.20, 0.43, 0.60, 0.12, "2. Mocked SDK contracts", "Pinecone query/upsert, Azure OpenAI, Azure AI Search", "#eadfff"),
        (0.10, 0.24, 0.80, 0.13, "1. Deterministic unit tests", "JSON loading, paths, prompt/context assembly, validation", "#dff4f1"),
    ]

    for x, y, width, height, title, detail, color in layers:
        points = [
            (x + 0.025, y),
            (x + width - 0.025, y),
            (x + width, y + height),
            (x, y + height),
        ]
        shape = Polygon(points, closed=True, facecolor=color, edgecolor="#183153", linewidth=1.8)
        ax.add_patch(shape)
        ax.text(0.5, y + height * 0.63, title, ha="center", va="center", fontsize=12, weight="bold", color="#10243e")
        ax.text(0.5, y + height * 0.28, detail, ha="center", va="center", fontsize=9, color="#314b63")

    ax.text(0.10, 0.14, "First safety gate", fontsize=10, weight="bold", color="#b42318")
    ax.text(
        0.10,
        0.10,
        "Refactor import-time API calls behind functions and inject clients before importing modules in tests.",
        fontsize=10,
        color="#314b63",
    )
    ax.text(0.10, 0.055, "Coverage status", fontsize=10, weight="bold", color="#0b6e69")
    ax.text(
        0.10,
        0.015,
        "Not measurable: there is no test suite, runner configuration, or safe executable test target.",
        fontsize=10,
        color="#314b63",
    )

    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "testing_strategy.png", dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


if __name__ == "__main__":
    architecture_diagram()
    testing_strategy_diagram()
