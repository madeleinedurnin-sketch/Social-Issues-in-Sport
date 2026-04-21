# Project 3: Group Research Plan

**Course:** KIN 7518 Social Issues in Sport
**Group:** CursorPros (Hailee Hernandez, Madeleine Durnin, Kaylee Hooper)
**Submitted:** April 9, 2026

---

## Repository Structure

- `README.md` — this plan
- `Python Script/run_b50_analysis.py` — main analysis pipeline
- `Python Script/generate_b50_figures.py` — visualization generation
- `Visualizations/` — six figures referenced in Section 8 (stance × platform, frame × platform, stance-frame association, blended vs. non-blended engagement, engagement by stance, integrated findings)
- `AI Verification/Comment_Selection_and_Analysis_Decisions.md` — coding decisions log
- `AI Verification/Session_Transcript.md` — full Cursor session transcript

The raw `B50_INS_COMMENT.xlsx`, `B50_X_COMMENT.xlsx`, and `B50_YT_COMMENT.xlsx` files are not committed to this repository.

---

## 1. Research Question

How do audiences across YouTube, X, and Instagram negotiate and react to the blending of sports entertainment and political messaging in the context of Donald Trump's appearance on Bryson DeChambeau's "Break 50" series?

### Context

The intersection of sports and politics has become increasingly visible in contemporary media, especially as social media allows public figures to blur the boundaries between entertainment, athletics, and political discourse. In the United States, rising political polarization has heightened sensitivity to political messaging in spaces traditionally viewed as neutral, including sports.

This phenomenon can be understood through Framing Theory, which explains how the presentation of content shapes audience interpretation. Audiences actively negotiate meaning, interpreting content through a sports lens, a political lens, or a combination of both. Public Sphere Theory adds that social media functions as a space for public debate and opinion formation. Donald Trump's appearance on Bryson DeChambeau's "Break 50" series provides a unique case to examine how audiences respond when sports and politics are intentionally blended, particularly across different social media platforms.

### Why It Matters

The United States is becoming increasingly partisan in its political views, and politics is being treated as something not to be discussed in mixed company as people have grown more outspoken (and at times hostile) about their political beliefs. With the continued integration of social media into everyday life, politicians are more visible in the media that fans and athletes create. People often debate whether sport should be kept separate from politics, or whether the two can have a productive relationship. This question helps us examine that boundary using a case where audiences are extremely outspoken on both sides, providing authentic insight into how sport-political integration is received and what that reception means for athletes and organizations weighing similar collaborations.

---

## 2. Dataset Selection & Justification

**Dataset Choice:** B50 / Trump Discourse

These three datasets are well aligned with the research question. Because all three are tied to Bryson DeChambeau's "Break 50" series and Donald Trump's guest appearance specifically, they isolate audience reaction to a single sport-political moment rather than to either figure's broader social media presence. Using data from three platforms (Instagram, X, YouTube) diversifies the comment styles available because of the different user behaviors and platform cultures involved. Together, the datasets provide both the raw text needed to see how people are reacting to the blending of sports and politics and the structural metrics needed to see where and how strongly those reactions are resonating across three fundamentally different social ecosystems. This allows direct comparison of how platform-specific cultures influence audience reactions.

**Files:**

- `B50_INS_COMMENT.xlsx`
- `B50_X_COMMENT.xlsx`
- `B50_YT_COMMENT.xlsx`

---

## 3. Variable Operationalization

| Construct | Operational Definition | Data Source / Indicator |
| --- | --- | --- |
| Platform-specific political stance expression | Explicit political positioning within comments | Text coding of `text` (INS, YT) and `contents` (X); keyword dictionaries (e.g., "MAGA," "rapist," "president," "former president," party labels) plus a manual validation sample. |
| Sports-entertainment vs. political framing | Primary thematic frame used by commenters when interpreting the content | Content coding of the same text fields using frame categories: sports/performance (e.g., "break 47," gameplay skill), politics/ideology (candidate evaluations, ideology), and blended (sports and political references in one comment). Optional support fields: `hashtag` in `B50_X_COMMENT.xlsx`, `source` in `B50_YT_COMMENT.xlsx`. |
| Engagement intensity of political-sport reactions | Magnitude of audience reaction to comments that blend sports and politics compared with comments that do not | Engagement metrics linked to coded comments: `likes` and `comment_re` in `B50_INS_COMMENT.xlsx`; `likes`, reply counts, retweets count, reference count, and comment views in `B50_X_COMMENT.xlsx`; `likes` and `comment_re` in `B50_YT_COMMENT.xlsx`. Compute platform-normalized averages and medians by frame and stance category. Engagement will be normalized across platforms to ensure comparability. |

---

## 4. Proposed Analyses

| Analysis Type | Description | RQ |
| --- | --- | --- |
| Framing pattern comparison | Compare prevalence of sports/performance, politics/ideology, and blended frames across YouTube, X, and Instagram | RQ 1 |
| Stance-by-frame association | Test whether political stance is associated with framing choice (e.g., whether pro/anti comments are more likely to be blended vs. single-frame) within and across platforms | RQ 1 |
| Engagement differential analysis | Compare normalized engagement (likes, replies, retweets, views where available) between blended and non-blended comments, and by stance category | RQ 1 |

These analyses allow us to compare how audiences frame content, express political stance, and engage with blended sports-political messaging across platforms.

---

## 5. Limitations & Potential Issues

1. **Deciphering user intent.** Comment sections are deeply embedded in internet culture and niche inside jokes, and it is difficult to accurately classify comments that use sports slang to make a political point (or vice versa) whether the coding is automated or manual. This ambiguity can lead to miscategorization of the data, potentially skewing findings about how boundaries are being negotiated.

2. **Cross-platform comparability.** Cross-platform analysis is a strength of the study, but it is not an apples-to-apples comparison. X fosters argumentative, text-heavy, real-time political discourse; Instagram is visual-first and tends toward aesthetic reactions and short-form emojis; YouTube's structure encourages longer, essay-style replies. Developing a unified coding framework that accurately measures "negotiation" across these architectures is complex, and a metric indicating deep engagement on X may mean something quite different on Instagram.

3. **Static snapshot.** The datasets capture audience reactions at scrape time. Online discourse around a polarizing political figure is highly fluid, and the way audiences negotiate the blending of sports and politics may shift as the political news cycle progresses or as the video is reshared in new contexts. Relying on a fixed dataset means the approach cannot capture how public perception evolves over time, restricting findings to an immediate reactionary window rather than a long-term understanding of audience reception.

These limitations should be considered when interpreting results, particularly when making cross-platform comparisons or broader generalizations.

---

## 6. Ethical Considerations

**Privacy.** This study relies on public data: user-generated comments from publicly accessible posts on Instagram, X, and YouTube. The datasets contain identifiable metadata, however, and to mitigate the risk of identifying specific individuals the data will be treated confidentially during analysis, with usernames and personally identifiable markers removed.

**Harm.** The intersection of politics and sport, especially involving a polarizing figure like Donald Trump, naturally elicits heated, partisan, and sometimes toxic discourse. Analyzing and presenting these comments could inadvertently amplify inflammatory rhetoric or partisan vitriol present in the data, and generalizing the findings could reinforce stereotypes such as assumptions about the political ideologies of all golf enthusiasts or characterizations of users on specific platforms. To prevent this, the research will maintain academic objectivity, focusing on how audiences negotiate meaning and boundaries rather than validating, judging, or giving an unfiltered platform to extreme sentiments.

**Bias.** Bias can exist in both the data and its interpretation. The datasets capture only the sentiments of a highly engaged minority who felt strongly enough to leave a comment, leaving the reactions of the silent majority unknown. The baseline audience also skews toward golf fans and Bryson DeChambeau subscribers, so reactions are not representative of the general public, and platform algorithms heavily bias which comments are seen and engaged with. Interpreting this data carries the risk of researcher bias as well, because political comments are often subjective, sarcastic, or culturally nuanced; we will be careful not to project our own political leanings onto coding and thematic analysis, and we will keep interpretations grounded in the data.

---

## 7. Group Role Assignments

| Role | Group Member | Primary Responsibilities |
| --- | --- | --- |
| Data Lead | Hailee | Data cleaning, preprocessing, file management |
| Methods Lead | Madeleine | Analysis design, tool implementation, documentation |
| Theory Lead | Kaylee | Literature integration, RQ refinement, interpretation |

---

## 8. Data Visualization Plan

**Primary Goal.** Each visualization addresses a different piece of the audience reaction question: how comments are framed, how stance is expressed, and how engagement varies across blended versus non-blended content.

**Visualization Description.** Two box plots show engagement around blended comments and the effect of explicit stance on engagement. Three bar graphs examine comment framing and platform comparison.

**Design Rationale.** Bar graphs and box plots show distributions and comparisons across platforms cleanly, especially when comparing multiple platforms and variables. Z-scores and chi-square tests are used to quantify the distributions, and the visualizations make those statistical patterns easier to read in plain language. Breaking the analysis into separate visualizations rather than packing everything into one chart helps the reader engage with each piece of the dataset on its own terms.

**Verification Methods:**

- Spot-checked calculations against source data
- Verified percentages and totals add up correctly
- Asked Cursor for multiple iterations and reviews for style and accuracy fixes (3–5 iterations per visualization)

**Files.** All six figures are in the `Visualizations/` folder of this repository:

- `Figure1_StanceByPlatform.png`
- `Figure2_FrameByPlatform.png`
- `Figure3_StanceFrameAssociation.png`
- `Figure4_Engagement_BlendedVsNon.png`
- `Figure5_Engagement_ByStance.png`
- `Figure6_Integrated_Findings.png`

**Brief Interpretation.** The combined set of visualizations indicates that blended comments perform better in engagement than comments that are explicitly political, and that some platforms are more political than others. These comments are not primarily about the video itself; they reveal what audiences think about the blending of politics and sport.

---

## 9. AI-Assisted Work Documentation

**Tools Used.** We used Cursor and GitHub for Project 3, primarily to develop and sort through the data and to coordinate work across the team via the repository.

**Verification Methods:**

- Code explanation: asked AI to explain each section of code, reviewed the explanations to confirm we understood the logic, and asked for code to be saved locally where helpful for review.
- Output validation: verified outputs made logical sense given the data, and compared AI results against what we already knew about the dataset.
- Iterative refinement: roughly four prompt iterations before getting usable output. Key refinements included cleaning the visualizations, clarifying the social context of comments, and asking the model whether anything was unclear.

**Learning Reflection.** We learned more about how to coordinate across different platforms and build collaborative tools that a group can share. We also learned that getting AI to produce the desired outcome usually takes multiple tries, and that human oversight is essential for ensuring accuracy and meaningful interpretation. The session-by-session decisions are documented in `AI Verification/Comment_Selection_and_Analysis_Decisions.md`, and the full Cursor session transcript is in `AI Verification/Session_Transcript.md`.
