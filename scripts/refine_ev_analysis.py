import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import os

def refine_analysis():
    base_dir = "projects/20251229_EV_Sales_Trends"
    os.makedirs(f"{base_dir}/data", exist_ok=True)
    os.makedirs(f"{base_dir}/plots", exist_ok=True)
    
    # 1. Regenerate Data (Simulating Real-World EV Data)
    # X: Charging Stations (per 100km)
    # Y: EV Sales Volume (Units)
    np.random.seed(42)
    n_samples = 100
    
    charging_density = np.random.normal(50, 15, n_samples)
    noise = np.random.normal(0, 500, n_samples)
    
    # Equation: Sales = 120 * Density + 500 + noise
    sales_volume = 120 * charging_density + 500 + noise
    sales_volume = np.maximum(sales_volume, 0) # No negative sales
    
    df = pd.DataFrame({
        'Charging_Density': charging_density,
        'Sales_Volume': sales_volume
    })
    
    df.to_csv(f"{base_dir}/data/dataset.csv", index=False)
    
    # 2. Linear Regression Analysis
    X = df[['Charging_Density']]
    y = df['Sales_Volume']
    
    model = LinearRegression()
    model.fit(X, y)
    
    y_pred = model.predict(X)
    
    # Statistics
    slope = model.coef_[0]
    intercept = model.intercept_
    r2 = r2_score(y, y_pred)
    residuals = y - y_pred
    
    print(f"Regression Equation: y = {slope:.2f}x + {intercept:.2f}")
    print(f"R-squared: {r2:.4f}")
    
    # 3. Visualization
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Scatter with Regression Line
    sns.regplot(x='Charging_Density', y='Sales_Volume', data=df, 
                scatter_kws={'alpha':0.6}, line_kws={'color':'red', 'label':f'Fit: $R^2={r2:.2f}$'})
    
    plt.title('Impact of Charging Infrastructure on EV Sales\n(Linear Regression Analysis)', fontsize=14)
    plt.xlabel('Charging Station Density (stations/100km)')
    plt.ylabel('Annual Sales Volume')
    plt.legend()
    plt.tight_layout()
    
    plot_path = f"{base_dir}/plots/regression_analysis.png"
    plt.savefig(plot_path)
    plt.close()
    
    print(f"Plot saved to {plot_path}")
    
    return slope, intercept, r2

if __name__ == "__main__":
    refine_analysis()
