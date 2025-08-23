## Purpose
The purpose of this analysis is to explore customer financial behavior using two perspectives:
1. The relationship between income and spending, to evaluate how customer resources translate into actual consumption.
2. The 3-month rolling trend in spending, to capture medium-term patterns while smoothing short-term fluctuations.
These insights aim to inform both exploratory understanding and potential predictive modeling.

## Feature
### Feature 1: Income vs Spending
1. Created a new feature: spend_income_ratio = spend / income.
2. Plotted the distribution of the ratio using a histogram with KDE to identify typical spending-to-income levels and detect outliers.
3. Interpreted ratio patterns to compare spending behavior across customers regardless of absolute income levels.

### Feature 2: Rolling 3-Month Spend Trend
1. Computed a rolling mean of spending over a 90-day window (spend_3m_trend).
2. Plotted a line chart to visualize the smoothed trajectory of spend over time.
3. Used this feature to highlight medium-term trends and reduce noise from daily fluctuations.

## Folder Structured
1. Readme on base folder
2. Code and Result Charts in Src folder

## Results
1. Income vs Spending: The spend-to-income ratio revealed differences in consumption intensity. Most customers cluster around typical spending levels relative to income, but a minority either underspend or overspend compared to the average, which may indicate distinct behavioral segments.
2. Rolling 3-Month Spending Trend: The smoothed time series line chart exposed the underlying trajectory of customer spending. While raw daily spend showed volatility, the rolling average revealed clearer patterns such as gradual increases or temporary declines, which are critical for trend detection and forecasting.

## Assumption and Risks
1. The dataset is synthetic and may not fully reflect real-world behavior.
2. Spending and income distributions are generated randomly, so real-world seasonality or structural effects may be absent.
3. Rolling averages assume sufficient continuity of daily data; gaps or irregular sampling could bias results.
4. The spend-to-income ratio assumes income is a reliable denominator; in cases where income is missing or unusually small, ratios may be unstable.