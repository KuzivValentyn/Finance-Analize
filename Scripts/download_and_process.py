import yfinance as yf
import pandas as pd
import os

output_file = r"C:\Users\kuziv\Downloads\processed_data.csv"

def download_financial_data():
    """
    Downloads EUR/PLN and WIG20 data from Yahoo Finance
    Returns dictionary with both datasets
    """
    print("Downloading financial data from Yahoo Finance...")
    
    data = {}
    tickers = {
        "EURPLN": "EURPLN=X",
        "WIG20": "^WIG20"
    }
    
    for name, code in tickers.items():
        try:
            df = yf.download(
                code,
                start="2018-01-01",
                end="2023-12-31",
                progress=False
            )
            if not df.empty:
                data[name] = df[['Close']].rename(columns={'Close': name})
                print(f"✓ {name} data downloaded successfully")
            else:
                print(f"✗ No data found for {name}")
        except Exception as e:
            print(f"Error downloading {name}: {str(e)}")
    
    return data

def process_data(raw_data):
    """
    Cleans and merges datasets, adds technical indicators
    Returns processed DataFrame
    """
    print("\nProcessing data...")
    
    merged = pd.concat([raw_data["EURPLN"], raw_data["WIG20"]], axis=1)
    
    cleaned = merged.dropna()
    
 
    cleaned['EURPLN_Daily_Change'] = cleaned['EURPLN'].pct_change() * 100
    cleaned['WIG20_Daily_Change'] = cleaned['WIG20'].pct_change() * 100
    cleaned['EURPLN_30d_MA'] = cleaned['EURPLN'].rolling(30).mean()
    cleaned['WIG20_30d_Volatility'] = cleaned['WIG20_Daily_Change'].rolling(30).std()
    
    final_data = cleaned.dropna()
    print(f"Processing complete. Final dataset has {len(final_data)} records")
    
    return final_data


def save_to_csv(dataframe):
    """
    Saves processed data to CSV in specified folder
    """
    try:
        dataframe.to_csv(output_file, encoding='utf-8-sig')
        print(f"\nData successfully saved to:\n{output_file}")
        print("\nFile contains:")
        print("- EUR/PLN exchange rates (2018-2023)")
        print("- WIG20 index values (2018-2023)")
        print("- Daily changes (%) for both series")
        print("- 30-day moving average (EUR/PLN)")
        print("- 30-day volatility (WIG20)")
    except Exception as e:
        print(f"Error saving file: {str(e)}")


if __name__ == "__main__":
    print("=== Financial Data Processor ===")
    
    raw_data = download_financial_data()
    
    if len(raw_data) == 2:
        processed_data = process_data(raw_data)
        
        save_to_csv(processed_data)
        
        print("\nFirst 5 rows of processed data:")
        print(processed_data.head())
    else:
        print("\nFailed to download complete dataset. Please check your internet connection.")
