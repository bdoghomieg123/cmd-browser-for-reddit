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
        for message in reddit.inbox.unread(limit=10):
            #some if statement should most likely go here to check if it is a private message or submission reply. note line below
            print("this is a PM")
            time.sleep(2)
            clear()
            print(message.body , "\n")
            author = str(message.author)
            body_of_msg = input("What would you like the body of the reply to be?\n")
            reddit.redditor(author).message(body_of_msg)
            print("Message Sent To:",author)
            message.mark_read()
            clear()
