import pandas as pd
import json

# Global variable to store report
report = ""

def log(text):
    """Print to screen AND add to report"""
    global report
    print(text)  # ← Use print(), not log()!
    report += text + "\n"

# Load data
with open(r'C:/Users/Rohit Jadiya/Downloads/data/Claude/ai-engineer-journey/epg_schedule_20260311_041046.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['valid'])

log("=== DATA QUALITY REPORT ===")
log("")

# Step 1: Check each column
log("--- Column Summary ---")
for column in df.columns:
    total = len(df)
    missing = df[column].isna().sum()
    missing_pct = (missing / total) * 100
    try:
        unique = df[column].nunique()
    except TypeError:
        unique = "N/A (list column)"
    
    log(f"{column}:")
    log(f"  Total: {total}")
    log(f"  Missing: {missing} ({missing_pct:.1f}%)")
    log(f"  Unique values: {unique}\n")

short_shows = df[df['runtime'] < 10]
log (f"shows with runtime < 10 min: {len(short_shows)}")
if len (short_shows) > 0:
    log(short_shows[['show_name','runtime','network']])


long_shows = df[df['runtime'] > 240]

log (f"\nshows with runtime > 240 min: {len(long_shows)}")
if len(long_shows) > 0:
    df_str = long_shows[['show_name', 'runtime','network']].to_string()
    log(df_str)

missing_network = df[df['network'].isna()]

log(f"\nShows with missing network: {len(missing_network)}")
if len(missing_network) > 0:
    df_str = missing_network[['show_name', 'airtime', 'network']].to_string()
    log(df_str)

with open('C:/Users/Rohit Jadiya/Downloads/data/Claude/ai-engineer-journey/phase-1-foundations/week-04-pandas-analysis/data_quality_report.txt', 'w') as f:
    f.write(report)

print("\n✅ Report saved to data_quality_report.txt")
