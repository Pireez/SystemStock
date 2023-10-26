from flask import Flask, render_template, request,redirect, session, flash, url_for

class Usuario:
    def  __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

usuario1 = Usuario("Gustavo","gustavo@gmail.com","123")
usuario2 = Usuario("Joe","joe@gmail.com","321")
usuario3 = Usuario("Lay","Lay@gmail.com","456")

usuarios = {usuario1.email : usuario1,
            usuario2.email : usuario2,
            usuario3.email : usuario3}


app = Flask(__name__)
 

@app.route("/")
def login():
    return render_template('login.html')
    
@app.route("/autenticar" , methods=['POST',])
def autenticar():
    if request.form['nome_login'] in usuarios:
        usuario = usuarios[request.form['nome_login']]
        if request.form['senha_login'] == usuario.senha:
            return redirect('menu')
        else:
            return redirect('/')

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')

app.run(debug=True)