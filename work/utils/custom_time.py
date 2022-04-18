from typing import Dict
from dataclasses import dataclass

@dataclass
class Time:
    hour: int = 12
    minute: int = 0
    second: int = 0
    am: bool = True

    def __str__(self) -> str:
        time_period = 'AM' if self.am else 'PM'

        txt = f"{self.hour:02}:{self.minute:02}:{self.second:02} {time_period}"
        return txt
    
    def __sub__(self, other) -> int:
        hdiff = self.hour - other.hour       
        mdiff = self.minute - other.minute
        sdiff = self.second - other.second

        seconds_diff =  (hdiff * 3600) + mdiff * 60 + (sdiff)
        return seconds_diff//60 # Rough distance in minutes
    
    def export(self) -> Dict[str, any]:
        return {
            "hour": self.hour,
            "minute": self.minute,
            "second": self.second,
            "am": self.am
        }


def main():
    new_time = Time(3,23,am=False)
    print(new_time)

if __name__ == '__main__':
    main()
