# simple-flask-app
Simple use case of Flask to build a web app

---
## Steps
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

