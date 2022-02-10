from flask import Flask, request
import excel_tools

application = Flask(__name__)

@application.route("/")
def hello():
    x = excel_tools.foo(3)
    return f"Hiii, Welcome to the locator app version {x}."

