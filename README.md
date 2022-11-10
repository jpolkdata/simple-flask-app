# simple-flask-app
Simple use case of Flask to build a web app

---
## Getting started
Create a python script called starter_app.py that contains this code

    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, Flask!"

Then on the terminal set the env variables and run the app
    set FLASK_APP=starter_app.py
    set FLASK_ENV=development
    flask run

The terminal will output the url for you to view the app in your browser

Running the app in development mode allows the app to automatically reload changes that we make in our script, and provides access to teh Flash debugger.

Here is an example of a couple other 'view functions' we could add to our app. The URL must always start with a slash, and there is no connection between the URL and the function name (even though I chose to name them the same below)

    # Everytime you load the /date url it will display the current time
    @app.route("/date")
    def date():
        return "This page was served at " + str(datetime.now())

    # Everytime you load the /views page it will track the total number of times you have loaded the page
    view_count = 0
    @app.route("/views")
    def views():
        global view_count
        view_count += 1
        return "This page has been viewed " + str(view_count) + " times"

---
## How Flask maps urls to view functions
Since the name of our script is starter_app.py, the name of our app is 'starter_app'. If we stop Flask and start the Python interpreter...

    python

...now we can run the commands below to import our app...
    >>> import starter_app
    >>> starter_app.app
    <Flask 'app'>

...and then call the **url_map** attribute command to see how the urls map
    >>> starter_app.app.url_map
    Map([<Rule '/static/<filename>' (GET, HEAD, OPTIONS) -> static>,
    <Rule '/' (GET, HEAD, OPTIONS) -> home>,
    <Rule '/date' (GET, HEAD, OPTIONS) -> date>,
    <Rule '/views' (GET, HEAD, OPTIONS) -> views>])
    >>>

So we can see an entry for each url we defined in our code. It also shows which view function each of those maps to, as well which HTTP methods each of those supports (i.e. GET, HEAD, OPTIONS).

The '/static/<filename>' mapping is added by default, meaning anything you put into the '/static' path in the project will be included automatically. This makes it easy for us to include things like images, CSS and JavaScript to our app.

---
## The Model-Template-View (MTV) pattern
Every modern web framework follows the same basic pattern called model-template-view. This is a set of best practices for organizing the code.

There are three types of components - models, templates, and views. Each has a clear responsibility. 

- **Models** refers to the data model layer. This would usually be a database such as MySQL or Oracle, but Flask does not provide a built-in data layer. To keep this app simple we instead connect to a file that contains JSON data.

- **Views** are the behavior layer and are Python functions which are mapped to URLs in our app

- **Templates** are the presentation layer and are components that will generate HTML and display data to our users. Flask expects these to be stored in a 'templates' folder within the project. For this project we are using a library called Jinja which allows us to generate dynamic HTML.

Outside of the Python world this will be referred to instead as the Model-View-Controller model, but is functionally the same.

---
## Move the environment variables to a file
Rather than specifying the variables on the terminal, we can set these via a file. That way they get automatically loaded when we run our app.

Create a new file in the root of the project folder named **.env**. In this file we will place 3 variables:

    FLASK_APP = starter_app.py
    FLASK_DEBUG = true
    FLASK_RUN_PORT = 5000

The 'FLASK_DEBUG' variable here replaces the FLASK_ENV variable we were previously setting, and is the newer way to enable debugging functionality. We are also now specifying the port that we want out app to map to via 'FLASK_RUN_PORT'.