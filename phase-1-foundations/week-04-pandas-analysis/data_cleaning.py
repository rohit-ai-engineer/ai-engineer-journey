import pandas as pd
import json

print("=== Week 4 Day 2: Data Cleaning ===\n")

# Load your EPG data
with open(r'C:/Users/Rohit Jadiya/Downloads/data/Claude/ai-engineer-journey/epg_schedule_20260311_041046.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['valid'])

print(f"📊 Loaded {len(df)} shows\n")

# Check for missing data in ALL columns
print("--- Missing Data Check ---")
print(df.isna().sum())


print("\n--- Fixing Missing Networks ---")

# Option 1: Fill with a default value
df_filled = df.copy()  # Make a copy so we don't modify original
df_filled['network'].fillna('Unknown Network', inplace=True)

print("\nAfter filling with 'Unknown Network':")
print(df_filled['network'].value_counts().tail(5))

# Check - should be 0 now
print(f"\nMissing networks after fill: {df_filled['network'].isna().sum()}")

print("\n--- Creating New Columns ---")

# Create a new column based on existing data
df['duration_hours'] = df['runtime'] / 60

# Create a column based on conditions
df['time_slot'] = 'Other'
df.loc[df['airtime'] >= '06:00', 'time_slot'] = 'Morning'
df.loc[df['airtime'] >= '12:00', 'time_slot'] = 'Afternoon'
df.loc[df['airtime'] >= '18:00', 'time_slot'] = 'Evening'
df.loc[df['airtime'] >= '22:00', 'time_slot'] = 'Late Night'

print("\nNew columns added:")
print(df[['show_name', 'airtime', 'runtime', 'duration_hours', 'time_slot']].head(10))

print("\n--- Shows by Time Slot ---")
print(df['time_slot'].value_counts())


print("\n" + "="*50)
print("MERGING DATA FROM MULTIPLE SOURCES")
print("="*50)

# Simulate Provider A data (your current data)
provider_a = df[['show_name', 'airtime', 'runtime', 'network']].head(10).copy()
provider_a['source'] = 'Provider_A'

# Simulate Provider B data (same shows, slightly different data)
provider_b = provider_a.copy()
provider_b['source'] = 'Provider_B'
provider_b['runtime'] = provider_b['runtime'] + 5  # Simulate conflict - different runtime!

print("\n--- Provider A Data ---")
print(provider_a[['show_name', 'runtime', 'source']])

# print("\n--- Provider B Data ---")
# print(provider_b[['show_name', 'runtime', 'source']])

# Merge them
merged = pd.concat([provider_a, provider_b], ignore_index=True)

# print("\n--- Merged Data (Both Sources) ---")
# print(merged[['show_name', 'runtime', 'source']])

# # Find conflicts (same show, different runtime)
# print("\n--- Detecting Conflicts ---")
# conflicts = merged.groupby('show_name')['runtime'].nunique()
# conflicted_shows = conflicts[conflicts > 1]

# print(f"Shows with conflicting runtime data: {len(conflicted_shows)}")
# print(conflicted_shows)

print("\n" + "="*50)
print("PRACTICE: Conflict Resolution")
print("="*50)

# Step 1: For each show, count how many times each provider gave CORRECT data historically
# (In real Project 1, this will be ML-based confidence scores)

provider_accuracy = {
    'Provider_A': 0.85,  # Provider A is correct 85% of the time
    'Provider_B': 0.92   # Provider B is correct 92% of the time (more reliable)
}

# Step 2: Add confidence scores to the merged data
merged['confidence'] = merged['source'].map(provider_accuracy)

print("\n--- Merged Data with Confidence Scores ---")
print(merged[['show_name', 'runtime', 'source', 'confidence']].head(12))

# Step 3: For each show, pick the value from the most confident source
resolved = merged.loc[merged.groupby('show_name')['confidence'].idxmax()]

print("\n--- Resolved Data (Picked Most Confident Source) ---")
print(resolved[['show_name', 'runtime', 'source', 'confidence']])

print("\n--- Which Provider Won? ---")
print(resolved['source'].value_counts())

