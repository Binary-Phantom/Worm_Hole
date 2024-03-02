from flask import render_template, session, request, url_for, flash, redirect
from minhocario import app, db
from .forms import RegistrationForm

@app.route('/')

def home():
    return "Seja bem vindo ao minhocário"


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = User(form.username.data, form.email.data,
              #      form.password.data)
       # db_session.add(user)
        flash('Obrigado por se cadastrar')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title="Cadastrar novo usuário")