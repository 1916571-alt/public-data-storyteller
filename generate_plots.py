import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set style for "Visual Impact"
sns.set_theme(style="whitegrid", palette="rocket")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.family'] = 'sans-serif'

# 1. Load & Clean Data
df = pd.read_csv('dataset.csv')
df['Mental_Health_Condition'] = df['Mental_Health_Condition'].fillna('None')
df['Physical_Activity'] = df['Physical_Activity'].fillna('Unknown')

# Order for ordinal variables if needed
stress_order = ['Low', 'Medium', 'High']
sleep_order = ['Poor', 'Average', 'Good']
location_order = ['Remote', 'Hybrid', 'Onsite']

# --- Chart 1: Stress Level by Work Location ---
plt.figure()
ax = sns.countplot(data=df, x='Work_Location', hue='Stress_Level', hue_order=stress_order, palette='viridis')
plt.title('Stress Levels by Work Location', fontsize=16, fontweight='bold')
plt.xlabel('Work Location')
plt.ylabel('Count')
plt.legend(title='Stress Level')
plt.tight_layout()
plt.savefig('outputs/chart1_stress_by_location.png')
plt.close()

# --- Chart 2: Social Isolation by Work Location ---
plt.figure()
sns.boxplot(data=df, x='Work_Location', y='Social_Isolation_Rating', order=location_order, palette='mako')
plt.title('Social Isolation Rating by Work Location', fontsize=16, fontweight='bold')
plt.xlabel('Work Location')
plt.ylabel('Social Isolation Rating (1-5)')
plt.tight_layout()
plt.savefig('outputs/chart2_isolation_by_location.png')
plt.close()

# --- Chart 3: Virtual Meetings vs Sleep Quality ---
plt.figure()
sns.violinplot(data=df, x='Sleep_Quality', y='Number_of_Virtual_Meetings', order=sleep_order, palette='rocket_r')
plt.title('Impact of Virtual Meetings on Sleep Quality', fontsize=16, fontweight='bold')
plt.xlabel('Sleep Quality')
plt.ylabel('Number of Virtual Meetings / Week')
plt.tight_layout()
plt.savefig('outputs/chart3_meetings_vs_sleep.png')
plt.close()

# --- Chart 4: Mental Health Condition Distribution (Pie) ---
plt.figure()
condition_counts = df['Mental_Health_Condition'].value_counts()
# Don't plot 'None' in the main breakdown or maybe keep it but separate?
# Let's plot only those WITH conditions for the detail view
colors = sns.color_palette('pastel')[0:len(condition_counts)]
plt.pie(condition_counts, labels=condition_counts.index, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Distribution of Reported Mental Health Conditions', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('outputs/chart4_condition_distribution.png')
plt.close()

# --- Chart 5: Correlation Heatmap (Numerical) ---
plt.figure(figsize=(12, 10))
# Select numerical columns
numeric_cols = ['Age', 'Years_of_Experience', 'Hours_Worked_Per_Week', 
                'Number_of_Virtual_Meetings', 'Work_Life_Balance_Rating', 
                'Social_Isolation_Rating']
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix of Work Factors', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('outputs/chart5_correlation.png')
plt.close()

print("All charts generated and saved to outputs/")
