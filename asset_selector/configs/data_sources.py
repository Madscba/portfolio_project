from dataclasses import dataclass

from web_scraper.web_crawler.configs.directories import Directories


@dataclass
class BronzeData:
    """Dataclass containing bronze tables."""

    bronze_path = Directories.DATA_PATH / "bronze"


@dataclass
class SilverData:
    """Dataclass containing bronze tables."""

    silver_path = Directories.DATA_PATH / "silver"


@dataclass
class GoldData:
    """Dataclass containing gold tables."""

    gold_path = Directories.DATA_PATH / "gold"
