import os
import datetime

import requests
from bs4 import BeautifulSoup


from main import hydrate_listing
from utils.simple_save import load_json, save_json

class Apartment:
    SAVE = {
        'json': save_json
    }
    LOAD = {
        'json': load_json
    }
    def __init__(self, 
                 url: str=None, 
                 street_address: str=None, 
                 last_updated: str=None,
                 hydrated: str=None,
                 monthly_rent: str=None,
                 bedrooms: str=None,
                 bathrooms: str=None,
                 square_feet: str=None,
                 phone_number: str=None,
                 low_price: str=None,
                 high_price: str=None,
                 low_beds: str=None,
                 high_beds: str=None,
                 low_baths: str=None,
                 high_baths: str=None):
        self.last_updated = last_updated
        self.hydrated = hydrated
        
        self.url= url
        self.street_address = street_address
        self.monthly_rent = monthly_rent
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.square_feet = square_feet
        self.phone_number = phone_number
        
        self.low_price = low_price
        self.high_price = high_price
        
        self.low_beds = low_beds
        self.high_beds = high_beds
        
        self.low_baths = low_baths
        self.high_baths = high_baths

        self.extra_data = dict()

    def __str__(self):
        hydrated = ""
        txt = f"""
{self.street_address}
{self.url}
"""
        if self.hydrated:
            hydrated = f"""
|${self.monthly_rent}| {self.street_address}
{self.bedrooms} beds - {self.bathrooms} baths | {self.square_feet}
{self.phone_number}
{self.url}

Lowest
${self.low_price}
{self.low_beds} beds - {self.low_baths} baths

Highest
${self.high_price}
{self.high_beds} beds - {self.high_baths} baths
"""
            return hydrated
        return txt
    
    def debug_print(self):
        txt = f"""
{self.url=}
{self.street_address=}
{self.last_updated=}
{self.hydrated=}
{self.monthly_rent=}
{self.bedrooms=}
{self.bathrooms=}
{self.square_feet=}
{self.phone_number=}
{self.low_price=}
{self.high_price=}
{self.low_beds=}
{self.high_beds=}
{self.low_baths=}
{self.high_baths=}
"""
        return txt
    
    def hydrate(self):
        self.hydrated = True
        HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
        url = self.url
        self.last_updated = datetime.datetime.now().strftime('%y%m%d')
        
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

            match t:
                # Rent
                case "monthly_rent":
                    nl = i.split("-")

                    if len(nl) > 1:
                        self.low_price = nl[0].strip().replace('$', '')
                        self.high_price = nl[1].strip().replace('$', '')
                        self.monthly_rent = self.low_price
                    else:
                        self.monthly_rent = nl[0].strip().replace('$', '')
                    
                # Beds
                case "bedrooms":
                    nl = i.split("-")
                    
                    if len(nl) > 1:
                        self.low_beds = nl[0].strip()
                        self.high_beds = nl[1].strip().split(' ')[0]
                        self.bedrooms = self.low_beds
                    else:
                        self.bedrooms = nl[0].strip().split(' ')[0]
                    
                # Baths
                case "bathrooms":
                    nl = i.split("-")
                    
                    if len(nl) > 1:
                        self.low_baths = nl[0].strip()
                        self.high_baths = nl[1].strip().split(' ')[0]
                        self.bathrooms = self.low_baths
                    else:
                        self.bathrooms = nl[0].strip().split(' ')[0]
                    
                # Square Feet
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
                        
                # Default case
                case _:
                    self.extra_data[t] = i
                    
        self.phone_number = phone_number


    def save(self, data, filename: str):
        # File Format 
        file_format = filename.split(".")[-1]

        # Use chosen save method
        if file_format in self.SAVE:
            self.SAVE[file_format](data, filename)
            return True
        return False


    def load(self, filename: str):
        data = None
        # File Format 
        file_format = filename.split(".")[-1]

        # Use chosen save method
        if file_format in self.LOAD:
            data = self.LOAD[file_format](filename)
        return data






if __name__ == "__main__":
    sample_data = load_json('data/los_angeles_apmt_listings.json')
    list_of_apartments = []
    for k, d in sample_data.items():
        new_apmt = Apartment(**d)
        list_of_apartments.append(new_apmt)

    for a in list_of_apartments:
        print(a)


