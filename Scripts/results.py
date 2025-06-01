import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.seasonal import STL
from pathlib import Path

data_file = Path(r"C:\Users\kuziv\OneDrive\Робочий стіл\Project\Data\processed_data.csv")

# Load data
df = pd.read_csv(data_file, index_col=0, parse_dates=True)
df = df.dropna(subset=['EURPLN', 'WIG20'])

# Regression of WIG20 on EURPLN
X = sm.add_constant(df['EURPLN'])  # add constant term
y = df['WIG20']

model = sm.OLS(y, X).fit()
print("=== Linear Regression Summary ===")
print(model.summary())

# Time series decomposition for EURPLN
stl_eurpln = STL(df['EURPLN'], seasonal=13)
res_eurpln = stl_eurpln.fit()
print("\n=== EUR/PLN Trend and Seasonality ===")
print(f"Trend head:\n{res_eurpln.trend.head()}")
print(f"Seasonal head:\n{res_eurpln.seasonal.head()}")

# Time series decomposition for WIG20
stl_wig20 = STL(df['WIG20'], seasonal=13)
res_wig20 = stl_wig20.fit()
print("\n=== WIG20 Trend and Seasonality ===")
print(f"Trend head:\n{res_wig20.trend.head()}")
print(f"Seasonal head:\n{res_wig20.seasonal.head()}")

