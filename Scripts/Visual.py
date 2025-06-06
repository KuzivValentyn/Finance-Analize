import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\kuziv\OneDrive\Робочий стіл\Project\Data\processed_data.csv"
try:
    data = pd.read_csv(file_path, skiprows=2)
    
    data.columns = ['Date', 'EURPLN', 'WIG20', 'Change_EURPLN', 
                   'MA30_EURPLN', 'Change_WIG20', 'Volatility_WIG20']
    
    data['Date'] = pd.to_datetime(data['Date'])
    
    plt.figure(figsize=(14, 7))
    
    plt.subplot(2, 1, 1)  # 2 rows, 1 column, first plot
    plt.plot(data['Date'], data['EURPLN'], 'b-', linewidth=1.5)
    plt.title('EUR/PLN Exchange Rate Over Time')
    plt.ylabel('Exchange Rate')
    plt.grid(True)
    
    plt.subplot(2, 1, 2)  # 2 rows, 1 column, second plot
    plt.plot(data['Date'], data['WIG20'], 'g-', linewidth=1.5)
    plt.title('WIG20 Index Performance')
    plt.ylabel('Index Value')
    plt.xlabel('Date')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
    if 'data' in locals():
        print("\nFirst 5 rows of data:")
        print(data.head())
