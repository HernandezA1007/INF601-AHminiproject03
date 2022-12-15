# INF601 - Advanced Programming in Python
# Antonio Hernandez
# Mini Project 3

# Proper import of packages used.
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()  # debug=True in ()

# Using Flask you need to setup the following:
    # Setup a proper folder structure, use the tutorial as an example.
    # You need to have a minimum of 5 pages, using a proper template structure.
    # You need to have at least one page that utilizes a form and has the proper GET and POST routes setup.
    # You need to setup a SQLlite database with a minimum of two tables, linked with a foreign key.
    # You need to use Bootstrap in your web templates. I won't dictate exactly what modules you need to use but the
    #       more practice here the better. You need to at least make use of a modal.
    # You need to setup some sort of register and login system, you can use the tutorial as an example.

# https://www.jetbrains.com/help/pycharm/creating-web-application-with-flask.html

# Folder Structure done, Jetbrains/Web App pages, form for register/login done, followed flaskr tutorial
# SQLlite used to store accounts and list, Bootstrap broken, database and app broke with "site package"?