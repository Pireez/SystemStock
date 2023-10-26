from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')

app.run(debug=True)