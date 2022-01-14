from flask import Flask, request

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hi, Welcome to the locator app"

