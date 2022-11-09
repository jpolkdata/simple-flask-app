from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/date")
def date():
    return "This page was served at " + str(datetime.now())

view_count = 0
@app.route("/views")
def views():
    global view_count
    view_count += 1
    return "This page has been viewed " + str(view_count) + " times"