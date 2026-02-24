# Reviewer-Critical Discussion Points

## Manuscript Title
**"Selenium nanoparticles, enhanced by kaempferol, mitigate acute kidney injury caused by rhabdomyolysis through antioxidant and anti-inflammatory actions that depend on the NRF2/NF-κB pathway"**

---

## TABLE OF CONTENTS

1. [Title-Level Concerns](#1-title-level-concerns)
2. [Selenium Nanoparticle (SeNP) Characterization Parameters](#2-selenium-nanoparticle-senp-characterization-parameters)
3. [Kaempferol "Enhancement" — Mechanistic Specificity](#3-kaempferol-enhancement--mechanistic-specificity)
4. [Rhabdomyolysis-Induced AKI Model Validity](#4-rhabdomyolysis-induced-aki-model-validity)
5. [NRF2/NF-κB Pathway Dependency Claim](#5-nrf2nf-κb-pathway-dependency-claim)
6. [Antioxidant Parameters — Specific Reviewer Targets](#6-antioxidant-parameters--specific-reviewer-targets)
7. [Anti-Inflammatory Parameters — Specific Reviewer Targets](#7-anti-inflammatory-parameters--specific-reviewer-targets)
8. [Dose–Response and Pharmacokinetic Concerns](#8-doseresponse-and-pharmacokinetic-concerns)
9. [Toxicology and Safety Profile](#9-toxicology-and-safety-profile)
10. [Statistical and Experimental Design Concerns](#10-statistical-and-experimental-design-concerns)
11. [Discussion Section — Structural Weaknesses Reviewers Will Target](#11-discussion-section--structural-weaknesses-reviewers-will-target)
12. [Summary Table of High-Risk Parameters](#12-summary-table-of-high-risk-parameters)

---

## 1. TITLE-LEVEL CONCERNS

### 1.1 Overclaiming in the Title
**Reviewer concern:** The title asserts that the therapeutic effects **"depend on"** the NRF2/NF-κB pathway. This is a strong mechanistic claim that implies pathway necessity (i.e., if you block NRF2 or NF-κB, the protective effect disappears).

**What reviewers will demand:**
- Evidence from **NRF2 knockout animals** or **NRF2 siRNA/shRNA knockdown** experiments showing loss of protection.
- Evidence from **NF-κB pathway inhibition** (e.g., BAY 11-7082, PDTC, or IκBα super-repressor) showing that anti-inflammatory effects are abolished.
- Without these loss-of-function experiments, the word **"depend"** is not justified. Reviewers will insist on changing it to "associated with" or "mediated in part by."

**Recommended language if knockouts are absent:**
> "...through antioxidant and anti-inflammatory actions **involving** the NRF2/NF-κB pathway"

### 1.2 "Enhanced by Kaempferol" — Ambiguity
**Reviewer concern:** Does "enhanced" mean:
- (a) Kaempferol is loaded onto/conjugated with SeNPs (a nanoformulation)?
- (b) Kaempferol is co-administered separately alongside SeNPs (combination therapy)?
- (c) Kaempferol enhances the synthesis/stability of SeNPs (green synthesis capping agent)?

Each interpretation has fundamentally different experimental requirements. Reviewers will demand clarity in the title itself.

---

## 2. SELENIUM NANOPARTICLE (SeNP) CHARACTERIZATION PARAMETERS

This is one of the **most scrutinized areas** in nanomedicine manuscripts. Reviewers (especially those from nanotechnology backgrounds) will be extremely picky about the following:

### 2.1 Particle Size and Polydispersity Index (PDI)
| Parameter | What Reviewers Expect | Common Pitfall |
|-----------|----------------------|----------------|
| Hydrodynamic diameter (DLS) | Report Z-average AND intensity-weighted size distribution | Reporting only Z-average without PDI |
| PDI value | Must be < 0.3 for biological applications; < 0.2 preferred | Not reporting PDI at all |
| TEM/SEM size | Must be reported alongside DLS; discrepancy must be explained | DLS-TEM size mismatch left unexplained |
| Size in biological media | Size in PBS, serum, or cell culture media (protein corona effect) | Only reporting size in water |

**Critical reviewer question:** *"What is the colloidal stability of SeNPs in physiological media over 24–72 hours? Did aggregation occur?"*

### 2.2 Zeta Potential
- Must be measured in the **medium used for biological experiments**, not just deionized water.
- Values between −30 mV and +30 mV suggest instability — reviewers will question long-term colloidal stability.
- If kaempferol is surface-loaded, zeta potential **before and after** loading must be compared.

### 2.3 Kaempferol Loading Efficiency and Release Profile
**If kaempferol is loaded onto SeNPs:**
| Parameter | Reviewer Expectation |
|-----------|---------------------|
| Encapsulation efficiency (EE%) | Must be quantified by UV-Vis or HPLC |
| Drug loading capacity (DLC%) | Must be reported |
| In vitro release profile | At pH 7.4 (physiological) AND pH 5.0–6.5 (inflammatory/lysosomal) |
| Release kinetics model | Fit to Higuchi, Korsmeyer-Peppas, or zero/first-order models |
| Burst release | Must be addressed — is there an initial burst? How much? |

**Reviewer will ask:** *"What percentage of kaempferol is released at the kidney injury site versus systemic circulation? How do you ensure targeted delivery?"*

### 2.4 FTIR / XRD / XPS Confirmation
- **FTIR:** Must show characteristic peaks confirming Se–O bonds and kaempferol functional groups (–OH stretching at ~3300 cm⁻¹, C=O at ~1660 cm⁻¹).
- **XRD:** Must confirm whether SeNPs are amorphous or crystalline (amorphous Se is more bioactive; crystalline Se is less so).
- **XPS:** If claimed, must show Se oxidation state (Se⁰ vs Se⁴⁺ vs Se⁶⁺) — this directly affects toxicity and bioactivity.

### 2.5 Stability Over Time
- Reviewers will ask for stability data at **4°C and 25°C over at least 30 days** (size, PDI, zeta potential changes).
- If lyophilized, reconstitution stability must be shown.

---

## 3. KAEMPFEROL "ENHANCEMENT" — MECHANISTIC SPECIFICITY

### 3.1 Synergy vs. Additivity vs. Independent Action
**This is a major reviewer target.** The title claims kaempferol "enhances" SeNP action. Reviewers will demand:

| Required Evidence | Method |
|-------------------|--------|
| SeNPs alone vs. Kaempferol alone vs. SeNPs + Kaempferol | Full factorial design with all three groups |
| Synergy quantification | Combination Index (CI) analysis using the Chou-Talalay method (CI < 1 = synergy, CI = 1 = additive, CI > 1 = antagonism) |
| Isobologram analysis | For dose-response synergy visualization |

**Without CI analysis, reviewers will reject the "enhancement" claim** and insist it be changed to "combination" or "co-treatment."

### 3.2 Kaempferol's Own NRF2/NF-κB Activity
**Critical issue:** Kaempferol is a well-known NRF2 activator and NF-κB inhibitor **on its own** (extensively published). Reviewers will ask:

> *"How do you distinguish the NRF2/NF-κB effects of kaempferol from those of selenium nanoparticles? Is the pathway activation simply due to kaempferol rather than the nanoparticle formulation?"*

**Required controls:**
- Kaempferol alone → NRF2/NF-κB measurement
- SeNPs alone → NRF2/NF-κB measurement
- SeNPs + Kaempferol → NRF2/NF-κB measurement
- Vehicle control → NRF2/NF-κB measurement

### 3.3 Kaempferol Bioavailability Paradox
Kaempferol has notoriously **poor oral bioavailability** (~2% in rodents). Reviewers will ask:
- *"What is the plasma concentration of kaempferol achieved in your model?"*
- *"Does nanoparticle loading improve kaempferol bioavailability? Show pharmacokinetic data."*
- *"Is the dose of kaempferol used pharmacologically relevant to human translation?"*

---

## 4. RHABDOMYOLYSIS-INDUCED AKI MODEL VALIDITY

### 4.1 Model Induction Method
**Most common model:** Intramuscular glycerol injection (50% v/v, 8–10 mL/kg) into hindlimbs of rats/mice after 24h water deprivation.

**Reviewer checkpoints:**
| Parameter | What Reviewers Will Scrutinize |
|-----------|-------------------------------|
| Glycerol concentration and volume | Must match established protocols (Zager, 1996; Kim et al., 2010) |
| Water deprivation period | 24h is standard; deviation must be justified |
| Time of sacrifice post-induction | 24h is standard for acute phase; 48–72h for progression |
| Bilateral vs. unilateral injection | Bilateral is standard; unilateral reduces severity |

### 4.2 Kidney Function Biomarkers
| Biomarker | Reviewer Expectation | Potential Criticism |
|-----------|---------------------|-------------------|
| Serum creatinine (sCr) | Must be measured by enzymatic method (Jaffe method has interferences with bilirubin, ketones) | Using Jaffe method without acknowledging limitations |
| Blood urea nitrogen (BUN) | Must be reported alongside sCr | Reporting only one marker |
| Serum cystatin C | More sensitive than sCr for early AKI detection | Not including this newer biomarker |
| Urinary KIM-1 | Gold-standard tubular injury biomarker | Absence will be noted by nephrology reviewers |
| Urinary NGAL | Early AKI biomarker | Absence will be noted |
| Urine output | Must be monitored (metabolic cages) | Not reporting oliguria/anuria data |

**High-risk reviewer comment:** *"Serum creatinine alone is insufficient to characterize AKI severity. The authors should include novel AKI biomarkers (KIM-1, NGAL, cystatin C) to strengthen their claims."*

### 4.3 Myoglobin and CK Levels
Since rhabdomyolysis is the cause:
- **Serum creatine kinase (CK):** Must be measured to confirm rhabdomyolysis severity.
- **Serum/urine myoglobin:** Must be quantified — this is the direct nephrotoxin.
- **Myoglobin cast formation:** Histological evidence of intratubular myoglobin casts (PAS staining).

**Reviewer will ask:** *"Did SeNPs reduce myoglobin-induced tubular obstruction, or only downstream inflammation? The mechanism of protection must be clarified."*

### 4.4 Histopathological Scoring
- Must use a **validated, semi-quantitative scoring system** (e.g., Jablonski score for ATN).
- Scoring must be performed by a **blinded pathologist**.
- Must include: tubular necrosis, cast formation, tubular dilation, brush border loss, inflammatory infiltration.
- **H&E alone is insufficient** — reviewers will expect PAS staining (for brush border and basement membrane) and possibly Masson's trichrome (for early fibrosis).

---

## 5. NRF2/NF-κB PATHWAY DEPENDENCY CLAIM

**This is the single most vulnerable claim in the manuscript.** The title states the effects **"depend on"** this pathway, which is a causality claim.

### 5.1 NRF2 Pathway — Required Evidence Hierarchy

| Evidence Level | Method | Strength |
|----------------|--------|----------|
| **Level 1 (Minimum)** | Western blot for NRF2, HO-1, NQO1, GCLC protein expression | Correlational only — insufficient for "dependency" |
| **Level 2** | Nuclear translocation of NRF2 (nuclear/cytoplasmic fractionation + WB, or immunofluorescence) | Shows activation but not dependency |
| **Level 3** | NRF2 ARE-luciferase reporter assay | Shows transcriptional activation |
| **Level 4 (Required for "depend")** | NRF2 knockout mice (Nfe2l2⁻/⁻) OR NRF2 siRNA knockdown showing loss of SeNP protection | Proves dependency |
| **Level 5 (Gold standard)** | NRF2 KO + pharmacological rescue (e.g., with sulforaphane) | Confirms specificity |

**If only Levels 1–3 are provided, reviewers will reject the "dependency" claim.**

### 5.2 NF-κB Pathway — Required Evidence Hierarchy

| Evidence Level | Method | Strength |
|----------------|--------|----------|
| **Level 1 (Minimum)** | Western blot for p-NF-κB p65, IκBα, p-IκBα | Correlational |
| **Level 2** | Nuclear translocation of NF-κB p65 (fractionation or IF) | Shows activation status |
| **Level 3** | NF-κB DNA-binding activity (EMSA or TransAM ELISA) | Shows functional activity |
| **Level 4 (Required for "depend")** | NF-κB inhibitor (BAY 11-7082, PDTC) co-treatment showing that SeNP anti-inflammatory effect is redundant with NF-κB inhibition | Supports dependency |
| **Level 5** | IKKβ conditional knockout in renal tubular cells | Proves tissue-specific dependency |

### 5.3 NRF2–NF-κB Crosstalk — The Elephant in the Room
**Reviewers who are pathway experts will raise this:** NRF2 and NF-κB have well-documented **reciprocal inhibitory crosstalk** (Wardyn et al., 2015; Bellezza et al., 2018):

- NRF2 activation suppresses NF-κB signaling (via HO-1, inhibition of IKK).
- NF-κB activation suppresses NRF2 signaling (via competition for CBP/p300 coactivators, promotion of NRF2 ubiquitination via Keap1).

**Reviewer question:** *"Is the observed NF-κB suppression a direct effect of SeNPs/kaempferol on NF-κB, or is it an indirect consequence of NRF2 activation? The authors must delineate the primary target."*

**Required experiment to address this:**
- NRF2 knockdown/KO → measure NF-κB status → if NF-κB is still suppressed by SeNPs, the effect is NRF2-independent.
- NF-κB inhibition → measure NRF2 status → if NRF2 is still activated by SeNPs, the effect is NF-κB-independent.

---

## 6. ANTIOXIDANT PARAMETERS — SPECIFIC REVIEWER TARGETS

### 6.1 Enzymatic Antioxidants
| Parameter | Assay Method | Reviewer Concern |
|-----------|-------------|-----------------|
| SOD activity | NBT reduction or xanthine oxidase method | Must specify SOD1 (Cu/Zn-SOD) vs SOD2 (Mn-SOD) — they have different subcellular locations and regulation |
| CAT activity | H₂O₂ decomposition (Aebi method) | Must report in appropriate units (U/mg protein) |
| GPx activity | NADPH oxidation coupled assay | **Critical:** Se is a cofactor for GPx. SeNPs may directly increase GPx activity by providing Se substrate — this is NOT an antioxidant "signaling" effect but a nutritional effect. Reviewers will demand this distinction. |
| GR activity | GSSG reduction assay | Often omitted — reviewers may request |

**High-priority reviewer comment on GPx:**
> *"The increase in GPx activity may simply reflect increased selenium bioavailability rather than NRF2-mediated transcriptional upregulation. The authors must measure GPx mRNA (RT-qPCR) to distinguish transcriptional activation from substrate-driven enzymatic enhancement."*

### 6.2 Non-Enzymatic Antioxidants
| Parameter | Method | Reviewer Concern |
|-----------|--------|-----------------|
| GSH / GSSG ratio | DTNB (Ellman's) method or HPLC | Must report RATIO, not just total GSH |
| MDA (lipid peroxidation) | TBARS assay | **Highly criticized assay** — TBARS is non-specific (reacts with sugars, amino acids). Reviewers may demand HPLC-based MDA or 4-HNE measurement or F2-isoprostanes |
| Protein carbonyl | DNPH derivatization | More specific than MDA for oxidative damage |
| 8-OHdG (DNA oxidative damage) | ELISA or immunohistochemistry | Adds strength if included |
| Total antioxidant capacity (TAC) | FRAP, ORAC, or ABTS | Non-specific — reviewers may dismiss |

### 6.3 Reactive Oxygen Species (ROS) Measurement
- **In vivo ROS:** DHE staining on kidney sections (superoxide), or DCFH-DA (general ROS).
- **Reviewer concern:** *"DCFH-DA is not specific for any particular ROS species and is prone to artifactual oxidation. The authors should use more specific probes (MitoSOX for mitochondrial superoxide, Amplex Red for H₂O₂)."*

### 6.4 Selenium Speciation
**This is unique to selenium nanoparticle studies and will be heavily scrutinized:**
- What is the oxidation state of Se in the nanoparticles (Se⁰)?
- Is Se metabolized to selenocysteine (SeCys) or selenomethionine (SeMet) in vivo?
- Tissue selenium levels (ICP-MS) in kidney, liver, and serum must be reported.
- **Reviewer question:** *"What is the selenium tissue distribution? Is there preferential accumulation in the kidney? Without biodistribution data, the claim of kidney-specific protection is weakened."*

---

## 7. ANTI-INFLAMMATORY PARAMETERS — SPECIFIC REVIEWER TARGETS

### 7.1 Cytokine Panel
| Cytokine | Method | Reviewer Expectation |
|----------|--------|---------------------|
| TNF-α | ELISA (serum + kidney tissue) | Must measure both systemic and local levels |
| IL-1β | ELISA | Must also assess **mature IL-1β vs pro-IL-1β** (inflammasome activation) |
| IL-6 | ELISA | Key in rhabdomyolysis-AKI |
| IL-18 | ELISA | Inflammasome-related; important in AKI |
| IL-10 | ELISA | Anti-inflammatory cytokine — shows resolution |
| MCP-1 (CCL2) | ELISA or IHC | Macrophage recruitment marker |

**Reviewer concern:** *"The authors measure only pro-inflammatory cytokines. What about anti-inflammatory mediators (IL-10, TGF-β)? A balanced cytokine profile is needed."*

### 7.2 Inflammasome Activation (NLRP3)
Rhabdomyolysis-AKI involves **NLRP3 inflammasome activation** (Komada et al., 2015). Reviewers will expect:
- NLRP3 protein expression (WB)
- ASC speck formation (IF)
- Caspase-1 activation (cleaved caspase-1 WB)
- Mature IL-1β and IL-18 levels

**Reviewer question:** *"Given the established role of NLRP3 inflammasome in rhabdomyolysis-AKI, why did the authors not investigate inflammasome components? This is a significant omission."*

### 7.3 Immune Cell Infiltration
- **Macrophage infiltration:** CD68 (total macrophages), CD86/iNOS (M1), CD206/Arg-1 (M2) — immunohistochemistry or flow cytometry.
- **Neutrophil infiltration:** MPO activity assay or Ly6G staining.
- **T cell involvement:** CD3, CD4, CD8 staining (less critical in acute phase but may be requested).

**Reviewer concern:** *"The authors claim anti-inflammatory effects but do not characterize the inflammatory infiltrate. Macrophage polarization (M1/M2) data would significantly strengthen the manuscript."*

### 7.4 Ferroptosis Connection
**Emerging and highly relevant:** Rhabdomyolysis-AKI involves **ferroptosis** (iron-dependent cell death from myoglobin-released iron). Selenium is a known **anti-ferroptotic element** (via GPX4).

**Reviewer question (very likely in 2025–2026):**
> *"Given the established role of ferroptosis in rhabdomyolysis-AKI and selenium's role in GPX4-mediated ferroptosis resistance, did the authors investigate ferroptosis markers (GPX4, ACSL4, lipid peroxidation by C11-BODIPY, iron deposition by Prussian blue staining)? This is a critical mechanistic gap."*

**This could be a major revision request.** Addressing ferroptosis would significantly strengthen the manuscript.

---

## 8. DOSE–RESPONSE AND PHARMACOKINETIC CONCERNS

### 8.1 Dose Selection Justification
| Question Reviewers Will Ask | Required Answer |
|-----------------------------|----------------|
| How were SeNP and kaempferol doses selected? | Must cite pilot studies or literature-based dose-finding |
| Was a dose-response curve generated? | At minimum 3 doses of each component |
| What is the selenium dose in mg/kg? | Must be compared to the Recommended Dietary Allowance (RDA) and Tolerable Upper Intake Level (UL) for selenium |
| Is the dose translatable to humans? | Allometric scaling (FDA guidance, Reagan-Shaw et al., 2008) must be discussed |

### 8.2 Treatment Timing (Prophylactic vs. Therapeutic)
**Critical reviewer concern:**
- **Pre-treatment (prophylactic):** If SeNPs were given BEFORE rhabdomyolysis induction, this is clinically irrelevant (you cannot predict rhabdomyolysis).
- **Post-treatment (therapeutic):** Clinically relevant but harder to show efficacy.
- **Concurrent treatment:** Must be clearly stated.

**Reviewer comment:** *"The authors administered SeNPs before injury induction. This prophylactic design limits clinical translatability. Can the authors provide data on post-injury treatment?"*

### 8.3 Route of Administration
- Oral? Intraperitoneal? Intravenous?
- Each route has different bioavailability and biodistribution implications.
- **IV administration** of nanoparticles raises concerns about **complement activation (CARPA)** and **rapid hepatic clearance**.
- **Oral administration** raises concerns about **GI degradation** and **poor absorption** of nanoparticles.

### 8.4 Pharmacokinetics and Biodistribution
**Reviewers will almost certainly request:**
- Plasma selenium concentration–time curve
- Tissue distribution (kidney, liver, spleen, lung) by ICP-MS
- Kidney-to-plasma ratio (to demonstrate renal accumulation)
- Elimination half-life

---

## 9. TOXICOLOGY AND SAFETY PROFILE

### 9.1 Selenium Toxicity Window
Selenium has a **narrow therapeutic index**. The difference between therapeutic and toxic doses is small.

| Parameter | Reviewer Expectation |
|-----------|---------------------|
| Acute toxicity (LD50) | Should be referenced or determined |
| Hepatotoxicity markers | ALT, AST must be measured |
| Selenosis signs | Hair loss, nail brittleness, garlic breath (in animals: weight loss, lethargy) |
| Chronic toxicity | If repeated dosing, must address accumulation |

### 9.2 Nanoparticle-Specific Toxicity
| Concern | Assessment Required |
|---------|-------------------|
| Hemolysis | Hemolysis assay on red blood cells |
| Complement activation | CH50 assay or C3a/C5a ELISA |
| Genotoxicity | Comet assay or micronucleus test |
| Organ toxicity | Histopathology of liver, spleen, lung, heart (not just kidney) |
| Hematological parameters | CBC with differential |

**Reviewer comment:** *"The authors focus exclusively on kidney outcomes but do not report systemic toxicity data. Liver function tests and histopathology of non-target organs are essential for a nanoparticle therapeutic."*

---

## 10. STATISTICAL AND EXPERIMENTAL DESIGN CONCERNS

### 10.1 Sample Size and Power Analysis
- **Was an a priori power analysis performed?** (G*Power or similar)
- **n per group:** Minimum n = 6–8 for in vivo studies; n = 3 is insufficient.
- Reviewers will reject studies with n < 5 per group for in vivo work.

### 10.2 Experimental Groups (Minimum Required)
| Group | Purpose |
|-------|---------|
| 1. Normal control (no intervention) | Baseline |
| 2. Sham control (vehicle only) | Vehicle effects |
| 3. Rhabdomyolysis only (disease model) | Disease baseline |
| 4. Rhabdomyolysis + SeNPs alone | SeNP effect |
| 5. Rhabdomyolysis + Kaempferol alone | Kaempferol effect |
| 6. Rhabdomyolysis + SeNPs-Kaempferol | Combination effect |
| 7. Rhabdomyolysis + Positive control drug | Benchmark (e.g., N-acetylcysteine or deferoxamine) |
| 8. Normal + SeNPs-Kaempferol | Toxicity control in healthy animals |

**Missing any of groups 4, 5, or 7 will be a major reviewer criticism.**

### 10.3 Statistical Tests
| Scenario | Appropriate Test | Common Error |
|----------|-----------------|--------------|
| Multiple group comparison | One-way ANOVA + post-hoc (Tukey or Bonferroni) | Using multiple t-tests without correction |
| Non-normal data | Kruskal-Wallis + Dunn's post-hoc | Assuming normality without testing |
| Histological scores (ordinal) | Non-parametric tests | Using parametric tests on ordinal data |
| Normality testing | Shapiro-Wilk (for n < 50) | Not reporting normality test results |
| Variance homogeneity | Levene's test | Not checking before ANOVA |

### 10.4 Blinding
- Was histological scoring performed **blinded**?
- Were biochemical assays performed **blinded**?
- Lack of blinding statement will be flagged.

### 10.5 Reproducibility
- Were experiments repeated independently?
- Are representative images from Western blots shown with **full-length blots** in supplementary data?
- **Reviewer demand (increasingly common):** *"Please provide uncropped Western blot images as supplementary material."*

---

## 11. DISCUSSION SECTION — STRUCTURAL WEAKNESSES REVIEWERS WILL TARGET

### 11.1 Failure to Address Limitations
Every manuscript must include a **limitations paragraph**. Common omissions:
- Single time-point analysis (only 24h post-injury)
- Lack of pharmacokinetic data
- Prophylactic vs. therapeutic design limitation
- Species-specific differences (rodent vs. human)
- Lack of long-term follow-up (AKI-to-CKD transition)

### 11.2 Failure to Compare with Existing Therapies
- How do SeNPs-Kaempferol compare to **N-acetylcysteine (NAC)**, the most commonly studied antioxidant in rhabdomyolysis-AKI?
- How do they compare to **aggressive IV fluid resuscitation**, the current standard of care?
- **Reviewer comment:** *"The authors do not discuss how their approach compares to current clinical management of rhabdomyolysis-AKI. Without this context, the clinical relevance is unclear."*

### 11.3 Failure to Discuss Clinical Translation
- What is the human equivalent dose?
- What is the proposed route of administration in humans?
- What are the regulatory hurdles for a selenium nanoparticle therapeutic?
- Is there a realistic path to clinical trials?

### 11.4 Over-Interpretation of Correlational Data as Causal
**The most common reviewer criticism in pathway studies:**
> *"The authors show that SeNPs increase NRF2 expression and decrease NF-κB activation. However, correlation does not imply causation. Without loss-of-function experiments, the authors cannot claim that the protective effects 'depend on' these pathways."*

### 11.5 Ignoring Alternative Mechanisms
Rhabdomyolysis-AKI involves multiple pathways beyond NRF2/NF-κB:
- **Ferroptosis** (GPX4, iron overload)
- **Mitochondrial dysfunction** (cytochrome c release, MPTP opening)
- **Endoplasmic reticulum stress** (GRP78, CHOP, ATF4)
- **Autophagy** (LC3, Beclin-1, p62)
- **Apoptosis** (caspase-3, Bax/Bcl-2, TUNEL)
- **Necroptosis** (RIPK1, RIPK3, MLKL)

**Reviewer comment:** *"The authors focus exclusively on NRF2/NF-κB but ignore other well-established cell death pathways in rhabdomyolysis-AKI. At minimum, apoptosis (TUNEL, caspase-3) and ferroptosis (GPX4) should be investigated."*

---

## 12. SUMMARY TABLE OF HIGH-RISK PARAMETERS

| # | Parameter/Claim | Risk Level | Likely Reviewer Action |
|---|----------------|------------|----------------------|
| 1 | "Depend on NRF2/NF-κB" without KO/KD data | 🔴 **CRITICAL** | Major revision or rejection |
| 2 | No synergy analysis (CI) for kaempferol enhancement | 🔴 **CRITICAL** | Demand CI analysis or title change |
| 3 | GPx increase attributed to NRF2 without mRNA data | 🔴 **CRITICAL** | Demand GPx mRNA or retract NRF2 claim for GPx |
| 4 | MDA measured by TBARS only | 🟡 **HIGH** | Request HPLC-MDA or 4-HNE |
| 5 | No ferroptosis investigation | 🟡 **HIGH** | Major revision request (2025–2026 expectation) |
| 6 | No NLRP3 inflammasome data | 🟡 **HIGH** | Major revision request |
| 7 | No biodistribution/PK data | 🟡 **HIGH** | Major revision or limitation acknowledgment |
| 8 | No novel AKI biomarkers (KIM-1, NGAL) | 🟡 **HIGH** | Request additional biomarkers |
| 9 | Prophylactic treatment design only | 🟡 **HIGH** | Question clinical relevance |
| 10 | No positive control drug group | 🟡 **HIGH** | Major experimental design flaw |
| 11 | SeNP characterization incomplete (no stability, no PDI) | 🟠 **MODERATE** | Minor-to-major revision |
| 12 | No blinding statement | 🟠 **MODERATE** | Request blinding confirmation |
| 13 | No uncropped Western blots | 🟠 **MODERATE** | Request supplementary data |
| 14 | No NRF2-NF-κB crosstalk discussion | 🟠 **MODERATE** | Request discussion revision |
| 15 | No hepatotoxicity/systemic toxicity data | 🟠 **MODERATE** | Request safety data |
| 16 | Insufficient sample size (n < 6) | 🟠 **MODERATE** | Question statistical power |
| 17 | No human dose equivalence discussion | 🟢 **LOW-MODERATE** | Request discussion addition |
| 18 | No comparison with standard of care | 🟢 **LOW-MODERATE** | Request discussion addition |

---

## RECOMMENDED PRE-SUBMISSION CHECKLIST

Before submission, ensure the manuscript addresses:

- [ ] NRF2 loss-of-function experiment (KO, KD, or inhibitor ML385)
- [ ] NF-κB inhibitor experiment (BAY 11-7082 or PDTC)
- [ ] Combination Index analysis for synergy claim
- [ ] GPx mRNA expression (not just activity)
- [ ] Complete SeNP characterization (size, PDI, zeta, FTIR, XRD, stability)
- [ ] Kaempferol loading/release profile (if nanoformulation)
- [ ] Biodistribution data (ICP-MS)
- [ ] Novel AKI biomarkers (KIM-1, NGAL)
- [ ] NLRP3 inflammasome markers
- [ ] Ferroptosis markers (GPX4, ACSL4)
- [ ] Apoptosis markers (TUNEL, caspase-3)
- [ ] Macrophage polarization (M1/M2)
- [ ] Hepatotoxicity markers (ALT, AST)
- [ ] Full uncropped Western blots in supplementary
- [ ] Blinding statement
- [ ] Power analysis
- [ ] Positive control drug group
- [ ] Limitations paragraph
- [ ] Clinical translation discussion

---

## KEY REFERENCES REVIEWERS MAY CITE AGAINST THE MANUSCRIPT

1. **Wardyn JD et al. (2015)** — NRF2/NF-κB crosstalk. *Free Radic Biol Med.* (Will be cited to challenge pathway independence claims)
2. **Komada T et al. (2015)** — NLRP3 in rhabdomyolysis-AKI. *J Am Soc Nephrol.* (Will be cited to demand inflammasome data)
3. **Stockwell BR et al. (2017)** — Ferroptosis review. *Cell.* (Will be cited to demand ferroptosis investigation)
4. **Chou TC (2010)** — Combination Index method. *Pharmacol Rev.* (Will be cited to demand synergy analysis)
5. **Reagan-Shaw S et al. (2008)** — Dose translation from animal to human. *FASEB J.* (Will be cited to demand dose translation)
6. **Sies H et al. (2017)** — Oxidative stress concept update. *Annu Rev Biochem.* (Will be cited to challenge non-specific antioxidant assays)
7. **Rayman MP (2012)** — Selenium and human health. *Lancet.* (Will be cited regarding selenium toxicity window)
8. **Friedmann Angeli JP et al. (2014)** — GPX4 and ferroptosis. *Nat Cell Biol.* (Will be cited to connect Se-GPX4-ferroptosis axis)

---

*Document prepared for pre-submission review optimization. Addressing these points proactively will significantly reduce revision cycles and improve acceptance probability.*
