from dataclasses import dataclass
import os
import datetime

from typing import List
from dataclasses import dataclass


@dataclass
class task:
    name: str
    description: str
    date: datetime.datetime
    url: str
    contact: str
    notes: str


if __name__ == '__main__':
    sample_job_data = {
        "company": "Linked In",
        "title": "Software Engineer",
        "description": "Welcome to LinkedIn, where helping people connect is our mission",
        "url": "https://www.LinkedIn.com",
        "contact": "Doug",
        "notes": "Very interested in the role would love to talk with someone currently in that position to get a better feel for the role and what it entails"
    }
    new_job = Job(**sample_job_data)
