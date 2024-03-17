import os
import requests
import datetime
from bs4 import BeautifulSoup

from utils.simple_save import save_json, load_json

"""
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}

# Finding url filters
base URL

https://www.apartments.com/los-angeles-ca/

https://www.apartments.com/chino-ca/

https://www.apartments.com/chino-ca/under-2500/
https://www.apartments.com/apartments-houses/chino-ca/under-2500/
https://www.apartments.com/apartments-houses/chino-ca/1-bathrooms-under-2500/


Target
https://www.apartments.com/belcourt-apartments-ontario-ca/zlmt57x/

Keep track of when listings are updated
url:
date:

Sorting

https://www.apartments.com/los-angeles-ca/?so=8
2 - Price(low to high)
8 - Last Updated

"""

def build_url(city: str, state: str=None, min_price: int=None, max_price: int=None, bathrooms: int=None, bedrooms: int=None):
    url = "https://www.apartments.com"
    city = city.replace(' ', '-') if city is not None else ""
    state = f'-{state.lower()}' if state is not None else "-ca"
    min_price = f"under-{min_price}" if min_price is not None else ""
    max_price = max_price.replace(' ', '-') if max_price is not None else ""
    bathrooms = bathrooms.replace(' ', '-') if bathrooms is not None else ""
    bedrooms = bedrooms.replace(' ', '-') if bedrooms is not None else ""

    return f"{url}/{city}{state}/{min_price}"

def get_listings(url: str):
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
    
    page = requests.get(url, headers=HEADERS, timeout=5)

    soup = BeautifulSoup(page.content, "html.parser")

    placards = soup.find("section", id="placards")

    articles = placards.find_all("article", attrs={"data-url": True})

    data = {}
    for item in articles:
        data[item['data-listingid']] = {
            "url": item['data-url'],
            "street_address": item.get('data-streetaddress', ""),
            "last_updated": datetime.datetime.now().strftime('%y%m%d')
        }

    return data


if __name__ == "__main__":

    FILENAME = "apmt_data.json"
    URL = "https://www.apartments.com/los-angeles-ca/"

    # Get Input to build url filters and sorting    
    CITY = input("CITY: ")
    STATE = input("STATE: ")
    MIN_PRICE = input("MIN_PRICE: ")
    if MIN_PRICE == "":
        MIN_PRICE = None

    URL = build_url(CITY, STATE, MIN_PRICE)
    print(URL)

    # Scrape Listing Urls
    data = get_listings(URL)
    print(data)

    save_json(data, f"data/{CITY}_apmt_listings.json")


