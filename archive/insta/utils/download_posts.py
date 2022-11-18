import os
import sys

import instaloader


# Download Metered Posts
def download_user_posts(username: str, post_count: int, client: instaloader.Instaloader):
    """ Downloads Specified number of posts from selected user and saves each post in its own directory """
    posts = instaloader.Profile.from_username(client.context, username).get_posts()
    for _, post in enumerate(posts):
        if _ >= post_count:
            return
        curr_post_dir = f"{username}_{_+1}"
        client.download_post(post, curr_post_dir)

def download_user_posts_single_dir(username: str, post_count: int, client: instaloader.Instaloader):
    """ Downloads Specified number of posts from selected user and saves all in a single directory """
    posts = instaloader.Profile.from_username(client.context, username).get_posts()
    for _, post in enumerate(posts):
        if _ >= post_count:
            return
        client.download_post(post, username)


# Download All Posts
def download_all_user_posts(username: str, client: instaloader.Instaloader):
    """ Downloads all posts from selected user and saves each post in its own directory """
    posts = instaloader.Profile.from_username(client.context, username).get_posts()
    for _, post in enumerate(posts):
        curr_post_dir = f"{username}_{_+1}"
        client.download_post(post, curr_post_dir)


def download_all_user_posts_single_dir(username: str, client: instaloader.Instaloader):
    """ Downloads all posts from selected user and saves all in a single directory """
    posts = instaloader.Profile.from_username(client.context, username).get_posts()
    for _, post in enumerate(posts):
        client.download_post(post, username)



def main():
    return

if __name__ == '__main__':
    main()
