import os
import instaloader


def main():
    username = "pau.codes"
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
    
    posts = instaloader.Profile.from_username(ig.context, username).get_posts()

    max_count = 5
    
    for _, post in enumerate(posts):
        if _ == 5:
            return
        ig.download_post(post, f"{username}_{_}")

if __name__ == '__main__':
    main()


