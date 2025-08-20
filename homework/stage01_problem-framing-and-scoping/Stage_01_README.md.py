#Stage01 Problem Framing & Scoping

# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
ndonesia’s economic growth is influenced by various factors, one of which is inflation, typically monitored via the Consumer Price Index. While the CPI captures price changes over time, understanding its nuanced relationship with economic growth trends—regionally and nationally—remains challenging. The problem, then, is:
1. How can data analytics be leveraged to extract actionable insights from Indonesia’s CPI data to inform and enhance economic growth strategies?
2. What specific economic indicators should be analyzed alongside the CPI to provide a more comprehensive view of economic health?

## Stakeholder & User
Stakeholders include:
1. Ministry of Finance 
2. Central Bank
3. Ministry of National Development Planning
4. Business/Industry Associations

User for this project will be:
1. Policy Analysts
2. Government

## Useful Answer & Decision
Predictive analytics can be employed to forecast future economic conditions based on historical CPI data and its relationship with other economic indicators.

## Assumptions & Constraints
1. CPI data (e.g. from BPS/IPOMSI or Bank Indonesia) is timely, sufficiently granular (national and regional), and historically consistent.
2. GDP, employment, consumption, and other macro indicators are available and align temporally with CPI.
3. Stakeholders have ready access to insights or dashboard tools derived from the analytics.
4. CPI is a meaningful predictor of economic changes in Indonesia (e.g. inflation’s impact on consumption and growth is significant).
5. Sufficient local computing infrastructure and analytics capacity exists.

## Known Unknowns / Risks
#Known
1. Historical CPI data (national level) and its broad trends.
2. Strong theoretical link between inflation (CPI) and economic performance.
3. Standard data sources: BPS, Bank Indonesia, World Bank, etc.
4. Basic analytic techniques (e.g., time-series modeling, correlation, regression).

#Unknown
1. Granularity: Are there monthly CPI data per province?
2. Real-time availability: what's the lag time on data releases?
3. Correlation strength: how strongly CPI predicts growth in various regions?
4. Confounding variables: What else (like exchange rates, global prices) significantly impact Indonesia’s CPI-growth dynamics?
5. Stakeholder readiness: What’s their capability to digest the analytics delivered?

#Risks
1. Misleading insights due to poor-quality or incomplete CPI or GDP data.
2. Overfitting models to historical quirks, leading to unreliable forecasts.
3. Delayed insights caused by data lags, reducing policy relevance.
4. Low buy-in if findings contradict established policy or understanding.
5. Data misinterpretation by non-technical stakeholders.

## Lifecycle Mapping
1. Initiation and Scoping: Define problem, stakeholders, and data sources.
2. Data Acquisition: Collect CPI and related economic data.
3. Exploratory Analysis: Analyze historical CPI trends and correlations with economic indicators.
4. Model Development: Build predictive models to forecast economic conditions based on CPI.
5. Visualization and Insights: Create dashboards or reports to communicate findings.
6. Deployment and Monitoring: Implement models in production and monitor performance.
7. Iteration and Maintenance: Continuously improve models and insights based on feedback and new data.

## Repo Plan
/data/, /src/, /notebooks/, /docs/ ; cadence for updates
(TBD)