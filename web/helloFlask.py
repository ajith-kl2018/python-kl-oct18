from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<b>Hello World!</b>"

@app.route("/goodbye")
def goodbye():
    return "<strong>Goodbye World!</strong>"


if __name__ == "__main__":
    app.run()
