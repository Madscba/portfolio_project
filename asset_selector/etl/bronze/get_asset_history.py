"""Test file."""

import pickle

import pandas as pd
import yfinance as yf

from asset_selector.configs.data_sources import BronzeData
from asset_selector.utils.data_helpers import load_file

# EXAMPLE USAGE
TICKERS = [
    'WMT',
    'AMZN',
    'AAPL',
    'GOOG',
    'UNH',
    'CI',
    'XOM',
    'CVX',
    'BRK-B',
    'JPM',
    'MCK',
    'ABC',
    'T',
    'VZ',
    'F',
]
NAMES = [
    'Walmart',
    'Amazon',
    'Apple',
    'Alphabet',
    'UnitedHealth Group',
    'Cigna',
    'Exxon Mobil',
    'Chevron',
    'Berkshire Hathaway',
    'JP Morgan Chase & Co',
    'McKesson',
    'AmerisourceBergen',
    'AT&T',
    'Verizon',
    'Ford Motor Company',
]
START_DATE = '2021-10-01'
END_DATE = '2022-01-01'
INTERVAL = "1wk"
PERIOD = "max"


def get_pricing_history(
    tickers=TICKERS,
    interval="1wk",
    start_date="2022-01-01",
    end_date="2024-08-01",
    period="max",
):
    """
    Purpose: Fetch pricing history from Yahoo from the asset with the given ticker.

    Input:
        ticker (STR), period (STR), interval (STR), start (STR), end (STR):
    Return:
        6xSeries [Open, High, Low, Close, Adj Close, Volume]
    """
    instrument = yf.download(
        tickers, start=start_date, end=end_date, interval=interval, period=period
    )
    instrument = instrument.dropna(axis=0)
    return instrument


if __name__ == "__main__":
    tickers = load_file(BronzeData.ticker_dict)
    tickers_dict = {}
    with open(BronzeData.ticker_not_avail, 'wb') as f:
        pickle.dump(tickers_dict, f)
    tickers_not_avail = load_file(BronzeData.ticker_not_avail)

    df_ticker_prices = pd.DataFrame()
    # for ticker in tqdm(TICKERS):
    #     print(ticker)
    instrument_hist = get_pricing_history(tickers=tickers.values())
    # if instrument_hist.shape[0]:
    #     df_ticker_prices =
    #     df_ticker_prices._append(instrument_hist, ignore_index=True)

    print(
        "Successfully retreived: ",
        100 * (df_ticker_prices.shape[1] / len(tickers.values())),
    )
    a = 2
    b = a**2
