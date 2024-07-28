import requests
from bs4 import BeautifulSoup



if __name__ == "__main__":
    url = "https://offerup.com/explore/k/1"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    r = requests.get(url, headers=headers)
    print(r.text[:15])
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup)





