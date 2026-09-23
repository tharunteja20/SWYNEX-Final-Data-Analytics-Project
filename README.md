# Final Data Analytics Project — Titanic Survival Case Study

**Internship Project — SWYNEX Technologies**
**Author:** Tharun Teja Errampalli

---

## 1. Problem Statement

The goal of this project was to take a raw, messy public dataset through a
complete analytics workflow — from cleaning, through exploratory analysis,
to a shareable interactive dashboard — and surface clear, business-relevant
insights.

**Business question:** *What factors most influenced whether a Titanic
passenger survived, and how strongly did each factor matter?*

Although the Titanic disaster is historical, the workflow mirrors a common
real-world business scenario: given a raw dataset of individual records
(customers, patients, passengers, transactions), identify quality issues,
clean the data, uncover the drivers of an outcome (survival, churn,
default, conversion), and present findings to non-technical stakeholders
in a way that's easy to explore and trust.

---

## 2. Dataset Information

- **Source:** Titanic passenger manifest — a widely used public dataset for
  data cleaning and analytics practice.
- **Original file:** https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
- **Size used:** 250-passenger extract of the classic 891-row dataset.
- **Columns:** PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch,
  Ticket, Fare, Cabin, Embarked.

---

## 3. Data Cleaning Process (Task 1)

Full code: [`clean_titanic.py`](clean_titanic.py) · Raw data: [`titanic_raw.csv`](titanic_raw.csv) · Cleaned data: [`titanic_cleaned.csv`](titanic_cleaned.csv)

**Issues identified:**
| Issue | Details |
|---|---|
| Missing values | Age missing ~19%, Cabin missing ~81%, Embarked missing 1 row |
| Duplicate records | Checked full-row and PassengerId duplicates — none found |
| Incorrect data types | Survived, Pclass, Sex, Embarked stored as plain numbers/strings instead of categories |
| Inconsistent values | Stray whitespace in text fields; a Fare of 0; inconsistent casing in Sex/Embarked |

**Cleaning steps performed:**
1. Trimmed whitespace from all text columns
2. Checked for and removed exact duplicate rows
3. Imputed missing Age using the median age within each Pclass + Sex group
4. Imputed missing Embarked with the mode (most frequent port)
5. Preserved missing Cabin as a new boolean flag (`HasCabinRecord`) instead of guessing values
6. Converted Survived, Pclass, Sex, Embarked to proper categorical types
7. Standardized casing (lowercase Sex, uppercase Embarked)
8. Removed any rows with invalid negative Fare

---

## 4. Exploratory Analysis (Task 2)

Full code: [`eda_titanic.py`](eda_titanic.py) · Full write-up: [`eda_insights.txt`](eda_insights.txt) · Charts: [`/charts`](charts)

**Key statistics calculated:** overall survival rate, survival rate by class/sex/embarkation port, average fare by class, average age by survival outcome, and a correlation matrix across the numeric features.

**Charts produced:**
| Chart | File |
|---|---|
| Survival rate by class | `charts/chart1_survival_by_class.png` |
| Survival rate by sex | `charts/chart2_survival_by_sex.png` |
| Age distribution by survival | `charts/chart3_age_distribution.png` |
| Fare distribution by class | `charts/chart4_fare_by_class.png` |
| Correlation heatmap | `charts/chart5_correlation_heatmap.png` |
| Survival by cabin record | `charts/chart6_survival_by_cabin_flag.png` |

![Survival by class](charts/chart1_survival_by_class.png)
![Survival by sex](charts/chart2_survival_by_sex.png)

---

## 5. Interactive Dashboard (Task 3)

File: [`dashboard.html`](dashboard.html) — open directly in any browser, or enable GitHub Pages on this repo for a live link.

Built as a self-contained interactive web dashboard (HTML/CSS/JavaScript +
Chart.js), since Power BI/Tableau were not available on the device used.
It includes:
- 4 live KPI cards (passenger count, survival rate, average fare, average age)
- Combinable filters for passenger class, sex, and embarkation port
- 5 interactive charts that recalculate instantly as filters change
- A written insights panel summarizing the key findings below

---

## 6. Key Business Insights

1. **Class determined chances of survival.** 1st class passengers survived
   at ~48%, more than 3rd class passengers at ~28% — an almost 2x gap
   driven purely by ticket class.
2. **Sex was the single strongest predictor.** Women survived at ~71%
   versus just ~15% for men, reflecting the "women and children first"
   evacuation policy.
3. **Younger passengers had a survival edge.** Survivors were on average
   about 4 years younger than non-survivors (24.7 vs 29.1 years).
4. **Fare tracked with both class and survival.** 1st class passengers
   paid roughly 5x the average fare of 3rd class passengers, and higher
   fares correlated with higher survival — reinforcing the class effect.
5. **Cabin record is a proxy for class, not an independent cause.**
   Passengers with a recorded cabin survived at ~58% vs ~29% without one,
   but this is best explained by cabin records being far more common on
   higher-class tickets.
6. **Port of embarkation showed a secondary effect.** Passengers who
   boarded at Cherbourg had a noticeably higher survival rate, plausibly
   linked to a higher proportion of 1st class passengers boarding there.

**Bottom line:** Survival on the Titanic was driven mainly by a
combination of sex, passenger class, and age — with fare and cabin
records acting as secondary indicators of that same underlying class
effect, rather than independent factors.

---

## 7. Project Files

```
├── README.md                      ← this case study document
├── titanic_raw.csv                ← original raw dataset
├── titanic_cleaned.csv            ← cleaned dataset (Task 1 output)
├── clean_titanic.py               ← cleaning script (Task 1)
├── eda_titanic.py                 ← exploratory analysis script (Task 2)
├── eda_insights.txt               ← auto-generated analysis summary (Task 2)
├── charts/                        ← 6 analysis charts (Task 2)
└── dashboard.html                 ← interactive dashboard (Task 3)
```

## 8. How to Reproduce

```bash
pip install pandas numpy matplotlib seaborn
python clean_titanic.py     # produces titanic_cleaned.csv
python eda_titanic.py       # produces charts + eda_insights.txt
```
Then open `dashboard.html` in any browser to explore the interactive dashboard.
