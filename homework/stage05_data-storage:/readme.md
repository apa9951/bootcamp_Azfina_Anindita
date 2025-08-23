Purpose

This project demonstrates how to:
- Create a **sample stock price DataFrame** with pandas
- Save it in CSV** and Parquet formats (my pyarrow error, as per recommendation chatGPT I used fastparquet)
- Reload both files
- Validate that they match in shape and data types
- Use unified `write_df` and `read_df` functions to automatically handle file formats

Feature
1. Automatic directory creation when saving files
2. Automatic format detection based on file suffix
3. Unified reading/writing API

Folder Structured
1. Code on base folder
2. Data Raw to save the DataFrame of AAPL
3. Data processed after parquet method

Why Parquet?
1. CSV = simple, portable, human-friendly backup.
2. Parquet = efficient, typed storage for performance.

I also use .env
DATA_DIR_RAW=data/raw
DATA_DIR_PROCESSED=data/processed