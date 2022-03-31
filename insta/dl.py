import os
import instaloader


def main():
    ig = instaloader.Instaloader()
    settings = { 
        "fast_update": False, 
        "profile_pic": True,
        "profile_pic_only": False, 
        "download_stories": False, 
        "download_stories_only": False, 
        "download_tagged": False, 
        "download_tagged_only": False,

    }
    # ig.download_profile("profile_name")

if __name__ == '__main__':
    main()


