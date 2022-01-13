###################### This file can be deleted:



from flask import Flask, render_template
import templates

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    print("hello, I'm in second page")
    app.run(debug=True, host="0.0.0.0", port=80)
