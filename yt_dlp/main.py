import os


from test_suite import run_suite

from utils.wrapper import extract_info, download_from_url, download_from_info_file


'''
ydl_opts = {
    'format': 'm4a'
}


URLS = ['https://www.youtube.com/watch?v=']

def longer_than_a_minute(info, *, incomplete):
    """Download only videos longer than a minute (or with unknown duration)"""
    duration = info.get('duration')
    if duration and duration < 60:
        return 'The video is too short'

ydl_opts = {
    'match_filter': longer_than_a_minute,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)
'''



URLS = ["https://www.youtube.com/watch?v=AOrYKHwymIQ"]
URL = URLS[-1]
INFO_PATH = "sample.info.json"



if __name__ == "__main__":
    # Run Test
    run_suite()

    # Get Info
    # info = extract_info(URL, filename=SAMPLE_INFO_PATH)
    
    # Download from Url
    download_from_url(URLS, opts={'format': 'mp4'})

