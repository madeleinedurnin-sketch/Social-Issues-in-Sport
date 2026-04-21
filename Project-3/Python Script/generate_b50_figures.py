from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import chi2_contingency, kruskal, mannwhitneyu


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "B50_coded_comments.csv"


def savefig_multi(base_name: str) -> None:
    plt.tight_layout()
    plt.savefig(BASE_DIR / f"{base_name}.png", dpi=300, bbox_inches="tight")
    plt.savefig(BASE_DIR / f"{base_name}.svg", bbox_inches="tight")
    plt.savefig(BASE_DIR / f"{base_name}.pdf", bbox_inches="tight")
    plt.close()


def main() -> None:
    sns.set_theme(style="whitegrid", context="paper")
    plt.rcParams.update(
        {
            "font.size": 11,
            "axes.titlesize": 14,
            "axes.labelsize": 12,
            "xtick.labelsize": 11,
            "ytick.labelsize": 11,
            "legend.fontsize": 10,
            "legend.title_fontsize": 10,
        }
    )
    df = pd.read_csv(DATA_PATH)

    platform_order = ["Instagram", "X", "YouTube"]
    stance_order = ["pro-Trump", "anti-Trump", "neutral/non-political"]
    frame_order = ["sports/performance", "politics/ideology", "blended"]
    stance_palette = ["#4C78A8", "#E45756", "#72B7B2"]
    frame_palette = ["#6C8EBF", "#9C755F", "#59A14F"]

    # Figure 1: stance proportions by platform
    t1 = pd.crosstab(df["platform"], df["stance"], normalize="index").reindex(
        index=platform_order, columns=stance_order, fill_value=0
    )
    ax = t1.mul(100).plot(kind="bar", figsize=(10, 6), color=stance_palette, edgecolor="black", linewidth=0.4)
    ax.set_title("Figure 1. Political Stance Proportions by Platform")
    ax.set_xlabel("Platform")
    ax.set_ylabel("Percent of Comments")
    ax.legend(title="Stance", bbox_to_anchor=(1.02, 1), loc="upper left")
    savefig_multi("Figure1_StanceByPlatform")

    # Figure 2: frame composition by platform
    t2 = pd.crosstab(df["platform"], df["frame"], normalize="index").reindex(
        index=platform_order, columns=frame_order, fill_value=0
    )
    ax = t2.mul(100).plot(
        kind="bar", stacked=True, figsize=(10, 6), color=frame_palette, edgecolor="black", linewidth=0.3
    )
    ax.set_title("Figure 2. Frame Composition by Platform")
    ax.set_xlabel("Platform")
    ax.set_ylabel("Percent of Comments")
    ax.legend(title="Frame", bbox_to_anchor=(1.02, 1), loc="upper left")
    savefig_multi("Figure2_FrameByPlatform")

    # Figure 3: stacked frame by stance
    t3 = pd.crosstab(df["stance"], df["frame"], normalize="index").reindex(
        index=stance_order, columns=frame_order, fill_value=0
    )
    ax = t3.mul(100).plot(
        kind="bar", stacked=True, figsize=(10, 6), color=frame_palette, edgecolor="black", linewidth=0.3
    )
    ax.set_title("Figure 3. Frame Composition Within Stance Categories")
    ax.set_xlabel("Stance")
    ax.set_ylabel("Percent of Comments")
    ax.legend(title="Frame", bbox_to_anchor=(1.02, 1), loc="upper left")
    savefig_multi("Figure3_StanceFrameAssociation")

    # Figure 4: engagement blended vs non-blended
    df["frame_type"] = df["is_blended"].map({1: "Blended", 0: "Non-blended"})
    plot_df4 = df.sample(min(20000, len(df)), random_state=42)
    plt.figure(figsize=(9, 6))
    sns.boxplot(
        data=plot_df4,
        x="frame_type",
        y="engagement_norm",
        hue="frame_type",
        order=["Non-blended", "Blended"],
        palette=["#9AA0A6", "#4C78A8"],
        width=0.5,
        legend=False,
    )
    plt.title("Figure 4. Normalized Engagement: Blended vs Non-blended")
    plt.xlabel("Frame Type")
    plt.ylabel("Engagement (within-platform z-score)")
    savefig_multi("Figure4_Engagement_BlendedVsNon")

    # Figure 5: engagement by stance
    plot_df5 = df.sample(min(25000, len(df)), random_state=42)
    plt.figure(figsize=(10, 6))
    sns.boxplot(
        data=plot_df5,
        x="stance",
        y="engagement_norm",
        hue="stance",
        order=stance_order,
        palette=stance_palette,
        width=0.55,
        legend=False,
    )
    plt.title("Figure 5. Normalized Engagement by Political Stance")
    plt.xlabel("Stance")
    plt.ylabel("Engagement (within-platform z-score)")
    plt.xticks(rotation=12)
    savefig_multi("Figure5_Engagement_ByStance")

    # Figure 6: integrated overview of the full findings
    stance_tab = pd.crosstab(df["platform"], df["stance"], normalize="index").reindex(
        index=platform_order, columns=stance_order, fill_value=0
    )
    frame_tab = pd.crosstab(df["platform"], df["frame"], normalize="index").reindex(
        index=platform_order, columns=frame_order, fill_value=0
    )

    # Statistical summary values for annotation panel
    t1_counts = pd.crosstab(df["platform"], df["stance"]).reindex(
        index=platform_order, columns=stance_order, fill_value=0
    )
    t2_counts = pd.crosstab(df["platform"], df["frame"]).reindex(
        index=platform_order, columns=frame_order, fill_value=0
    )
    chi1 = chi2_contingency(t1_counts)
    chi2 = chi2_contingency(t2_counts)
    g_blended = df.loc[df["is_blended"] == 1, "engagement_norm"]
    g_non = df.loc[df["is_blended"] == 0, "engagement_norm"]
    mw = mannwhitneyu(g_blended, g_non, alternative="two-sided")
    kw = kruskal(
        df.loc[df["stance"] == "pro-Trump", "engagement_norm"],
        df.loc[df["stance"] == "anti-Trump", "engagement_norm"],
        df.loc[df["stance"] == "neutral/non-political", "engagement_norm"],
    )

    fig, axes = plt.subplots(2, 2, figsize=(15, 10), gridspec_kw={"height_ratios": [1, 1.1]})
    fig.suptitle("Figure 6. Integrated Summary of Cross-Platform Findings", fontsize=16, y=0.98)

    # Panel A: stance by platform
    ax = axes[0, 0]
    stance_tab.mul(100).plot(kind="bar", ax=ax, color=stance_palette, edgecolor="black", linewidth=0.3)
    ax.set_title("A. Stance Distribution by Platform")
    ax.set_xlabel("Platform")
    ax.set_ylabel("Percent")
    ax.legend_.remove()

    # Panel B: frame by platform
    ax = axes[0, 1]
    frame_tab.mul(100).plot(kind="bar", stacked=True, ax=ax, color=frame_palette, edgecolor="black", linewidth=0.3)
    ax.set_title("B. Frame Composition by Platform")
    ax.set_xlabel("Platform")
    ax.set_ylabel("Percent")
    ax.legend_.remove()

    # Panel C: engagement effects
    ax = axes[1, 0]
    sample_eng = df.sample(min(18000, len(df)), random_state=42).copy()
    sample_eng["frame_type"] = sample_eng["is_blended"].map({1: "Blended", 0: "Non-blended"})
    sns.boxplot(
        data=sample_eng,
        x="frame_type",
        y="engagement_norm",
        hue="frame_type",
        order=["Non-blended", "Blended"],
        palette=["#9AA0A6", "#4C78A8"],
        legend=False,
        width=0.52,
        ax=ax,
    )
    ax.set_title("C. Engagement by Frame Type")
    ax.set_xlabel("Frame Type")
    ax.set_ylabel("Engagement (z-score)")

    # Panel D: key takeaways + stats
    ax = axes[1, 1]
    ax.axis("off")
    key_text = (
        "Key Findings\n"
        "1) Most comments are neutral/non-political,\n"
        "   but explicit stance varies by platform.\n"
        "2) Sports/performance framing dominates,\n"
        "   with stronger politicization on X/YouTube.\n"
        "3) Stance and frame are strongly associated.\n"
        "4) Blended and explicit-political comments\n"
        "   receive higher normalized engagement.\n\n"
        f"Stats Snapshot\n"
        f"- Stance x Platform: chi2={chi1.statistic:.1f}, p<{max(chi1.pvalue,1e-300):.2g}\n"
        f"- Frame x Platform: chi2={chi2.statistic:.1f}, p<{max(chi2.pvalue,1e-300):.2g}\n"
        f"- Blended vs Non: U={mw.statistic:.1f}, p<{max(mw.pvalue,1e-300):.2g}\n"
        f"- Engagement by Stance: H={kw.statistic:.1f}, p<{max(kw.pvalue,1e-300):.2g}"
    )
    ax.text(
        0.02,
        0.98,
        key_text,
        va="top",
        ha="left",
        fontsize=11,
        bbox={"facecolor": "#F7F7F7", "edgecolor": "#BBBBBB", "boxstyle": "round,pad=0.6"},
    )

    # Shared legends
    fig.legend(stance_order, title="Stance", loc="upper center", ncol=3, bbox_to_anchor=(0.30, 0.93))
    fig.legend(frame_order, title="Frame", loc="upper center", ncol=3, bbox_to_anchor=(0.74, 0.93))
    savefig_multi("Figure6_Integrated_Findings")


if __name__ == "__main__":
    main()
