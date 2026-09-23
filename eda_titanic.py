"""
Task 2: Exploratory Data Analysis - Titanic Passenger Dataset
Uses the cleaned dataset produced in Task 1 (titanic_cleaned.csv).
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 110

# ----------------------------------------------------------------------
# 1. LOAD CLEANED DATA
# ----------------------------------------------------------------------
df = pd.read_csv("titanic_cleaned.csv")
print("Shape:", df.shape)
print(df.describe(include="all"))

insights = []

# ----------------------------------------------------------------------
# 2. KEY STATISTICS
# ----------------------------------------------------------------------
overall_survival_rate = df["Survived"].mean()
print(f"\nOverall survival rate: {overall_survival_rate:.2%}")

survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_sex = df.groupby("Sex")["Survived"].mean()
survival_by_embarked = df.groupby("Embarked")["Survived"].mean()
avg_fare_by_class = df.groupby("Pclass")["Fare"].mean()
avg_age_by_survival = df.groupby("Survived")["Age"].mean()
corr_matrix = df[["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]].corr()

print("\nSurvival rate by class:\n", survival_by_class)
print("\nSurvival rate by sex:\n", survival_by_sex)
print("\nSurvival rate by embarkation port:\n", survival_by_embarked)
print("\nAverage fare by class:\n", avg_fare_by_class)
print("\nAverage age by survival:\n", avg_age_by_survival)
print("\nCorrelation matrix:\n", corr_matrix)

# ----------------------------------------------------------------------
# 3. CHART 1 - Survival rate by passenger class
# ----------------------------------------------------------------------
plt.figure(figsize=(6, 4))
survival_by_class.plot(kind="bar", color=["#4C72B0", "#55A868", "#C44E52"])
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart1_survival_by_class.png")
plt.close()

# ----------------------------------------------------------------------
# 4. CHART 2 - Survival rate by sex
# ----------------------------------------------------------------------
plt.figure(figsize=(6, 4))
survival_by_sex.plot(kind="bar", color=["#DD8452", "#4C72B0"])
plt.title("Survival Rate by Sex")
plt.xlabel("Sex")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart2_survival_by_sex.png")
plt.close()

# ----------------------------------------------------------------------
# 5. CHART 3 - Age distribution by survival
# ----------------------------------------------------------------------
plt.figure(figsize=(7, 4))
sns.histplot(data=df, x="Age", hue="Survived", multiple="stack", bins=20, palette=["#C44E52", "#55A868"])
plt.title("Age Distribution by Survival Outcome")
plt.xlabel("Age")
plt.ylabel("Passenger Count")
plt.tight_layout()
plt.savefig("chart3_age_distribution.png")
plt.close()

# ----------------------------------------------------------------------
# 6. CHART 4 - Fare distribution by class (boxplot)
# ----------------------------------------------------------------------
plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="Pclass", y="Fare", palette="Set2")
plt.title("Fare Distribution by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")
plt.tight_layout()
plt.savefig("chart4_fare_by_class.png")
plt.close()

# ----------------------------------------------------------------------
# 7. CHART 5 - Correlation heatmap
# ----------------------------------------------------------------------
plt.figure(figsize=(6, 5))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Numeric Features")
plt.tight_layout()
plt.savefig("chart5_correlation_heatmap.png")
plt.close()

# ----------------------------------------------------------------------
# 8. CHART 6 - Survival by HasCabinRecord (bonus)
# ----------------------------------------------------------------------
survival_by_cabin_flag = df.groupby("HasCabinRecord")["Survived"].mean()
plt.figure(figsize=(6, 4))
survival_by_cabin_flag.plot(kind="bar", color=["#8172B2", "#64B5CD"])
plt.title("Survival Rate: Has Cabin Record vs Not")
plt.xlabel("Has Cabin Record")
plt.ylabel("Survival Rate")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart6_survival_by_cabin_flag.png")
plt.close()

print("\nAll charts saved.")

# ----------------------------------------------------------------------
# 9. WRITE INSIGHTS TO FILE
# ----------------------------------------------------------------------
insights_text = f"""
EXPLORATORY DATA ANALYSIS - KEY INSIGHTS
Titanic Passenger Dataset (cleaned, n={len(df)})
{"=" * 55}

1. Overall survival rate was {overall_survival_rate:.1%}, but this varied
   sharply by passenger class: 1st class passengers survived at
   {survival_by_class[1]:.1%}, compared to only {survival_by_class[3]:.1%}
   for 3rd class. Wealth/class was strongly tied to survival chances.

2. Sex was the single strongest predictor of survival: women survived at
   {survival_by_sex['female']:.1%} versus just {survival_by_sex['male']:.1%}
   for men, consistent with the historical "women and children first"
   evacuation policy.

3. Survivors were on average younger than non-survivors
   ({avg_age_by_survival[1]:.1f} years vs {avg_age_by_survival[0]:.1f} years),
   suggesting children and younger passengers had a survival edge over
   older passengers.

4. Fare correlated with class as expected -- 1st class passengers paid
   roughly {avg_fare_by_class[1]:.0f} on average vs {avg_fare_by_class[3]:.0f}
   for 3rd class -- and higher fares were positively correlated with
   survival, reinforcing the class-based survival gap.

5. Passengers with a recorded cabin number survived at
   {survival_by_cabin_flag[True]:.1%} compared to {survival_by_cabin_flag[False]:.1%}
   for those without one. Since cabin records are far more common
   among 1st/2nd class tickets, this is another proxy signal for the
   class effect on survival, rather than an independent cause.

6. The correlation heatmap shows Pclass has a meaningful negative
   correlation with Survived, meaning lower-numbered (better) classes
   were associated with higher survival, matching the patterns already
   observed in the class breakdown above.

Overall, the analysis shows survival on the Titanic was driven mainly by
a combination of sex, passenger class, and age, with fare and cabin
records acting as secondary indicators of the same underlying class effect.
"""

with open("eda_insights.txt", "w") as f:
    f.write(insights_text)

print(insights_text)
print("Saved: eda_insights.txt")
