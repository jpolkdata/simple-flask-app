# from datetime import datetime
from flask import Flask, render_template
from data_model import db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "welcome.html",
        message="Here's a message from the view that is loaded via Jinja"
        )

@app.route("/superhero/<int:index>")
def superhero_view(index):
    return render_template("superheroes.html", superhero=db[index])

if __name__ == '__main__':
   app.run()