import pandas as pd
import json

with open(r'C:/Users/Rohit Jadiya/Downloads/data/Claude/ai-engineer-journey/epg_schedule_20260311_041046.json', 'r') as f:
    data =json.load(f)

df = pd.DataFrame(data['valid'])

morning_shows = df[(df['airtime'] >= '06:00') & (df['airtime'] < '12:00')]

print("=== total morning shows = " + str(len(morning_shows)))

avg_runtime = morning_shows.groupby('network')['runtime'].mean()

print(avg_runtime)