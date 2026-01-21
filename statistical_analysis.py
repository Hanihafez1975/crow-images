import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import f_oneway, ttest_ind
import json

# Load the data
df = pd.read_csv('experimental_data.csv')

output_params = ['Release_percent', 'PI3K', 'AKT1', 'TGFbeta', 'Caspase3', 'Caspase9', 'FGF2', 'P53']

print("=" * 80)
print("COMPREHENSIVE STATISTICAL ANALYSIS")
print("=" * 80)

# Calculate mean and SEM for each condition
stats_summary = {}

for param in output_params:
    print(f"\n{'=' * 80}")
    print(f"PARAMETER: {param}")
    print(f"{'=' * 80}")
    
    stats_summary[param] = {}
    
    # Group by time and pH
    grouped = df.groupby(['Time_h', 'pH'])[param]
    
    print("\nMean ± SEM by condition:")
    for (time, ph), group in grouped:
        mean_val = group.mean()
        sem_val = group.sem()
        std_val = group.std()
        n = len(group)
        
        condition = f"{time}h_pH{ph}"
        stats_summary[param][condition] = {
            'mean': float(mean_val),
            'sem': float(sem_val),
            'std': float(std_val),
            'n': int(n)
        }
        
        print(f"  {time}h, pH {ph}: {mean_val:.4f} ± {sem_val:.4f} (n={n})")
    
    # ANOVA for time effect at each pH
    print(f"\n  ANOVA - Effect of Time at different pH levels:")
    for ph in df['pH'].unique():
        groups = [df[(df['Time_h'] == t) & (df['pH'] == ph)][param].values 
                  for t in sorted(df['Time_h'].unique())]
        f_stat, p_val = f_oneway(*groups)
        print(f"    pH {ph}: F={f_stat:.4f}, p={p_val:.4e}")
    
    # ANOVA for pH effect at each time point
    print(f"\n  ANOVA - Effect of pH at different time points:")
    for time in sorted(df['Time_h'].unique()):
        groups = [df[(df['Time_h'] == time) & (df['pH'] == ph)][param].values 
                  for ph in sorted(df['pH'].unique())]
        f_stat, p_val = f_oneway(*groups)
        print(f"    {time}h: F={f_stat:.4f}, p={p_val:.4e}")
    
    # Two-way ANOVA (simplified)
    print(f"\n  Overall variability:")
    print(f"    Total variance: {df[param].var():.4f}")
    print(f"    Between-group variance (Time): {df.groupby('Time_h')[param].mean().var():.4f}")
    print(f"    Between-group variance (pH): {df.groupby('pH')[param].mean().var():.4f}")

# Save statistical summary
with open('statistical_summary.json', 'w') as f:
    json.dump(stats_summary, f, indent=2)

print("\n" + "=" * 80)
print("CORRELATION ANALYSIS")
print("=" * 80)

# Calculate correlation matrix
correlation_matrix = df[output_params].corr()
print("\nPearson Correlation Matrix:")
print(correlation_matrix)

# Save correlation matrix
correlation_matrix.to_csv('correlation_matrix.csv')

# Identify strong correlations
print("\nStrong correlations (|r| > 0.7):")
for i in range(len(output_params)):
    for j in range(i+1, len(output_params)):
        corr_val = correlation_matrix.iloc[i, j]
        if abs(corr_val) > 0.7:
            p1 = output_params[i]
            p2 = output_params[j]
            print(f"  {p1} vs {p2}: r = {corr_val:.4f}")

print("\n" + "=" * 80)
print("Statistical analysis complete!")
print("Files saved: statistical_summary.json, correlation_matrix.csv")
print("=" * 80)
