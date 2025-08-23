Purpose
This document explains the design, purpose, and usage of the data cleaning module (cleaning.py) as implemented for the homework project. The goal of the module is to provide a standardized pipeline for handling missing values, normalizing numeric columns, and ensuring consistent column types across the dataset. By applying this pipeline, raw data can be systematically transformed into a processed dataset that is ready for analysis or modeling.

Feature
1. fill_missing_median(df, columns=None)
This function replaces missing numeric values with the median of each respective column. If no column list is provided, the function automatically selects all numeric columns in the dataset. Median imputation was chosen because it is less sensitive to outliers compared to mean imputation.

2. drop_missing(df, columns=None, threshold=None)
This function removes rows with missing values according to user-defined rules. If a column list is provided, rows missing any of those columns are removed. If a threshold is defined, the function keeps only those rows where at least the specified proportion of non-null values is present. In the absence of both parameters, rows with any missing value are dropped.

3. normalize_data(df, columns=None, method='minmax')
This function normalizes numeric columns using one of two available methods:

4. Min–Max scaling, which transforms values to a range between 0 and 1.

5. Standard scaling, which standardizes values into z-scores with mean 0 and standard deviation 1.
If no specific columns are indicated, the function applies normalization to all numeric columns.

6. correct_column_types(df)
This function enforces consistent data types for specific columns:
a. The price column is converted from string format (e.g., "$100") into a numeric float.
b. The date_str column is converted into a proper datetime object, with missing values filled using forward fill followed by backward fill.
c. The category column is standardized by converting text to lowercase, filling missing values with the placeholder "unknown", and casting the column as a categorical type.

Folder Structured
1. Code and Readme on base folder
2. Data Raw and Processed in Data Folder
3. Cleaning.py in src Folder

Assumption for Data Cleansing
1. The data cleaning pipeline is designed under the following assumptions:
2. Numeric columns with missing values should be imputed using the median because it provides robustness against outliers.
3. Rows with excessive missing values (greater than 50%) are not informative and should be removed to preserve data quality.
4. The price column is expected to contain values prefixed with a dollar sign (e.g., "$100"). The cleaning function assumes this formatting and removes the symbol before conversion to float.
5. The date_str column may contain missing values. It is assumed that forward filling followed by backward filling is an acceptable imputation strategy for dates, preserving temporal order.
6. The category column may contain mixed cases or missing values. To maintain consistency, all text values are converted to lowercase and missing entries are replaced with "unknown".
7. Normalization of numeric columns is applied to prepare the dataset for algorithms sensitive to feature scaling. The default choice is Min–Max normalization unless otherwise specified.