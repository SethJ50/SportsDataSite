""" from website import create_app

app = create_app()

if __name__ == '__main__': # only runs if you run this file directly
    app.run(debug=True) """

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello, world"


if __name__ == "__main__":
    app.run(debug=True)

