"""Test file."""

from dataclasses import dataclass

from asset_selector.configs.directories import Directories


@dataclass
class BronzeData:
    """Dataclass containing bronze tables."""

    bronze_path = Directories.DATA_PATH / "bronze"
    positiv_liste = bronze_path / 'skats_positivliste_xml'

    # files
    ticker_dict = bronze_path / "isin_to_ticker_dictionary.pkl"
    ticker_not_avail = bronze_path / "tickers_not_available_yfinance.pkl"


@dataclass
class SilverData:
    """Dataclass containing bronze tables."""

    silver_path = Directories.DATA_PATH / "silver"


@dataclass
class GoldData:
    """Dataclass containing gold tables."""

    gold_path = Directories.DATA_PATH / "gold"
