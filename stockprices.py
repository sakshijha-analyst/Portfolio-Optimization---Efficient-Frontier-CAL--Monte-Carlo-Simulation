import yfinance as yf
import pandas as pd

# Step 1: Define your portfolio
stocks = {
    "Reliance Industries": "RELIANCE.NS",
    "Tata Consultancy Services": "TCS.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "Infosys": "INFY.NS",
    "ICICI Bank": "ICICIBANK.NS"
}

# Step 2: Create empty dataframe
portfolio_data = pd.DataFrame()

# Step 3: Loop and download data
for name, ticker in stocks.items():

    data = yf.download(ticker, start="2004-01-01", auto_adjust=False)

    print(data.columns)  # to check columns

    # Flatten if multi-index
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    adj_close = data[["Adj Close"]].copy()
    adj_close.rename(columns={"Adj Close": name}, inplace=True)

    portfolio_data = pd.concat([portfolio_data, adj_close], axis=1)

# Step 4: Print output
print(portfolio_data.head())

portfolio_data.to_excel("portfolio_data.xlsx")
