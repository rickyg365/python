import os

import requests
from bs4 import BeautifulSoup

from typing import List, Dict
from dataclasses import dataclass

"""
#? Moved map
https://mls.foreclosure.com/listing/search.html?
q=Pasadena,%20CA&pt=sf&pt=mf&pi=&pa=&bdi=&bhi=&
loc=Pasadena,%20CA&boundingTopLeft=&boundingBottomRight=
&st=ca&cno=&ci=pasadena&ps=&pg=1&o=pt&ob=asc&zip=&

#? Unmoved Map
https://mls.foreclosure.com/listing/search.html?
ci=palmdale&st=ca&utm_source=internal&utm_medium=link
&utm_campaign=MLS_top_links

https://mls.foreclosure.com/listing/search.html?
ci=pacific+palisades&st=ca&utm_source=internal
&utm_medium=link&utm_campaign=MLS_top_links

https://mls.foreclosure.com/listing/search.html?
ci=palos+verdes+peninsula&st=ca&utm_source=internal&utm_medium=link
&utm_campaign=MLS_top_links


https://mls.foreclosure.com/listings/city-of-industry-ca/


https://mls.foreclosure.com/listing/search.html?
ci=chatsworth&st=ca&utm_source=internal&utm_medium=link
&utm_campaign=MLS_top_links



https://mls.foreclosure.com/listing/search.html?
q=Palmdale+CA

can simplify link to 
https://mls.foreclosure.com/listing/search.html?
ci=chatsworth&st=ca

ci -> city
st -> state

base_url = https://mls.foreclosure.com/listing/search.html
complete_url = f"{base_url}?ci={city_name}&st={state_initials}"
or
# Requires proper name and capitals for state initials
complete_url = f"{base_url}?q={city_name}+{state_initials}"


page = requests.get(complete_url)
status = page.status_code
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify)
"""

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
})

# Model
@dataclass
class Model:
    def __post_init__(self):
        pass

    def __str__(self) -> str:
        txt = ""
        return txt

# Scraper
class ScrapeMLS:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        txt = ""
        return txt



def test_url(url):
    page = requests.get(url, headers=headers)
    status = page.status_code
    soup = BeautifulSoup(page.content, 'html.parser')
    print(status)

    if status != 200:
        return
    print(soup.prettify)


def main():
    city_name = "redondo beach".replace(' ', "+")
    state_initials = "ca"

    base_url = "https://mls.foreclosure.com/listing/search.html"
    complete_url_1 = f"{base_url}?ci={city_name}&st={state_initials}"
    
    # Requires proper name and capitals for state initials
    complete_url_2 = f"{base_url}?q={city_name.title()}+{state_initials.upper()}"

    # test_url(complete_url_1)    
    # test_url(complete_url_2)

    # test_url("https://mls.foreclosure.com/listings/city-of-industry-ca/")


if __name__ == '__main__':
    main()
