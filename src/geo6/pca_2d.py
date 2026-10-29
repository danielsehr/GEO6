import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.lines import Line2D

from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from typing import Any


def prepare_pca_data(
    df: pd.DataFrame,
    features: list[str],
    ) -> tuple[pd.DataFrame, np.ndarray]: 
    
    # Keep only the selected variables and group labels
    df_pca = df[["sample", *features]]

    # Impute missing values with the median of each variable
    imputer = SimpleImputer(strategy="median")
    X_imputed = imputer.fit_transform(df_pca[features])

    # Standardize variables because they have different variances
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_imputed)
    
    return df_pca, X_scaled


def calc_pca(
    X_scaled: np.ndarray,
    df_pca: pd.DataFrame,
    num_components: int = 2,
) -> tuple[PCA, pd.DataFrame]:

    pca = PCA(n_components=num_components)
    scores = pca.fit_transform(X_scaled)

    df_scores = pd.DataFrame(
        scores,
        columns=[f"PC{i + 1}" for i in range(num_components)],
        index=df_pca.index,
    )

    df_scores["sample"] = df_pca["sample"].values

    return pca, df_scores


def plot_pca(
    df: pd.DataFrame,
    pca: PCA,
    features: list[str],
    substance_mapping: dict,
) -> Figure:

    arrow_mapping = {
        'sir_1_mg_per_g_h': "sir 1",
        'sir_2_mg_per_g_h': "sir 2",
        'sir_3_mg_per_g_h': "sir 3",
        'sir_4_mg_per_g_h': "sir 4",
        'sir_5_mg_per_g_h': "sir 5",
        'sir_6_mg_per_g_h': "sir 6",
        'sir_7_mg_per_g_h': "sir 7",
        'sir_8_mg_per_g_h': "sir 8",
        'sir_9_mg_per_g_h': "sir 9",
        'sir_10_mg_per_g_h': "sir 10",
        'sir_11_mg_per_g_h': "sir 11",
    }

    fig, ax = plt.subplots(figsize=(10, 8))

    # Plot sample scores
    for group in ["B", "I", "U", "F"]:
        mask = df["sample"] == group

        ax.scatter(
            df.loc[mask, "PC1"],
            df.loc[mask, "PC2"],
            label=group,
            s=65,
            alpha=0.8,
        )

    # Scale loading arrows for visibility
    scores_max = np.abs(df[["PC1", "PC2"]].to_numpy()).max()
    loadings = pca.components_.T[:, :2]

    loading_scale = scores_max * 0.7

    for i, feature in enumerate(features):
        x_loading = loadings[i, 0] * loading_scale
        y_loading = loadings[i, 1] * loading_scale

        ax.annotate(
            "",
            xy=(x_loading, y_loading),
            xytext=(0, 0),
            arrowprops=dict(
                arrowstyle="->",
                linewidth=1.2,
                alpha=0.8,
            ),
        )

        ax.text(
            x_loading * 1.08,
            y_loading * 1.08,
            arrow_mapping[feature],
            fontsize=8,
            ha="center",
            va="center",
        )

    # Axis labels
    ax.set_xlabel(
        f"PC1 ({pca.explained_variance_ratio_[0]:.1%})"
    )
    ax.set_ylabel(
        f"PC2 ({pca.explained_variance_ratio_[1]:.1%})"
    )

    # ax.set_title("PCA Biplot of MicroResp Measurements")
    
    # Legend 1: Soil sample groups
    group_legend = ax.legend(
        title="Soil sample",
        loc="upper right",
    )
    ax.add_artist(group_legend)

    # Legend 2: SIR substrate mapping
    sir_legend_handles = [
        Line2D(
            [0], [0],
            color="black",
            linewidth=1.2,
            # marker=">",
            markersize=5,
            label=f"{arrow_mapping[feature]}: {substance_mapping[feature]}",
        )
        for feature in features
        if feature in substance_mapping
    ]

    ax.legend(
        handles=sir_legend_handles,
        title="Substrate",
        loc="upper left",
        # bbox_to_anchor=(1.02, 1),
        borderaxespad=0,
        fontsize=8,
    )


    ax.axhline(0, color="grey", linewidth=0.7, alpha=0.5)
    ax.axvline(0, color="grey", linewidth=0.7, alpha=0.5)

    plt.tight_layout()
    


    # Variance explained
    print(
        pd.Series(
            pca.explained_variance_ratio_,
            index=["PC1", "PC2"],
        ).map("{:.1%}".format)
    )

    print(
        f"Total variance explained by the first 2 PCs: "
        f"{pca.explained_variance_ratio_.sum():.1%}"
    )
    
    
    return fig


def print_pca_loadings(
    pca: PCA,
    features: list[str],
) -> None:

    print("\nPCA loadings:")
    print(
        pd.DataFrame(
            pca.components_.T,
            index=features,
            columns=["PC1", "PC2"],
        )
    )
    
    
def perform_2d_pca(
    df: pd.DataFrame,
    features: list[str],
    substance_mapping: dict,
) ->  Figure:

    df_pca, X_scaled = prepare_pca_data(
        df=df,
        features=features,
    )

    pca, df_scores = calc_pca(
        X_scaled=X_scaled,
        df_pca=df_pca,
    )

    print_pca_loadings(pca=pca, features=features)
    
    plot = plot_pca(
        df=df_scores, 
        pca=pca, features=features,
        substance_mapping=substance_mapping,
    )
    
    return plot