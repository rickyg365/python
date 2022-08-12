import os

import instaloader

from utils.handle_files import get_args, group_by_subname
from utils.download_posts import download_all_user_posts, download_user_posts


def main():
    ig = instaloader.Instaloader()

    username = get_args(default_value="astyles_thebarber")
    
    # Built in Method
    # ig.download_profile(username)
    
    # Custom Methods
    download_user_posts(username, 25, ig)
  
    group_by_subname(
        target=username,
        dir_path=f"user/{username}"
    )


if __name__ == '__main__':
    main()
