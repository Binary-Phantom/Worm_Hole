from flask import render_template, session, request, url_for
from minhocario import app, db

@app.route('/')

def home():
    return "Seja bem vindo ao minhocário"


@app.route('/registrar')

def registrar():
    return render_template('admin/registrar.html', title="Cadastrar Usuário")