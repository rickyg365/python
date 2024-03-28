import os

from main import build_url, get_listings, hydrate_listing
from utils.simple_save import load_json, save_json

from apartment import Apartment


def get_user_input(input_text: str, return_type=None):
    user_input = input(input_text)

    if user_input == "":
        return None
    
    if return_type is not None:
        return return_type(user_input)
    
    return user_input



col, row = os.get_terminal_size()
# Search for listings (and Hydrate)
CITY = get_user_input("Select City: ")
MAX_PRICE = get_user_input("Max price: ", int)

listings_url = build_url(city=CITY, state=None, min_price=None, max_price=MAX_PRICE, bathrooms=None, bedrooms=None)
listings_data = get_listings(listings_url)


# Display Listings
selection_cache = {}
idx = 1
for listing_id, listing_data in listings_data.items():
    print(f"""
{'_'*col}
[{idx}] {listing_data.get('street_address', 'No ADDRESS')}
{listing_data.get('url', 'No URL')}
""")
    selection_cache[idx] = listing_id
    idx += 1

# Select Listing for more Details!
selected_idx = get_user_input("Select Listing: ", int)

selected_listing_data = listings_data[selection_cache[selected_idx]]

hydrated_listing_data = hydrate_listing(selected_listing_data)

print(hydrated_listing_data)

print(f"""
{hydrated_listing_data.get('street_address', 'No ADDRESS')}
{hydrated_listing_data.get('bathrooms', 'No BATHROOMS')}
{hydrated_listing_data.get('phone_number', 'No PHONE NUMBER')}
{hydrated_listing_data.get('url', 'No URL')}

END
""")


# Analyze Listings

sample_apt = Apartment(**selected_listing_data)
print(sample_apt)
sample_apt.hydrate()
print(sample_apt)


























