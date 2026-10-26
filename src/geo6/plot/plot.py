from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from geo6.config.config import Config

config = Config()


def save_plot(
    plot: plt.figure,
    name: str,
    ) -> None:
    
    plot.savefig(
        Path(config.plot_output_dir) / f"{name}.png",
        dpi=300,
        bbox_inches="tight",
    )

def plot_basal_resp_boxplot(df: pd.DataFrame) -> plt.figure:
    fig, ax = plt.subplots(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x="sample",
        y="br_mg_per_g_h",
        ax=ax,
    )

    sns.stripplot(
        data=df,
        x="sample",
        y="br_mg_per_g_h",
        # jitter=0.05,
        alpha=0.7,
        ax=ax,
        # hue="subrep"
    )

    ax.set(
        xlabel="Soil sample",
        ylabel=r"Basal respiration (mg CO$_2$ g$^¹$ h$^¹$)",
    )
    
    return fig


def plot_basal_resp_rootextract_boxplot(df: pd.DataFrame) -> plt.figure:

    extract_order = ["F", "I", "U"]
    
    sns.set_theme(style="whitegrid")

    g = sns.catplot(
        data=df,
        x="sample",
        y="respiration",
        hue="extract",
        hue_order=extract_order,
        col="concentration",
        kind="box",
        height=5,
        aspect=1.1,
        sharey=True,
        showfliers=False,
        boxprops={"alpha": 0.5},
    )

    # Overlay individual observations
    for ax, concentration in zip(g.axes.flat, [1, 2]):
        subset = df[df["concentration"] == concentration]

        sns.stripplot(
            data=subset,
            x="sample",
            y="respiration",
            hue="extract",
            dodge=True,
            jitter=0.12,
            alpha=0.7,
            size=3,
            ax=ax,
            legend=False
        )
        
    g.set_axis_labels(
        "Soil type",
        r"Basal respiration (mg CO$_2$ g$^{-1}$ h$^{-1}$)",
    )
    
    sns.move_legend(
    g,
    "upper right",
    bbox_to_anchor=(1.02, 1),
    title="Plant extract",
    borderaxespad=0,
)

    g.figure.subplots_adjust(left=0.9)

    g.set_titles("Concentration {col_name}")

    # g.figure.suptitle(
    #     "Basal respiration across plant species and root extract, added at two concentrations.",
    #     y=1.05,
    # )

    plt.tight_layout()
    plt.show()
    
    return g


def plot_sir_boxplots(
    df: pd.DataFrame,
    mapping: list[str],
    ) -> plt.Figure:
    
    g = sns.catplot(
        data=df,
        x="sample",
        y="value",
        col="substance",
        hue="substance",
        col_wrap=4,
        kind="box",
        legend=False
    )

    for ax, substance in zip(g.axes.flat, mapping):
        subset = df[df["substance"] == substance]

        sns.stripplot(
            data=subset,
            x="sample",
            y="value",
            # hue="substance",
            color="black", 
            dodge=True,
            jitter=0.12,
            alpha=0.7,
            size=3,
            ax=ax,
            legend=False
        )

        ax.set(
            xlabel="Soil sample",
            ylabel=r"Basal respiration (mg CO$_2$ g$^¹$ h$^¹$)",
        )
    g.set_titles("{col_name}")
        
    return g
