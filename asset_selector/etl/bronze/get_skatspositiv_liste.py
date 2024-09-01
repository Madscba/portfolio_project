import requests
from bs4 import BeautifulSoup
import urllib.parse
import os
import pandas as pd
import re
from asset_selector.configs.data_sources import BronzeData
from asset_selector.configs.static import TODAY,positiv_liste_url,  SMILEY

def download_positiv_liste(url:str= positiv_liste_url):
    """
    Function that finds the positiv-liste on skats website and download to data if it does not already exists
    Args:
        url: str (): URL of skats-website with the positiv-liste

    Returns:

    """
    # Send a GET request to the webpage
    response = requests.get(url)
    assert response.status_code == 200, f"Request failed w. code: {response.status_code}"

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links on the page
    links = soup.find_all('a')

    # Create a directory to store downloaded files
    data_path = BronzeData.positiv_liste
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    # Iterate through links and download XML files
    for link in links:
        href = link.get('href')
        if href and href.lower().endswith('.xlsx'):
            if str(TODAY.year) in href:
                # Construct absolute URL if necessary
                file_url = urllib.parse.urljoin(url, href)

                # Get the filename from the URL
                base_name = os.path.basename(file_url)
                filename = data_path / base_name

                if not os.path.isfile(filename):
                    # Download the file
                    print(f"Downloading: {file_url}")
                    file_response = requests.get(file_url)

                    df = pd.read_excel(file_url)
                    assert (df.shape[0] > 1) & (df.shape[1] > 1), f"No content in the file. df has shape: {df.shape}"

                    # Save the file
                    with open(filename, 'wb') as file:
                        file.write(file_response.content)

                    print(f"Downloaded new version of sheet: {base_name}")
                else:
                    print(f"Latest version already downloaded: {base_name} {SMILEY}")

def get_latest_positiv_liste(date_pattern = r"(\d{2})(\d{2})(\d{4})")-> pd.DataFrame:
    #Get files names from bronze folder
    filenames = os.listdir(BronzeData.positiv_liste)

    # Regular expression to match the date


    # Search for the date in the filename
    str_dates = [re.search(date_pattern, filename).group(0) for filename in filenames]
    dates = pd.DataFrame([pd.to_datetime(str_date,format="%d%m%Y") for str_date in str_dates])
    idx_largest_date = dates.idxmax()[0]

    df_positiv_liste = pd.read_excel(BronzeData.positiv_liste / filenames[idx_largest_date])
    return df_positiv_liste

if __name__ == "__main__":
    # Example usage
    # download_positiv_liste()
    get_latest_positiv_liste()