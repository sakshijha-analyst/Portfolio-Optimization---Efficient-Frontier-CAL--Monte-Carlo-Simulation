import yfinance as yf
import pandas as pd

stocks = {
    "Reliance Industries": "RELIANCE.NS",
    "Tata Consultancy Services": "TCS.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "Infosys": "INFY.NS",
    "ICICI Bank": "ICICIBANK.NS"
}

portfolio_data = pd.DataFrame()

for name, ticker in stocks.items():

    data = yf.download(ticker, start="2004-01-01", auto_adjust=False)

    print(data.columns)  

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    adj_close = data[["Adj Close"]].copy()
    adj_close.rename(columns={"Adj Close": name}, inplace=True)

    portfolio_data = pd.concat([portfolio_data, adj_close], axis=1)

print(portfolio_data.head())

portfolio_data.to_excel("portfolio_data.xlsx")


