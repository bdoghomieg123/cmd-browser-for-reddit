# Terminal/CMD reddit Browser

Hello! Welcome to a recreate of something that probably already exists. I just wanted to write it from scratch myself.

This is basically a plain-text way to view reddit posts. I'll write more detailed instructions on use when I become un-lazy.

For now, you get instructions on how to set it up only (which were pre-written by me. You're welcome.)


To use this program, follow these instructions:

- Install Praw(latest version. Do this by going into cmd and typing "Pip install praw")
- Python3.x (Python2.x will not work. For this reason, I discourage use on Linux unless you know what you're doing. It's frustrating. To switch to Py3 as Py2 is default on Linux)
- Create an app in the Reddit settings. To do that, follow these steps:
    - Go to https://www.reddit.com/prefs/apps
    - scroll down until you see "Create another app"
    - name it whatever you would like.
    - You will see 3 selection options. "Web app," "Installed app," and "Script." For this, you will choose "Script."
    - description is optional. Just type jibberish text in this box if you so desire.
    - About URL: just enter "www.example.com." This field isn't absolutely necessary
    - Redirect URL: Same as About URL.
    - Click "Create app"
    - Keep this tab open for the next step
- You will next need to setup the Praw.ini file. I have included a shell file for you within the repo. (No it does not have my credentials. I'm not that dumb.)
    - Open the praw.ini file from the repository.
    - Open the tab with the app you just created.
    - client_id: 2 spaces underneath your script name is the client_id. Copy and paste that into your Praw.ini file under "client_id"
    - client_secret: You will see something in the applet page you just created that says "Secret." The code to the right of that is your client secret. Copy and paste that into the client secret portion of the praw.ini file.
    - password: your reddit password
    - username: your reddit username
    - user_agent: Enter jibberish here. I just put "Idk" (without the quotes.)
- Run the main.py program. (As of 8/4/19. The inbox reader is broken. Feel free to read my shit code. Godspeed if you attempt to fix it.)
- Text editor: If you don't have any special text editor other than notepad, I recommend geany. It's easier to run programs in geany. install geany from here: https://www.geany.org/download/releases/
- Open the program in geany. To run program in geany, simply press the F5 key.
- Thank You and I hope you enjoy this program!
