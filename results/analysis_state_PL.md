
# 📊 Analiza korelacji między indeksem WIG20 a parą walutową EUR/PLN

---

## 🧪 Metodologia badania

- **Okres analizy**: Dane dzienne od **2018-02-15**
- **Zastosowane metody**:
  - 📈 Regresja liniowa (OLS)
  - 📉 Dekompozycja STL (Seasonal-Trend using LOESS)
  - 📊 Statystyki opisowe

---

## 📉 Wyniki regresji liniowej

> **Model**: OLS (Ordinary Least Squares)  
> **Zmienna zależna**: `WIG20`  
> **Zmienna niezależna**: `EUR/PLN`

| Wskaźnik            | Wartość         |
|---------------------|------------------|
| **R² (R-kwadrat)**  | 0.360            |
| **Statystyka F**    | 486.3            |
| **P-wartość (F)**   | 7.98e-86         |
| **Liczba obserwacji** | 865            |
| **AIC**             | 11 560           |
| **BIC**             | 11 570           |

---

### 📌 Współczynniki modelu

| Zmienna     | Współczynnik | Błąd Std. | Statystyka t | P>|t| | Przedział ufności [0.025, 0.975] |
|-------------|--------------|------------|---------------|-------|----------------------------|
| const       | 7256.23      | 234.23     | 30.98         | 0.000 | [6796.51, 7715.96]         |
| EURPLN      | -1179.17     | 53.47      | -22.05        | 0.000 | [-1284.12, -1074.22]       |

---

📌 **Interpretacja**:  
Związek między kursem EUR/PLN a indeksem WIG20 jest statystycznie istotny.  
Negatywny współczynnik (-1179.17) sugeruje, że wzrost kursu EUR/PLN wiąże się ze spadkiem indeksu WIG20.
