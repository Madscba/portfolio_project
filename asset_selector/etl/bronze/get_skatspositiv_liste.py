import requests
from bs4 import BeautifulSoup
import urllib.parse
import os
from asset_selector.configs.data_sources import BronzeData

def download_xml_files(url):
    # Send a GET request to the webpage
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all links on the page
    links = soup.find_all('a')

    # Create a directory to store downloaded files
    data_path = BronzeData.bronze_path / 'skats_positivliste_xml'
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    # Iterate through links and download XML files
    for link in links:
        href = link.get('href')
        if href and href.lower().endswith('.xlsx'):
            if "2024" in href:
                # Construct absolute URL if necessary
                file_url = urllib.parse.urljoin(url, href)

                # Get the filename from the URL
                filename = data_path / os.path.basename(file_url)

                # Download the file
                print(f"Downloading: {file_url}")
                file_response = requests.get(file_url)

                # Save the file
                with open(filename, 'wb') as file:
                    file.write(file_response.content)

                print(f"Downloaded: {filename}")

if __name__ == "__main__":
    # Example usage
    webpage_url = "https://skat.dk/erhverv/ekapital/vaerdipapirer/beviser-og-aktier-i-investeringsforeninger-og-selskaber-ifpa"
    download_xml_files(webpage_url)