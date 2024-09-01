from asset_selector.etl.bronze.get_skatspositiv_liste import download_positiv_liste, get_latest_positiv_liste
from asset_selector.utils.helpers import init_logger

logger = init_logger()

if __name__ == "__main__":
    logger.info("Starting Bronze ETL")
    logger.info("Downloading skats positiv liste")
    download_positiv_liste()

    df_positiv_list = get_latest_positiv_liste()

