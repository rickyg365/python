import os
from utils.load_save import save_json, load_json

# But What if we change these, the order in which I write the tests matters, 
# I need to run test_save_json() first to create the file that will be tested 
# by test_load_json()
GLOBAL_TEST_PATH = "data/test_data.json"
GLOBAL_TEST_DATA = {
        "key 1": 1,
        "key 2": "test_string",
        "key 3": [1, "2", 1 + 2]
    }

def test_save_json():
    """ Is this the best way to test saving a file lmao, prob not """
    save_json(GLOBAL_TEST_DATA, GLOBAL_TEST_PATH)
    assert os.path.exists(GLOBAL_TEST_PATH)

def test_load_json():
    read_data = load_json(GLOBAL_TEST_PATH)
    assert read_data == GLOBAL_TEST_DATA

def run_tests():
    tests = [
        test_save_json,
        test_load_json
    ]

    result_map = {
        "pass": '.',
        "fail": 'x'
    }

    result_map_str = "  ".join([f"[{symbol}] {state}" for state, symbol in result_map.items()])
    for test in tests:
        try:
            test()
            result = True
        except AssertionError:
            result = False
        
        result_char = result_map['pass'] if result else result_map['fail']

        # Display Result        
        print(f"[{result_char}] {test.__name__}")
    print(f"Legend: {result_map_str}")

