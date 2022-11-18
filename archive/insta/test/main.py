import os
import sys
import shutil

import time

import instaloader

def get_args(default_value: str="thv"):
    args = sys.argv

    # if length != 2: Return Default
    if len(args) == 2:
        return sys.argv[1]
    
    # Default
    return default_value


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


# Handle Files
def group_by_subname(target: str, dir_path: str):
    # Create new final dir (if not already exists)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    # Get all file names, from main source
    for item in os.listdir():
        # Split each name w/ "_"
        t  = item.split("_")[0]
        
        if t != target:
            continue

        # if split[0] == target: add to new dir
        # Move file
        try:
            shutil.move(item, dir_path)
        except shutil.Error as shutil_error:
            # print(shutil_error)
            rewrite = input(f"Rewrite {item}?: ")
            if rewrite != "y":
                continue
            
            new_name = input(">>> ")
            shutil.move(item, f"{dir_path}/{new_name}")
            
        print(f"Move: {item} -> {dir_path}/")

    return


def main():
    ig = instaloader.Instaloader()

    username = get_args(default_value="dianaspartyrentals")
    
    # Built in Method
    # ig.download_profile(username)
    
    # Custom Methods
    # download_all_user_posts(username, ig)
  
    group_by_subname(
        target=username,
        dir_path=f"user/{username}"
    )


if __name__ == '__main__':
    main()


