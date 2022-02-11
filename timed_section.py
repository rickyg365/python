import os

import time
import functools


def progress_bar(current_val, max_val, bar_width=20):
    # Calculate ratio of current/max
    ratio = current_val/max_val
    # Can also use floor div above, but may introduce an early rounding error
    final_current = int(ratio*bar_width)

    return f"[{final_current*'#':<{bar_width}}]"

def timed_section(func):
    """ A decorator for timing a code section """
    @functools.wraps(func)
    def timer(*args, **kwargs):
        # Start Time
        start_time = time.perf_counter()

        # Wrapped Function
        final_value = func(*args, **kwargs)
        
        # End Time
        end_time = time.perf_counter()
        # Total Time Elapsed
        total_time = end_time - start_time

        print(f"[ {func.__name__} ]: {total_time:.2f}")
        
        return final_value
    return timer


@timed_section
def waste_time(end_time=2):
    print("running function")
    time.sleep(end_time)
    print("finished")

@timed_section
def kill_time(end_time=15):
    ref_time = time.perf_counter()

    while True:
        current_time = time.perf_counter() - ref_time
        new_bar = progress_bar(current_time, end_time)

        print(f"{current_time:.1f} {new_bar}", end="\r")
        
        if current_time >= end_time:
            print(f"{30*' '}", end="\r")
            return
        time.sleep(.1)
        

if __name__ == "__main__":
    waste_time()
    kill_time()
