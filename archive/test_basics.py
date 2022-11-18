import os

import timeit
import numpy as np


def while_loop(n=100_000_000):
    while n:
        n -= 1
    return

def for_loop(n=100_000_000):
    for _ in range(n):
        pass
    return

def np_loop(n=100_000_000):
    for _ in np.arange(n):
        pass   
    return

def for_loop_sum(n=100_000_000):
    return sum(range(n))

def np_loop_sum(n=100_000_000):
    return np.sum(np.arange(n))  


def run_tests():
    my_test = {
        "For Loop": for_loop,
        "While Loop": while_loop,
        "Numpy Loop": np_loop,
        "For Loop Sum": for_loop_sum,
        "Numpy Loop Sum": np_loop_sum
    }

    for test_name, test_func in my_test.items():
        print(f"{test_name}: \t\t", timeit.timeit(test_func, number=1))
    
if __name__ == '__main__':
    run_tests()
