import pandas as pd
import scipy.stats as stats
import numpy as np

# Load data
df = pd.read_csv('dataset.csv')

# --- Data Cleaning Log & Preprocessing ---
print("### Data Cleaning Log")
initial_rows = len(df)
print(f"- Initial Row Count: {initial_rows}")
print("- Missing Values Handling:")
print(f"  - Mental_Health_Condition: {df['Mental_Health_Condition'].isnull().sum()} missing -> Filled with 'None'")
df['Mental_Health_Condition'] = df['Mental_Health_Condition'].fillna('None')
print(f"  - Physical_Activity: {df['Physical_Activity'].isnull().sum()} missing -> Filled with 'Unknown'")
df['Physical_Activity'] = df['Physical_Activity'].fillna('Unknown')

# --- Statistical Analysis ---
print("\n### Statistical Verification")

# 1. Pearson Correlation: Virtual Meetings vs Sleep Quality
# Mapping ordinal variables to numeric
sleep_map = {'Poor': 1, 'Average': 2, 'Good': 3}
df['Sleep_Score'] = df['Sleep_Quality'].map(sleep_map)

# Check if mapping worked (no NaNs)
if df['Sleep_Score'].isnull().sum() > 0:
    print("Warning: unexpected values in Sleep_Quality")

corr, p_value = stats.pearsonr(df['Number_of_Virtual_Meetings'], df['Sleep_Score'])
print(f"1. Correlation (Meetings vs Sleep Score): Pearson r = {corr:.4f}, p-value = {p_value:.4e}")
if p_value < 0.05:
    print("   -> Statistically SIGNIFICANT negative correlation (as meetings go up, sleep quality goes down).")
else:
    print("   -> Not statistically significant.")

# 2. T-Test: Remote vs Onsite Stress Levels
# Mapping Stress Level
stress_map = {'Low': 1, 'Medium': 2, 'High': 3}
df['Stress_Score'] = df['Stress_Level'].map(stress_map)

remote_stress = df[df['Work_Location'] == 'Remote']['Stress_Score']
onsite_stress = df[df['Work_Location'] == 'Onsite']['Stress_Score']

t_stat, t_p_val = stats.ttest_ind(remote_stress, onsite_stress, equal_var=False) # Welch's t-test
print(f"\n2. T-Test (Remote vs Onsite Stress): t-statistic = {t_stat:.4f}, p-value = {t_p_val:.4e}")
print(f"   - Remote Mean Stress: {remote_stress.mean():.2f}")
print(f"   - Onsite Mean Stress: {onsite_stress.mean():.2f}")
if t_p_val < 0.05:
    print("   -> Statistically SIGNIFICANT difference in stress levels.")
else:
    print("   -> No statistically significant difference observed.")

# --- Data Quality & Bias Check ---
print("\n### Data Bias & Limitations")
print("1. Region Distribution:")
print(df['Region'].value_counts(normalize=True) * 100)
print("\n2. Job Role Distribution (Top 5):")
print(df['Job_Role'].value_counts(normalize=True).head(5) * 100)
print("\n3. Gender Distribution:")
print(df['Gender'].value_counts(normalize=True) * 100)

