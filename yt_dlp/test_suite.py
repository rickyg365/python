import os
from typing import List, Dict, Callable
from utils.wrapper import extract_info, download_from_url, download_from_info_file


'''
Test
'''

TEST_URLS = ["https://www.youtube.com/watch?v=AOrYKHwymIQ"]
TEST_URL = TEST_URLS[-1]
TEST_INFO_PATH = "data/sample.info.json"


def test_info(url: str=TEST_URL, filename: str=TEST_INFO_PATH):
    # Get Info (save info)
    info = extract_info(url=url, filename=filename)

    # Download from Info File
    download_from_info_file(filename=filename)


    # Download While Getting Info
    # info = extract_info(URL, filename=SAMPLE_INFO_PATH, download=True)
    
    print(info)


def test_download_url(urls: List[str]=TEST_URLS):
    download_from_url(urls, opts={'format': 'mp4'})


def test_download_formats(urls: List[str]=TEST_URLS):
    # Video
    download_from_url(urls, opts={'format': 'mp4'})

    # Audio
    download_from_url(urls, opts={'format': 'm4a'})


TESTS = [test_download_formats, test_download_url, test_info]

def run_suite(tests: List[Callable]=TESTS):
    for test in tests:
        # Run test
        test()


if __name__ == "__main__":
    run_suite()
