from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, Mundo!"

app.run(debug=True)