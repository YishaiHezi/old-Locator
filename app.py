from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi! this is the locator app 1"

app.run()

