from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/puppy1")
def puppy1():
    return render_template('puppy1.html')

@app.route("/puppy2")
def puppy2():
    return render_template('puppy2.html')
