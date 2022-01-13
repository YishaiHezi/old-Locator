###################### This file can be deleted:



from flask import Flask


app = Flask(__name__)

@app.route("/")
def main():
    return "Hi! this is the locator app 1"


