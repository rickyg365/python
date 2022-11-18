from typing import List, Dict
from datetime import datetime
from dataclasses import dataclass


"""
@Function 
parse_raw_data(raw_entry: Dict)
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


def parse_raw_data(raw_entry: Dict):
    parsed_item = {}

    # Get Data
    parsed_item['title'] = raw_entry.get('title', None)
    parsed_item["url"] = raw_entry.get('link', None)
    parsed_item["summary"] = raw_entry.get('summary', None)
    
    raw_datetime = raw_entry.get('published', None)
    raw_tags = raw_entry.get('tags', list())

    # Clean Data
    if raw_datetime is not None:
        # Tue, 22 Mar 2022 01:14:01 +0000  *Remove the last 6 char
        date_format = "%a, %d %b %Y %H:%M:%S"
        parsed_item["publication_data"] = datetime.strptime(raw_datetime[:-6], date_format)

    cleaned_tags = []
    for tag in raw_tags:
        cleaned_tags.append(tag['term'])

    parsed_item["tags"] = cleaned_tags
    
    return parsed_item


@dataclass
class NYT_ENTRY:
    title: str
    publication_data: datetime
    summary: str
    url: str
    tags: List[str]
    width: int = 40

    def __str__(self) -> str:
        # Format into output
        final_text = f"""
[{self.publication_data}]
{self.title}
{'_'*self.width}
{self.summary}
{'_'*self.width}
{self.url}
"""
        return final_text

