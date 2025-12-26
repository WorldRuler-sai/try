from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "We! <H1>DDDD</H1>"

if __name__ == '__main__':
    app.run()