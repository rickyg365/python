import os
import sys

import instaloader

def get_args():
    args = sys.argv

    # if length != 2: Return Default
    if len(args) == 2:
        return sys.argv[1]
    
    # Default
    return "thv"

def download_user_posts(username: str, post_count: int, client: instaloader.Instaloader):
    posts = instaloader.Profile.from_username(client.context, username).get_posts()
    for _, post in enumerate(posts):
        if _ > post_count:
            return
        client.download_post(post, username)

def main():
    ig = instaloader.Instaloader()

    username = get_args()
    ig.download_profile(username)
    # download_user_posts(username, count, ig)

if __name__ == '__main__':
    main()


