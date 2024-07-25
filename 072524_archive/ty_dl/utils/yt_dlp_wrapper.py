import yt_dlp

"""
Wrapper for yt_dlp to enable easier use
"""

def download_link(url, options=None):
    # No option case
    if options is None:
        options = {}

    print(options)

    with yt_dlp.YoutubeDL(options) as ydl:
        error_code = ydl.download(url)

    # Feedback
    if error_code:
        return False
    return True


def video_options(output_path=None):
    # Default Options for Playlist Download
    use_default = output_path is None
    output_path = "%(title)s.%(ext)s" if use_default else output_path

    options = {
        'output': output_path
    }

    # Download
    return options


def playlist_options(output_path=None):
    # Default Options for Playlist Download
    use_default = output_path is None
    output_path = "%(playlist)s/%(title)s.%(ext)s" if use_default else output_path

    options = {
        'output': output_path
    }

    # Downlaod
    return options
