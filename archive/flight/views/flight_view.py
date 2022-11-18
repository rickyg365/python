from utils.helper import parse_seconds


class SimplifiedView:
    def __init__(self, initial_data):
        self.data = initial_data
        self.cache = None

    def __str__(self) -> str:
        if self.cache is not None:
            return self.cache
            
        # Format Time
        date_format = f"%m/%d/%y %I:%M %p"

        d_time = self.data.departure_time.strftime(date_format)
        a_time = self.data.arrival_time.strftime(date_format)

        total_days, total_hours, total_minutes, total_seconds = parse_seconds(self.data.duration)

        # Convert into display string
        days = "" if total_days == 0 else f"{total_days:.0f}days"
        hours = "" if total_hours == 0 else f"{total_hours:.0f}hr"
        minutes = "" if total_minutes == 0 else f"{total_minutes:.0f}min"
        seconds = "" if total_seconds == 0 else f"{total_seconds:.0f}sec"

        txt = f"""\n[ {self.data.airline} ]: {self.data.departure.code:^5} -> {self.data.arrival.code:^5}
{'-'*60}
[{d_time:^17}]  {self.data.departure.name:^10}
[{a_time:^17}]  {self.data.arrival.name:^10}
{'-'*60}
Total Price: ${self.data.price}  Total Duration: {days} {hours} {minutes} {seconds}"""
        return txt
    
    def update_data(self, new_data):
        self.data = new_data
        self.cache = str(self)

class FullDetailView:
    def __init__(self, initial_data):
        self.data = initial_data
        self.cache = None

    def __str__(self) -> str:
        if self.cache is not None:
            return self.cache

        # Format Time
        date_format = f"%m/%d/%y %I:%M %p"

        d_time = self.data.departure_time.strftime(date_format)
        a_time = self.data.arrival_time.strftime(date_format)

        total_days, total_hours, total_minutes, total_seconds = parse_seconds(self.data.duration)

        # Convert into display string
        days = "" if total_days == 0 else f"{total_days:.0f}days"
        hours = "" if total_hours == 0 else f"{total_hours:.0f}hr"
        minutes = "" if total_minutes == 0 else f"{total_minutes:.0f}min"
        seconds = "" if total_seconds == 0 else f"{total_seconds:.0f}sec"

        txt = f"""\n[ {self.data.airline} ]: {self.data.departure.code:^5} -> {self.data.arrival.code:^5}
{'-'*60}
[{d_time:^17}]  {self.data.departure.name:^10}
[{a_time:^17}]  {self.data.arrival.name:^10}
{'-'*60}
Total Price: ${self.data.price}  Total Duration: {days} {hours} {minutes} {seconds}"""
        self.cache = txt
        return txt

    def update_data(self, new_data):
        self.data = new_data
        self.cache = str(self)


def main():
    return

if __name__ == '__main__':
    main()
