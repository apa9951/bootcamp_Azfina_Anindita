## Purpose
The purpose of this analysis is to evaluate whether a baseline linear regression can adequately explain excess asset returns using factor-style predictors (market, size, value, momentum). We also test whether extending the model with a **transformed feature** (`momentum²`) improves model fit and satisfies linear regression assumptions.

## Feature
### Feature 1: Baseline Linear Regression
- Define predictors: `mkt_excess`, `size`, `value`, and `momentum`.  
- Split dataset into training and testing sets (80/20).  
- Fit an ordinary least squares (OLS) regression.  
- Evaluate model performance with **R²** and **RMSE**.  
- Diagnose assumptions using residual plots: residuals vs. fitted, histogram, QQ plot, and lag-1 check.  

### Feature 2: Extended Model with `momentum²`
- Add transformed feature `momentum²` to predictors.  
- Refit OLS regression with the extended feature set.  
- Re-evaluate performance (R² and RMSE).  
- Compare residual diagnostics with the baseline model.  
- Interpret whether the new model corrects violations (especially linearity).  


## Folder Structured
1. Readme on base folder
2. Code and Result Charts in notebooks folder

## Results
- **Baseline model:**  
  - Residuals vs. momentum showed **curvature**, violating linearity.  
  - R² and RMSE were acceptable but left unexplained structure.  
  - Diagnostics revealed mild heteroscedasticity due to noise scaling with market factor.  

- **Model with `momentum²`:**  
  - Higher R² and lower RMSE (both train and test).  
  - Residual plots showed more random scatter, fixing the linearity issue.  
  - Homoscedasticity improved, though some variance heterogeneity remained.  

## Assumption and Risks
1. The dataset is synthetic and may not fully reflect real-world behavior.
2. The dataset could fit linear model (even with curved residual or heteroscedasticity)
3. Residuals showed no autocorrelation; independence holds.  

