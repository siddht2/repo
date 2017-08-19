from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return("<\h1>hello</h1>")

@app.route("/members")
def error():
    return("members page")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
