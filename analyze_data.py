import pandas as pd
import numpy as np
from scipy import stats
import json

# Load the data
df = pd.read_csv('experimental_data.csv')

# Display basic information
print("=" * 80)
print("EXPERIMENTAL DATA STRUCTURE")
print("=" * 80)
print(f"\nTotal number of runs: {len(df)}")
print(f"\nColumns: {list(df.columns)}")
print(f"\nData types:\n{df.dtypes}")

# Experimental design
print("\n" + "=" * 80)
print("EXPERIMENTAL DESIGN")
print("=" * 80)
time_points = sorted(df['Time_h'].unique())
ph_levels = sorted(df['pH'].unique())
print(f"\nTime points (hours): {time_points}")
print(f"pH levels: {ph_levels}")
print(f"\nReplicates per condition: {df.groupby(['Time_h', 'pH']).size().unique()}")

# Output parameters
output_params = ['Release_percent', 'PI3K', 'AKT1', 'TGFbeta', 'Caspase3', 'Caspase9', 'FGF2', 'P53']

print("\n" + "=" * 80)
print("DESCRIPTIVE STATISTICS - ALL PARAMETERS")
print("=" * 80)
print("\n", df[output_params].describe())

# Group by conditions
print("\n" + "=" * 80)
print("MEAN VALUES BY CONDITION (Time x pH)")
print("=" * 80)

results = {}
for param in output_params:
    print(f"\n{param}:")
    pivot = df.pivot_table(values=param, index='Time_h', columns='pH', aggfunc='mean')
    print(pivot)
    results[param] = pivot.to_dict()

# Save initial analysis
with open('initial_analysis.json', 'w') as f:
    json.dump({
        'experimental_design': {
            'time_points': [int(x) for x in time_points],
            'ph_levels': [float(x) for x in ph_levels],
            'total_runs': int(len(df)),
            'replicates': 3
        },
        'output_parameters': output_params,
        'mean_values_by_condition': {k: {str(ki): {str(kj): float(vj) for kj, vj in vi.items()} for ki, vi in v.items()} for k, v in results.items()}
    }, f, indent=2)

print("\n" + "=" * 80)
print("Initial analysis saved to initial_analysis.json")
print("=" * 80)
