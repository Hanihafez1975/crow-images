import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.gridspec import GridSpec
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9

# Load data
df = pd.read_csv('experimental_data.csv')

output_params = ['Release_percent', 'PI3K', 'AKT1', 'TGFbeta', 'Caspase3', 'Caspase9', 'FGF2', 'P53']
param_labels = {
    'Release_percent': 'Drug Release (%)',
    'PI3K': 'PI3K Expression (fold change)',
    'AKT1': 'AKT1 Expression (fold change)',
    'TGFbeta': 'TGF-β Expression (fold change)',
    'Caspase3': 'Caspase-3 Expression (fold change)',
    'Caspase9': 'Caspase-9 Expression (fold change)',
    'FGF2': 'FGF2 Expression (fold change)',
    'P53': 'P53 Expression (fold change)'
}

colors_ph = {5.4: '#e74c3c', 6.5: '#3498db', 7.4: '#2ecc71'}
colors_time = {12: '#9b59b6', 24: '#e67e22', 36: '#1abc9c'}

print("Creating visualizations...")

# Figure 1: Drug Release Profiles
print("  - Figure 1: Drug Release Profiles")
fig1, axes = plt.subplots(1, 2, figsize=(12, 5))

# Panel A: Release vs Time at different pH
for ph in sorted(df['pH'].unique()):
    data = df[df['pH'] == ph].groupby('Time_h')['Release_percent'].agg(['mean', 'sem'])
    axes[0].errorbar(data.index, data['mean'], yerr=data['sem'], 
                     marker='o', linewidth=2, markersize=8, capsize=5,
                     label=f'pH {ph}', color=colors_ph[ph])
axes[0].set_xlabel('Time (hours)')
axes[0].set_ylabel('Drug Release (%)')
axes[0].set_title('A. Drug Release Kinetics')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Panel B: Release vs pH at different time points
for time in sorted(df['Time_h'].unique()):
    data = df[df['Time_h'] == time].groupby('pH')['Release_percent'].agg(['mean', 'sem'])
    axes[1].errorbar(data.index, data['mean'], yerr=data['sem'], 
                     marker='s', linewidth=2, markersize=8, capsize=5,
                     label=f'{time}h', color=colors_time[time])
axes[1].set_xlabel('pH')
axes[1].set_ylabel('Drug Release (%)')
axes[1].set_title('B. pH-Dependent Release')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('figure1_drug_release.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 2: PI3K/AKT Pathway
print("  - Figure 2: PI3K/AKT Pathway")
fig2, axes = plt.subplots(2, 2, figsize=(12, 10))

for idx, param in enumerate(['PI3K', 'AKT1']):
    # Time effect
    for ph in sorted(df['pH'].unique()):
        data = df[df['pH'] == ph].groupby('Time_h')[param].agg(['mean', 'sem'])
        axes[idx, 0].errorbar(data.index, data['mean'], yerr=data['sem'], 
                             marker='o', linewidth=2, markersize=8, capsize=5,
                             label=f'pH {ph}', color=colors_ph[ph])
    axes[idx, 0].set_xlabel('Time (hours)')
    axes[idx, 0].set_ylabel(param_labels[param])
    axes[idx, 0].set_title(f'{chr(65+idx*2)}. {param} Expression - Time Course')
    axes[idx, 0].legend()
    axes[idx, 0].grid(True, alpha=0.3)
    
    # pH effect
    for time in sorted(df['Time_h'].unique()):
        data = df[df['Time_h'] == time].groupby('pH')[param].agg(['mean', 'sem'])
        axes[idx, 1].errorbar(data.index, data['mean'], yerr=data['sem'], 
                             marker='s', linewidth=2, markersize=8, capsize=5,
                             label=f'{time}h', color=colors_time[time])
    axes[idx, 1].set_xlabel('pH')
    axes[idx, 1].set_ylabel(param_labels[param])
    axes[idx, 1].set_title(f'{chr(66+idx*2)}. {param} Expression - pH Response')
    axes[idx, 1].legend()
    axes[idx, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('figure2_pi3k_akt.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 3: Apoptotic Markers
print("  - Figure 3: Apoptotic Markers")
fig3, axes = plt.subplots(2, 2, figsize=(12, 10))

for idx, param in enumerate(['Caspase3', 'Caspase9']):
    # Time effect
    for ph in sorted(df['pH'].unique()):
        data = df[df['pH'] == ph].groupby('Time_h')[param].agg(['mean', 'sem'])
        axes[idx, 0].errorbar(data.index, data['mean'], yerr=data['sem'], 
                             marker='o', linewidth=2, markersize=8, capsize=5,
                             label=f'pH {ph}', color=colors_ph[ph])
    axes[idx, 0].set_xlabel('Time (hours)')
    axes[idx, 0].set_ylabel(param_labels[param])
    axes[idx, 0].set_title(f'{chr(65+idx*2)}. {param} Expression - Time Course')
    axes[idx, 0].legend()
    axes[idx, 0].grid(True, alpha=0.3)
    
    # pH effect
    for time in sorted(df['Time_h'].unique()):
        data = df[df['Time_h'] == time].groupby('pH')[param].agg(['mean', 'sem'])
        axes[idx, 1].errorbar(data.index, data['mean'], yerr=data['sem'], 
                             marker='s', linewidth=2, markersize=8, capsize=5,
                             label=f'{time}h', color=colors_time[time])
    axes[idx, 1].set_xlabel('pH')
    axes[idx, 1].set_ylabel(param_labels[param])
    axes[idx, 1].set_title(f'{chr(66+idx*2)}. {param} Expression - pH Response')
    axes[idx, 1].legend()
    axes[idx, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('figure3_caspases.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 4: Growth Factors and Tumor Suppressors
print("  - Figure 4: Growth Factors and Tumor Suppressors")
fig4, axes = plt.subplots(2, 3, figsize=(15, 10))

for idx, param in enumerate(['TGFbeta', 'FGF2', 'P53']):
    # Time effect
    for ph in sorted(df['pH'].unique()):
        data = df[df['pH'] == ph].groupby('Time_h')[param].agg(['mean', 'sem'])
        axes[0, idx].errorbar(data.index, data['mean'], yerr=data['sem'], 
                             marker='o', linewidth=2, markersize=8, capsize=5,
                             label=f'pH {ph}', color=colors_ph[ph])
    axes[0, idx].set_xlabel('Time (hours)')
    axes[0, idx].set_ylabel(param_labels[param])
    axes[0, idx].set_title(f'{chr(65+idx)}. {param} - Time Course')
    axes[0, idx].legend()
    axes[0, idx].grid(True, alpha=0.3)
    
    # pH effect
    for time in sorted(df['Time_h'].unique()):
        data = df[df['Time_h'] == time].groupby('pH')[param].agg(['mean', 'sem'])
        axes[1, idx].errorbar(data.index, data['mean'], yerr=data['sem'], 
                             marker='s', linewidth=2, markersize=8, capsize=5,
                             label=f'{time}h', color=colors_time[time])
    axes[1, idx].set_xlabel('pH')
    axes[1, idx].set_ylabel(param_labels[param])
    axes[1, idx].set_title(f'{chr(68+idx)}. {param} - pH Response')
    axes[1, idx].legend()
    axes[1, idx].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('figure4_growth_factors.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 5: Heatmaps
print("  - Figure 5: Heatmaps")
fig5, axes = plt.subplots(1, 2, figsize=(14, 6))

# Panel A: Mean expression heatmap
mean_data = df.groupby(['Time_h', 'pH'])[output_params].mean()
mean_data_pivot = mean_data.reset_index().pivot(index='Time_h', columns='pH')

# Normalize each parameter for better visualization
normalized_data = pd.DataFrame()
for param in output_params:
    param_data = mean_data_pivot[param]
    normalized_data[param] = ((param_data - param_data.min().min()) / 
                              (param_data.max().max() - param_data.min().min())).stack()

normalized_pivot = normalized_data.unstack()
normalized_pivot.index = [f'{int(t)}h' for t in normalized_pivot.index]
normalized_pivot.columns = [f'pH {c}' for c in normalized_pivot.columns]

sns.heatmap(normalized_pivot, annot=True, fmt='.2f', cmap='RdYlGn_r', 
            cbar_kws={'label': 'Normalized Expression'}, ax=axes[0], linewidths=0.5)
axes[0].set_title('A. Normalized Expression Heatmap')
axes[0].set_xlabel('')
axes[0].set_ylabel('Time')

# Panel B: Correlation matrix
corr_matrix = df[output_params].corr()
mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=1)
sns.heatmap(corr_matrix, mask=mask, annot=True, fmt='.2f', cmap='coolwarm', 
            center=0, vmin=-1, vmax=1, square=True, ax=axes[1], linewidths=0.5,
            cbar_kws={'label': 'Pearson Correlation'})
axes[1].set_title('B. Parameter Correlation Matrix')

plt.tight_layout()
plt.savefig('figure5_heatmaps.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 6: Comprehensive Dashboard
print("  - Figure 6: Comprehensive Dashboard")
fig6 = plt.figure(figsize=(16, 12))
gs = GridSpec(3, 3, figure=fig6, hspace=0.3, wspace=0.3)

# Row 1: Drug release and key pathway markers
ax1 = fig6.add_subplot(gs[0, 0])
for ph in sorted(df['pH'].unique()):
    data = df[df['pH'] == ph].groupby('Time_h')['Release_percent'].agg(['mean', 'sem'])
    ax1.errorbar(data.index, data['mean'], yerr=data['sem'], 
                marker='o', linewidth=2, markersize=6, capsize=4,
                label=f'pH {ph}', color=colors_ph[ph])
ax1.set_xlabel('Time (h)')
ax1.set_ylabel('Release (%)')
ax1.set_title('A. Drug Release')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.3)

ax2 = fig6.add_subplot(gs[0, 1])
for ph in sorted(df['pH'].unique()):
    data = df[df['pH'] == ph].groupby('Time_h')['PI3K'].agg(['mean', 'sem'])
    ax2.errorbar(data.index, data['mean'], yerr=data['sem'], 
                marker='o', linewidth=2, markersize=6, capsize=4,
                label=f'pH {ph}', color=colors_ph[ph])
ax2.set_xlabel('Time (h)')
ax2.set_ylabel('PI3K (fold)')
ax2.set_title('B. PI3K Expression')
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3)

ax3 = fig6.add_subplot(gs[0, 2])
for ph in sorted(df['pH'].unique()):
    data = df[df['pH'] == ph].groupby('Time_h')['AKT1'].agg(['mean', 'sem'])
    ax3.errorbar(data.index, data['mean'], yerr=data['sem'], 
                marker='o', linewidth=2, markersize=6, capsize=4,
                label=f'pH {ph}', color=colors_ph[ph])
ax3.set_xlabel('Time (h)')
ax3.set_ylabel('AKT1 (fold)')
ax3.set_title('C. AKT1 Expression')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

# Row 2: Apoptotic markers
ax4 = fig6.add_subplot(gs[1, 0])
for ph in sorted(df['pH'].unique()):
    data = df[df['pH'] == ph].groupby('Time_h')['Caspase3'].agg(['mean', 'sem'])
    ax4.errorbar(data.index, data['mean'], yerr=data['sem'], 
                marker='o', linewidth=2, markersize=6, capsize=4,
                label=f'pH {ph}', color=colors_ph[ph])
ax4.set_xlabel('Time (h)')
ax4.set_ylabel('Caspase-3 (fold)')
ax4.set_title('D. Caspase-3 Expression')
ax4.legend(fontsize=8)
ax4.grid(True, alpha=0.3)

ax5 = fig6.add_subplot(gs[1, 1])
for ph in sorted(df['pH'].unique()):
    data = df[df['pH'] == ph].groupby('Time_h')['Caspase9'].agg(['mean', 'sem'])
    ax5.errorbar(data.index, data['mean'], yerr=data['sem'], 
                marker='o', linewidth=2, markersize=6, capsize=4,
                label=f'pH {ph}', color=colors_ph[ph])
ax5.set_xlabel('Time (h)')
ax5.set_ylabel('Caspase-9 (fold)')
ax5.set_title('E. Caspase-9 Expression')
ax5.legend(fontsize=8)
ax5.grid(True, alpha=0.3)

ax6 = fig6.add_subplot(gs[1, 2])
for ph in sorted(df['pH'].unique()):
    data = df[df['pH'] == ph].groupby('Time_h')['P53'].agg(['mean', 'sem'])
    ax6.errorbar(data.index, data['mean'], yerr=data['sem'], 
                marker='o', linewidth=2, markersize=6, capsize=4,
                label=f'pH {ph}', color=colors_ph[ph])
ax6.set_xlabel('Time (h)')
ax6.set_ylabel('P53 (fold)')
ax6.set_title('F. P53 Expression')
ax6.legend(fontsize=8)
ax6.grid(True, alpha=0.3)

# Row 3: Growth factors and summary
ax7 = fig6.add_subplot(gs[2, 0])
for ph in sorted(df['pH'].unique()):
    data = df[df['pH'] == ph].groupby('Time_h')['TGFbeta'].agg(['mean', 'sem'])
    ax7.errorbar(data.index, data['mean'], yerr=data['sem'], 
                marker='o', linewidth=2, markersize=6, capsize=4,
                label=f'pH {ph}', color=colors_ph[ph])
ax7.set_xlabel('Time (h)')
ax7.set_ylabel('TGF-β (fold)')
ax7.set_title('G. TGF-β Expression')
ax7.legend(fontsize=8)
ax7.grid(True, alpha=0.3)

ax8 = fig6.add_subplot(gs[2, 1])
for ph in sorted(df['pH'].unique()):
    data = df[df['pH'] == ph].groupby('Time_h')['FGF2'].agg(['mean', 'sem'])
    ax8.errorbar(data.index, data['mean'], yerr=data['sem'], 
                marker='o', linewidth=2, markersize=6, capsize=4,
                label=f'pH {ph}', color=colors_ph[ph])
ax8.set_xlabel('Time (h)')
ax8.set_ylabel('FGF2 (fold)')
ax8.set_title('H. FGF2 Expression')
ax8.legend(fontsize=8)
ax8.grid(True, alpha=0.3)

# Bar chart comparing conditions
ax9 = fig6.add_subplot(gs[2, 2])
conditions = []
caspase3_means = []
for time in sorted(df['Time_h'].unique()):
    for ph in sorted(df['pH'].unique()):
        conditions.append(f'{time}h\npH{ph}')
        caspase3_means.append(df[(df['Time_h']==time) & (df['pH']==ph)]['Caspase3'].mean())

x_pos = np.arange(len(conditions))
bars = ax9.bar(x_pos, caspase3_means, color=['#e74c3c', '#3498db', '#2ecc71']*3, alpha=0.7)
ax9.set_xticks(x_pos)
ax9.set_xticklabels(conditions, fontsize=7, rotation=45, ha='right')
ax9.set_ylabel('Caspase-3 (fold)')
ax9.set_title('I. Caspase-3 by Condition')
ax9.grid(True, alpha=0.3, axis='y')

plt.savefig('figure6_dashboard.png', dpi=300, bbox_inches='tight')
plt.close()

print("\nAll visualizations created successfully!")
print("Files saved:")
print("  - figure1_drug_release.png")
print("  - figure2_pi3k_akt.png")
print("  - figure3_caspases.png")
print("  - figure4_growth_factors.png")
print("  - figure5_heatmaps.png")
print("  - figure6_dashboard.png")
