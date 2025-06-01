
# Finance Analysis Project — Extended Documentation

## Project Overview
This project downloads financial market data, processes it, and performs statistical analysis and visualization. The focus is on analyzing the correlation between the EUR/PLN exchange rate and the WIG20 stock index.

---

## Project Structure

```
Finance-Analize/
├── Core Files/
│   ├── download_and_process.py  # Downloads raw data from Yahoo Finance, processes it, and saves cleaned data
│   ├── analysis.py              # Performs statistical correlation analysis on the processed data
│   ├── result.py                # Generates analytical reports and summary statistics
│   └── visual.py                # Creates visualizations (graphs and charts) of the data relationships
├── Data/
│   └── processed_data.csv       # Output file containing cleaned and processed data
├── Reports/
│   ├── figures/                 # Graphs and images
│   └── documents/               # Report files in PDF, DOCX, etc.
├── Config/
│   ├── settings.json            # General project settings
│   └── parameters.yaml          # Project parameters
├── requirements.txt             # Python dependencies
└── README.md                    # Project overview and basic instructions
```

---

## Setup Instructions

1. Clone or download the repository:

```bash
git clone https://github.com/KuzivValentyn/Finance-Analize.git
cd Finance-Analize
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the data download and processing script:

```bash
python Core\download_and_process.py
```

4. Run the statistical analysis:

```bash
python Core\analysis.py
```

5. Generate reports:

```bash
python Core\result.py
```

6. Create visualizations:

```bash
python Core\visual.py
```

---

## Key Features

- Automated data download from Yahoo Finance using the `yfinance` library.
- Data cleaning and processing pipeline to prepare datasets for analysis.
- Statistical correlation and regression analysis between EUR/PLN and WIG20.
- Multiple visualization options including time series plots, heatmaps, and regression scatter plots.
- Automated report generation in user-friendly formats.

---

## Outputs

- Cleaned and processed dataset saved as `Data/processed_data.csv`.
- Statistical reports and summaries stored in `Reports/documents/`.
- Visualizations saved in `Reports/figures/`, including:
  - Time series plots
  - Correlation heatmaps
  - Scatter plots with regression lines
  - Moving average charts

---

## Requirements

- Python 3.8 or higher
- Stable internet connection for data download
- Python packages listed in `requirements.txt`, including but not limited to:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scipy
  - statsmodels
  - yfinance

---

## Usage Workflow

The typical workflow for this project consists of:

1. **Download and process data:**  
   The script `download_and_process.py` fetches historical data for EUR/PLN and WIG20 (2018-2023), cleans it, computes necessary indicators, and saves a unified CSV.

2. **Analyze data:**  
   `analysis.py` performs statistical analyses such as correlation matrices, stationarity tests, and regression.

3. **Generate reports:**  
   `result.py` creates summary statistics and exports detailed reports.

4. **Visualize data:**  
   `visual.py` generates plots and charts that help interpret relationships and trends.

---

## Notes

- Historical data availability depends on Yahoo Finance data coverage.
- The project is modular, so each part can be adapted or expanded independently.
- Detailed logs and error handling ensure traceability during data processing and analysis.

---

## Contact and Contribution

Feel free to open issues or pull requests in the GitHub repository to contribute or report problems.

---

*This document supplements the primary `README.md` and provides an extended guide for users and collaborators.*
