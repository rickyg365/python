import os

from typing import Dict, List
from datetime import datetime
from dataclasses import dataclass


def parse_raw_data(raw_entry: Dict):
    parsed_item = {}

    # Get Data
    parsed_item['title'] = raw_entry.get('title', None)
    parsed_item["source"] = raw_entry.get('link', None)
    parsed_item["summary"] = raw_entry.get('summary', None)
    parsed_item["pub_time"] = raw_entry.get('published', None)
    raw_tags = raw_entry.get('tags', list())

    cleaned_tags = []
    for tag in raw_tags:
        cleaned_tags.append(tag['term'])

    parsed_item["all_tags"] = cleaned_tags
    
    return parsed_item


@dataclass
class NYT_ENTRY:
    title: str
    publication_data: datetime
    summary: str
    url: str
    tags: List[str]

    def __str__(self) -> str:
        return ""




def main():
    return

if __name__ == '__main__':
    main()
