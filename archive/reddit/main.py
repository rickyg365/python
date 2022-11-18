import os
import praw

from typing import List, Dict

from utils.handle_env import load_env_var
from utils.analyze_obj import analyze_list

from models.submission.submission_view import submission_analytical_view, submission_working_view

""" 


"""
'''
    author  ->  Provides an instance of Redditor.
    comments  ->  Provides an instance of CommentForest.   
    created_utc  ->  Time the submission was created, represented in Unix Time.
    id  ->  ID of the submission
    is_self  ->  Whether or not the submission is a selfpost (text-only).
    self_text  ->  submissions selftext - an empty string if a link post.
    name  ->  Fullname of the submission
    num_comments  ->  number of comments 
    permalink  ->  A permalink for the submission.
    poll_data  ->  A PollData object representing the data of this submission, if it is a poll submission.
    score  ->  number of upvotes 
    subreddit  ->  Provides an instance of Subreddit.
    title  ->  title of the submission.
    upvote_ratio  ->  percentage of upvotes from all votes
    url  ->  URL the submission links to, or the permalink if a selfpost.
    
    '''

def main():
    # Load in env variables
    CLIENT_ID, CLIENT_SECRET = load_env_var(
        env_path="token.env", 
        key_list=["CLIENT_ID", "CLIENT_SECRET"]
        )

    # Create Reddit instance
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent = "Test Submission Script (by u/rickyg3)",
    )


    # Access data
    # subreddit_name = "cscareerquestions"
    # # subreddit = reddit.subreddit(subreddit_name).hot(limit=5)
    
    def build_feed(sub_name: str="all", sort_by: str="top", amount: int=10):
        match sort_by:
            case "hot":
                return reddit.subreddit(sub_name).hot(limit=amount)
            case "top":
                return reddit.subreddit(sub_name).top(limit=amount)
            case "new":
                return reddit.subreddit(sub_name).new(limit=amount)
            case _:
                return None
    
    def input_custom_feed():
        sub = input("Subreddit: ")
        sort_by = input("Sort: ")
        amount = int(input("How many posts?: "))

        return build_feed(sub, sort_by, amount)

    welcome_txt = "Welcome to Reddit TUI"
    print(f"\n{welcome_txt:<65}\n{'-'*65}")
    # Pre Chosen
    # top_five_all = reddit.subreddit("all").top(limit=5)
    # hot_ten_all = reddit.subreddit("all").hot(limit=5)
    # top_five_pokemon = reddit.subreddit("pokemon").top(limit=5)
    # hot_five_pokemon = reddit.subreddit("pokemon").hot(limit=5)
   
    # top_five_all = build_feed(sub_name="all", sort_by="top", amount=5)
    # hot_ten_all = build_feed(sub_name="all", sort_by="top", amount=5)
    # top_five_pokemon = build_feed(sub_name="pokemon", sort_by="top", amount=5)
    # hot_five_pokemon = build_feed(sub_name="pokemon", sort_by="hot", amount=5)

    # options = {
    #     "top_five_all": top_five_all,
    #     "hot_ten_all": hot_ten_all,
    #     "top_five_pokemon": top_five_pokemon,
    #     "hot_five_pokemon": hot_five_pokemon
    # }

    # choices = "\n".join([f"* {x}" for x in options.keys()])
    # while True:
    #     print(choices)
    #     u_input = input("\n>>> ")
    #     if u_input == 'q':
    #         break

    #     chosen_item = options[u_input]

    #     for submission in chosen_item:
    #         new_view = submission_working_view(submission)
    #         # new_view = submission_analytical_view(submission)
    #         print("\n", new_view)
    #         input("")

    # Custom Feed
    while True:
        new_feed = input_custom_feed()
        print(f"{'-'*65}\n")
        
        # Post by Post
        # for submission in new_feed:
        #     new_view = submission_working_view(submission)
        #     # new_view = submission_analytical_view(submission)
        #     print("\n", new_view)
        #     input("")

        # Scroll Feed
        spacer = '|'
        scrollable_feed = f"/\n/".join([submission_working_view(submission) if submission.is_self else submission_analytical_view(submission) for submission in new_feed])
        print(scrollable_feed)

        u_input = input("\n>>> ")
        if u_input == 'q':
            break        


if __name__ == '__main__':
    main()
 