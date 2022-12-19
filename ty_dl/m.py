import os
import sys

import yt_dlp

"""
# ydl_opts = {
#     # 'match_filter': longer_than_a_minute,
# }

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     error_code = ydl.download(PLAYLIST_URL)

# if error_code:
#     print("fuck something broke")
"""

def download_playlist(playlist_url, options=None):
    # Options
    if options is None:
        options = {}

    # Downlaod    
    with yt_dlp.YoutubeDL(options) as ydl:
        error_code = ydl.download(playlist_url)

    # Feedback
    if error_code:
        return False
    
    return True


def longer_than_a_minute(info, *, incomplete):
    """Download only videos longer than a minute (or with unknown duration)"""
    duration = info.get('duration')

    if duration and duration < 60:
        return 'The video is too short'


if __name__ == "__main__":
    # PLAYLIST_URL = 'https://youtube.com/playlist?list=PLD85eRe7NELF7EFIl4YMQOxFw_3S7LNaR'
    PLAYLIST_URL = sys.argv[1] if len(sys.argv) > 2 else 'https://youtube.com/playlist?list=PLD85eRe7NELF7EFIl4YMQOxFw_3S7LNaR'

    options = {
        # 'match_filter': longer_than_a_minute
        'output': "%(playlist)s/%(title)s.%(ext)s"
    }

    status = download_playlist(PLAYLIST_URL, options)

    if not status:
        print("oops...")
