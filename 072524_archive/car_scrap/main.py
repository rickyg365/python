import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup

"""

Search
cars & trucks w/ min max price
https://offerup.com/explore/k/5/1?PRICE_MIN=4000&PRICE_MAX=10000


Car Entry
https://offerup.com/item/detail/dbc32487-4cac-398d-ae53-d9e1ba1cd693?cid=5.1



<a 
    title="2020 Nissan Murano" 
    class="jss7846 jss7847 jss8203 jss8190" 
    href="/item/detail/dbc32487-4cac-398d-ae53-d9e1ba1cd693?cid=5.1" 
    aria-label="2020 Nissan Murano $4,500 18k miles in Los Angeles, CA " 
    tabindex="0"
>...</a>

"""
def main():
    
    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0'}
    url = 

    page = requests.get(url, headers=HEADERS, timeout=5)

    soup = BeautifulSoup(page.content, "html.parser")
    return

if __name__ == "__main__":
    main()