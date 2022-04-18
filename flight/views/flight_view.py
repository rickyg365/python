from utils.helper import parse_seconds


class SimplifiedView:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        # Format Time
        date_format = f"%m/%d/%y"
        time_format = f"%I:%M %p"
        date = self.departure_time.strftime(date_format)
        d_time = self.departure_time.strftime(time_format)
        a_time = self.arrival_time.strftime(time_format)

        total_days, total_hours, total_minutes, total_seconds = parse_seconds(self.duration)

        txt = f"""{'-'*60}
[ {self.airline} ]: {self.departure.code:^5}[{d_time:^8}]  -> {self.arrival.code:^5}[{a_time:^17}]  
{'-'*60}
Total Duration:  {total_hours:.0f}hr {total_minutes:.0f}min {total_seconds:.0f}sec"""
        return txt
    
    def update_data(self, new_data):
        # re update all attrs
        return

class FullDetailView:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        # Format Time
        date_format = f"%m/%d/%y %I:%M %p"

        d_time = self.departure_time.strftime(date_format)
        a_time = self.arrival_time.strftime(date_format)

        total_days, total_hours, total_minutes, total_seconds = parse_seconds(self.duration)

        txt = f"""\n[ {self.airline} ]: {self.departure.code:^5} -> {self.arrival.code:^5}
{'-'*60}
[{d_time:^17}]  {self.departure.name:^10}
[{a_time:^17}]  {self.arrival.name:^10}
{'-'*60}
Total Duration:  {total_hours:.0f}hr {total_minutes:.0f}min {total_seconds:.0f}sec"""
        return txt


def main():
    return

if __name__ == '__main__':
    main()
