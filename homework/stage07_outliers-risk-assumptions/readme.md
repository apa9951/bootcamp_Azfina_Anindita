## Purpose
This project focuses on detecting and handling outliers in synthetic financial time series data. Outliers can distort statistical measures and risk assumptions in modeling. The notebook (homework_stage07.ipynb) demonstrates methods to detect, flag, treat, and analyze the effect of outliers, followed by sensitivity analysis.

## Feature
1. Data Generation
- Synthetic business-day time series (Jan–Jun 2022).
- Column daily_return: simulated normal distribution with small negative drift before May, and injected “shock” values in May (large positive and negative jumps).
- Column daily_return_2: correlated with daily_return plus Gaussian noise.
- Data saved to data/raw/outliers_homework.csv.

2. Output Detection
- Two methods were implemented (IQR Method and Z Score Method)
- The notebook flags outliers in both daily_return and daily_return_2, counts them, and extracts rows for inspection.

3. Outlier Treatment (Winsorization)
- Function winsorize_series(series, lower=0.05, upper=0.95) clips values below the 5th percentile and above the 95th percentile.
- Applied to both return series to reduce the influence of extreme shocks while keeping dataset size constant.

4. Visualization
- Boxplot to visualize outliers relative to quartiles.
- Histogram to show distribution shape before treatment.

5. Sensitivity Analysis
To assess the effect of outliers:
- Compared mean, median, std before and after outlier removal/winsorization.
- Results showed (1) Medians remained stable (robust to outliers); (2) Means shifted closer to medians after winsorization; (3) Standard deviations decreased significantly (≈67–74%), reducing volatility.

6. Results
- Outliers were detected in both return columns using IQR and Z-score.
- Winsorization effectively dampened shocks without deleting data.
- Sensitivity analysis confirmed that outliers inflated variance, and trimming them gave more robust central estimates.

## Folder Structured
1. Code and Readme on base folder
2. Data Raw in Data/Raw Folder
3. Histogram, Boxplot, and Sensitivy Analysis in Data/Processed Folder


## Assumption for Data Cleansing
1. Daily returns can be modeled as Gaussian with occasional extreme shocks.
2. IQR is robust for skewed data; Z-score assumes approximate normality.
3. Winsorization thresholds (5% and 95%) are sufficient to mitigate extremes without over-censoring.
4. Visualizations provide intuitive support for the statistical findings.