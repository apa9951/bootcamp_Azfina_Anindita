# Titanic Survival Prediction

## 1. Purpose
This project uses machine learning to predict passenger survival on the Titanic shipwreck, based on demographic and travel data. It was developed for the **NYU Bootcamp** and follows the classic [Kaggle Titanic competition](https://www.kaggle.com/competitions/titanic).

## 2. Features / Steps
- Load datasets from Kaggle and seaborn
- Data cleaning:
  - Handle missing values
  - Drop redundant features
  - Encode categorical variables
- Feature scaling with `StandardScaler`
- Model training with `RandomForestClassifier`
- Model evaluation using confusion matrix

## 3. Results
- RandomForestClassifier achieves strong performance in predicting survival.
- Confusion matrix shows a balanced ability to classify both survivors and non-survivors.

## 4. Assumptions
- Dropped or imputed missing data does not introduce bias
- Features selected are representative of survival chances
- Random forest provides a reasonable baseline model
- Training and testing data distributions are consistent

## 5. Folder Structure
- Base folder for Readme
- Notebooks for Results in Kaggle
- Src for source code
- Data for raw, train, and final result of prediction

## 6. Future Works
- Experiment with advanced machine learning models (e.g., Gradient Boosting, XGBoost, LightGBM).
- Perform hyperparameter tuning on RandomForestClassifier to maximize performance.
- Explore more sophisticated feature engineering (e.g., family size, title extraction from names).
- Apply cross-validation for more robust performance estimation.
-	Visualize feature importance to interpret model decisions and identify key survival predictors.
