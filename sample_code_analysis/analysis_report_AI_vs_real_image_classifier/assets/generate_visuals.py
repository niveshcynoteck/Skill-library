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

    ax.text(0.04, 0.955, "Real vs AI Image Classifier: Observed Pipelines", fontsize=22, weight="bold", color="#10243e")
    ax.text(
        0.04,
        0.92,
        "Two independent scripts. Training saves an H5 file; inference instead loads a committed SavedModel. Dataset folders are absent from the repository.",
        fontsize=10,
        color="#46647f",
    )

    ax.text(0.04, 0.875, "Training pipeline (model/model.py)", fontsize=14, weight="bold", color="#0b6e69")
    add_box(ax, 0.04, 0.68, 0.13, 0.10, "Dataset/train\nDataset/valid\nDataset/test", "#f3f6f8")
    add_box(ax, 0.22, 0.70, 0.15, 0.09, "flow_from_directory\n224x224 batch 32\nbinary, rescale 1/255", "#dcecff")
    add_box(ax, 0.42, 0.70, 0.15, 0.09, "DenseNet121 (ImageNet)\n+ classification head", "#eadfff")
    add_box(ax, 0.62, 0.70, 0.14, 0.09, "fit: 10 epochs\nEarlyStopping p=3\nval_loss", "#fbe7bb")
    add_box(ax, 0.81, 0.72, 0.14, 0.08, "save\nsaved_models/\ndensenet_model.h5", "#dff4f1")
    add_box(ax, 0.81, 0.57, 0.14, 0.08, "evaluate on test\naccuracy, precision\nrecall, F1", "#dff4f1")

    add_arrow(ax, (0.17, 0.75), (0.22, 0.75), "missing", dashed=True)
    add_arrow(ax, (0.37, 0.745), (0.42, 0.745))
    add_arrow(ax, (0.57, 0.745), (0.62, 0.745))
    add_arrow(ax, (0.76, 0.75), (0.81, 0.755))
    add_arrow(ax, (0.88, 0.72), (0.88, 0.66))
    add_arrow(ax, (0.81, 0.63), (0.81, 0.60), "writes", dashed=True)

    ax.plot([0.04, 0.96], [0.42, 0.42], color="#c7d4df", linewidth=1.5)
    ax.text(0.04, 0.38, "Inference pipeline (src/prediction.py)", fontsize=14, weight="bold", color="#0b6e69")

    add_box(ax, 0.04, 0.20, 0.13, 0.10, "model/\nSavedModel\n(committed)", "#f3f6f8")
    add_box(ax, 0.22, 0.22, 0.14, 0.09, "load_model('model')\nat import time", "#fbe7bb")
    add_box(ax, 0.41, 0.22, 0.14, 0.09, "image file\nload_img 224x224\n/255, expand dims", "#dcecff")
    add_box(ax, 0.60, 0.22, 0.13, 0.09, "model.predict\nbatch of 1", "#eadfff")
    add_box(ax, 0.78, 0.22, 0.17, 0.09, "sigmoid > 0.5\n'Real' / 'AI-Generated'\nconfidence", "#dff4f1")

    add_arrow(ax, (0.17, 0.25), (0.22, 0.25), dashed=True)
    add_arrow(ax, (0.36, 0.265), (0.41, 0.265), "hardcoded path", dashed=True)
    add_arrow(ax, (0.55, 0.265), (0.60, 0.265))
    add_arrow(ax, (0.73, 0.265), (0.78, 0.265))

    ax.text(0.04, 0.13, "Branch note", fontsize=10, weight="bold", color="#b42318")
    ax.text(
        0.04,
        0.09,
        "All code and model artifacts exist only on the 'model' branch. The default branch 'main' contains only README.md, LICENSE, and .gitignore.",
        fontsize=10,
        color="#314b63",
    )
    ax.text(0.04, 0.045, "Storage note", fontsize=10, weight="bold", color="#b42318")
    ax.text(
        0.04,
        0.005,
        "*.pb files use Git LFS, but model/variables/variables.data-00000-of-00001 (~87 MiB) is committed as a regular Git blob.",
        fontsize=10,
        color="#314b63",
    )

    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "architecture.png", dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def model_head_diagram():
    fig, ax = plt.subplots(figsize=(10, 11))
    fig.patch.set_facecolor("#f7fafc")
    ax.set_facecolor("#f7fafc")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.5, 0.97, "Classifier Head Architecture", fontsize=21, weight="bold", color="#10243e", ha="center")
    ax.text(
        0.5,
        0.935,
        "DenseNet121 (ImageNet) + fully connected head, binary sigmoid output",
        fontsize=10,
        color="#46647f",
        ha="center",
    )

    layers = [
        (0.24, 0.84, "DenseNet121 base\ninput (224, 224, 3)\nweights: imagenet", "#eadfff"),
        (0.28, 0.72, "GlobalAveragePooling2D", "#dcecff"),
        (0.24, 0.60, "Dense 512, ReLU", "#fbe7bb"),
        (0.28, 0.49, "BatchNormalization", "#dcecff"),
        (0.28, 0.40, "Dropout 0.3", "#f3f6f8"),
        (0.28, 0.31, "Dense 64, ReLU", "#fbe7bb"),
        (0.28, 0.22, "Dropout 0.6", "#f3f6f8"),
        (0.28, 0.13, "Dense 32, ReLU", "#fbe7bb"),
        (0.28, 0.045, "Dropout 0.6", "#f3f6f8"),
    ]
    for x, y, label, color in layers:
        width = 0.52 if label.startswith("DenseNet121") else 0.44
        add_box(ax, 0.5 - width / 2, y, width, 0.075, label, color)

    add_arrow(ax, (0.5, 0.84), (0.5, 0.795))
    add_arrow(ax, (0.5, 0.72), (0.5, 0.675))
    add_arrow(ax, (0.5, 0.60), (0.5, 0.565))
    add_arrow(ax, (0.5, 0.49), (0.5, 0.475))
    add_arrow(ax, (0.5, 0.40), (0.5, 0.385))
    add_arrow(ax, (0.5, 0.31), (0.5, 0.295))
    add_arrow(ax, (0.5, 0.22), (0.5, 0.205))
    add_arrow(ax, (0.5, 0.13), (0.5, 0.115))
    add_arrow(ax, (0.5, 0.045), (0.5, 0.005))

    add_box(ax, 0.30, 0.005, 0.40, 0.065, "Dense 1, sigmoid\noutput p(Real)", "#dff4f1")

    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "model_architecture.png", dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def testing_strategy_diagram():
    fig, ax = plt.subplots(figsize=(13, 9))
    fig.patch.set_facecolor("#f7fafc")
    ax.set_facecolor("#f7fafc")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.05, 0.94, "Recommended Testing Strategy", fontsize=22, weight="bold", color="#10243e")
    ax.text(
        0.05,
        0.90,
        "No tests exist. Build confidence from deterministic units upward; keep the 90+ MiB model load out of unit tests.",
        fontsize=10,
        color="#46647f",
    )

    layers = [
        (0.38, 0.76, 0.24, 0.10, "4. Opt-in live run", "One real image against the committed SavedModel", "#ffe2df"),
        (0.29, 0.60, 0.42, 0.11, "3. Model-level smoke", "Small saved-model inference test, marked and gated", "#fbe7bb"),
        (0.20, 0.43, 0.60, 0.12, "2. Contract tests", "Mocked Keras model; verify inputs, outputs, thresholds", "#eadfff"),
        (0.10, 0.24, 0.80, 0.13, "1. Deterministic unit tests", "Preprocessing, label/confidence decoding, metric math", "#dff4f1"),
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
        "Move model loading out of module import and make image paths explicit before writing tests.",
        fontsize=10,
        color="#314b63",
    )
    ax.text(0.10, 0.055, "Coverage status", fontsize=10, weight="bold", color="#0b6e69")
    ax.text(
        0.10,
        0.015,
        "Not measurable: no test suite, runner configuration, or safe executable test target exists.",
        fontsize=10,
        color="#314b63",
    )

    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "testing_strategy.png", dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


if __name__ == "__main__":
    architecture_diagram()
    model_head_diagram()
    testing_strategy_diagram()
