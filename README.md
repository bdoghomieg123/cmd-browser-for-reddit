# Terminal/CMD reddit Browser

Hello! Welcome to a recreate of something that probably already exists. I just wanted to write it from scratch myself.

This is basically a plain-text way to view reddit posts. I'll write more detailed instructions on use when I become un-lazy.

For now, you get instructions on how to set it up only (which were pre-written by me. You're welcome.)


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
- Run the main.py program. (As of 8/4/19. The inbox reader is broken. Feel free to read my shit code. Godspeed if you attempt to fix it.)
- Text editor: If you don't have any special text editor other than notepad, I recommend geany. It's easier to run programs in geany. install geany from here: https://www.geany.org/download/releases/
- Open the program in geany. To run program in geany, simply press the F5 key.
- Thank You and I hope you enjoy this program!
