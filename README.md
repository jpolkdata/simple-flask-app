# simple-flask-app
Simple use case of Flask to build a web app

---
## Getting started
Create a python script called app.py that contains this code

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, Flask!"

Then on the terminal set the env variables and run the app
    set FLASK_APP=app.py
    set FLASK_ENV=development
    flask run

The terminal will output the url for you to view the app in your browser

Now you will be running the app in development mode and can continue making changes. If you hit an error you may receive a page with detailed information. Some of these error messages would be a security risk for a production site, but they are included because we specifically set our FLASK_ENV variable to 'development'

---
## How Flask maps urls to view functions
Since the name of our script is app.py, the name of our app is actually 'app'. If we stop Flask and start the
Python interpreter 

    python

Now we can run the commands below to import our app. The naming here is funky since we actually called our script 'app', so really you reference it as app.app
    >>> import app
    >>> app.app
    <Flask 'app'>

Now call the **url_map** attribute command to see how the urls map
    >>> app.app.url_map
    Map([<Rule '/static/<filename>' (GET, HEAD, OPTIONS) -> static>,
    <Rule '/' (GET, HEAD, OPTIONS) -> home>,
    <Rule '/date' (GET, HEAD, OPTIONS) -> date>,
    <Rule '/views' (GET, HEAD, OPTIONS) -> views>])
    >>>

So we can see an entry for each url we defined in our code. It also shows which view function each of those maps to, as well which HTTP methods each of those supports (i.e. GET, HEAD, OPTIONS).

The '/static/<filename>' mapping is added by default, meaning anything you put into the '/static' path in the project will be included automatically. This makes it easy for us to include things like images, CSS and JavaScript to our app.
