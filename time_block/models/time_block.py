from typing import List, Dict
from dataclasses import dataclass, field

from utils.custom_time import Time
from views.time_block_view import TimeBlockView


@dataclass
class TimeBlock:
    title: str
    description: str = ""
    start_time: Time = field(default_factory=Time())
    end_time: Time = field(default_factory=Time(1))
    size: int = 30

    def __post_init__(self):
        self.view = TimeBlockView(self.size)

    def __str__(self) -> str:
        data_str = f"""
Title: {self.title}
Description: {self.description}
Start Time: {self.start_time}
End Time: {self.end_time}
"""

        if self.view is None:
            return data_str
         
        detailed_str = self.view.print(self.export())
        return detailed_str
    
    def export(self) -> Dict[str, any]:
        export_data = {
            "title": self.title,
            "description":  self.description,
            "start_time": self.start_time.export(),
            "end_time": self.end_time.export()
        }
        return export_data


def main():
    block_data = {
        "title": "Test Block",
        "description": "This is just a sample test block!",
        "start_time": Time(2, am=False),
        "end_time": Time(2, 30, am=False)
    }
    new_block = TimeBlock(**block_data)
    print(new_block)

    t1 = block_data["start_time"]
    t2 = block_data["end_time"]

    print(t2 - t1, "minute difference")


if __name__ == '__main__':
    main()
