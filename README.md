# Terminal/CMD reddit Browser

Hello! Welcome to a recreate of something that probably already exists. I just wanted to write it from scratch myself.

This is basically a plain-text way to view reddit posts. To view instructions on things you can modify to tailor to your browsing habits, scroll down to the "Instructions" Section.

First and Foremost, don't file issue reports on Github. I don't look at them. If there's a problem, DM me on Reddit (Kapow-bitch is my username.)


To use this program, follow these instructions:

- Install Python3. Python2 will not work. For this reason, I discourage use on Linux unless you know what you're doing. It's frustrating to switch to Py3 as Py2 is default on Linux)
- Install Praw(latest version. Do this by going into cmd and typing "Pip install praw" (note: you must have Python installed to do this))
- Create an app in the Reddit settings. To do that, follow these steps:
    - Go to https://www.reddit.com/prefs/apps
    - scroll down until you see "Create another app" or if you're not a nerd like me, click the box that says "Are you a developer? Create an app..." or sum like that. I don't wanna delete my apps to find out. You get the point.
    - name it whatever you would like.
    - You will see 3 selection options. "Web app," "Installed app," and "Script." For this, you will choose "Script."
    - Description: Just type jibberish text in this box.
    - About URL: just type "http://www.example.com." (Without quotes)
    - Redirect URL: Same as About URL.
    - Click "Create app"
    - Keep this tab open for the next step
- You will next need to setup the Praw.ini file. I have included a shell file for you within the repo. (No it does not have my credentials. I'm not that dumb. I know that may come as a shock to some.)
    - Open the praw.ini file from the repository.
    - Open the tab with the app you just created.
    - client_id: 2 spaces underneath your script name is the client_id. Copy and paste that into your Praw.ini file under "client_id"
    - client_secret: You will see something in the applet page you just created that says "Secret." The code to the right of that is your client secret. Copy and paste that into the client secret portion of the praw.ini file.
    - password: your reddit password
    - username: your reddit username
    - user_agent: Enter jibberish here. I just put "Idk" (without the quotes.)
- Run the main.py program. All the parts of the program will run within this one file. I finally fixed the inbox reader. Thanks Reddit.
- Text editor: If you don't have any special text editor other than notepad, I recommend geany. It's easier to run programs in geany. install geany from here: https://www.geany.org/download/releases/
- Open the program in geany. To run program in geany, simply press the F5 key.
- Thank You and I hope you enjoy this program!

# Intructions on use
Here is the portion that I finally promised to make (somehow I feel everyone who downloads this is lucky I became unlazy and decided to make this section...)

Anyways, I will run through all the lines of Main.py that you can edit to tailor to your browsing habits.

- Line 12: Subreddit switcher
  - Want to only browse a certain subreddit? Where it says "all", switch that to the one subreddit that you want to browse. Please note that you can only browse one sub at a time if you change this.

- Line 15: sort
  - You can change what posts you see. Hot, Top, New, controversial, or whatever the other options are. Where it says "new", just change that to whatever you're trying to see.

- Lines 16-23: subreddit exclusion.
  - if you want to see that sub, or you want to see stuff on over 18 subreddits, remove lines 20-23. If you want to exclude a different subreddit, replace "catloversyay2019" with the subreddit you don't want to see. Or if you agree with my filter, after the end quotes of "catloversyay2019" type:
  or "<subreddit name>"

- Line 24: Search
  - if you only want to see posts with a certain keyword in the title, in the empty quotes on line 24, type what keyword you want.
