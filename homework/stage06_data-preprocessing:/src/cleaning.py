# Cleaning py
# df = cleaning.fill_missing_median(df, ['col1','col2'])
# df = cleaning.drop_missing(df, threshold=0.5)
# df = cleaning.normalize_data(df, ['col1','col2'])

# src/cleaning.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def fill_missing_median(df, columns=None):
    """
    Fill missing numeric values with the median of each column.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame
        columns (list, optional): Columns to fill. If None, use numeric columns.
    
    Returns:
        pd.DataFrame: DataFrame with missing values filled
    """
    df_copy = df.copy()
    if columns is None:
        columns = df_copy.select_dtypes(include=np.number).columns
    for col in columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].median())
    return df_copy


def drop_missing(df, columns=None, threshold=None):
    """
    Drop rows with missing values.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame
        columns (list, optional): Drop rows if any of these columns are missing.
        threshold (float, optional): Keep rows with at least `threshold * n_columns` non-null values.
    
    Returns:
        pd.DataFrame: DataFrame with rows dropped
    """
    df_copy = df.copy()
    if columns is not None:
        return df_copy.dropna(subset=columns)
    if threshold is not None:
        return df_copy.dropna(thresh=int(threshold * df_copy.shape[1]))
    return df_copy.dropna()


def normalize_data(df, columns=None, method='minmax'):
    """
    Normalize numeric data using MinMax or Standard scaling.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame
        columns (list, optional): Columns to normalize. If None, use numeric columns.
        method (str): 'minmax' or 'standard'
    
    Returns:
        pd.DataFrame: DataFrame with normalized columns
    """
    df_copy = df.copy()
    if columns is None:
        columns = df_copy.select_dtypes(include=np.number).columns
    
    if method == 'minmax':
        scaler = MinMaxScaler()
    elif method == 'standard':
        scaler = StandardScaler()
    else:
        raise ValueError("method must be 'minmax' or 'standard'")
    
    df_copy[columns] = scaler.fit_transform(df_copy[columns])
    return df_copy

#fill missing
def fill_missing_general(df):
    """
    Fill missing values for numeric, categorical, and datetime columns.
    """
    df_copy = df.copy()

    # Numeric → median
    num_cols = df_copy.select_dtypes(include=np.number).columns
    for col in num_cols:
        df_copy[col] = df_copy[col].fillna(df_copy[col].median())

    # Categorical → "unknown"
    cat_cols = df_copy.select_dtypes(include="object").columns
    for col in cat_cols:
        df_copy[col] = df_copy[col].fillna("unknown")

    # Datetime → forward fill then backward fill
    dt_cols = df_copy.select_dtypes(include="datetime64[ns]").columns
    for col in dt_cols:
        df_copy[col] = df_copy[col].ffill().bfill()

    return df_copy


