# from datetime import datetime
from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from data_model import db, save_db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("welcome.html", superheroes = db)

@app.route("/superhero/<int:index>")
def superhero_view(index):
    try:
        superhero = db[index]
        return render_template("superheroes.html"
            , superhero=superhero
            , index=index
            , max_index=len(db)-1)
    except IndexError:
        abort(404)

@app.route("/add_superhero", methods=["GET", "POST"])
def add_superhero():
    if request.method == "POST":
        # The user submitted a new hero
        superhero = {"Name": request.form['Name'],
            "Alias": request.form['Alias']}
        db.append(superhero)
        save_db()
        return redirect(url_for('superhero_view',index=len(db)-1))
    else:
        return render_template("add_superhero.html")

# REST API Endpoints
@app.route("/api/superhero/")
def api_superhero_list():
    return jsonify(db)

@app.route("/api/superhero/<int:index>")
def api_superhero_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)

if __name__ == '__main__':
   app.run()