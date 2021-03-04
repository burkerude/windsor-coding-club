#!/usr/bin/env python3
from flask import Flask, render_template
import random

app = Flask(__name__)

#set max age for cached pages to zero
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#Routes
@app.route("/")
def root():
    return render_template("home.html").replace("background.JPEG", f"backgrounds/{random.randint(0, 3)}.JPEG")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug=False, port=5000)
