import os
import feedparser

from model import NYT_ENTRY, parse_raw_data


""" 
URL: https://rss.nytimes.com/services/xml/rss/nyt/World.xml

"""
cols, rows = os.get_terminal_size()

feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
feed = feedparser.parse(feed_url)

# Loop through and get articles
for i in range(25):
    new_entry = feed.entries[i]

    final_entry = NYT_ENTRY(**parse_raw_data(new_entry), width=cols)
    print(final_entry)


