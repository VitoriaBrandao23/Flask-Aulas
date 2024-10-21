from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Olá <br> mundo!</h1>'

@app.route('/aluno')
def aluno():
    return render_template('form.html') 

@app.route('/envio', methods=['POST'])
def envioForms():
    nom = request.form['nome']
    return render_template('aluno.html', n=nom)