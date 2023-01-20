# basic-quiz-app
## a sample quiz app meant for learning various modules like tkinter, requests, sqlite3, etc.

To use the app, first run ```database_gen.py``` and then run ```main_app_ui.py```.

## Introduction
This is a quiz app created with ```tkinter```, ```sqlite3``` and ```requests```. It has a user login system and shows a leaderboard of all users. The user data is stored in an sqlite database. 

The ```requests``` module is used to connect to the [quiz api](https://opentdb.com/api.php) and request quiz questions based on the user-provided information.

The app keeps track of the total and correct questions done by the user and uses this to provide a ranking on the leaderboard. 

```tkinter``` is used to provide a GUI-based interface for the user, allowing the user to click and select the options needed, along with hints provided for the register and login functions.
