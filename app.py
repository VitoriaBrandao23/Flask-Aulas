from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Olá <br> mundo!</h1>'

@app.route('/aluno/<nome>')
def aluno(nome):
    return f'<h1>{nome}</h1>'