'''
Meme Quiz
Author: 420s
'''
from flask import Flask, flash, redirect, render_template, url_for, flash, request, session

app = Flask(__name__)

@app.route("/")  # this sets the route to this page
def index():
    return render_template('index.html')    # provide the webpage

if __name__ == "__main__":  # checks if program is run as a script or imported as module, and runs only if as script
    app.run(debug=True, host='0.0.0.0')   # at 127.0.0.1:5000
