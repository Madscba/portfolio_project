import yfinance as yf
import pandas as pd

#EXAMPLE USAGE
TICKERS = ['WMT', 'AMZN','AAPL','GOOG','UNH','CI','XOM','CVX','BRK-B','JPM','MCK','ABC','T','VZ','F']
NAMES = ['Walmart','Amazon','Apple','Alphabet','UnitedHealth Group','Cigna','Exxon Mobil','Chevron','Berkshire Hathaway','JP Morgan Chase & Co','McKesson','AmerisourceBergen','AT&T','Verizon','Ford Motor Company']
START_DATE = '2021-10-01'
END_DATE = '2022-01-01'
INTERVAL = "1wk"
PERIOD = "max"

def get_pricing_history(tickers=TICKERS,interval="1wk",start_date="2016-01-01", end_date = "2022-01-01",period="max"):
    """
    Purpose: Fetch pricing history from Yahoo from the asset with the given ticker
    Docs: https://pypi.org/project/yfinance/

    Input:
        ticker (STR), period (STR), interval (STR), start (STR), end (STR):
    Return:
        6xSeries [Open, High, Low, Close, Adj Close, Volume]
    """
    instrument = yf.download(tickers,start=start_date, end = end_date, interval=interval,period=period)
    instrument = instrument.dropna(axis = 0)
    return instrument

# def load_stocks(tickers=TICKERS,interval=INTERVAL,start_date=START_DATE, end_date = END_DATE):
#     """
#     Purpose: get several ticker pricing histories. See global variables defined in top document to see default arguments.
#     Input:
#         tickers [List of STR], interval (STR),start_date (STR), end_date = (STR)
#     Return:
#         DataFrame consisting of 6x series pr. ticker given.
#     """
#     pricing_hist = get_pricing_history(ticker=tickers, interval=interval, start_date=start_date,end_date=end_date)
#     return df

if __name__ == "__main__":
    get_pricing_history()



