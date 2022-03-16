import os
from typing import Callable, List

from sample import API
from utils.progress_bar import progress_bar

"""
ToDo:
    Maybe implement a Result return type

    -> result -> (bool, return_obj)

    EX.
        return True, self.get_get_data_point(1)

"""
def create_instance():
    file_path = "data/test_path.json"
    return API(file_path)


def test_instantiate():
    file_path="data/test_path.json"
    try:
        new_api_instance = API(file_path)
        # print(new_api_instance)
    except Exception as e:
        return False
    return True

def test_show_all_data():
    test_instance = create_instance()
    if test_instance is None:
        return False

    # test_instance.show_all_data()
    return True

def test_random_entry():
    test_instance = create_instance()
    if test_instance is None:
        return False
    test_random_entry = test_instance.get_random_data_point()
    return True

def test_get_data_entry():
    test_instance = create_instance()
    if test_instance is None:
        return False

    sample_entry = test_instance.get_data_point(1)
    return True

def test_load_data():
    test_instance = create_instance()

    if test_instance is None:
        return False

    test_load_data_path = "data/sample_data.json"
    test_instance.load_data(test_load_data_path)
    return True

def run_tests(list_of_tests: List[Callable], terminal_width:int):
    success = "[ Pass ]"
    failure = "[ Fail ]"
    for test in list_of_tests:
        test_status = test()

        print(f"{success if test_status else failure}: {test.__name__}")


if __name__ == "__main__":
    t_w, t_h = os.get_terminal_size()
    
    tests = [
        test_instantiate,
        test_get_data_entry,
        test_random_entry,
        test_load_data,
        test_show_all_data,
    ]

    run_tests(tests, t_w)
