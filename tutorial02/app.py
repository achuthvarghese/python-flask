from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! Run Flask using code.</p>"


if __name__ == "__main__":
    app.run(debug=True)
