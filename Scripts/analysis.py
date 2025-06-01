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

def load_data():
    """Load and prepare the data with robust error handling"""
    print("=== Loading Data ===")
    file_path = r"C:\Users\kuziv\OneDrive\Робочий стіл\Project\Data\processed_data.csv"
    
    try:
        # First attempt to read the file
        temp_df = pd.read_csv(file_path)
        print("Found columns:", temp_df.columns.tolist())
        
        # Try to identify a date column
        date_col = None
        for col in temp_df.columns:
            if 'date' in col.lower():
                date_col = col
                break
        
        # If no date column found but data has sequential index
        if date_col is None:
            print("No date column found - using sequential index")
            data = temp_df.copy()
            data.index = pd.RangeIndex(start=0, stop=len(data))
        else:
            print(f"Using '{date_col}' as date column")
            data = pd.read_csv(file_path, parse_dates=[date_col], index_col=date_col)
            data.index.name = 'Date'  # Standardize name
        
        # Validate required columns
        required_cols = ['EURPLN', 'WIG20']
        missing_cols = [col for col in required_cols if col not in data.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        print("\nData loaded successfully:")
        print(f"Time range: {data.index[0]} to {data.index[-1]}" if hasattr(data.index, 'dtype') else "No datetime index")
        print(f"Shape: {data.shape}")
        
        return data
    
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at: {file_path}")
    except Exception as e:
        raise Exception(f"Error loading data: {str(e)}")

def plot_time_series(data):
    """Plot time series with safe column checking"""
    print("\n=== Time Series Visualization ===")
    
    plots_config = [
        ('EURPLN', 'EUR/PLN Exchange Rate', 'Rate'),
        ('WIG20', 'WIG20 Index', 'Index Value'),
        ('EURPLN_Daily_Change', 'EUR/PLN Daily Changes', '% Change'),
        ('WIG20_Daily_Change', 'WIG20 Daily Changes', '% Change'),
        ('EURPLN_30d_MA', 'EUR/PLN 30-day MA', 'Rate'),
        ('WIG20_30d_Volatility', 'WIG20 30-day Volatility', 'Volatility')
    ]
    
    fig, axes = plt.subplots(3, 2, figsize=(15, 12))
    
    for ax, (col, title, ylabel) in zip(axes.flat, plots_config):
        try:
            if col in data.columns:
                data[col].plot(ax=ax, title=title)
                ax.set_ylabel(ylabel)
            else:
                ax.set_title(f"{title} (Data Missing)")
                ax.text(0.5, 0.5, 'No Data', ha='center', va='center')
        except Exception as e:
            ax.set_title(f"Error plotting {col}")
            ax.text(0.5, 0.5, str(e), ha='center', va='center')
    
    plt.tight_layout()
    plt.show()

def analyze_correlations(data):
    """Safe correlation analysis"""
    print("\n=== Correlation Analysis ===")
    
    try:
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) < 2:
            print("Insufficient numeric columns for correlation")
            return
        
        corr_matrix = data[numeric_cols].corr()
        print("\nCorrelation Matrix:")
        print(corr_matrix)
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
                   mask=np.triu(np.ones_like(corr_matrix, dtype=bool)))
        plt.title('Correlation Heatmap (Lower Triangle)')
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Correlation analysis failed: {str(e)}")

def time_series_decomposition(data):
    """Robust time series decomposition"""
    print("\n=== Time Series Decomposition ===")
    
    def safe_decompose(series, title, period=30):
        try:
            if len(series.dropna()) < 2*period:
                print(f"Not enough data for {title} decomposition")
                return
                
            result = seasonal_decompose(series.dropna(), period=period)
            fig = result.plot()
            fig.set_size_inches(12, 8)
            fig.suptitle(title)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Failed to decompose {title}: {str(e)}")
    
    for col in ['EURPLN', 'WIG20']:
        if col in data.columns:
            safe_decompose(data[col], f'{col} Decomposition')

def perform_statistical_tests(data):
    """Safe statistical testing"""
    print("\n=== Statistical Tests ===")
    
    # Normality tests
    for col in ['EURPLN_Daily_Change', 'WIG20_Daily_Change']:
        if col in data.columns:
            print(f"\nNormality test for {col}:")
            try:
                stat, p = stats.shapiro(data[col].dropna())
                print(f"Shapiro-Wilk: stat={stat:.4f}, p={p:.4f}")
                print("Normal" if p > 0.05 else "Non-normal")
            except Exception as e:
                print(f"Normality test failed: {str(e)}")
    
    # Stationarity tests
    for col in ['EURPLN', 'WIG20']:
        if col in data.columns:
            print(f"\nStationarity test for {col}:")
            try:
                result = sm.tsa.adfuller(data[col].dropna())
                print(f"ADF Statistic: {result[0]:.4f}")
                print(f"p-value: {result[1]:.4f}")
                print("Critical Values:")
                for key, val in result[4].items():
                    print(f"\t{key}: {val:.4f}")
                print("Stationary" if result[1] < 0.05 else "Non-stationary")
            except Exception as e:
                print(f"Stationarity test failed: {str(e)}")

def linear_regression_analysis(data):
    """Safe regression analysis"""
    print("\n=== Linear Regression Analysis ===")
    
    if 'WIG20' not in data.columns or 'EURPLN' not in data.columns:
        print("Missing required columns for regression")
        return
    
    try:
        # Prepare data
        valid_data = data[['WIG20', 'EURPLN']].dropna()
        if len(valid_data) < 10:
            raise ValueError("Insufficient data points for regression")
            
        X = sm.add_constant(valid_data['WIG20'])
        y = valid_data['EURPLN']
        
        # Fit model
        model = sm.OLS(y, X).fit()
        print(model.summary())
        
        # Plot results
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        sns.regplot(x='WIG20', y='EURPLN', data=valid_data, 
                   ax=ax1, line_kws={'color': 'red'})
        ax1.set_title('Regression Plot')
        
        residuals = model.resid
        sns.histplot(residuals, kde=True, ax=ax2)
        ax2.set_title('Residuals Distribution')
        
        plt.tight_layout()
        plt.show()
        
    except Exception as e:
        print(f"Regression analysis failed: {str(e)}")

def main():
    """Main analysis workflow with error handling"""
    try:
        print("=== Starting Analysis ===")
        data = load_data()
        
        plot_time_series(data)
        analyze_correlations(data)
        time_series_decomposition(data)
        perform_statistical_tests(data)
        linear_regression_analysis(data)
        
        print("\n=== Analysis Completed Successfully ===")
        
    except Exception as e:
        print(f"\n!!! Analysis Failed !!!")
        print(f"Error: {str(e)}")
        print("Possible solutions:")
        print("- Check file path and permissions")
        print("- Verify required columns exist")
        print("- Ensure sufficient data points")
        print("- Check for NaN/infinite values")

if __name__ == "__main__":
    main()