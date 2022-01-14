from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hi! this is the locator app 1"


