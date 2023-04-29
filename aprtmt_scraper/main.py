import os
import json

import requests
from bs4 import BeautifulSoup

from typing import List, Dict, Any


"""
Data from https://www.apartments.com/

Sample Queries
Ontario, Ca -> https://www.apartments.com/ontario-ca/
Ontario, Ca/_-$2500/_-1bds -> https://www.apartments.com/ontario-ca/max-1-bedrooms-under-2500/
Ontario, Ca/$2000-$2500/1-2bds -> https://www.apartments.com/ontario-ca/1-to-2-bedrooms-2000-to-2500/
Ontario, Ca/$2000-$2500/1bds -> https://www.apartments.com/ontario-ca/1-bedrooms-2000-to-2500/

Get initial data upon loading list
    - property name
    - property address
    - pricing range
    - bed range
    - ameneties
    - Contact
        - phone

if property is chosen follow link and get extra data
    - bathrooms
    - square feet
    ~ pricing and floor plans
    ~ description
    - features
    - contact
        - phone
        - property website
    - amenities(re)
    - services
    - extra*
    - features
    - Lease details and features
        - Parking
        - utilities
        - lease options
        - property info
    - neighborhood
    - transportation
    - points of interest
        - shopping centers
        - parks and recreation
    - confirm address and phone number
"""


# Handle Queries
def build_apartment_query_url(city: str, state: str, price_min: float = None, price_max: float = None, bedrooms_min: float = None, bedrooms_max: float = None):
    # base url
    BASE_URL = "https://www.apartments.com/"

    # city-state
    if city is None and state is None:
        return BASE_URL

    city_state = f"{city}-{state}/"

    # bedrooms range
    b_range = ""
    b_min = bedrooms_min is not None  # True if Bed Min exist
    b_max = bedrooms_max is not None  # True if Bed Max exist

    if b_min and b_max:
        b_range = f"{bedrooms_min}-to-{bedrooms_max}-bedrooms"
    elif b_min:
        b_range = f"min-{bedrooms_min}-bedrooms"
    elif b_max:
        b_range = f"max-{bedrooms_max}-bedrooms"

    # Sep
    if b_min or b_max:
        b_range += "-"

    # Price Range
    p_range = ""
    p_min = price_min is not None  # True if Price Min exist
    p_max = price_max is not None  # True if Price Max exist

    if p_min and p_max:
        p_range = f"{price_min}-{price_max}/"
    elif p_min:
        p_range = f"over-{price_max}/"
    elif p_max:
        p_range = f"under-{price_max}/"

    return f"{BASE_URL}{city_state}{b_range}{p_range}"


# Get Query Results, apartment list


# Scrape each entry in list
# INDV RESULT: https://www.apartments.com/archer-hollywood-los-angeles-ca/zrmncdx/

"""
- property name
- property address
- pricing range
- bed range
- ameneties
- Contact
    - phone
--------------------------------
- bathrooms
- square feet
~ pricing and floor plans
~ description
- features
- contact
    - phone
    - property website
- amenities(re)
- services
- extra*
- features
- Lease details and features
    - Parking
    - utilities
    - lease options
    - property info
- neighborhood
- transportation
- points of interest
    - shopping centers
    - parks and recreation
- confirm address and phone number
"""


class Listing:
    def __init__(self, url: str = None):
        self.url = url
        self._id = None
        self.name = None
        self.address = None
        self.price = None
        self.beds = None
        self.ameneties = None
        self.contact_phone = None
        #
        self.bathrooms = None
        self.square_feet = None
        self.pricing_floor_plans = None
        self.description = None
        self.features = None
        self.contact_site = None
        self.services = None
        self.features = None
        self.parking = None
        self.utilities = None
        self.lease_opteions = None
        self.property_info = None
        self.neighborhood = None
        self.transportation = None
        self.shopping = None
        self.parks_and_recreation = None
        # self.
        # self.
        # self.

    def __str__(self):
        txt = f"""
{self.name}
{self.address}
{self.price}
{self.beds}
{", ".join(self.ameneties)}
{self.contact_phone}
"""
        return txt

    def load_path(self, path: str):
        with open(path, 'r') as load_buffer:
            data = json.load(load_buffer)

        self.url = data.get("url", None)
        self._id = data.get("id", None)
        self.name = data.get("name", None)
        self.address = data.get("address", None)
        self.price = data.get("price", None)
        self.beds = data.get("beds", None)
        self.ameneties = data.get("ameneties", None)
        self.contact_phone = data.get("contact_phone", None)
        self.bathrooms = data.get("bathrooms", None)
        self.square_feet = data.get("square_feet", None)
        self.pricing_floor_plans = data.get("pricing_floor_plans", None)
        self.description = data.get("description", None)
        self.features = data.get("features", None)
        self.contact_site = data.get("contact_site", None)
        self.services = data.get("services", None)
        self.features = data.get("features", None)
        self.parking = data.get("parking", None)
        self.utilities = data.get("utilities", None)
        self.lease_opteions = data.get("lease_opteions", None)
        self.property_info = data.get("property_info", None)
        self.neighborhood = data.get("neighborhood", None)
        self.transportation = data.get("transportation", None)
        self.shopping = data.get("shopping", None)
        self.parks_and_recreation = data.get("parks_and_recreation", None)

        return self

    def save_data(self, base_path: str = "data/apartments/"):
        save_data = {
            "url": self.url,
            "id": self._id,
            "name": self.name,
            "address": self.address,
            "price": self.price,
            "beds": self.beds,
            "ameneties": self.ameneties,
            "contact_phone": self.contact_phone,
            "bathrooms": self.bathrooms,
            "square_feet": self.square_feet,
            "pricing_floor_plans": self.pricing_floor_plans,
            "description": self.description,
            "features": self.features,
            "contact_site": self.contact_site,
            "services": self.services,
            "features": self.features,
            "parking": self.parking,
            "utilities": self.utilities,
            "lease_opteions": self.lease_opteions,
            "property_info": self.property_info,
            "neighborhood": self.neighborhood,
            "transportation": self.transportation,
            "shopping": self.shopping,
            "parks_and_recreation": self.parks_and_recreation,
        }
        with open(f"{base_path}{self._id}.json", 'w') as save_buffer:
            json.dump(save_data, save_buffer, indent=4)


def main():
    BASE_PATH = "data/apartments/"
    empty_query = {
        "city": None,
        "state": None,
        "price_min": None,
        "price_max": None,
        "bedrooms_min": None,
        "bedrooms_max": None,
    }

    city_state_query = {
        "city": "los-angeles",
        "state": "ca",
        "price_min": None,
        "price_max": None,
        "bedrooms_min": None,
        "bedrooms_max": None,
    }

    capped_query = {
        "city": "los-angeles",
        "state": "ca",
        "price_min": None,
        "price_max": 2_000,
        "bedrooms_min": None,
        "bedrooms_max": 2,
    }

    queries = [empty_query, city_state_query, capped_query]
    urls = [build_apartment_query_url(**q) for q in queries]

    print("\n".join(urls))

    # Run Search
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    r = requests.get("https://www.apartments.com/los-angeles-ca/",
                     timeout=5, headers=headers)

    # print(r.content)
    # Get soup
    search_soup = BeautifulSoup(r.content, "html.parser")
    # search_soup.prettify()
    # print(search_soup.prettify())

    # Get List
    apartment_urls = []

    soup = search_soup.find('section', id="placards")

    soup = soup.find('div', id="placardContainer")

    soup = soup.find('ul')

    if soup is not None:
        listings = soup.find_all('li', class_='mortar-wrapper')

        for listing in listings:
            url_element = listing.find('article')
            new_url = url_element['data-url']
            # Find ID
            # new_url[-8:-1]
            apartment_id = new_url.split("/")[-2]

            # Scrape for initial data
            constructed_path = f"{BASE_PATH}{apartment_id}.json"
            if os.path.exists(constructed_path):
                new_listing = Listing().load_path(constructed_path)
                apartment_urls.append(new_listing)
                continue

            def txt_if_valid(soup_result: BeautifulSoup):
                if soup_result is None:
                    return
                return soup_result.text

            title = listing.find('span', class_="js-placardTitle title")
            title = txt_if_valid(title)

            street_address = listing.find(
                'div', class_="property-address js-url")
            street_address = txt_if_valid(street_address)

            price = listing.find('p', class_="property-pricing")
            price = txt_if_valid(price)

            beds = listing.find('p', class_="property-beds")
            beds = txt_if_valid(beds)

            amenity_node = listing.find('p', class_="property-amenities")
            amenities = amenity_node.find_all('span')
            amenities = [txt_if_valid(a) for a in amenities]

            phone_num = listing.find('a', class_="phone-link js-phone")
            if phone_num is None:
                phone_num = listing.find(
                    'a', class_="phone-link js-phone js-student-housing")

            phone_num = txt_if_valid(phone_num)

#             print(f"""{title}{street_address}{price}{beds}{amenities}{phone_num}""")

            # Create Listing
            new_listing = Listing(new_url)
            new_listing._id = apartment_id
            new_listing.name = title
            new_listing.address = street_address
            new_listing.price = price
            new_listing.beds = beds
            new_listing.ameneties = amenities
            new_listing.contact_phone = phone_num.strip()

            apartment_urls.append(new_listing)

    # Parse through each url for data, or only when requesting more data
    for l in apartment_urls:
        constructed_path = f"{BASE_PATH}{l._id}.json"
        if os.path.exists(constructed_path):
            continue
        print(l)
        l.save_data(BASE_PATH)


if __name__ == "__main__":
    main()
