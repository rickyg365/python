import os

def get_fullscreen_url(raw_url:str) -> str:
    base_url, video_code = raw_url.split("=")

    return f"https://www.youtube.com/embed/{video_code}"

if __name__ == '__main__':
    ...

