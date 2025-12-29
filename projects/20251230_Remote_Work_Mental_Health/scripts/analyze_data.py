import pandas as pd

# Load data
try:
    df = pd.read_csv('dataset.csv')
    print("### Data Info")
    print(df.info())
    print("\n### First 5 Rows")
    print(df.head())
    print("\n### Missing Values")
    print(df.isnull().sum())
    print("\n### Describe")
    print(df.describe(include='all'))
except Exception as e:
    print(f"Error loading data: {e}")
