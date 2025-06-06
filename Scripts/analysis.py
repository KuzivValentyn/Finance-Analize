import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.seasonal import STL
from pathlib import Path

data_file = Path(r"C:\Users\kuziv\OneDrive\Робочий стіл\Project\Data\processed_data.csv")

try:
    df = pd.read_csv(
        data_file,
        index_col=0,  # Use first column as index
        parse_dates=True,
        date_parser=lambda x: pd.to_datetime(x, errors='coerce')  # Convert to datetime, invalid parsing becomes NaT
    )
    
    df = df[pd.to_datetime(df.index, errors='coerce').notna()]
    
    if isinstance(df.index, pd.DatetimeIndex):
        df = df.asfreq('D')  # Set daily frequency (adjust as needed: 'M' for monthly, 'Q' for quarterly, etc.)
    
    df['EURPLN'] = pd.to_numeric(df['EURPLN'], errors='coerce')
    df['WIG20'] = pd.to_numeric(df['WIG20'], errors='coerce')
    df = df.dropna(subset=['EURPLN', 'WIG20'])

    print("\nDataFrame Info:")
    print(df.head())
    print("\nData Types:")
    print(df.dtypes)
    print("\nIndex Frequency:", df.index.freq)
    
    X = sm.add_constant(df['EURPLN'])  # Add intercept term
    y = df['WIG20']
    model = sm.OLS(y, X).fit()  # Ordinary Least Squares regression
    print("\n=== Linear Regression Summary ===")
    print(model.summary())
    
    try:
        stl_eurpln = STL(df['EURPLN'], period=12)  # 12 for monthly data with yearly seasonality
        res_eurpln = stl_eurpln.fit()
        print("\n=== EUR/PLN Trend and Seasonality ===")
        print(res_eurpln.trend.head())
        
        stl_wig20 = STL(df['WIG20'], period=12)
        res_wig20 = stl_wig20.fit()
        print("\n=== WIG20 Trend and Seasonality ===")
        print(res_wig20.trend.head())
    except Exception as e:
        print("\nError in STL Decomposition:", str(e))

except Exception as e:
    print("Error processing data:", str(e))
