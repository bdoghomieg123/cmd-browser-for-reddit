import praw
import time
import os
import re
from common import clear
from readinbox import readInbox



reddit=praw.Reddit('bot1')

subreddit = reddit.subreddit('all')
posts_already_seen = []
while True:
    for submission in subreddit.new(limit=10):
        if submission.subreddit == "catloversyay2019": #this subreddit is just weird man. check it out for yourself if you don't believe me.
            print("nah lol this sub weird")
            time.sleep(2)
            clear()
        if submission.subreddit.over18 == True: #Lol Not letting you see that stuff by default. 
            print("This subreddit is NSFW")
            time.sleep(2)
            clear()
        elif re.search("",submission.title,re.IGNORECASE):
            if submission.is_self:
                if submission.id not in posts_already_seen:
                    print("This was posted in", submission.subreddit,'\n')
                    print(submission.title,'\n')
                    print(submission.selftext,'\n')
                    posts_already_seen.append(submission.id)
                    commentAsk = input("Would you like to comment on this?[y/n]")
                    if commentAsk.lower() == "y":
                        clear()
                        user_reply = input("What would you like to reply to this post?")
                        submission.reply(user_reply)
                        clear()
                        print("Replied to",submission.title)
                        time.sleep(2)
                        clear()
                    elif commentAsk.lower() == "n":
                        clear()
                        print("Ok...\n")
                    upvote_ask = input("Would you like to upvote this?[y/n]\n")
                    if upvote_ask.lower() == "y":
                        clear()
                        submission.upvote()
                        print("post upvoted")
                        time.sleep(2)
                    elif upvote_ask.lower() == "n":
                        clear()
                        print("ok moving on...")
                    time.sleep(2)
                    clear()


                    """
                    Everything below this line is broken Don't uncomment unless you know what you're doing.
                    It's an attempt at integrating the readinbox file to make everything run from one file. However, I've yet to figure out how to differentiate
                    comments on posts from private messages. Feel free to fix this

                    readOrNah = input("Do you want to read your inbox?[y/n]")
                    if readOrNah.lower() == "y":
                        readInbox()
                    elif readOrNah.lower() == "n":
                        print("Ok. Going to next post")
                        time.sleep(2)
                        clear()
                        """
