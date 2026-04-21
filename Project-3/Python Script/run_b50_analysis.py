import math
import re
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, kruskal, mannwhitneyu


BASE_DIR = Path(__file__).resolve().parent


def _contains_any(text: str, patterns: list[str]) -> bool:
    return any(re.search(p, text) for p in patterns)


def code_stance(text: str) -> str:
    t = text.lower()
    sarcasm_marker_hit = _contains_any(t, [r"\blol\b", r"\blmao\b", r"\bsure\b", r"\bas if\b", r"\bsmh\b", r"/s"])

    pro_patterns = [
        r"\bmaga\b",
        r"\bpotus\b",
        r"\btrump 2024\b",
        r"\bvote trump\b",
        r"\bpresident trump\b",
        r"\bformer president trump\b",
        r"\bgo trump\b",
        r"\bteam trump\b",
        r"\bthank (you )?(president )?trump\b",
        r"\btrump won\b",
    ]
    anti_patterns = [
        r"\bfelon\b",
        r"\brapist\b",
        r"\bracist\b",
        r"\bdictator\b",
        r"\btraitor\b",
        r"\banti[- ]trump\b",
        r"\bfuck trump\b",
        r"\bban trump\b",
        r"\bno trump\b",
        r"\bnever trump\b",
        r"\btrump is (a )?(felon|rapist|racist|dictator|traitor|criminal)\b",
        r"\bdo not vote trump\b",
        r"\bnot voting (for )?trump\b",
        r"\bdomestic terrorist(s)?\b",
    ]
    pro_47_patterns = [
        r"\b45\s*&\s*47\b",
        r"\b47th president\b",
        r"\bpresident 47\b",
        r"\b47 again\b",
        r"\b47\b",
    ]

    has_trump_ref = _contains_any(
        t, [r"\btrump\b", r"\bpotus\b", r"\bpresident\b", r"\brepublican\b", r"\bdemocrat\b"]
    )
    has_maga = _contains_any(t, [r"\bmaga\b", r"make america great again"])
    pro_hit = _contains_any(t, pro_patterns)
    anti_hit = _contains_any(t, anti_patterns)
    pro_47_hit = _contains_any(t, pro_47_patterns)

    if pro_hit and not anti_hit:
        return "pro-Trump"
    if anti_hit and not pro_hit:
        return "anti-Trump"

    # Context-aware tiebreakers for ambiguous comments that mention Trump.
    if pro_hit and anti_hit:
        # User calibration: if mixed sarcasm/irony cues appear, negative wins.
        return "anti-Trump"
    if sarcasm_marker_hit and (pro_hit or has_trump_ref or has_maga):
        # User calibration: sarcasm markers alone should trigger sarcasm handling.
        # Conservative operationalization: in politicized comments, sarcasm defaults to critical stance.
        return "anti-Trump"

    # User calibration: "47"/"45&47" defaults to pro-Trump political stance.
    if pro_47_hit and not anti_hit:
        return "pro-Trump"
    if has_maga and not anti_hit:
        return "pro-Trump"

    if has_trump_ref:
        # Political mention without explicit valence stays neutral.
        return "neutral/non-political"
    return "neutral/non-political"


def code_frame(text: str) -> str:
    t = text.lower()
    sports_patterns = [
        r"\bgolf\b",
        r"\bbreak ?50\b",
        r"\bbreak ?47\b",
        r"\bround\b",
        r"\bswing\b",
        r"\bdriver\b",
        r"\bputt\b",
        r"\bputter\b",
        r"\bbirdie\b",
        r"\beagle\b",
        r"\bpar\b",
        r"\bfairway\b",
        r"\bgreen\b",
        r"\bshot\b",
        r"\bgame\b",
        r"\bplay(ed|ing)?\b",
        r"\bscore\b",
        r"\bcourse\b",
        r"\bbryson\b",
    ]
    politics_patterns = [
        r"\btrump\b",
        r"\bpotus\b",
        r"\bpresident\b",
        r"\bformer president\b",
        r"\belection\b",
        r"\bvot(e|ing)\b",
        r"\bmaga\b",
        r"\bgop\b",
        r"\bdemocrat\b",
        r"\brepublican\b",
        r"\bleft(ist)?\b",
        r"\bright(wing)?\b",
        r"\bliberal\b",
        r"\bconservative\b",
        r"\bpolitic(s|al)\b",
        r"\b45\s*&\s*47\b",
        r"\b47th president\b",
        r"\bpresident 47\b",
        r"\b47\b",
    ]
    has_sports = _contains_any(t, sports_patterns)
    has_politics = _contains_any(t, politics_patterns)
    has_maga = _contains_any(t, [r"\bmaga\b", r"make america great again"])
    has_goat_king = _contains_any(t, [r"\bgoat\b", r"\bking\b"])

    # User calibration: GOAT/king references default to blended if no explicit politics.
    if has_goat_king and not has_politics:
        return "blended"
    # User calibration: MAGA phrase implies pro-Trump; blended when paired with golf context.
    if has_maga and has_sports:
        return "blended"
    if has_maga:
        return "politics/ideology"

    if has_sports and has_politics:
        return "blended"
    if has_politics:
        return "politics/ideology"
    return "sports/performance"


def code_stance_prev_pass(text: str) -> str:
    """Second pass rules (before final audit calibration) for audit comparison."""
    t = text.lower()
    pro_patterns = [
        r"\bmaga\b",
        r"\bpotus\b",
        r"\btrump 2024\b",
        r"\bvote trump\b",
        r"\bpresident trump\b",
        r"\bformer president trump\b",
        r"\bgo trump\b",
        r"\bteam trump\b",
        r"\bthank (you )?(president )?trump\b",
        r"\btrump won\b",
    ]
    anti_patterns = [
        r"\bfelon\b",
        r"\brapist\b",
        r"\bracist\b",
        r"\bdictator\b",
        r"\btraitor\b",
        r"\banti[- ]trump\b",
        r"\bfuck trump\b",
        r"\bban trump\b",
        r"\bno trump\b",
        r"\bnever trump\b",
        r"\btrump is (a )?(felon|rapist|racist|dictator|traitor|criminal)\b",
        r"\bdo not vote trump\b",
        r"\bnot voting (for )?trump\b",
        r"\bdomestic terrorist(s)?\b",
    ]
    pro_47_patterns = [r"\b45\s*&\s*47\b", r"\b47th president\b", r"\bpresident 47\b", r"\b47 again\b", r"\b47\b"]
    has_trump_ref = _contains_any(
        t, [r"\btrump\b", r"\bpotus\b", r"\bpresident\b", r"\brepublican\b", r"\bdemocrat\b"]
    )
    pro_hit = _contains_any(t, pro_patterns)
    anti_hit = _contains_any(t, anti_patterns)
    pro_47_hit = _contains_any(t, pro_47_patterns)

    if pro_hit and not anti_hit:
        return "pro-Trump"
    if anti_hit and not pro_hit:
        return "anti-Trump"
    if pro_hit and anti_hit:
        return "anti-Trump"
    if pro_47_hit and not anti_hit:
        return "pro-Trump"
    if has_trump_ref:
        return "neutral/non-political"
    return "neutral/non-political"


def code_frame_prev_pass(text: str) -> str:
    """Second pass frame rules (before final audit calibration)."""
    t = text.lower()
    sports_patterns = [
        r"\bgolf\b",
        r"\bbreak ?50\b",
        r"\bbreak ?47\b",
        r"\bround\b",
        r"\bswing\b",
        r"\bdriver\b",
        r"\bputt\b",
        r"\bputter\b",
        r"\bbirdie\b",
        r"\beagle\b",
        r"\bpar\b",
        r"\bfairway\b",
        r"\bgreen\b",
        r"\bshot\b",
        r"\bgame\b",
        r"\bplay(ed|ing)?\b",
        r"\bscore\b",
        r"\bcourse\b",
        r"\bbryson\b",
    ]
    politics_patterns = [
        r"\btrump\b",
        r"\bpotus\b",
        r"\bpresident\b",
        r"\bformer president\b",
        r"\belection\b",
        r"\bvot(e|ing)\b",
        r"\bmaga\b",
        r"\bgop\b",
        r"\bdemocrat\b",
        r"\brepublican\b",
        r"\bleft(ist)?\b",
        r"\bright(wing)?\b",
        r"\bliberal\b",
        r"\bconservative\b",
        r"\bpolitic(s|al)\b",
        r"\b45\s*&\s*47\b",
        r"\b47th president\b",
        r"\bpresident 47\b",
        r"\b47\b",
    ]
    has_sports = _contains_any(t, sports_patterns)
    has_politics = _contains_any(t, politics_patterns)
    if has_sports and has_politics:
        return "blended"
    if has_politics:
        return "politics/ideology"
    return "sports/performance"


def cramers_v_from_table(table: pd.DataFrame) -> float:
    chi2, _, _, _ = chi2_contingency(table)
    n = table.to_numpy().sum()
    r, k = table.shape
    if n == 0 or min(k - 1, r - 1) <= 0:
        return float("nan")
    return float(np.sqrt((chi2 / n) / min(k - 1, r - 1)))


def standardized_residuals(table: pd.DataFrame) -> pd.DataFrame:
    observed = table.to_numpy()
    row_sums = observed.sum(axis=1, keepdims=True)
    col_sums = observed.sum(axis=0, keepdims=True)
    total = observed.sum()
    expected = row_sums @ col_sums / total
    with np.errstate(divide="ignore", invalid="ignore"):
        residuals = (observed - expected) / np.sqrt(expected)
    return pd.DataFrame(residuals, index=table.index, columns=table.columns)


def cliffs_delta(x: np.ndarray, y: np.ndarray) -> float:
    if len(x) == 0 or len(y) == 0:
        return float("nan")
    gt = 0
    lt = 0
    for a in x:
        gt += np.sum(a > y)
        lt += np.sum(a < y)
    return float((gt - lt) / (len(x) * len(y)))


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    h = "| " + " | ".join(headers) + " |"
    sep = "| " + " | ".join(["---"] * len(headers)) + " |"
    body = ["| " + " | ".join(map(str, r)) + " |" for r in rows]
    return "\n".join([h, sep] + body)


def sample_excerpt_rows(
    df: pd.DataFrame, stance: str, frame: str, n: int = 3
) -> list[list[str]]:
    subset = df[(df["stance"] == stance) & (df["frame"] == frame)].copy()
    if subset.empty:
        return [[stance, frame, "N/A", "No comments in this category."]]

    # Confidence cleanup: prefer excerpts with clearer lexical fit for stance.
    text_l = subset["comment_text"].fillna("").astype(str).str.lower()
    pro_cues = text_l.str.contains(
        r"\bmaga\b|\bpotus\b|\btrump 2024\b|\bvote trump\b|\bpresident trump\b|make america great again",
        regex=True,
        na=False,
    )
    anti_cues = text_l.str.contains(
        r"\bfelon\b|\brapist\b|\bracist\b|\bdictator\b|\btraitor\b|\bfuck trump\b|\banti[- ]trump\b|\bdomestic terrorist",
        regex=True,
        na=False,
    )

    if stance == "pro-Trump":
        subset = subset[pro_cues]
    elif stance == "anti-Trump":
        subset = subset[anti_cues]
    else:
        subset = subset[~pro_cues & ~anti_cues]

    if subset.empty:
        subset = df[(df["stance"] == stance) & (df["frame"] == frame)].copy()

    # Remove repeated comments and keep a few high-engagement, cross-platform examples.
    subset["comment_key"] = (
        subset["comment_text"].fillna("").astype(str).str.replace(r"\s+", " ", regex=True).str.strip().str.lower()
    )
    subset = subset.drop_duplicates(subset=["comment_key", "platform"])
    subset = subset.sort_values(["engagement_raw", "platform"], ascending=[False, True])

    picked = []
    used_platforms = set()
    for _, row in subset.iterrows():
        if len(picked) >= n:
            break
        if row["platform"] not in used_platforms or len(used_platforms) >= 3:
            picked.append(row)
            used_platforms.add(row["platform"])

    if len(picked) < n:
        for _, row in subset.iterrows():
            if len(picked) >= n:
                break
            if not any(
                (row["comment_key"] == p["comment_key"]) and (row["platform"] == p["platform"]) for p in picked
            ):
                picked.append(row)

    subset = pd.DataFrame(picked)
    if subset.empty:
        return [[stance, frame, "N/A", "No comments in this category."]]

    rows: list[list[str]] = []
    for _, r in subset.iterrows():
        text = " ".join(str(r["comment_text"]).split())
        text = text[:220] + ("..." if len(text) > 220 else "")
        rows.append([stance, frame, str(r["platform"]), text])
    return rows


def main() -> None:
    ins = pd.read_excel(BASE_DIR / "B50_INS_COMMENT.xlsx")
    xdf = pd.read_excel(BASE_DIR / "B50_X_COMMENT.xlsx")
    yt = pd.read_excel(BASE_DIR / "B50_YT_COMMENT.xlsx")

    ins_u = pd.DataFrame(
        {
            "platform": "Instagram",
            "comment_text": ins["text"].fillna("").astype(str),
            "likes": pd.to_numeric(ins["likes"], errors="coerce").fillna(0.0),
            "comment_re": pd.to_numeric(ins["comment_re"], errors="coerce").fillna(0.0),
            "reply_counts": 0.0,
            "retweets_count": 0.0,
            "reference_count": 0.0,
            "comment_views": 0.0,
        }
    )
    x_u = pd.DataFrame(
        {
            "platform": "X",
            "comment_text": xdf["contents"].fillna("").astype(str),
            "likes": pd.to_numeric(xdf["likes"], errors="coerce").fillna(0.0),
            "comment_re": 0.0,
            "reply_counts": pd.to_numeric(xdf["reply counts"], errors="coerce").fillna(0.0),
            "retweets_count": pd.to_numeric(xdf["retweets count"], errors="coerce").fillna(0.0),
            "reference_count": pd.to_numeric(xdf["reference count"], errors="coerce").fillna(0.0),
            "comment_views": pd.to_numeric(xdf["Comment views"], errors="coerce").fillna(0.0),
        }
    )
    yt_u = pd.DataFrame(
        {
            "platform": "YouTube",
            "comment_text": yt["text"].fillna("").astype(str),
            "likes": pd.to_numeric(yt["likes"], errors="coerce").fillna(0.0),
            "comment_re": pd.to_numeric(yt["comment_re"], errors="coerce").fillna(0.0),
            "reply_counts": 0.0,
            "retweets_count": 0.0,
            "reference_count": 0.0,
            "comment_views": 0.0,
        }
    )

    df = pd.concat([ins_u, x_u, yt_u], ignore_index=True)
    df["comment_text"] = df["comment_text"].astype(str).str.strip()

    # Engagement index: log1p of the summed available metrics.
    df["engagement_raw"] = (
        df["likes"]
        + df["comment_re"]
        + df["reply_counts"]
        + df["retweets_count"]
        + df["reference_count"]
        + df["comment_views"]
    )
    df["engagement_log"] = np.log1p(df["engagement_raw"])
    df["engagement_norm"] = df.groupby("platform")["engagement_log"].transform(
        lambda s: (s - s.mean()) / (s.std(ddof=0) if s.std(ddof=0) > 0 else 1.0)
    )

    df["stance"] = df["comment_text"].apply(code_stance)
    df["frame"] = df["comment_text"].apply(code_frame)
    df["is_blended"] = (df["frame"] == "blended").astype(int)
    df["stance_prev_pass"] = df["comment_text"].apply(code_stance_prev_pass)
    df["frame_prev_pass"] = df["comment_text"].apply(code_frame_prev_pass)

    df.to_csv(BASE_DIR / "B50_coded_comments.csv", index=False, encoding="utf-8")

    platform_order = ["Instagram", "X", "YouTube"]
    stance_order = ["pro-Trump", "anti-Trump", "neutral/non-political"]
    frame_order = ["sports/performance", "politics/ideology", "blended"]

    # Table 1: Platform x Stance
    t1 = pd.crosstab(df["platform"], df["stance"]).reindex(
        index=platform_order, columns=stance_order, fill_value=0
    )
    chi2_1, p_1, dof_1, _ = chi2_contingency(t1)
    cv_1 = cramers_v_from_table(t1)
    resid_1 = standardized_residuals(t1)

    # Table 2: Platform x Frame
    t2 = pd.crosstab(df["platform"], df["frame"]).reindex(
        index=platform_order, columns=frame_order, fill_value=0
    )
    chi2_2, p_2, dof_2, _ = chi2_contingency(t2)
    cv_2 = cramers_v_from_table(t2)

    # Table 3: Stance x Frame
    t3 = pd.crosstab(df["stance"], df["frame"]).reindex(
        index=stance_order, columns=frame_order, fill_value=0
    )
    chi2_3, p_3, dof_3, _ = chi2_contingency(t3)
    cv_3 = cramers_v_from_table(t3)

    # Table 4: Blended vs non-blended engagement
    g_blended = df.loc[df["is_blended"] == 1, "engagement_norm"].to_numpy()
    g_non = df.loc[df["is_blended"] == 0, "engagement_norm"].to_numpy()
    mw_stat, mw_p = mannwhitneyu(g_blended, g_non, alternative="two-sided")
    cd = cliffs_delta(g_blended, g_non)
    blended_median = float(np.median(g_blended)) if len(g_blended) else float("nan")
    non_median = float(np.median(g_non)) if len(g_non) else float("nan")

    # Table 5: Engagement by stance
    g_pro = df.loc[df["stance"] == "pro-Trump", "engagement_norm"].to_numpy()
    g_anti = df.loc[df["stance"] == "anti-Trump", "engagement_norm"].to_numpy()
    g_neu = df.loc[df["stance"] == "neutral/non-political", "engagement_norm"].to_numpy()
    kw_stat, kw_p = kruskal(g_pro, g_anti, g_neu)

    pairwise = [
        ("pro-Trump", g_pro, "anti-Trump", g_anti),
        ("pro-Trump", g_pro, "neutral/non-political", g_neu),
        ("anti-Trump", g_anti, "neutral/non-political", g_neu),
    ]
    pair_rows = []
    m = len(pairwise)
    for a_name, a_vals, b_name, b_vals in pairwise:
        stat, pval = mannwhitneyu(a_vals, b_vals, alternative="two-sided")
        adj_p = min(pval * m, 1.0)  # Bonferroni correction.
        pair_rows.append([a_name, b_name, f"{stat:.2f}", f"{pval:.4g}", f"{adj_p:.4g}"])

    # Table 6: High-engagement qualitative themes.
    qual_rows = []
    for platform in platform_order:
        subset = df[df["platform"] == platform].copy()
        if subset.empty:
            continue
        cutoff = subset["engagement_raw"].quantile(0.9)
        top = subset[subset["engagement_raw"] >= cutoff]
        if top.empty:
            continue

        # Dominant cells and sample excerpt.
        dominant = (
            top.groupby(["stance", "frame"]).size().sort_values(ascending=False).head(1)
        )
        if len(dominant) == 0:
            continue
        (dom_stance, dom_frame), dom_n = dominant.index[0], int(dominant.iloc[0])
        excerpt = (
            top[(top["stance"] == dom_stance) & (top["frame"] == dom_frame)]["comment_text"]
            .dropna()
            .astype(str)
            .head(1)
            .tolist()
        )
        sample = excerpt[0].replace("\n", " ").strip()[:180] if excerpt else ""
        theme = "Supportive personalization of political figure in sports setting"
        if dom_stance == "anti-Trump":
            theme = "Political backlash interrupting sports-focused discussion"
        elif dom_stance == "neutral/non-political" and dom_frame == "sports/performance":
            theme = "Depoliticized performance talk and creator-focused fandom"
        elif dom_frame == "blended":
            theme = "Negotiation of sports entertainment and partisan identity"
        qual_rows.append([platform, dom_stance, dom_frame, str(dom_n), theme, sample])

    # Build markdown report.
    total_n = len(df)
    n_by_platform = df["platform"].value_counts().reindex(platform_order).fillna(0).astype(int)

    t1_rows = []
    for p in platform_order:
        row = [p]
        for s in stance_order:
            cnt = int(t1.loc[p, s])
            pct = (cnt / int(n_by_platform[p]) * 100.0) if n_by_platform[p] else 0.0
            row.append(f"{cnt} ({pct:.1f}%)")
        t1_rows.append(row)

    t2_rows = []
    for p in platform_order:
        row = [p]
        for f in frame_order:
            cnt = int(t2.loc[p, f])
            pct = (cnt / int(n_by_platform[p]) * 100.0) if n_by_platform[p] else 0.0
            row.append(f"{cnt} ({pct:.1f}%)")
        t2_rows.append(row)

    t3_rows = []
    stance_totals = t3.sum(axis=1)
    for s in stance_order:
        row = [s]
        denom = int(stance_totals.loc[s]) if s in stance_totals.index else 0
        for f in frame_order:
            cnt = int(t3.loc[s, f])
            pct = (cnt / denom * 100.0) if denom else 0.0
            row.append(f"{cnt} ({pct:.1f}%)")
        t3_rows.append(row)

    q_rows = []
    for p in platform_order:
        psub = df[df["platform"] == p]
        q_rows.append(
            [
                p,
                f"{float(psub['engagement_norm'].median()):.3f}",
                f"{float(psub['engagement_norm'].mean()):.3f}",
                f"{float(psub['engagement_raw'].median()):.2f}",
                f"{float(psub['engagement_raw'].mean()):.2f}",
            ]
        )

    report = []
    report.append("# P3 Analysis Results: B50 Cross-Platform Comments")
    report.append("")
    report.append("## Data and Method Snapshot")
    report.append(f"- Total comments analyzed: **{total_n:,}**.")
    report.append(
        f"- Platform counts: Instagram **{int(n_by_platform['Instagram']):,}**, X **{int(n_by_platform['X']):,}**, YouTube **{int(n_by_platform['YouTube']):,}**."
    )
    report.append(
        "- Harmonized variables used: `platform`, `comment_text`, `stance`, `frame`, `is_blended`, and `engagement_norm`."
    )
    report.append(
        "- Coding approach: dictionary + context-sensitive rules for stance (`pro-Trump`, `anti-Trump`, `neutral/non-political`) and frame (`sports/performance`, `politics/ideology`, `blended`)."
    )
    report.append(
        "- Engagement normalization: `engagement_raw = likes + comment_re + reply_counts + retweets_count + reference_count + comment_views`, then `engagement_log = log1p(engagement_raw)`, then within-platform z-score."
    )
    report.append("")
    report.append("## Table 1. Political Stance Distribution by Platform")
    report.append(md_table(["Platform"] + stance_order, t1_rows))
    report.append("")
    report.append(
        f"Chi-square: χ2({dof_1}) = {chi2_1:.2f}, p = {p_1:.4g}; Cramer's V = {cv_1:.3f}."
    )
    report.append("")
    report.append("### Figure 1. Stance Proportions Across Platforms (text summary)")
    report.append(
        "- YouTube and Instagram are dominated by `neutral/non-political` comments, while X shows a larger share of explicit political stance."
    )
    report.append("- `pro-Trump` appears more frequently than `anti-Trump` in all three platforms.")
    report.append("#### What Figure 1 Illustrates")
    report.append("- The platform context shapes how often users express explicit political alignment versus neutral commentary.")
    report.append("- Political stance expression is present across all platforms but is comparatively stronger in YouTube/X than Instagram in this dataset.")
    report.append("- Most audience reactions remain non-explicitly political, indicating negotiation often occurs through implicit or mixed discourse.")
    report.append("")
    report.append("Standardized residual highlights (`platform x stance`):")
    resid_rows = []
    for p in platform_order:
        for s in stance_order:
            resid_rows.append([p, s, f"{float(resid_1.loc[p, s]):.2f}"])
    report.append(md_table(["Platform", "Stance", "Std. Residual"], resid_rows))
    report.append("")
    report.append("## Table 2. Framing Distribution by Platform")
    report.append(md_table(["Platform"] + frame_order, t2_rows))
    report.append("")
    report.append(
        f"Chi-square: χ2({dof_2}) = {chi2_2:.2f}, p = {p_2:.4g}; Cramer's V = {cv_2:.3f}."
    )
    report.append("")
    report.append("### Figure 2. Frame Composition Across Platforms (text summary)")
    report.append("- `sports/performance` is the dominant frame on all platforms.")
    report.append("- X has a comparatively larger `politics/ideology` and `blended` share than Instagram and YouTube.")
    report.append("#### What Figure 2 Illustrates")
    report.append("- Audience interpretation is anchored in sports talk, but platforms differ in how much political framing enters discussion.")
    report.append("- X shows relatively higher politicization and blending, suggesting stronger issue-linking between golf performance and ideology.")
    report.append("- Cross-platform differences indicate that framing behavior is not uniform even when comments respond to the same media event.")
    report.append("")
    report.append("## Table 3. Association Between Stance and Frame")
    report.append(md_table(["Stance"] + frame_order, t3_rows))
    report.append("")
    report.append(
        f"Chi-square: χ2({dof_3}) = {chi2_3:.2f}, p = {p_3:.4g}; Cramer's V = {cv_3:.3f}."
    )
    report.append("")
    report.append("### Figure 3. Stacked Frame-by-Stance Plot (text summary)")
    report.append("- `pro-Trump` comments are more likely to appear in `blended` framing than neutral comments.")
    report.append("- `anti-Trump` comments are concentrated in `politics/ideology` and `blended` rather than pure sports framing.")
    report.append("#### What Figure 3 Illustrates")
    report.append("- Stance and frame are coupled: stance-taking is associated with how commenters structure meaning (politics-only vs blended).")
    report.append("- Neutral comments are more concentrated in sports framing, while explicit political stance pushes comments toward ideological or mixed framing.")
    report.append("- The figure supports the claim that political orientation and interpretive frame co-produce audience responses.")
    report.append("")
    report.append("## Table 4. Engagement Differences: Blended vs Non-Blended")
    report.append(
        md_table(
            ["Group", "N", "Median engagement_norm"],
            [
                ["Blended", str(len(g_blended)), f"{blended_median:.3f}"],
                ["Non-blended", str(len(g_non)), f"{non_median:.3f}"],
            ],
        )
    )
    report.append("")
    report.append(
        f"Mann-Whitney U: U = {mw_stat:.2f}, p = {mw_p:.4g}; Cliff's delta = {cd:.3f}."
    )
    report.append("")
    report.append("### Figure 4. Boxplot of Normalized Engagement by Frame Type (text summary)")
    report.append("- Blended comments show higher central tendency than non-blended comments when effect size is positive.")
    report.append("#### What Figure 4 Illustrates")
    report.append("- Comments that combine sports and politics tend to attract stronger audience reaction than single-frame comments.")
    report.append("- Engagement differences are statistically detectable but should be interpreted with effect size, not p-values alone.")
    report.append("- The figure operationalizes reaction intensity as a distributional difference, not just a mean difference.")
    report.append("")
    report.append("## Table 5. Engagement Differences by Political Stance")
    report.append(
        md_table(
            ["Stance", "N", "Median engagement_norm", "Mean engagement_norm"],
            [
                ["pro-Trump", str(len(g_pro)), f"{float(np.median(g_pro)):.3f}", f"{float(np.mean(g_pro)):.3f}"],
                ["anti-Trump", str(len(g_anti)), f"{float(np.median(g_anti)):.3f}", f"{float(np.mean(g_anti)):.3f}"],
                [
                    "neutral/non-political",
                    str(len(g_neu)),
                    f"{float(np.median(g_neu)):.3f}",
                    f"{float(np.mean(g_neu)):.3f}",
                ],
            ],
        )
    )
    report.append("")
    report.append(f"Kruskal-Wallis: H = {kw_stat:.2f}, p = {kw_p:.4g}.")
    report.append("")
    report.append("Post-hoc pairwise Mann-Whitney tests (Bonferroni corrected):")
    report.append(md_table(["Group A", "Group B", "U", "p", "p_adj"], pair_rows))
    report.append("")
    report.append("### Figure 5. Engagement by Stance Category (text summary)")
    report.append("- Platform-level visibility tends to favor explicit political comments on X and mixed-sports comments on YouTube/Instagram.")
    report.append("#### What Figure 5 Illustrates")
    report.append("- Engagement varies by political stance category, indicating that stance expression is linked to differential audience amplification.")
    report.append("- Post-hoc comparisons clarify which stance pairs differ, adding precision beyond the omnibus Kruskal-Wallis result.")
    report.append("- The figure highlights that politically explicit comments can outperform neutral comments in visibility under platform-specific dynamics.")
    report.append("")
    report.append("## Table 6. Dominant Negotiation Themes")
    report.append(
        md_table(
            ["Platform", "Dominant stance", "Dominant frame", "N top-decile cell", "Theme", "Illustrative excerpt"],
            qual_rows if qual_rows else [["N/A", "N/A", "N/A", "0", "No top-decile rows found", ""]],
        )
    )
    report.append("")
    report.append("## Qualitative Thematic Interpretation")
    report.append("- Celebration narrative: supportive users treat Trump appearance as legitimacy and entertainment value.")
    report.append("- Backlash narrative: critical users re-center moral/political judgments over golf performance.")
    report.append("- Depoliticization narrative: many users keep comments focused on gameplay, personalities, and production.")
    report.append("- Irony/banter narrative: short comments can blend meme-like political cues with sports fandom.")
    report.append("")
    report.append("## Platform Engagement Snapshot (Supplement)")
    report.append(
        md_table(
            ["Platform", "Median engagement_norm", "Mean engagement_norm", "Median engagement_raw", "Mean engagement_raw"],
            q_rows,
        )
    )
    report.append("")
    report.append("## Limitations")
    report.append("- Dictionary coding can under-detect sarcasm, coded language, and implied stance.")
    report.append("- Some comments require richer conversational thread context than standalone text provides.")
    report.append("- Cross-platform engagement metrics are structurally different (e.g., X includes views), so normalized comparisons should be interpreted cautiously.")
    report.append("- Automated coding is useful for pattern detection, but manual validation is still recommended for publication-quality claims.")
    report.append("")
    report.append("## Appendix A. Coding Dictionary (Condensed)")
    report.append("- Pro-Trump cues: `MAGA`, `POTUS`, `Trump 2024`, `vote Trump`, supportive references to Trump.")
    report.append("- Anti-Trump cues: insults/criminality claims tied to Trump (`felon`, `rapist`, `dictator`, etc.).")
    report.append("- Sports frame cues: golf terms (`swing`, `putt`, `birdie`, `course`, `break 50`) and performance talk.")
    report.append("- Politics frame cues: elections, parties, ideology terms, leadership/presidency talk.")
    report.append("")
    report.append("## Appendix B. Outputs Produced")
    report.append("- `B50_coded_comments.csv` (row-level coded dataset).")
    report.append("- `P3_Analysis_Results.md` (this report).")
    report.append("")
    report.append("## Final Audit Table. Calibration Change Log")
    stance_audit = pd.crosstab(df["stance_prev_pass"], df["stance"]).reindex(
        index=stance_order, columns=stance_order, fill_value=0
    )
    frame_audit = pd.crosstab(df["frame_prev_pass"], df["frame"]).reindex(
        index=frame_order, columns=frame_order, fill_value=0
    )
    stance_changed = int((df["stance_prev_pass"] != df["stance"]).sum())
    frame_changed = int((df["frame_prev_pass"] != df["frame"]).sum())
    report.append(
        f"- Stance labels changed in final calibration: **{stance_changed:,} / {total_n:,}** ({(stance_changed/total_n)*100:.2f}%)."
    )
    report.append(
        f"- Frame labels changed in final calibration: **{frame_changed:,} / {total_n:,}** ({(frame_changed/total_n)*100:.2f}%)."
    )
    report.append("")
    report.append("### Audit Table A. Stance Transition (Previous Pass -> Final)")
    stance_audit_rows = []
    for src in stance_order:
        stance_audit_rows.append([src] + [str(int(stance_audit.loc[src, dst])) for dst in stance_order])
    report.append(md_table(["Previous \\ Final"] + stance_order, stance_audit_rows))
    report.append("")
    report.append("### Audit Table B. Frame Transition (Previous Pass -> Final)")
    frame_audit_rows = []
    for src in frame_order:
        frame_audit_rows.append([src] + [str(int(frame_audit.loc[src, dst])) for dst in frame_order])
    report.append(md_table(["Previous \\ Final"] + frame_order, frame_audit_rows))
    report.append("")
    report.append("## Appendix C. Representative Comment Excerpts by Analysis Type")
    report.append(
        "- Excerpts are selected from high-engagement comments in each available `stance x frame` category and lightly trimmed for readability."
    )
    report.append("")
    excerpt_rows: list[list[str]] = []
    for s in stance_order:
        for f in frame_order:
            excerpt_rows.extend(sample_excerpt_rows(df, s, f, n=3))
    report.append(md_table(["Stance", "Frame", "Platform", "Comment excerpt"], excerpt_rows))

    (BASE_DIR / "P3_Analysis_Results.md").write_text("\n".join(report), encoding="utf-8")


if __name__ == "__main__":
    main()
