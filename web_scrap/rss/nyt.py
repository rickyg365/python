import os
import feedparser

""" 
URL: https://rss.nytimes.com/services/xml/rss/nyt/World.xml


Entry Keys:

    [title]: str
    [title_detail]: Dict[str, str] -> 'language', ...
    [links]: List[Dict[str, str]] -> select item form list, item['href'] to get url
    [link]: or just use this one lmaoooo
    [id]: or this one???? is it the same link always?
    [guidislink]: bool
    [summary]: str
    [summary_detail]: same as title_detail   
    [published]: str/datetime?
    [published_parsed]: time.struct_time  
    [tags]: List[Dict[str, str]] -> keys: 'term', 'scheme', 'label'
"""


feed_url = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"


feed = feedparser.parse(feed_url)

first_entry = feed.entries[0]


cols, rows = os.get_terminal_size()
count = 0
for entry in feed.entries:
    if count > 5:
        break
    # Get Data
    title = entry['title']
    source = entry['link']
    summary = entry['summary']
    pub_time = entry['published']
    all_tags = entry.get('tags', list())

    cleaned_tags = []
    tag_text = ""
    for tag in all_tags:
        cleaned_tags.append(tag['term'])
        tag_text += f"[{tag['term']}] "
    
    # Format into output
    final_text = f"{'-'*cols}\n"

    # Can add tags after summary seperator {tag_text}
    final_text = f"""

[{pub_time[:-6]}]
{title}
{'_'*cols}
{summary}
{'_'*cols}  
{source}
"""
    count += 1
    print(final_text)






