#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

@app.route("/<name>")
def greet_user(name):
    return "Hi, {}!!".format(name)


if __name__ == "__main__":
    app.run(debug=True)
