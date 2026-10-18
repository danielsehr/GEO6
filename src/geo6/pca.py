import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
    num_components: int = 3,
    ) -> tuple[PCA, pd.DataFrame]:
    
    
    pca = PCA(n_components=num_components)
    scores = pca.fit_transform(X_scaled)

    df_scores = pd.DataFrame(
        scores,
        columns=["PC1", "PC2", "PC3"],
        index=df_pca.index,
    )
    
    df_scores["sample"] = df_pca["sample"].values
    
    return pca, df_scores


def plot_pca(df: pd.DataFrame, pca: PCA) -> None:
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    for group in ["B", "I", "U", "F"]:
        mask = df["sample"] == group

        ax.scatter(
            df.loc[mask, "PC1"],
            df.loc[mask, "PC2"],
            df.loc[mask, "PC3"],
            label=group,
            s=65,
            alpha=0.8,
        )

    ax.set_xlabel(
        f"PC1 ({pca.explained_variance_ratio_[0]:.1%})"
    )
    ax.set_ylabel(
        f"PC2 ({pca.explained_variance_ratio_[1]:.1%})"
    )
    ax.set_zlabel(
        f"PC3 ({pca.explained_variance_ratio_[2]:.1%})"
    )

    ax.set_title("3D PCA of MicroResp measurements")
    ax.legend(title="Plant group")

    plt.tight_layout()
    plt.show()

    # Variance explained by each component
    print(
        pd.Series(
            pca.explained_variance_ratio_,
            index=["PC1", "PC2", "PC3"],
        ).map("{:.1%}".format)
    )

    print(
        f"Total variance explained by first 3 PCs: "
        f"{pca.explained_variance_ratio_.sum():.1%}"
    )