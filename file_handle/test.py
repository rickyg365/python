from os import walk

from utils.directory_obj import DirectoryData

# Util
def display_os_walk(dir_name: str):
    for (dirpath, dirnames, filenames) in walk(dir_name):
        print(dirpath, dirnames, filenames)

# Test
def test_dir(test_path: str):
    dir_obj = DirectoryData(test_path)
    print(dir_obj)
    
def test_broken_dir(test_path: str):
    broken_obj = DirectoryData(test_path)
    print(broken_obj)

def test_empty_dir(test_path: str):
    empty_obj = DirectoryData(test_path)
    print(empty_obj)


if __name__ == '__main__':
    # Use a Path module instead of double backslash
    dir_name = "tests\\fake_dir"
    empty_dir_name = "tests\\empty_dir"
    broken_dir = "tests\\non_existent_dir"
    
    test_dir(dir_name)
    test_empty_dir(empty_dir_name)
    test_broken_dir(broken_dir)
