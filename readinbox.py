import praw
import re
import os
import time
import random as rando
from common import clear
from praw.models import Message
from praw.models import Inbox


def readInbox():
    reddit=praw.Reddit('bot1')
    for x in range(1):
        for item in reddit.inbox.unread(limit=10):
            if isinstance(item, Message):
                print("This is a private message")
                time.sleep(2)
                clear()
                print(item.body , "\n")
                author = str(item.author)
                #subject_of_msg = input("What would you like the subject of this message to be?")
                body_of_msg = input("What would you like the body of the reply to be?\n")
                item.reply(body_of_msg)
                print("Message Sent To:",author)
                item.mark_read()
                clear()
            else:
                print("This is a submission reply\n")
                print(item.body)
                author = str(item.author)
                replyOrNah = input("Would you like to reply to this?[y/n]")
                if replyOrNah.lower() == "y":
                    clear()
                    user_comment_reply = input("What would you like to reply to this?")
                    item.reply(user_comment_reply)
                    print("Bot replied to", author)
                    item.mark_read()
                elif replyOrNah.lower() == "n":
                    print("Ok. moving on...")
                    item.mark_read()
                else:
                    item.mark_read()
