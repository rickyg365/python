
def parse_seconds(total_seconds: float):
    # Defaults
    seconds_per_hour = 60 * 60
    seconds_per_day = seconds_per_hour * 24

    days = 0
    hours = 0
    minutes = 0
    seconds = 0

    #! Method 1 - Floor Division and Modulus Operator
    # # Full Days, Time left in seconds
    # days, time_left = total_seconds//seconds_per_day, total_seconds%seconds_per_day

    # # Full hours
    # hours, total_minutes = time_left//seconds_per_hour, time_left%seconds_per_hour

    # # Full minutes
    # minutes, seconds = total_minutes//60, total_minutes%60

    #! Method 2 - DivMod
    # Full Days, Time left in seconds
    days, time_left = divmod(total_seconds, seconds_per_day)

    # Full hours, Time left in seconds
    hours, total_minutes = divmod(time_left,seconds_per_hour)

    # Full minutes, Time left in seconds
    minutes, seconds = divmod(total_minutes, 60)


    #! Method 3 - Custom Function
    # days, time_left = split_time(total_seconds, seconds_per_day)
    # hours, time_left = split_time(time_left, seconds_per_hour)
    # minutes, seconds = split_time(time_left, 60)  # seconds per minute

    return days, hours, minutes, seconds

