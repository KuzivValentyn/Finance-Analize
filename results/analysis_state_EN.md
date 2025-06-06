
# Correlation Analysis between the WIG20 Index and the EUR/PLN Currency Pair

---

# Research Methodology

*Analysis period** Daily data from **2018-02-15**
**Methods used**
  Linear regression (OLS)
  STL decomposition (Seasonal-Trend using LOESS)
  Descriptive statistics

---

##  Linear Regression Results

 **Model**: OLS (Ordinary Least Squares)  
 **Dependent variable** `WIG20`  
 **Independent variable** `EUR/PLN`

| Metric              | Value           |
|---------------------|------------------|
| **R² (R-squared)**  | 0.360            |
| **F-statistic**     | 486.3            |
| **P-value (F)**     | 7.98e-86         |
| **Observations**    | 865              |
| **AIC**             | 11,560           |
| **BIC**             | 11,570           |

---

###  Model Coefficients

| Variable    | Coefficient | Std. Error | t-Statistic | P>|t| | Confidence Interval [0.025, 0.975] |
|-------------|-------------|------------|-------------|-------|-------------------------------|
| const       | 7256.23     | 234.23     | 30.98       | 0.000 | [6796.51, 7715.96]            |
| EURPLN      | -1179.17    | 53.47      | -22.05      | 0.000 | [-1284.12, -1074.22]          |

---

📌 **Interpretation**:  
There is a statistically significant relationship between the EUR/PLN exchange rate and the WIG20 index.  
The negative coefficient (-1179.17) indicates that as the EUR/PLN rate increases, the WIG20 index tends to decrease.
