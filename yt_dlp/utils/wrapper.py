import yt_dlp
from typing import Dict, List, Callable


from file_handler import save_json

def extract_info(url: str, filename: str=None, download: bool=False):
    info = None
    ydl_opts = {}
    save = False if filename is None else True


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url=url, download=download)

        if save:
            save_json(info, filename)
    
    return info

def download_from_url(urls: List[str], opts: Dict=None):
    info = None
    ydl_opts = {} if opts is None else opts
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)


def download_from_info_file(filename: str):
    with yt_dlp.YoutubeDL() as ydl:
        error_code = ydl.download_with_info_file(filename)
    
    print("Video failed to downlaod" if error_code else "Video downloaded successfully")
