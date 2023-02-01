import pandas as pd
import pandas_datareader as pdr
import yfinance as yf

AAPL = yf.Ticker("AAPL")
stock_history = AAPL.history(period="max")
print(stock_history)
