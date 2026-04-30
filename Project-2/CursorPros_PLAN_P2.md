# Project 2: Group Research Plan

**Course:** KIN 7518 Social Issues in Sport  
**Due:** Friday, March 20, 2026 by 11:59 PM  
**Submission:** Email to [yqian@lsu.edu](mailto:yqian@lsu.edu) — One member submits, **CC all group members**  
**Format:** Markdown (.md) file

---

## Research Questions & Significance

For each research question, address all three components below. The goal is to show the logical connection between the phenomenon you're investigating, the question you're asking, and why it matters.

### RQ 1

**The Question:**  
How do YouTube content creators frame TGL's commercialization of professional golf, and in what ways does audience   discourse in the comments reflect public acceptance, resistance, or ambivalence toward a technology-driven, entertainment-first sport model? 

**The Context:**  
The context for this question is due to the emergence of the TGL as an “entertainment-first” alternative to traditional professional golf. This is the first of its kind, as it focuses on technology-driven, shorter-format gameplay compared to the traditional PGA Tour or LIV Golf. This framework leans heavily towards the YouTube content creators in its effort to commercialize the sport as legitimate. 

## **Why It Matters:**  
This matters, as the rise of the TGL shows a shift in how sports are produced, consumed, and valued. By understanding how YouTube creators and their audience consume its commercialization, we can help explain whether fans are ready for this technology-driven model or if they will remain loyal to the traditions seen in the PGA Tour or LIV Golf. The stakes are significant, as athletes will have to adapt to new formats, fans will influence if it is successful or not, and media organizations will shape the narrative around the sport. Leagues and investors have a heavy stake in this, as it is their money on the line. For researchers and industry professionals, this moment in sport will offer insight into the future direction of sport and will show if innovation will redefine sport or disrupt the norm.  

## Dataset Selection & Justification

Identify which dataset you are using and explain why.

**Dataset Choice:** We have decided to use the TGLCOMMENT and TGLVIDEO datasets. These datasets are appropriate for our research question.  
**Justification:**  
The TGLCOMMENT and TGLVIDEO datasets are appropriate datasets for our research question because they both allow us to analyze the fan discourse and context in how that discourse is occurring. Since our research question focuses on how youtube commenters talk about the legitimacy of TGL’s new league format. It is important that we have access to both the comments and the engagement surrounding those comments.  
The TGLCOMMENT dataset provides a large dataset with direct insight into how the viewers are interpreting TGL. This includes whether they view the league as not "real" golf or something exciting and new. This will show us if the legitimacy is being constructed, debated, or challenged by the fans.  
The TGLVIDEO pairs with this by providing us with data such as views, likes, and comment counts. This allows us to examine how different types of videos influence the type of discourse found in the comments. It will also help us identify if the high engagement videos tend to generate more positive (legitimacy) or negative (not legitimate) narratives.   

**Key files you plan to use:**

- TGLCOMMENT.xlsx  
- TGLVIDEO.xlsx

---

### Preliminary Variable Operationalization



|**Construct**|**Operational Definition**|**Data Source/ Indicator**|**Keyword Search**|
|-|-|-|-|
|Legitimacy|Whether the public accepts TGL as a valid alternative to a traditional golf competition|Keyword search in TGLCOMMENT.xlsx and TGLVIDEO.xlsx|gimmick, not real, future of golf, tradition, seriousness|
|Technology|Does the influence of technology in TGL shift the audience perspectives. Helps focus whether the audience focus is on the quality of play or the technology present|Keyword search in TGLCOMMENT.xlsx and TGLVIDEO.xlsx|innovation, entertainment, fan experience, screen graphics, technology|
|Commercialization|The spread in popularity of the TGL and whether from audience opinions the league is viable for long-term growth|Keyword search in TGLCOMMENT.xlsx and TGLVIDEO.xlsx|investor, growth, sponsor, legitimacy, money grab, commericialized|

---

## Proposed Analyses

Outline the analytical approaches you plan to use. For each, explain how it addresses your RQ.


| Analysis Type                       | Description                                                                                                                                                                                                                                                              | RQ Addressed |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ |
| Keyword/Thematic Frequency          | Identify and count key terms related to legitimacy, such as “real golf," "legitimacy," "innovation," “future,” and “entertainment.” This helps show how often certain legitimacy narratives are in the comments.                                                         | RQ 1         |
| Engagement Comparison               | Identify comments that reference the fan's perspective of how they will view TGL relative to how they may view tradional golf competitions. These comments will also help judge whether the fan's are actively engaging with the league in a positive or negative light. | RQ1          |
| Technology-Based Discourse Analysis | Identify comments that mention TGL’s technological features (simulator, virtual course, graphics, broadcast setup) and examine how those features are tied to perceptions of legitimacy.                                                                                 | RQ1          |


---

## Limitations & Potential Issues

Identify at least 2-3 limitations or challenges with your approach. Be honest—acknowledging limits is a strength, not a weakness.

1. One of the limitations is that this dataset is Youtube does not represent the full audience of TGL. Comment sections tend to be for more opinionated people, which makes the comment section more polarizing than it actually is. That means we are reflecting a certain group of fans, rather than the public.
2. Another limitation is that comments can lack context or be difficult for AI to interpret. Jokes and sarcasm may be miscoded and can impact the accuracy.
3. Lastly, engagement metrics do not really directly reflect sentiment or meaning. A video with high engagement can have both positive and negative reactions so we cannot assume that higher engagement means support for TGL.

---

## Ethical Considerations

**Privacy**

When analyzing comment and video data, we are looking at data that is publicly available on YouTube. Individuals who post comments may not expect their content to be used in analysis like this. Because of this key point, there is a risk of identifying individuals through usernames and profile details or direct quotes. To address this, we will anonymize all data, avoid using identifiable information, and paraphrase comments when possible to protect user privacy.

**Harm**

There is a potential for harm if our analysis unintentionally reinforces stereotypes or amplifies negative narratives. There might be discussion throughout the comments and videos that includes commentary about certain groups or the perception of exclusivity, wealth, or demographics involved in the sport. Without the proper context, these perspectives can lead the way to reinforce the existing stereotypes. We will acknowledge and evaluate all content, making sure it is clear that these views are not representative of all audiences.

**Bias**

Bias can influence how the data is both collected and interpreted. Selecting only highly visible or viral videos and comments can overrepresent extreme opinions, simply due to the algorithm. Personal biases may also shape how the data is analyzed. To minimize these effects, it is important to be transparent about data selection and acknowledge any limitations in the analysis.

---

## Group Role Assignments

Specify who is responsible for what. Titles are flexible, but responsibilities must be clear.


| Role         | Group Member | Primary Responsibilities                              |
| ------------ | ------------ | ----------------------------------------------------- |
| Data Lead    | Hailee       | Data cleaning, preprocessing, file management         |
| Methods Lead | Madeleine    | Analysis design, tool implementation, documentation   |
| Theory Lead  | Kaylee       | Literature integration, RQ refinement, interpretation |


---

## Data Visualization Plan

Create at least ONE data visualization that addresses your research question(s). This is a required deliverable due with your project plan.

**Primary Goal:**  
What story does your visualization tell? What specific question does it answer?

Our story aims to show how fans perceive the legitimacy of TGL and how those perceptions differ across different types of videos. We really want to understand whether audience reactions are more supportive, opposing, or mixed and how that relates to engagement. 

**Visualization Description:**  
Describe what type of chart/graph you're creating and what it will show. (e.g., "Bar chart comparing frequency of X vs. Y," "Line graph showing change over time," "Word cloud of most common themes")

We will create a bar graph that compares the frequency of the legitimacy themes across the TGL videos. In addition, we might include a second visualization, like a pie chart or another bar chart, to show the overall portion of the themes in the dataset. 

**Design Rationale:**  
Why did you choose this visualization type? How does it clarify your argument or make your data more understandable?

A bar graph allows us to clearly compare the different categories of legitimacy discourse across the videos, making it easy to see patterns and differences. The other chart will help show the distribution of the audience discourse. 

**Verification Methods:**  
How will you ensure your visualization accurately represents your data?

- Spot-checked calculations against source data  
- Had groupmate review for accuracy  
- Verified percentages/totals add up correctly  
- Other: We will compare the visualization back to our coded data to ensure it reflects the themes we are using.

**The Visualization:**  
Embed your visualization here (as an image) or provide a link to the file.

  
  
**Brief Interpretation (2-3 sentences):**  
What does this visualization show? What pattern or insight does it reveal?

The grouped bar chart reveals that News Analysis videos generate the most delegitimizing discourse (189 comments), significantly outpacing legitimizing comments (113) in that category. This suggests that journalistic or opinion-driven content tends to attract more critical reactions from viewers. In contrast, Video Podcasts and Vlogs skew more positive, with legitimizing comments outnumbering delegitimizing ones. The donut chart shows that overall, legitimizing (8.7%) and delegitimizing (8.4%) discourse are nearly evenly split among the 6,102 total comments, while technology-focused discourse accounts for 5.8%, indicating that tech features are a notable but secondary focus in the audience conversation about TGL's legitimacy.

---

## AI-Assisted Work Documentation & Verification

If you used AI tools (Antigravity, Cursor, ChatGPT, etc.) for any part of this plan, document your process and verification methods.

**Tools Used:**  
Which AI tools/IDEs did you use, and for what purpose?

For our project, we mainly utilized Cursor and Antigravity to sort through the datasets and help develop our visualizations. We also used Claude integrated into our IDEs to help further develop our project.

**Verification Methods:**  
How did you verify AI outputs were accurate and appropriate?

- **Code Explanation:**  
  - I asked AI to explain what each line/section of code does  
  - I reviewed explanations and understand the logic 
  - I saved code files within the workspace to reference if needed 
 
- **Output Validation:**  
  - I cross-checked AI calculations against manual spot-checks (specify  of checks: )  
  - I verified outputs make logical sense given my data  
  - I compared AI results with what I know about my dataset
  - I utilized multiple IDEs and prompts to test outputs across situations and compare for accuracy and consistency

