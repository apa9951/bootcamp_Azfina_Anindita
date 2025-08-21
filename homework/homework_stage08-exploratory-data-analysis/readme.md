## Purpose
The purpose of this project is to explore and clean a synthetic dataset containing customer demographics, income, transactions, and spending behavior across multiple regions. The analysis aims to generate insights on relationships between variables, identify data quality issues, and prepare the dataset for further predictive modeling.

## Feature
1. Data Generation & Injection: Synthetic data was created with variables such as date, region, age, income, transactions, and spend, along with injected missing values and outliers.
2. Exploratory Analysis: Conducted statistical summaries, correlation checks, and visualizations (time series plots, box plots, scatter plots) to understand key trends and relationships.
3. Data Cleaning: Identified missing values and extreme outliers in income, spend, and transactions; proposed strategies for handling them.
4. Feature Engineering: Suggested derived metrics such as spend-per-transaction, income-to-spend ratio, and rolling averages over time to strengthen downstream models.

## Folder Structured
1. Readme and Code on base folder
2. Result/processed charts in Data folder

## Results
1. Spending and income distributions vary across regions, suggesting region is a strong explanatory feature; 
2. Transactions play a stronger role than income in predicting spend, with a clear interaction effect between the two;
3. Demographic variation in average age by region could be important in real-world applications, even though the synthetic data introduces randomness. 

## Future Work
These findings could provide a foundation for building predictive models and identifying key drivers of customer spending.

## Assumption and Risks
1. The dataset is synthetic, so it may not fully reflect real-world behavior, seasonal effects, or business processes.
2. Age is randomly generated per record rather than fixed per customer, which may distort relationships with spend and transactions.
3. Missing values and outliers were injected artificially, which may differ from how data quality issues occur in practice.
4. Regional and temporal effects may be oversimplified compared to real market dynamics.