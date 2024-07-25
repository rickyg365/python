import os
import argparse

# External
import yt_dlp

"""
Youtube Downloader

Notes:
- look into using subparser for more customization w/ commands

references:
    yt_dlp:     https://github.com/yt-dlp/yt-dlp
    argparse:   https://docs.python.org/3/library/argparse.html
"""
# Setup Parser
parser = argparse.ArgumentParser(
    prog = 'YoutubeDownloader',
    description = 'Download a single youtube video or a whole playlist',
    epilog = 'main functionality provided by yt_dlp'
)

group = parser.add_mutually_exclusive_group()
group.add_argument('-s', '--single', action='store_true', help="single video download")
group.add_argument('-p', '--playlist', action='store_true', help="playlist download")

parser.add_argument('link', type=str)


if __name__ == "__main__":
    # Get Arguments
    args = parser.parse_args()  # Namespace

    DOWNLOAD_LINK = args.link
    OUTPUT_DIR = input("Choose a directory name: ")  # Find way to get playlist name

    # Options
    options = {}

    if args.single:  # Download single video
        URL_TYPE = "video"
        # options['output'] = "%(title)s.%(ext)s"

    if args.playlist:  # Download playlist
        URL_TYPE = "playlist"
        # options['output'] = "%(playlist)s/%(title)s.%(ext)s"
        
    # options['progress_hooks'] = [my_hook]

    # Download
    with yt_dlp.YoutubeDL(options) as ydl:
        error_code = ydl.download(DOWNLOAD_LINK)
    
    # Organize Files
    if not error_code:
        # Move videos into vid dir
        for file in os.listdir():
            is_video = file.endswith(".mp4")
            file_exist = os.path.exists(f"{URL_TYPE}/{OUTPUT_DIR}/{file}")
            
            if is_video and not file_exist:
                os.renames(file, f"downloads/{URL_TYPE}/{OUTPUT_DIR}/{file}")

    print(f"[{'error' if error_code else 'success'}] {URL_TYPE} Download: {DOWNLOAD_LINK}")
