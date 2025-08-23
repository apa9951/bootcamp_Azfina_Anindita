## Purpose
The purpose of this project is to demonstrate how to apply both time series forecasting (linear regression) and classification (logistic regression) to financial-like return data. The dataset was simulated with trends and noise to mimic realistic stock returns. By building features, training models, and evaluating performance, we establish a baseline for predictive modeling in finance.

## Feature
0. Data Set Creation: Generate synthetic daily returns with sinusoidal trend + random noise. Construct cumulative price series.
1. Feature Engineering
- Lag features (previous returns).
- Rolling mean and rolling standard deviation.
- Momentum (difference between today and yesterday’s price).
2. Split Data
- Forecasting: last 25% as test (time-aware split).
- Classification: predict up/down movement.
3. Forecast Model
- Predict next-day return using Linear Regression.
- Evaluate with RMSE.
4. Classification Model
- Predict whether next return is up (>0) or down (≤0).
- Use Logistic Regression inside a pipeline with StandardScaler.
- Evaluate with accuracy, precision, recall, F1, and confusion matrix.

## Folder Structured
1. Readme on base folder
2. Code in notebook folder
3. Data Raw in data folder

## Results
#### Forecasting (Linear Regression)
1. RMSE: The linear regression model achieved a reasonably low RMSE, indicating predictive power over a naive baseline.
2. Visualization: Predictions followed the general trend of actual returns, though with noise and misses on sudden jumps.

#### Classification (Logistic Regression)
1. Performance: Logistic regression achieved balanced accuracy, precision, recall, and F1 scores above random chance.
2. Confusion Matrix: Demonstrated good separation between up and down days.

## Assumption and Risks
#### Forecasting Model (Linear Regression)
1. Assumes a linear relationship between features and next return.
2. Assumes stationarity (patterns remain stable over time).
3. Assumes homoscedasticity (constant variance of errors).
#### Classification Model (Logistic Regression)
1. Assumes linear relationship between predictors and log-odds of outcome.
2. Assumes independence of observations, which is violated in time series.
3. Assumes past return patterns generalize to future market conditions.

