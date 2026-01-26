from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib import colors
from datetime import datetime
import os

# Create PDF
pdf_filename = 'visualization_report.pdf'
doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                       topMargin=0.75*inch, bottomMargin=0.75*inch,
                       leftMargin=0.75*inch, rightMargin=0.75*inch)

# Container for the 'Flowable' objects
elements = []

# Define styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#2c3e50'),
    spaceAfter=30,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.HexColor('#34495e'),
    spaceAfter=12,
    spaceBefore=12,
    fontName='Helvetica-Bold'
)

caption_style = ParagraphStyle(
    'Caption',
    parent=styles['Normal'],
    fontSize=10,
    textColor=colors.HexColor('#7f8c8d'),
    spaceAfter=20,
    alignment=TA_CENTER,
    fontName='Helvetica-Oblique'
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=11,
    textColor=colors.HexColor('#2c3e50'),
    spaceAfter=12,
    alignment=TA_JUSTIFY,
    leading=14
)

print("Creating PDF visualization report...")

# Title Page
elements.append(Spacer(1, 1.5*inch))
title = Paragraph("Visualization Report", title_style)
elements.append(title)
elements.append(Spacer(1, 0.3*inch))

subtitle = Paragraph(
    "pH and Time-Dependent Effects of Chitosan-Encapsulated<br/>Selenadiazole Derivative on MCF7 Breast Cancer Cells",
    ParagraphStyle('Subtitle', parent=styles['Normal'], fontSize=14, 
                   alignment=TA_CENTER, textColor=colors.HexColor('#34495e'))
)
elements.append(subtitle)
elements.append(Spacer(1, 0.5*inch))

date_text = Paragraph(
    f"Generated: {datetime.now().strftime('%B %d, %Y')}",
    ParagraphStyle('Date', parent=styles['Normal'], fontSize=11, 
                   alignment=TA_CENTER, textColor=colors.HexColor('#7f8c8d'))
)
elements.append(date_text)
elements.append(PageBreak())

# Introduction
elements.append(Paragraph("Overview", heading_style))
intro_text = """
This report presents comprehensive visualizations of experimental data examining the effects of 
chitosan-encapsulated selenadiazole derivative on MCF7 breast cancer cells. The study investigates 
drug release kinetics and molecular marker expression across three time points (12h, 24h, 36h) and 
three pH conditions (5.4, 6.5, 7.4). Key parameters analyzed include drug release percentage, 
PI3K/AKT pathway components, apoptotic markers (Caspase-3, Caspase-9), growth factors (TGF-β, FGF2), 
and tumor suppressor P53.
"""
elements.append(Paragraph(intro_text, body_style))
elements.append(Spacer(1, 0.3*inch))

# Figure 1
elements.append(PageBreak())
elements.append(Paragraph("Figure 1: Drug Release Profiles", heading_style))
if os.path.exists('figure1_drug_release.png'):
    img1 = Image('figure1_drug_release.png', width=6.5*inch, height=6.5*inch*5/12)
    elements.append(img1)
    caption1 = Paragraph(
        "<b>Figure 1.</b> Drug release kinetics of chitosan-encapsulated selenadiazole derivative. "
        "(A) Time-dependent release at different pH values showing maximum release at acidic pH 5.4. "
        "(B) pH-dependent release profiles at different time points demonstrating pH-responsive behavior. "
        "Data presented as mean ± SEM (n=3).",
        caption_style
    )
    elements.append(caption1)

# Figure 2
elements.append(PageBreak())
elements.append(Paragraph("Figure 2: PI3K/AKT Signaling Pathway", heading_style))
if os.path.exists('figure2_pi3k_akt.png'):
    img2 = Image('figure2_pi3k_akt.png', width=6.5*inch, height=6.5*inch*10/12)
    elements.append(img2)
    caption2 = Paragraph(
        "<b>Figure 2.</b> Expression profiles of PI3K/AKT pathway components. "
        "(A-B) PI3K expression shows time and pH-dependent upregulation, with highest levels at 36h and pH 7.4. "
        "(C-D) AKT1 expression demonstrates similar patterns with maximum expression at neutral to alkaline pH. "
        "Data presented as mean ± SEM (n=3).",
        caption_style
    )
    elements.append(caption2)

# Figure 3
elements.append(PageBreak())
elements.append(Paragraph("Figure 3: Apoptotic Markers", heading_style))
if os.path.exists('figure3_caspases.png'):
    img3 = Image('figure3_caspases.png', width=6.5*inch, height=6.5*inch*10/12)
    elements.append(img3)
    caption3 = Paragraph(
        "<b>Figure 3.</b> Expression of pro-apoptotic caspases. "
        "(A-B) Caspase-3 expression is highest at acidic pH 5.4 and early time points (12h), indicating enhanced apoptosis. "
        "(C-D) Caspase-9 follows similar trends, with maximum expression at pH 5.4 and 12h treatment. "
        "Both markers show inverse correlation with pH. Data presented as mean ± SEM (n=3).",
        caption_style
    )
    elements.append(caption3)

# Figure 4
elements.append(PageBreak())
elements.append(Paragraph("Figure 4: Growth Factors and Tumor Suppressors", heading_style))
if os.path.exists('figure4_growth_factors.png'):
    img4 = Image('figure4_growth_factors.png', width=6.5*inch, height=6.5*inch*10/15)
    elements.append(img4)
    caption4 = Paragraph(
        "<b>Figure 4.</b> Expression profiles of growth regulatory factors. "
        "(A, D) TGF-β expression increases with time at acidic pH but shows complex pH-dependent patterns. "
        "(B, E) FGF2 expression is upregulated at neutral to alkaline pH and increases with time. "
        "(C, F) P53 tumor suppressor shows highest expression at 24h and acidic pH 5.4, correlating with apoptotic activity. "
        "Data presented as mean ± SEM (n=3).",
        caption_style
    )
    elements.append(caption4)

# Figure 5
elements.append(PageBreak())
elements.append(Paragraph("Figure 5: Heatmap Analysis", heading_style))
if os.path.exists('figure5_heatmaps.png'):
    img5 = Image('figure5_heatmaps.png', width=6.5*inch, height=6.5*inch*6/14)
    elements.append(img5)
    caption5 = Paragraph(
        "<b>Figure 5.</b> Comprehensive heatmap analysis. "
        "(A) Normalized expression heatmap across all time-pH conditions showing distinct clustering patterns. "
        "Acidic pH conditions (5.4) show high caspase expression while neutral pH (7.4) shows elevated PI3K/AKT. "
        "(B) Pearson correlation matrix revealing strong negative correlations between apoptotic markers "
        "(Caspase-3, Caspase-9) and survival pathway components (PI3K, AKT1, FGF2).",
        caption_style
    )
    elements.append(caption5)

# Figure 6
elements.append(PageBreak())
elements.append(Paragraph("Figure 6: Comprehensive Dashboard", heading_style))
if os.path.exists('figure6_dashboard.png'):
    img6 = Image('figure6_dashboard.png', width=7*inch, height=7*inch*12/16)
    elements.append(img6)
    caption6 = Paragraph(
        "<b>Figure 6.</b> Integrated dashboard of all measured parameters. "
        "(A) Drug release kinetics, (B-C) PI3K/AKT pathway activation, (D-E) Caspase-mediated apoptosis, "
        "(F) P53 tumor suppressor, (G-H) Growth factor expression (TGF-β, FGF2), and (I) Condition-specific "
        "Caspase-3 expression. The dashboard illustrates coordinated regulation of survival and death pathways "
        "in response to pH and time. Data presented as mean ± SEM (n=3).",
        caption_style
    )
    elements.append(caption6)

# Summary
elements.append(PageBreak())
elements.append(Paragraph("Key Findings", heading_style))
summary_text = """
<b>1. pH-Responsive Drug Release:</b> Maximum drug release (80.8%) occurs at acidic pH 5.4, 
mimicking the tumor microenvironment, with sustained release over 36 hours.<br/><br/>

<b>2. Apoptotic Pathway Activation:</b> Caspase-3 and Caspase-9 expression is significantly 
elevated at acidic pH (5.4), correlating with enhanced drug release and indicating robust 
apoptotic induction.<br/><br/>

<b>3. PI3K/AKT Survival Pathway:</b> PI3K and AKT1 expression increases with time and at 
neutral to alkaline pH, suggesting compensatory survival mechanisms that are suppressed 
under acidic conditions.<br/><br/>

<b>4. P53 Tumor Suppressor:</b> P53 expression peaks at 24h and acidic pH, coordinating 
with caspase activation to promote cell death.<br/><br/>

<b>5. Growth Factor Modulation:</b> FGF2 and TGF-β show pH-dependent regulation, with 
FGF2 upregulation at neutral pH potentially contributing to survival signaling.<br/><br/>

<b>6. Strong Correlations:</b> Negative correlations between apoptotic markers and survival 
pathway components (r < -0.9) indicate antagonistic regulation of cell fate decisions.
"""
elements.append(Paragraph(summary_text, body_style))

# Build PDF
doc.build(elements)

print(f"\nPDF report created successfully: {pdf_filename}")
print(f"Total pages: ~{len([e for e in elements if str(type(e)).find('PageBreak') > -1]) + 1}")
