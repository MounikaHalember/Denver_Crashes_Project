# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 12:38:18 2025

@author: mouni
"""

# 📦 Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 📁 Load data
df = pd.read_csv("C:\\Users\\mouni\\OneDrive\\Documents\\CU denver\\Independent Study\\ODC_TRANS_HIN_L_-3816087389854757363.csv")

# 📊 Summary by Tier
print("\n--- Summary Statistics by Tier ---")
tier_summary = df.groupby("Tier")["CrashRate"].describe()
print(tier_summary)

# 🔝 Top 10 Streets by Crash Rate
print("\n--- Top 10 Streets by Crash Rate ---")
top_10_streets = df.sort_values(by="CrashRate", ascending=False).head(10)
print(top_10_streets[["Street Name", "CrashRate", "Tier", "Shape__Length"]])

# 📈 Boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Tier", y="CrashRate", palette="Set2")
plt.title("Crash Rate Distribution by Tier", fontsize=14)
plt.xlabel("Tier")
plt.ylabel("Crash Rate")
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# 📐 Statistical Testing
tier_1 = df[df["Tier"] == 1]["CrashRate"]
tier_2 = df[df["Tier"] == 2]["CrashRate"]

# ANOVA
anova = stats.f_oneway(tier_1, tier_2)
print("\n--- ANOVA Test ---")
print(f"F-statistic: {anova.statistic:.2f}")
print(f"p-value: {anova.pvalue:.4e}")
if anova.pvalue < 0.05:
    print("✅ Significant difference in crash rates between Tier 1 and Tier 2.")
else:
    print("❌ No significant difference found.")

# Welch's T-Test
t_test = stats.ttest_ind(tier_1, tier_2, equal_var=False)
print("\n--- Welch's T-Test (unequal variances) ---")
print(f"T-statistic: {t_test.statistic:.2f}")
print(f"p-value: {t_test.pvalue:.4e}")
if t_test.pvalue < 0.05:
    print("✅ Crash rate difference is statistically significant.")
else:
    print("❌ No significant difference found.")
    
# Get top 10 streets by crash rate
top_10_crash_streets = df.sort_values(by="CrashRate", ascending=False).head(10)

# Print results
print("🚨 Top 10 Streets by Crash Rate:")
for i, row in top_10_crash_streets.iterrows():
    print(f"{i+1}. {row['Street Name']} - Crash Rate: {row['CrashRate']:.2f}")
    

# Correlation Test
corr_coefficient, p_value = stats.pearsonr(df["Shape__Length"], df["CrashRate"])
print(f"Pearson Correlation Coefficient: {corr_coefficient:.4f}")
print(f"P-Value: {p_value:.4f}")

# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df["Shape__Length"], df["CrashRate"], alpha=0.7)
plt.title("Crash Rate vs Street Length")
plt.xlabel("Street Length (meters)")
plt.ylabel("Crash Rate")
plt.grid(True)
plt.tight_layout()
plt.show()

# Define threshold for short vs long streets (you can adjust threshold)
threshold_length = 1500  # meters

# Create groups
short_streets = df[df["Shape__Length"] <= threshold_length]["CrashRate"]
long_streets = df[df["Shape__Length"] > threshold_length]["CrashRate"]

# Perform Welch's t-test
t_stat, p_val = stats.ttest_ind(short_streets, long_streets, equal_var=False)

print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_val:.4f}")

if p_val < 0.05:
    print("✅ Significant difference between crash rates of short and long streets.")
else:
    print("❌ No significant difference between crash rates of short and long streets.")