import flask
from flask import *
from tkinter import *

app = Flask(__name__)

# @app.route('/<name>')
# def home(name):
     # return render_template('web1.html')

@app.route('/')
def index():
    return "HHHHHHHHHHHHHHHHHHHHH-Chaitu"

if __name__ == '__main__':
    app.run()


