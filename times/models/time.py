import os

from enum import Enum
from dataclasses import dataclass

# Time
@dataclass
class Time():
    military: int # 1-24
    minutes: int
    hours: int  # 12 hr format

    def __str__(self) -> str:
        am_pm = "am" if self.military <=12 else "pm"
        txt = f"{self.hours:02.0f}:{self.minutes:02} {am_pm}"
        return txt
    
    def export(self):
        return {
            "military": self.military,
            "minutes": self.minutes,
            "hours": self.hours
        }


# Time Block
@dataclass
class TimeBlock:
    title: str
    start_time: Time
    end_time: Time
    duration: float = 0.00

    def __str__(self) -> str:
        txt = f"{self.title}: {self.start_time} -> {self.end_time} [{self.duration:.2f} hrs]"
        return txt
        
    def export(self):
        return {
            "title": self.title,
            "start_time": self.start_time.export(),
            "end_time": self.end_time.export(),
            "duration": self.duration
        }

