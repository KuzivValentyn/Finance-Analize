import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
import warnings

# Configuration
warnings.filterwarnings('ignore')
pd.set_option('display.float_format', '{:.4f}'.format)
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def load_and_clean_data():
    """Load and clean the data with robust error handling"""
    print("=== Loading and Cleaning Data ===")
    file_path = r"C:\Users\kuziv\OneDrive\Робочий стіл\Project\Data\processed_data.csv"
    
    try:
        data = pd.read_csv(file_path)
        print("Found columns:", data.columns.tolist())
        
        # Convert numeric columns (handle string values)
        numeric_cols = ['EURPLN', 'WIG20', 'EURPLN_Daily_Change', 
                       'WIG20_Daily_Change', 'EURPLN_30d_MA', 'WIG20_30d_Volatility']
        
        for col in numeric_cols:
            if col in data.columns:
                data[col] = pd.to_numeric(data[col].astype(str).str.replace(r'[^\d.-]', '', regex=True), 
                                        errors='coerce')
        
        # Handle date if exists
        date_col = next((col for col in data.columns if 'date' in col.lower()), None)
        if date_col:
            data[date_col] = pd.to_datetime(data[date_col], errors='coerce')
            data = data.set_index(date_col).sort_index()
            data.index.name = 'Date'
        
        # Validate required data
        if data[['EURPLN', 'WIG20']].isna().all().any():
            raise ValueError("Required columns contain no valid numeric data")
            
        print(f"\nData loaded successfully. Shape: {data.shape}")
        return data.dropna()
    
    except Exception as e:
        raise Exception(f"Data loading error: {str(e)}")

def plot_time_series(data, cols):
    """Efficient time series plotting"""
    fig, axes = plt.subplots(len(cols)//2 + len(cols)%2, 2, figsize=(15, 5*len(cols)//2))
    axes = axes.flatten()
    
    for ax, col in zip(axes, cols):
        if col in data.columns:
            data[col].plot(ax=ax, title=col)
        else:
            ax.set_title(f"{col} (Missing)")
            ax.text(0.5, 0.5, 'No Data', ha='center', va='center')
    
    plt.tight_layout()
    plt.show()

def analyze_data(data):
    """Perform all analyses on cleaned data"""
    # Time Series Plots
    plot_cols = ['EURPLN', 'WIG20', 'EURPLN_Daily_Change', 
                'WIG20_Daily_Change', 'EURPLN_30d_MA', 'WIG20_30d_Volatility']
    plot_time_series(data, [col for col in plot_cols if col in data.columns])
    
    # Correlation Analysis
    numeric_data = data.select_dtypes(include=[np.number])
    if len(numeric_data.columns) >= 2:
        corr = numeric_data.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', mask=np.triu(corr))
        plt.title('Correlation Matrix')
        plt.show()
    
    # Statistical Tests
    for col in ['EURPLN_Daily_Change', 'WIG20_Daily_Change']:
        if col in data.columns:
            stat, p = stats.shapiro(data[col].dropna())
            print(f"{col} normality: {'Normal' if p > 0.05 else 'Non-normal'} (p={p:.4f})")
    
    # Regression Analysis
    if all(col in data.columns for col in ['EURPLN', 'WIG20']):
        X = sm.add_constant(data['WIG20'])
        y = data['EURPLN']
        model = sm.OLS(y, X).fit()
        
        print("\nRegression Results:")
        print(model.summary().tables[1])
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        sns.regplot(x='WIG20', y='EURPLN', data=data, ax=ax1)
        sns.histplot(model.resid, kde=True, ax=ax2)
        plt.tight_layout()
        plt.show()

def main():
    try:
        data = load_and_clean_data()
        analyze_data(data)
        print("\n=== Analysis Completed Successfully ===")
    except Exception as e:
        print(f"\n!!! Analysis Failed: {str(e)}")

if __name__ == "__main__":
    main()
