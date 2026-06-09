from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/boletim")
def boletim():
    return render_template('boletim.html')
