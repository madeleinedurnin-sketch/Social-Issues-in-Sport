# Project 1 Analysis Script

Below is the Python script developed to process the Angel Reese & Caitlin Clark datasets according to the analytical approach specified in the Project 1 Research Plan (`CursorPros_PLAN_P1.md`).

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re

# File Paths
BASE_DIR = "/Users/kayleehooper/Downloads/PROJECT1"
INS_COMMENTS_FILE = os.path.join(BASE_DIR, "ARCC_INS", "ARCC_INS_COMMENT.xlsx")
YT_COMMENTS_FILE = os.path.join(BASE_DIR, "ARCC_YT", "ARCC_YT_COMMENT.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "ARCC_INS", "Project 1 code")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define Keywords for analysis
ATHLETE_KEYWORDS = {
    'Reese': ['reese', 'angel', 'bayou barbie'],
    'Clark': ['clark', 'caitlin', 'cc']
}

THEME_KEYWORDS = {
    'Personality': ['attitude', 'class', 'character', 'arrogant', 'humble', 'classless', 'respect', 'trash talk', 'cocky'],
    'Skill': ['stats', 'points', 'rebounds', 'better', 'score', 'shoot', 'defense', 'goat', 'record', 'assist'],
    'Beauty': ['pretty', 'ugly', 'looks', 'hair', 'body', 'beautiful', 'lashes', 'makeup', 'attractive']
}

def find_text_column(df):
    """Dynamically find the column that most likely contains comment text."""
    possible_names = ['text', 'comment', 'content', 'message', 'body', 'msg']
    for col in df.columns:
        if col.lower() in possible_names:
            return col
    # Fallback: find the column with the highest average string length
    string_cols = df.select_dtypes(include=['object']).columns
    if not string_cols.empty:
        lengths = {col: df[col].astype(str).str.len().mean() for col in string_cols}
        return max(lengths, key=lengths.get)
    return None

def analyze_comments(df, text_column):
    """Analyze the text column for mentions and themes."""
    # Convert text to lowercase string, handling NaNs
    texts = df[text_column].astype(str).str.lower()
    
    # 1. Mentions
    reese_mask = texts.str.contains('|'.join(ATHLETE_KEYWORDS['Reese']), na=False)
    clark_mask = texts.str.contains('|'.join(ATHLETE_KEYWORDS['Clark']), na=False)
    
    df['Mentions_Reese'] = reese_mask
    df['Mentions_Clark'] = clark_mask
    df['Cross_Mention'] = reese_mask & clark_mask
    
    # 2. Themes
    for theme, keywords in THEME_KEYWORDS.items():
        pattern = '|'.join([rf"\b{kw}\b" for kw in keywords])
        df[f'Theme_{theme}'] = texts.str.contains(pattern, flags=re.IGNORECASE, na=False)
        
    return df

print("Loading Data...")
dfs = []

# Load Instagram Comments
if os.path.exists(INS_COMMENTS_FILE):
    print("Loading Instagram comments...")
    df_ins = pd.read_excel(INS_COMMENTS_FILE)
    col = find_text_column(df_ins)
    if col:
        df_ins = analyze_comments(df_ins, col)
        df_ins['Platform'] = 'Instagram'
        dfs.append(df_ins)

# Load YouTube Comments
if os.path.exists(YT_COMMENTS_FILE):
    print("Loading YouTube comments...")
    # Use low_memory=False to handle potential mixed types in CSV
    df_yt = pd.read_csv(YT_COMMENTS_FILE, low_memory=False)
    col = find_text_column(df_yt)
    if col:
        df_yt = analyze_comments(df_yt, col)
        df_yt['Platform'] = 'YouTube'
        dfs.append(df_yt)

if not dfs:
    print("No valid data loaded. Please check the file paths and structures.")
    exit()

# Combine Data
df_all = pd.concat(dfs, ignore_index=True)

print(f"Total comments processed: {len(df_all)}")

# --- Visualization 1: Pie Chart of Comment Themes ---
print("Generating Pie Chart...")
theme_counts = {
    'Personality': df_all['Theme_Personality'].sum(),
    'Skill': df_all['Theme_Skill'].sum(),
    'Beauty': df_all['Theme_Beauty'].sum()
}

# Filter out zero counts
theme_counts = {k: v for k, v in theme_counts.items() if v > 0}

if theme_counts:
    plt.figure(figsize=(8, 8))
    plt.pie(theme_counts.values(), labels=theme_counts.keys(), autopct='%1.1f%%', 
            colors=['#ff9999','#66b3ff','#99ff99'], startangle=140)
    plt.title('Proportion of Comment Themes\n(Personality, Skill, Beauty Standards)')
    pie_path = os.path.join(OUTPUT_DIR, 'Theme_Proportion_PieChart.png')
    plt.savefig(pie_path, bbox_inches='tight')
    plt.close()
    print(f"Pie chart saved to {pie_path}")

# --- Visualization 2: Bar Graph of Cross-Mentions by Theme ---
print("Generating Bar Chart...")
# Filter for cross-mentions only
df_cross = df_all[df_all['Cross_Mention']]

if not df_cross.empty:
    cross_theme_counts = {
        'Personality': df_cross['Theme_Personality'].sum(),
        'Skill': df_cross['Theme_Skill'].sum(),
        'Beauty': df_cross['Theme_Beauty'].sum()
    }
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=list(cross_theme_counts.keys()), y=list(cross_theme_counts.values()), palette='viridis')
    plt.title('Cross-Mention Frequency by Theme (Clark & Reese in same comment)')
    plt.xlabel('Comment Theme')
    plt.ylabel('Number of Cross-Mention Comments')
    
    # Add value labels on top of bars
    for i, v in enumerate(cross_theme_counts.values()):
        plt.text(i, v + (max(cross_theme_counts.values())*0.01), str(v), ha='center')
        
    bar_path = os.path.join(OUTPUT_DIR, 'Cross_Mention_Frequency_BarChart.png')
    plt.savefig(bar_path, bbox_inches='tight')
    plt.close()
    print(f"Bar chart saved to {bar_path}")

print("Analysis complete.")
```
