import os
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

    def __str__(self):
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


