""" 

"""
import datetime

def submission_analytical_view(raw_submission) -> str:
    submission_text = f""" 
ID: {raw_submission.id}
Title: {raw_submission.title}
Author: {raw_submission.author}
Created: {raw_submission.created_utc}
Name: {raw_submission.name}
Number of Comments: {raw_submission.num_comments}
Upvotes: {raw_submission.score}
Subreddit: {raw_submission.subreddit}
ratio: {raw_submission.upvote_ratio}
url: {raw_submission.url}
shortlink: {raw_submission.shortlink}
permalink: {raw_submission.permalink}
selftext: {raw_submission.selftext}
"""
    return submission_text


def submission_working_view(raw_submission) -> str:     
    """   
    _________________________________________________________________
    [r/cscareerquestions] ~ u/whydidIdothis3920 | 1597890118.0
    `
    Why did I spend 4 year getting a CS degree for Web Development 
    when people doing coding bootcamp for a few weeks and are able 
    to get same jobs? [id1tug]
    `
    https://redd.it/id1tug

    1676 comments  7114 upvotes 4582 downvotes  
    _________________________________________________________________

    # Prototype 2
        
_________________________________________________________________
Why did I spend 4 year getting a CS degree for Web Development...
[r/cscareerquestions] by u/whydidIdothis3920
-----------------------------------------------------------------

What the hell?

Did I waste my time doing CS if I want to get into web dev?

Seem like CS is more for thing like embedded engineering, data engineering, etc.

What is point of CS degree if i want to become web dev???

08-19-2020 - https://redd.it/id1tug
-----------------------------------------------------------------
1676 comments  7117 upvotes 454 downvotes
-----------------------------------------------------------------

    """
    bot_sep = 65*'_'
    mid_sep = 65*'-'

    title = f"{raw_submission.title[:62]}..."
    subreddit = f"r/{raw_submission.subreddit}"
    user = f"u/{raw_submission.author}"
    converted_date = datetime.datetime.fromtimestamp(raw_submission.created_utc).strftime("%m-%d-%Y")
    main_text = f"{raw_submission.selftext}"
    short = f"{raw_submission.shortlink}"
    comment_num = f"{raw_submission.num_comments}"
    ratio = float(f"{raw_submission.upvote_ratio}")
    upvotes = int(f"{raw_submission.score}")
    total_votes = int(upvotes/ratio)
    down_votes = total_votes - upvotes


    submission_text = f"""
{bot_sep}
{title}
[{subreddit}] by {user}
{mid_sep}

{main_text}

{converted_date} ~ {short}
{mid_sep}
{comment_num} comments  {upvotes} upvotes {down_votes} downvotes
{mid_sep}
"""
    return submission_text

