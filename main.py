import flask
from flask import *
from tkinter import *

app = Flask(__name__)

@app.route('/<name>')
def home(name):
     return render_template('web.html')

@app.route('/')
def index():
    return "Hi there! Welcome to the Flask app."

if __name__ == '__main__':
    app.run()
