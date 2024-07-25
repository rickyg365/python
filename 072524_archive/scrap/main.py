import os
import time
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
    max_price = f"under-{max_price}" if max_price is not None else ""
    bathrooms = bathrooms.replace(' ', '-') if bathrooms is not None else ""
    bedrooms = bedrooms.replace(' ', '-') if bedrooms is not None else ""

    return f"{url}/{city}{state}/{max_price}"

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

def hydrate_listing(current_data):
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
    url = current_data['url']
    current_data['last_updated'] = datetime.datetime.now().strftime('%y%m%d')
    
    page = requests.get(url, headers=HEADERS, timeout=5)

    soup = BeautifulSoup(page.content, "html.parser")
    # articles = placards.find_all("article", attrs={"data-url": True})

    # Phone Number
    phone_number = soup.find("span", class_="phoneNumber").text

    # Main Info
    main_info = soup.find('ul', class_="priceBedRangeInfo")

    data_points = main_info.find_all('div', class_="priceBedRangeInfoInnerContainer")

    for d in data_points:

        t = d.find('p', class_='rentInfoLabel').text
        i = d.find('p', class_='rentInfoDetail').text

        if t is None: 
            continue
        t = t.lower()
        t = t.replace(' ', '_')

        # Rent
        # Beds
        # Baths
        # Square Feet
        match t:
            case "monthly_rent":
                nl = i.split("-")

                if len(nl) > 1:
                    current_data['low_price'] = nl[0].strip().replace('$', '')
                    current_data['high_price'] = nl[1].strip().replace('$', '')
                else:
                    current_data[t] = nl[0].strip().replace('$', '')
                
            case "bedrooms":
                nl = i.split("-")
                
                if len(nl) > 1:
                    current_data['low_beds'] = nl[0].strip()
                    current_data['high_beds'] = nl[1].strip().split(' ')[0]
                else:
                    current_data[t] = nl[0].strip().split(' ')[0]
                
                
            case "bathrooms":
                nl = i.split("-")
                
                if len(nl) > 1:
                    current_data['low_baths'] = nl[0].strip()
                    current_data['high_baths'] = nl[1].strip().split(' ')[0]
                else:
                    current_data[t] = nl[0].strip().split(' ')[0]
                
            case _:
                current_data[t] = i
                
    

    # Pricing and Floor Plans
    # Community Ammenities
    # Apartment Features
    # Fees and Policies
    # Neighborhood
    # Education
    # Transportation
    # Points of Interest
    # Ratings
    # Photos


    current_data['phone_number'] = phone_number

    return current_data




if __name__ == "__main__":

    URL = "https://www.apartments.com/los-angeles-ca/"
    CITY = "los angeles"
    FILENAME = f"data/{CITY.replace(' ', '_')}_apmt_listings.json"
    # Get Input to build url filters and sorting    
    # CITY = input("CITY: ")
    # STATE = input("STATE: ")
    # MAX_PRICE = input("MAX_PRICE: ")
    # if MAX_PRICE == "":
    #     MAX_PRICE = None

    # URL = build_url(CITY, state=STATE, max_price=MAX_PRICE)
    # print(URL)

    # Scrape Listing Urls
    # data = get_listings(URL)
    # print(data)

    # save_json(data, FILENAME)


    # Load Data
    data = load_json(FILENAME)
    # print(data)

    # Hydrate Listings
    total_listings = len(data)
    empty_space = total_listings
    filled_space = 0
    for id, d in data.items():
        prog_bar = f"[{filled_space*'*'}{empty_space*' '}]"
        print(prog_bar, end='\r')
        empty_space -= 1
        filled_space += 1

        # if d.get('hydrated', False):
        #     continue
        d["hydrated"] = True
        data[id] = hydrate_listing(d)
        time.sleep(1)

    # Save Hydrated Data
    save_json(data, FILENAME)

