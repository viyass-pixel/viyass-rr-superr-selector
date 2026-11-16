# Rajasthan Royals War Room Dashboard — SupeRR Selector Season 2
> **Theme:** "Who Holds Their Nerve? The Most Reliable Players Under Pressure for the IPL 2027 Auction"  
> **Author:** Viyass Pixel  
> **Live Interactive Dashboard:** [https://viyass-pixel.github.io/viyass-rr-superr-selector/](https://viyass-pixel.github.io/viyass-rr-superr-selector/)

---

## 🎯 Executive Summary & Objective

This repository contains the complete analytics pipeline, data models, Power BI assets, and an interactive web dashboard built for the **Rajasthan Royals Auction War Room** for **SupeRR Selector Season 2**.

Our task is to evaluate high-pressure player performance across domestic and international T20 leagues (2022–2026) using proprietary ball-by-ball match data, diagnose Rajasthan Royals' squad vulnerabilities, and construct an auction recruitment board for the **IPL 2027 Auction**.

---

## 🔬 Methodology: Isolating True Pressure from Noise

Raw pressure statistics (like naive strike rates or averages) suffer from immense sample noise ($\rho = -0.12$ rank repeatability). Our model establishes statistical repeatability ($\rho = +0.29$) through a three-stage pipeline:

1. **Leverage Index (LI) Quantification:**  
   Deliveries are evaluated using gradient-boosted out-of-fold match-state models (Win Prob AUC: **0.89 in chases**, **0.68 in 1st innings**). A ball is flagged as a **Pressure Ball** if it falls in the **top 25% of Leverage Index** ($LI \ge 0.0209$).
   * Pressure balls generate **3.56% win-probability swing per ball** (vs 0.95% on normal balls — **3.8x multiplier**).
   * Wicket hazard spikes by **56%** (1 dismissal every 17 balls).
   * 61% of pressure events occur in 2nd-innings chases.

2. **Run Value over Expectation (RV) & WPA:**  
   Every ball is priced based on remaining run expectancy and win probability added (winsorized $[-12, +8]$ runs).

3. **Empirical-Bayes Shrinkage:**  
   To prevent small samples from dominating the rankings, ratings anchor on true baseline skill with prior strength $K=400$ balls for batters and $K=1,300$ balls for bowlers:
   $$\text{Score} = \text{Base Skill} + \frac{n}{n + 400} \times (\text{Pressure RV} - \text{Base Skill})$$

---

## 🔍 Rajasthan Royals Squad Pressure Diagnostic

Profiling RR's IPL 2024–2026 pressure deliveries reveals the exact franchise strengths and bleeds:

| Segment | RR Value (Runs/Ball) | League Avg | Net Differential | War Room Diagnosis |
| :--- | :---: | :---: | :---: | :--- |
| **Batting: Powerplay (1–6)** | **+0.25** | +0.06 | **+0.19 (Surplus)** | **Elite Strength:** Anchor around Vaibhav Sooryavanshi & Jaiswal. Zero auction capital needed. |
| **Batting: Middle Overs (7–15)** | -0.04 | +0.02 | **-0.06 (Deficit)** | Stagnation when rebuilding; requires middle-order stabiliser. |
| **Batting: Death Overs (16–20)** | -0.11 | -0.01 | **-0.10 (Severe Bleed)** | Finishers collapse under pressure (Hetmyer 90th, Parag 91st, Jadeja 98th). |
| **Bowling: Powerplay (1–6)** | +0.04 | +0.05 | -0.01 (Par) | Stable baseline (Trent Boult & Sandeep Sharma). |
| **Bowling: Spin Attack** | **-0.16** | 0.00 | **-0.16 (Critical Bleed)** | Spin unit bleeds runs (Ravi Bishnoi 138th among 143 bowlers). |
| **Bowling: Death Overs (16–20)** | **-0.06** | **+0.13** | **-0.19 (Critical Bleed)** | RR's biggest gap. Jofra Archer (14th) is isolated without a death partner. |

---

## 📋 The 4-Pillar IPL 2027 Auction Target Board

To solve these exact deficits, RR should allocate its purse toward four specific player targets:

```
+------------------------------------------------------------------------------------------------------+
| 1. DEATH-OVERS PACE PARTNER FOR ARCHER                                                               |
|    • Primary Target: Mustafizur Rahman (₹8.5 Cr | Econ 7.40 | BPW 14.0 | 44% at death | LHB angle)   |
|    • Alternative Target: Nathan Ellis (₹6.5 Cr | Econ 7.78 | Wicket every 14.5 balls)               |
|    • High-Upside Value: Blessing Muzarabani (₹3.0 Cr | Express bounce)                               |
+------------------------------------------------------------------------------------------------------+
| 2. PRESSURE SPIN ENFORCER                                                                            |
|    • Primary Target: Varun Chakravarthy (₹9.5 Cr | Econ 7.37 | 41% dots | Saves Overseas Slot)        |
|    • Marquee (If Released): Rashid Khan (₹16.0 Cr | Dual threat +93 RV chase hitting)                 |
|    • Value Alternate: Noor Ahmad (₹4.5 Cr | +95 RV defending totals)                                 |
+------------------------------------------------------------------------------------------------------+
| 3. CLUTCH DEATH FINISHER / CHASER                                                                    |
|    • Primary Target: Tim David (₹9.0 Cr | SR 185, 205 vs pace | 53% at death | 67% in chases)        |
|    • Value Indian Pick: Ashutosh Sharma (₹3.5 Cr | SR 187, 217 vs pace | 82% at death)               |
|    • Marquee Target: Heinrich Klaasen (₹15.0 Cr | SR 188 vs spin)                                    |
+------------------------------------------------------------------------------------------------------+
| 4. MIDDLE-ORDER STABILISER (NO. 3 / 4)                                                               |
|    • Primary Target: Josh Inglis (₹6.0 Cr | 74% positive innings | SR 185 pace / 180 spin)           |
|    • Free Agent Alternate: Glenn Maxwell (₹7.5 Cr | Tier A pool guarantee | SR 200 at death)         |
+------------------------------------------------------------------------------------------------------+
```

---

## 📂 Repository Structure

```
├── index.html                           # Live Interactive War Room Dashboard (GitHub Pages)
├── RR_War_Room_Dashboard.html           # Standalone Dashboard Application
├── README.md                            # Comprehensive War Room Documentation
├── data/
│   ├── RR_WarRoom_Top_Batters.csv       # Top 12 pressure batters with z-scores & splits
│   ├── RR_WarRoom_Top_Bowlers.csv       # Top 12 pressure bowlers with economy & death stats
│   ├── RR_Squad_Diagnostics.csv         # RR vs League benchmark deficit analysis
│   ├── RR_Auction_Target_Board.csv      # Auction targets, price estimates & verdicts
│   ├── RR_Methodology_Metrics.csv       # Statistical parameters & leverage thresholds
│   ├── Full_Batters_Universe_2022_2026.csv # 413 batters with complete phase splits
│   ├── Full_Bowlers_Universe_2022_2026.csv # 425 bowlers with complete phase economy
│   ├── RajasthanRoyals_WarRoom_Theme.json # Official RR Power BI Theme
│   ├── RR_WarRoom_DAX_Measures.dax      # 20+ DAX measure formulas
│   └── PowerBI_Setup_Guide.md           # Step-by-step 5-page Power BI visual guide
└── generate_powerbi_data.py             # Data transformation & feature engineering script
```

---

## 🚀 How to Enable GitHub Pages

1. Navigate to repository **Settings** > **Pages** in GitHub.
2. Under **Build and deployment** > **Branch**, select `main` and root `/`.
3. Click **Save**.
4. The live dashboard will deploy within 1–2 minutes at:  
   **`https://viyass-pixel.github.io/viyass-rr-superr-selector/`**
