###################### This file can be deleted:



from flask import Flask, render_template
import templates

app = Flask(__name__)

@app.route("\")
def main():
    return "Hi! this is the locator app 1"

if __name__ == "__main__":
    print("hello, I'm in second page")
    app.run()
