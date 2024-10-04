"""Test file."""

import pickle

from tqdm import tqdm

from asset_selector.configs.data_sources import BronzeData
from asset_selector.etl.bronze.get_skatspositiv_liste import get_latest_positiv_liste
from asset_selector.utils.helpers import get_ticker_symbol_from_isin
from asset_selector.utils.helpers import init_logger

logger = init_logger()

if __name__ == "__main__":
    logger.info("Starting Bronze ETL")
    logger.info("Downloading skats positiv liste")
    # download_positiv_liste()

    df_positiv_list = get_latest_positiv_liste()

    isin_of_assets = df_positiv_list['ISIN']
    isin_of_assets.dropna(inplace=True)

    # TODO save tickers as df instead
    with open(BronzeData.ticker_dict, 'rb') as f:
        tickers_dict = pickle.load(f)

    n_req = 0
    for isin in tqdm(isin_of_assets, desc="fetching ticker-sybols from ISIN-no"):
        if isin not in tickers_dict:
            ticker = get_ticker_symbol_from_isin(isin)
            if ticker:
                tickers_dict[isin] = ticker

            n_req += 1
            if n_req % 25 == 0:
                with open(BronzeData.ticker_dict, 'wb') as f:
                    pickle.dump(tickers_dict, f)

    a = 2
    b = a**2
