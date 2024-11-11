import requests
from bs4 import BeautifulSoup
'''
NOTES
CompTIA 220-1101 A+ Training Course
a#video-title

Does not work because youtube uses javascript to load shit
use yt-dl or yt-dlp
'''

if __name__ == "__main__":
    url = "https://www.youtube.com/playlist?list=PLG49S3nxzAnnOmvg5UGVenB_qQgsh01uC"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    r = requests.get(url, headers=headers)
    # print(r.text[:15])
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup)

    # content = soup.select_one('div#content')
    
    titles = soup.select('a#video-title')
    for item in titles:
        print()
        print(item.title)



