import pandas as pd
import json

# Load data
with open(r'C:/Users/Rohit Jadiya/Downloads/data/Claude/ai-engineer-journey/epg_schedule_20260311_041046.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['valid'])

# Group by network and calculate stats
network_stats = df.groupby('network').agg({
    'runtime': ['mean', 'count', 'max']
})

# Sort by average runtime (longest first) and get top 10
top_10_networks = network_stats.sort_values(('runtime', 'mean'), ascending=False).head(10)

print("=== Top 10 Networks by Average Runtime ===\n")
print(top_10_networks)