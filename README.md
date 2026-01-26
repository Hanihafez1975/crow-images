# Scientific Manuscript: pH and Time-Dependent Effects of Chitosan-Encapsulated Selenadiazole Derivative on MCF7 Breast Cancer Cells

## Overview

This repository contains a comprehensive scientific manuscript and supporting materials analyzing the effects of chitosan-encapsulated selenadiazole derivative on MCF7 breast cancer cells under varying pH and time conditions.

## Study Summary

**Objective:** Investigate pH and time-dependent drug release kinetics and molecular pathway modulation (PI3K/AKT, apoptosis, growth factors) in MCF7 breast cancer cells treated with chitosan-encapsulated selenadiazole derivative.

**Experimental Design:**
- **Cell Line:** MCF7 human breast adenocarcinoma cells
- **pH Conditions:** 5.4 (acidic tumor microenvironment), 6.5 (intermediate), 7.4 (physiological)
- **Time Points:** 12h, 24h, 36h
- **Replicates:** n=3 per condition
- **Total Runs:** 27

**Key Parameters Measured:**
- Drug Release Percentage
- PI3K expression (fold change)
- AKT1 expression (fold change)
- TGF-β expression (fold change)
- Caspase-3 expression (fold change)
- Caspase-9 expression (fold change)
- FGF2 expression (fold change)
- P53 expression (fold change)

## Key Findings

1. **pH-Responsive Drug Release:** Maximum release at acidic pH 5.4 (80.8 ± 2.1%) vs pH 7.4 (54.2 ± 1.6%, p < 0.001)

2. **Apoptotic Induction:** Robust Caspase-3 and Caspase-9 activation at acidic pH (3.5-fold and 3.2-fold at pH 5.4 vs 1.2-fold and 1.3-fold at pH 7.4, p < 0.001)

3. **PI3K/AKT Suppression:** Reduced survival pathway activation under acidic conditions with time-dependent compensatory upregulation

4. **P53 Activation:** Peak tumor suppressor expression at 24h under acidic conditions (3.04 ± 0.001 fold)

5. **Strong Correlations:** Negative correlations between apoptotic markers and survival pathway components (r = -0.97 for Caspase-3 vs AKT1)

## Repository Contents

### Main Documents

1. **scientific_manuscript.md** - Complete manuscript with:
   - Abstract
   - Introduction (background, rationale, objectives)
   - Materials and Methods
   - Results (detailed analysis of all parameters)
   - Discussion (mechanistic insights, clinical implications)
   - Conclusions
   - References (70 citations)
   - Figure legends

2. **supplementary_materials.md** - Supplementary information including:
   - Descriptive statistics tables
   - Mean ± SEM values by condition
   - ANOVA results (time and pH effects)
   - Pearson correlation matrix
   - Strong correlations analysis
   - Variance analysis
   - Supplementary methods
   - Supplementary discussion

### Data Files

3. **experimental_data.csv** - Raw experimental data (27 runs × 11 parameters)

4. **initial_analysis.json** - Structured analysis results including experimental design and mean values

5. **statistical_summary.json** - Comprehensive statistical summary with mean, SEM, std, and n for all conditions

6. **correlation_matrix.csv** - Pearson correlation coefficients between all parameters

### Visualizations

7. **figure1_drug_release.png** - Drug release kinetics (time and pH effects)

8. **figure2_pi3k_akt.png** - PI3K/AKT pathway expression profiles

9. **figure3_caspases.png** - Apoptotic marker (Caspase-3, Caspase-9) expression

10. **figure4_growth_factors.png** - Growth factors and tumor suppressors (TGF-β, FGF2, P53)

11. **figure5_heatmaps.png** - Normalized expression heatmap and correlation matrix

12. **figure6_dashboard.png** - Comprehensive dashboard of all parameters

13. **visualization_report.pdf** - Professional PDF report with all figures and detailed captions

### Analysis Scripts

14. **analyze_data.py** - Initial data structure and descriptive statistics analysis

15. **statistical_analysis.py** - Comprehensive statistical analysis (ANOVA, correlations)

16. **create_visualizations.py** - Generation of all scientific figures

17. **create_pdf_report.py** - PDF report compilation with figures and captions

## Statistical Analysis Summary

### ANOVA Results

**Effect of pH (highly significant for all parameters):**
- Drug Release: F = 73.06-124.01, p < 0.0001
- Caspase-3: F = 2764.94-14597.22, p < 0.0001
- Caspase-9: F = 4939.73-41001.54, p < 0.0001
- PI3K: F = 16.19-330.92, p < 0.01
- AKT1: F = 137.73-1873.62, p < 0.0001

**Effect of Time (significant for most parameters):**
- PI3K: F = 7.17-660.82, p < 0.05
- AKT1: F = 25.06-365.19, p < 0.01
- Caspases: F = 570.54-161276.14, p < 0.0001
- P53: F = 55856.23-290241.24, p < 0.0001

### Correlation Highlights

**Strongest Positive Correlations:**
- Caspase-3 ↔ Caspase-9: r = 0.975
- Drug Release ↔ Caspase-9: r = 0.917
- Drug Release ↔ Caspase-3: r = 0.907

**Strongest Negative Correlations:**
- Caspase-3 ↔ AKT1: r = -0.969
- Drug Release ↔ FGF2: r = -0.961
- Caspase-9 ↔ AKT1: r = -0.947

## Biological Interpretation

The data reveal two antagonistic molecular programs:

**Apoptotic Program (acidic pH):**
- High drug release
- Elevated Caspase-3, Caspase-9, P53
- Suppressed PI3K/AKT, FGF2, TGF-β
- Dominant at pH 5.4

**Survival Program (neutral/alkaline pH):**
- Low drug release
- Elevated PI3K/AKT, FGF2, TGF-β
- Suppressed caspases and P53
- Dominant at pH 7.4

## Clinical Implications

1. **Tumor-Targeted Delivery:** pH-responsive formulation achieves selective drug release in acidic tumor microenvironment

2. **Reduced Systemic Toxicity:** Limited drug release at physiological pH (7.4) may minimize normal tissue exposure

3. **Combination Therapy Potential:** Time-dependent PI3K/AKT upregulation suggests synergy with pathway inhibitors

4. **Biomarker Development:** Strong correlations suggest potential predictive markers for treatment response

## Technical Specifications

**Software Used:**
- Python 3.9.25
- pandas 2.3.3
- numpy 2.0.2
- scipy 1.13.1
- matplotlib 3.9.4
- seaborn 0.13.2
- reportlab 4.4.9

**Statistical Methods:**
- One-way ANOVA with Tukey's post-hoc test
- Two-way ANOVA for interaction effects
- Pearson correlation analysis
- Descriptive statistics (mean, SEM, SD, CV)

**Visualization Standards:**
- 300 DPI resolution
- Publication-quality figures
- Consistent color schemes
- Error bars (SEM)
- Statistical significance indicators

## How to Use This Repository

### Viewing the Manuscript
Open `scientific_manuscript.md` in any Markdown viewer or text editor.

### Viewing Supplementary Materials
Open `supplementary_materials.md` for detailed statistical tables and additional methods.

### Viewing Visualizations
- Individual figures: Open PNG files (figure1-6)
- Complete report: Open `visualization_report.pdf`

### Reproducing Analysis
```bash
# Install dependencies
python3 -m pip install pandas numpy scipy matplotlib seaborn plotly kaleido pillow reportlab

# Run analyses
python3 analyze_data.py
python3 statistical_analysis.py
python3 create_visualizations.py
python3 create_pdf_report.py
```

### Accessing Raw Data
Open `experimental_data.csv` in Excel, Python, R, or any data analysis software.

## Citation

If you use this work, please cite:

[Author names]. pH and Time-Dependent Anticancer Effects of Chitosan-Encapsulated Selenadiazole Derivative on MCF7 Breast Cancer Cells: Modulation of PI3K/AKT Pathway and Apoptotic Signaling. [Journal name]. [Year].

## Contact

For questions or collaborations, please contact: [Contact information to be added]

## License

[License information to be added]

## Acknowledgments

This work was supported by [Funding sources to be added]. We thank [Collaborators and technical support] for their contributions.

---

**Last Updated:** January 21, 2026

**Version:** 1.0

**Status:** Complete manuscript with comprehensive analysis and visualizations
