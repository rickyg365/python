# import os
# import feedparser

# # from model import NYT_ENTRY, parse_raw_data


# """ 
# URL: https://trends.google.com/trends/trendingsearches/daily

# """
# cols, rows = os.get_terminal_size()

# feed_url = "https://trends.google.com/trends/trendingsearches/daily"
# feed = feedparser.parse(feed_url)

# print(feed.entries)

# input("")

# # Loop through and get articles
# for _, entry in enumerate(feed.entries):
#     if _ == 25:
#         break
#     print(entry)
#     # final_entry = NYT_ENTRY(**parse_raw_data(new_entry), width=cols)
#     # print(final_entry)
# else:
#     print("No Entries!")

import pytrends
from pytrends.request import TrendReq

# connect to google 
lang = 'en-US'
timezone = 360

pytrends = TrendReq(hl=lang, tz=timezone)

# build payload

# list of keywords to get data 
kw_list = [
    "market",
    "science",
    "climate"
    ]

pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m') 

#1 Interest over Time
data = pytrends.interest_over_time() 
data = data.reset_index() 


# import plotly.express as px

# fig = px.line(data, x="date", y=kw_list, title='Keyword Web Search Interest Over Time')
# fig.show() 


# pytrends.get_historical_interest(
#     kw_list, 
#     year_start=2021, 
#     month_start=9, 
#     day_start=1, 
#     hour_start=0, 
#     year_end=2021, 
#     month_end=9, 
#     day_end=30, 
#     hour_end=0, 
#     cat=0, 
#     sleep=0
# )


start_date = {
    "year_start": 2021,
    "month_start": 9,
    "day_start": 1,
    "hour_start": 0,
}
end_date = {
    "year_end": 2021,
    "month_end": 9,
    "day_end": 1,
    "hour_end": 0,
}

h_data = pytrends.get_historical_interest(
    kw_list, 
    **start_date,
    **end_date,
    cat=0, 
    sleep=0
)


print(h_data)