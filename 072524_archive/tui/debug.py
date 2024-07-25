"""
"""


def debug(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return inner
