from flask import render_template, session, request, url_for, flash, redirect
from minhocario import app, db, bcrypt
from .models import User
from .forms import RegistrationForm
import os 






@app.route('/')

def home():
    return render_template ('admin/index.html', title='kekkk')


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():

        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, nickname=form.nickname.data, email=form.email.data,         
        password = hash_password)
        db.session.add(user)
        db.session.commit()

        flash(f' {form.nickname.data} Obrigado por se cadastrar', 'success')
        return redirect(url_for('home'))
    return render_template('admin/registrar.html', form=form, title="Cadastrar novo usuário")