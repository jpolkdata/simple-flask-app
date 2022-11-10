# simple-flask-app
Simple use case of Flask to build a web app

---
## Getting started
Rather than specifying the app variables on the terminal we set them via the **.env** file so that get automatically loaded as we run our app. That file contains these variables:

    FLASK_APP = app.py
    FLASK_DEBUG = true
    FLASK_RUN_PORT = 5000

---
## The Model-Template-View (MTV) pattern
Every modern web framework follows the same basic pattern called model-template-view. This is a set of best practices for organizing the code.

There are three types of components - models, templates, and views. Each has a clear responsibility. 

- **Models** refers to the data model layer. This would usually be a database such as MySQL or Oracle, but Flask does not provide a built-in data layer. To keep this app simple we instead connect to a file that contains JSON data.

- **Views** are the behavior layer and are Python functions which are mapped to URLs in our app

- **Templates** are the presentation layer and are components that will generate HTML and display data to our users. Flask expects these to be stored in a 'templates' folder within the project. For this project we are using a library called Jinja which allows us to generate dynamic HTML.

Outside of the Python world this will be referred to instead as the Model-View-Controller model, but is functionally the same.

---
## Images
I've used a comic book photograph for the welcome page. This image is courtesy of Erik Mclean via the Unsplash photo gallery. The photo is free for commercial and non-commerical use under the Unsplash License.

https://unsplash.com/photos/LSPUdV6IWsY