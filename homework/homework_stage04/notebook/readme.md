Notebook for Homework Stage04

-------------------------API PULL------------------------------------

Purpose:
1. Get Most Active Stocks page from Yahoo Finance and loads the data into a Pandas DataFrame for analysis or storage.
2. URL https://finance.yahoo.com/most-active

Params and Assumption
1. The Yahoo Finance Most Active Stocks page structure remains consistent (e.g., the first <table> element contains the desired stock data).
2. The first row of the table is the header row.
3. The table has both <th> (header) and <td> (data) cells.
4. The script runs in an environment with internet access and Python packages installed (requests, BeautifulSoup, and Pandas)
5. Yahoo Finance allows access with a standard User-Agent string to prevent bot blocking.
6. Data is small enough to be loaded into memory using Pandas.

Logic Flow
1. Import Libraries: Load requests, BeautifulSoup from bs4, and pandas.
2. Define URL: Assign Yahoo Finance's Most Active Stocks page to the variable url.
3. Send HTTP GET Request: Use requests.get(url, headers=headers) with a User-Agent to mimic a browser.
4. Check Response: Call response.raise_for_status() to ensure the request succeeded (HTTP 200).
5. Parse HTML with BeautifulSoup: Create a BeautifulSoup object to parse the HTML text.
6. Locate the Table: Use soup.find("table") to retrieve the first <table> element from the HTML.
7. Extract Rows: Iterate through each <tr> (table row) and extract text from <td> and <th> cells.
8. Separate Header and Data: Assume the first row is the header, store it in header, and the rest in data.
9. Create Pandas DataFrame: Pass data and header into pd.DataFrame() to create a structured table.
10. Output Sample: Print the first 5 rows using df.head().


---------------------SCRAPING---------------------
Purpose:
1. Retrieves daily stock price data for a given ticker symbol.
2. first attempts to fetch data from the Alpha Vantage API; If the API request fails (e.g., invalid key, rate limit exceeded, network error), the script falls back to scraping historical data from Yahoo Finance.
3. URL:
a. https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_KEY} (i used chatGPT to get the API to ALPHAVANTAGE)
b. https://finance.yahoo.com/quote/{symbol}/history

Params and Assumption:
1. Alpha Vantage API is available and the ALPHA_KEY is valid.
2. The "Time Series (Daily)" structure in Alpha Vantage’s JSON response does not change.
3. Yahoo Finance's HTML structure remains consistent, with the historical data in the first <table> element.
4. Data volume from both API and scraping is small enough to fit in memory.
5. For scraping, a browser-like User-Agent is used to reduce blocking risk.

Logic Flow:
1. Import Libraries
2. Set Parameter (stock symbol as symbol, ALPHA_KEY as the API key)
3. Primary Data Source: Alpha Vantage API 
4. If error go to fallback Yahoo Finance Scraping


