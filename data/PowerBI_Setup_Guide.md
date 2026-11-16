# Rajasthan Royals War Room — Power BI Dashboard Setup & Build Guide
**SupeRR Selector Season 2 (Round 1 Submission)**  
*Theme: "Who Holds Their Nerve? Most Reliable Players Under Pressure for IPL 2027 Auction"*

---

## 1. Executive Summary & Dashboard Objective

This dashboard is engineered for the **Rajasthan Royals Auction War Room** to evaluate player reliability under high-pressure domestic and international T20 match states (2022–2026) and execute a surgical recruitment plan at the **IPL 2027 Auction**.

### Core Franchise Questions Solved:
1. **The Pressure Definition**: Which deliveries truly determine match outcomes? (Top 25% Leverage Index; 3.8x win-probability swing per ball).
2. **The Rajasthan Royals Diagnostic**: Where does the current RR squad bleed value under pressure? (Death-overs bowling: `-0.19 runs/ball` deficit; Spin attack under pressure: `-0.16 runs/ball` deficit; Death-overs batting: `-0.10 runs/ball`).
3. **The Recruitment Strategy**: Which specific players possess battle-tested nerve, robust sample size, and high repeatability across independent halves to solve RR's 4 critical squad deficits?

---

## 2. Data Files Prepared in Your Workspace

All necessary CSV datasets and theme files are generated and ready in:  
`c:\Users\viyass\Documents\antigravity\intelligent-nobel\data\`

| File Name | Purpose | Key Columns |
| :--- | :--- | :--- |
| **`RR_WarRoom_Top_Batters.csv`** | Top 12 pressure batters with z-scores, stability, phase & matchup splits | `Rank`, `Player`, `Pressure_Score_Z`, `Pressure_Strike_Rate`, `Balls_Per_Dismissal`, `SR_vs_Pace_Pressure`, `SR_vs_Spin_Pressure`, `RR_Strategic_Fit` |
| **`RR_WarRoom_Top_Bowlers.csv`** | Top 12 pressure bowlers with economy, death share, wicket frequency | `Rank`, `Player`, `Pressure_Score_Z`, `Pressure_Economy`, `Balls_Per_Wicket`, `Dot_Ball_Pct`, `Death_Pressure_Pct`, `RR_Strategic_Fit` |
| **`RR_Squad_Diagnostics.csv`** | RR vs League Benchmark across Powerplay, Middle, Death, Pace, Spin | `Segment`, `Department`, `RR_Value_Per_Ball`, `League_Avg_Value`, `Net_Surplus_Deficit`, `Status`, `Tactical_Action` |
| **`RR_Auction_Target_Board.csv`** | IPL 2027 Auction Targets mapped to 4 tactical needs, tiers & purse | `Strategic_Need`, `Target_Priority`, `Player`, `Slot`, `Est_Auction_Price_Cr`, `Pressure_Score_Z`, `War_Room_Verdict` |
| **`RR_Methodology_Metrics.csv`** | Statistical rigor, sample size, Leverage Index & model parameters | `Metric_Category`, `Metric_Name`, `Value`, `Unit`, `Benchmark`, `Insight` |
| **`Full_Batters_Universe_2022_2026.csv`** | Master table of 413 batters across 804 matches | Full phase splits, Pace/Spin splits, Chase SR |
| **`Full_Bowlers_Universe_2022_2026.csv`** | Master table of 425 bowlers across 804 matches | Full phase economy, dot ball %, death-overs wickets |
| **`RajasthanRoyals_WarRoom_Theme.json`** | Official RR War Room theme (Royal Pink, Royal Blue, Gold, Slate) | Imports colors, fonts, card styles, dark-mode canvas |
| **`RR_WarRoom_DAX_Measures.dax`** | 20+ DAX formulas ready to copy-paste | Batting, bowling, diagnostic & simulation measures |

---

## 3. How to Set Up Power BI in 5 Minutes

### Step 1: Open Power BI & Apply the Rajasthan Royals Theme
1. Open **Power BI Desktop**.
2. Click on the **View** tab in the top ribbon.
3. Click the dropdown arrow on **Themes** -> select **Browse for themes...**.
4. Browse to:  
   `c:\Users\viyass\Documents\antigravity\intelligent-nobel\data\RajasthanRoyals_WarRoom_Theme.json`
5. Click **Open**. Your canvas, charts, and cards are now automatically styled in official Rajasthan Royals branding!

### Step 2: Load the Datasets
1. On the **Home** tab, click **Get Data** -> **Text/CSV**.
2. Select and load each of the 5 key files from the `data\` folder:
   - `RR_WarRoom_Top_Batters.csv`
   - `RR_WarRoom_Top_Bowlers.csv`
   - `RR_Squad_Diagnostics.csv`
   - `RR_Auction_Target_Board.csv`
   - `RR_Methodology_Metrics.csv`
3. *(Optional)* If you want full drilldowns for any of the 400+ domestic & international players, also load `Full_Batters_Universe_2022_2026.csv` and `Full_Bowlers_Universe_2022_2026.csv`.
4. Click **Load**. (Loading takes less than 2 seconds!).

### Step 3: Add the DAX Measures
1. In the Fields pane on the right, right-click on `RR_Squad_Diagnostics` or `RR_WarRoom_Top_Batters` and select **New Measure**.
2. Open `data\RR_WarRoom_DAX_Measures.dax` in any text editor and copy the required measures.

---

## 4. Power BI Page-by-Page Visual Wireframe Guide

We recommend a **5-Page Executive War Room Dashboard Layout**:

```
+-----------------------------------------------------------------------------------------+
| [RR LOGO]  RAJASTHAN ROYALS AUCTION WAR ROOM — SUPERR SELECTOR S2                      |
| Tabs: [1. Executive Overview] [2. RR Squad Audit] [3. Top Batters] [4. Top Bowlers] [5. Auction Board] |
+-----------------------------------------------------------------------------------------+
```

---

### PAGE 1: Executive War Room & Pressure Framework
**Goal:** Prove to RR leadership that you have isolated true pressure from ordinary noise.

#### Recommended Visuals:
1. **Header KPI Cards (Top Row - 4 Cards):**
   - Card 1: `184,944` Deliveries Analyzed (804 Matches, 2022–2026)
   - Card 2: `46,236` Pressure Deliveries (Top 25% Leverage Index)
   - Card 3: `3.56%` Win-Probability Swing / Ball (vs 0.95% ordinary — **3.8x leverage**)
   - Card 4: `5.86%` Wicket Hazard (1 dismissal every 17 balls)
2. **Clustered Column Chart (Middle Left):**
   - *Title:* "How Pressure Truly Separates from Ordinary Play"
   - *X-Axis:* Metric (`Balls Left`, `Wickets Down`, `Chase Win Prob`, `Wicket Rate %`)
   - *Y-Axis:* Value
   - *Legend:* Ordinary Balls vs Pressure Balls
   - *Takeaway:* Pressure balls cut balls remaining by half, double wickets down, and spike required rate to 18.9.
3. **Donut / Stacked Bar (Middle Right):**
   - *Title:* "Pressure Distribution by Match Context"
   - *Data:* 61% Chases (2nd Innings) vs 39% Defending (1st Innings).
4. **Methodology Matrix Table (Bottom):**
   - *Columns:* `Metric_Name`, `Value`, `Benchmark`, `Insight` from `RR_Methodology_Metrics.csv`.
   - Explains the Empirical-Bayes shrinkage ($K=400$ balls for batters, $K=1300$ for bowlers) to eliminate small-sample flukes.

---

### PAGE 2: RR Squad Diagnostic (Where the Royals Bleed)
**Goal:** Pinpoint exact vulnerabilities in the existing Rajasthan Royals squad under pressure.

#### Recommended Visuals:
1. **Tornado / Diverging Bar Chart (Center Stage):**
   - *Title:* "RR Pressure Differential: Value Above/Below League Average (Runs/Ball)"
   - *Y-Axis:* `Segment` (`Batting - Powerplay`, `Batting - Middle`, `Batting - Death`, `Bowling - Death`, `Bowling - Spin`)
   - *X-Axis:* `Net_Surplus_Deficit`
   - *Conditional Color:* Green (`#10B981`) for surplus, Bright Pink/Red (`#EA1A85` / `#EF4444`) for deficit.
   - *Key Insights Visualized:*
     - **Powerplay Batting Surplus:** `+0.19 runs/ball` (Vaibhav Sooryavanshi & Jaiswal dominate!).
     - **Death-Overs Bowling Deficit:** `-0.19 runs/ball` (RR death bowling conceded `-0.06` vs league `+0.13`).
     - **Spin Attack Deficit:** `-0.16 runs/ball` (Ravi Bishnoi ranked 138th among 143 bowlers).
     - **Death-Overs Batting Deficit:** `-0.10 runs/ball` (Hetmyer 90th, Parag 91st, Jadeja 98th).
2. **Key Personnel Status Table (Bottom):**
   - *Table Fields:* `Segment`, `Status`, `Key_Personnel`, `Tactical_Action`.
   - Callout box showing: *"Do not spend auction capital on Powerplay Batters. Funnel 100% of budget into Death Pace, Mystery Spin, and a Proven Finisher."*

---

### PAGE 3: Top Pressure Batters Leaderboard
**Goal:** Present the 10 most reliable batters under pressure and their situational archetypes.

#### Recommended Visuals:
1. **Scatter Plot (Main Visual - Top Left):**
   - *X-Axis:* `Pressure_Strike_Rate` (140 to 220)
   - *Y-Axis:* `Expected_Pressure_RV` (Run Value Added per ball)
   - *Bubble Size:* `Pressure_Balls_Total`
   - *Color Legend:* `Role` (Powerplay Aggressor, Middle Stabiliser, Death Finisher)
   - *Player Labels:* Vaibhav Sooryavanshi, Abhishek Sharma, Josh Inglis, Tim David, Heinrich Klaasen, Ashutosh Sharma.
2. **Leaderboard Matrix Table (Right Half):**
   - *Columns:* `Rank`, `Player`, `Nation`, `Role`, `Pressure_Score_Z`, `Pressure_Strike_Rate`, `Balls_Per_Dismissal`, `Positive_Pressure_Innings_Pct`, `Bootstrap_Top10_Pct`.
   - *Conditional Formatting:* Data bar on `Pressure_Score_Z`, color scale on `Pressure_Strike_Rate`.
3. **Player Archetype Slicer (Top Right):**
   - Slicer by `Role`: All, Powerplay Aggressor, Middle-Order Stabiliser, Death Finisher.
4. **Pace vs Spin Matchup Comparison Bar Chart (Bottom):**
   - Clustered Bar comparing `SR_vs_Pace_Pressure` and `SR_vs_Spin_Pressure` for each top batter.
   - Highlights Harry Brook's spin weakness (118 vs spin) vs Klaasen's spin mastery (188 vs spin).

---

### PAGE 4: Top Pressure Bowlers (Death Pace & Mystery Spin)
**Goal:** Unpack the elite bowlers who restrict scoring and strike when match leverage peaks.

#### Recommended Visuals:
1. **Scatter Plot (Economy vs Strike Ability):**
   - *X-Axis:* `Pressure_Economy` (Lower is better, reverse axis: 6.0 to 8.5)
   - *Y-Axis:* `Balls_Per_Wicket` (Lower is better, reverse axis: 10 to 35)
   - *Bubble Size:* `Pressure_Balls_Total`
   - *Color Legend:* `Bowling_Type` (Pace vs Spin)
   - *Callouts:* Mustafizur Rahman (Econ 7.40, BPW 14), Nathan Ellis (Econ 7.78, BPW 14.5), Kuldeep Yadav (Econ 6.70, BPW 11.1), Sunil Narine (Econ 7.10, BPW 23).
2. **Phase Execution 100% Stacked Bar Chart:**
   - *Y-Axis:* `Player`
   - *X-Axis:* % Breakdown of pressure balls across `Powerplay_Pressure_Pct`, `Middle_Pressure_Pct`, `Death_Pressure_Pct`.
   - Clearly proves Mustafizur (44% death), Bumrah (42% death), and Ellis (39% death) are authentic death specialists.
3. **Leaderboard Table (Bottom Half):**
   - *Columns:* `Rank`, `Player`, `Bowling_Type`, `Pressure_Score_Z`, `Pressure_Economy`, `Balls_Per_Wicket`, `Dot_Ball_Pct`, `Bootstrap_Top10_Pct`, `RR_Strategic_Fit`.

---

### PAGE 5: IPL 2027 Auction War Room Board
**Goal:** Provide the actionable decision tree for the Rajasthan Royals recruitment table.

#### Recommended Visuals:
1. **Tactical Need Cards (Top Row - 4 Action Columns):**
   - **Need 1: Death-Overs Pace Partner for Archer**  
     *Primary:* Mustafizur Rahman (₹8.5 Cr) | *Alternative:* Nathan Ellis (₹6.5 Cr) | *Value:* Blessing Muzarabani (₹3.0 Cr)
   - **Need 2: Pressure Spin Enforcer**  
     *Primary:* Varun Chakravarthy (₹9.5 Cr) | *Alternative:* Noor Ahmad (₹4.5 Cr) | *Marquee:* Rashid Khan (₹16 Cr)
   - **Need 3: Death Finisher / Chaser**  
     *Primary:* Tim David (₹9.0 Cr) | *Value Indian:* Ashutosh Sharma (₹3.5 Cr) | *Marquee:* Heinrich Klaasen (₹15 Cr)
   - **Need 4: Middle-Order Stabiliser**  
     *Primary:* Josh Inglis (₹6.0 Cr) | *Fallback:* Glenn Maxwell (₹7.5 Cr, Tier A free agent)
2. **Interactive Auction Target Matrix (Middle):**
   - *Table Fields:* `Strategic_Need`, `Target_Priority`, `Player`, `Slot`, `Est_Auction_Price_Cr`, `Pressure_Score_Z`, `War_Room_Verdict`.
3. **Hypothetical Purse Gauge / Card (Bottom Right):**
   - Gauge displaying total allocated spend vs purse limit.
   - Example 4-Player Strategy:  
     *Mustafizur (8.5) + Varun Chakravarthy (9.5) + Tim David (9.0) + Josh Inglis (6.0) = ₹33.0 Cr total spend.*

---

## 5. Submission Checklist for SupeRR Selector S2 (Unstop)

When submitting your dashboard entry on Unstop:
1. **Export to PDF:** In Power BI Desktop, go to **File** -> **Export** -> **Export to PDF**. The pages will render into an ultra-high resolution document.
2. **Methodology Justification:** Emphasize that your rankings use **Empirical-Bayes shrinkage**, out-of-fold **Win Probability models**, and **Leverage Index**, eliminating small-sample noise.
3. **Franchise Alignment:** Clearly state how each pick directly counteracts Rajasthan Royals' quantified deficits in death bowling (`-0.19 runs/ball`) and middle spin (`-0.16 runs/ball`).
