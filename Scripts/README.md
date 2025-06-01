# EUR/PLN and WIG20 Data Analysis Project

This project downloads historical data for EUR/PLN currency pair and WIG20 stock index, processes it by calculating daily changes and technical indicators, and performs correlation analysis with visualization.

## Files

- `download_and_process.py` — downloads data from Yahoo Finance, processes it, and saves the cleaned dataset as CSV.
- `analysis.py` — loads the processed data, performs correlation analysis, and visualizes the results using plots.
- `requirements.txt` — lists Python dependencies required for the project.

## Setup

1. Clone the repository or download the files.  
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the data download and processing script:

```bash
python download_and_process.py
```

2. Run the analysis script to generate correlation plots:

```bash
python analysis.py
```

## Output

Processed data is saved in the `Data/processed_data.csv` file. Correlation heatmap and scatter plots will be displayed during analysis.

## Notes

Make sure you have an internet connection when downloading data. The project uses Yahoo Finance API via `yfinance` library.
