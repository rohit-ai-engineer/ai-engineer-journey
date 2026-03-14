import pandas as pd
import json 

with open (r'C:/Users/Rohit Jadiya/Downloads/data/Claude/ai-engineer-journey/epg_schedule_20260311_041046.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['valid'])

df_copy = df.copy()

primetime_shows = df[(df['airtime'] >= '20:00') & (df['airtime'] < '22:00')]

print(primetime_shows)

print(f"Total primetime shows: {len(primetime_shows)}")
print(primetime_shows[['show_name', 'airtime', 'network']].head())

print("\n=== Primetime Shows Per Network ===")
print(primetime_shows['network'].value_counts())


avg_primetime_runtime = primetime_shows['runtime'].mean()
print(f"\nAverage primetime runtime: {avg_primetime_runtime:.1f} minutes")


df['is_primetime'] = False
df.loc[(df['airtime'] >= '20:00') & (df['airtime'] < '22:00'), 'is_primetime'] = True

print("\n=== Primetime Column Check ===")
print(f"Total primetime shows: {df['is_primetime'].sum()}")  # Counts True values
print(df[['show_name', 'airtime', 'is_primetime']].head(10))
