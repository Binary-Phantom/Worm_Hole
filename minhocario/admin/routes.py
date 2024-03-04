from flask import render_template, session, request, url_for, flash, redirect
from minhocario.products.models import Additens
from werkzeug.utils import secure_filename
from minhocario import app, db, bcrypt
from .models import User
from .forms import RegistrationForm,LoginFormulario
import os 






@app.route('/admin')

def admin():
    if 'email' not in session:
        flash(f'Por favor, Cadastre-se.', 'danger') 
        return redirect(url_for('login'))
    produtos = Additens.query.all()
    return render_template ('admin/index.html', title='Página inicial', produtos=produtos)


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
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title="Cadastrar novo usuário")


@app.route ('/login',methods=['GET', 'POST'])
def login():
   form=LoginFormulario(request.form)
   if request.method == "POST" and form.validate():
       user= User.query.filter_by(email=form.email.data).first()
       if user and bcrypt.check_password_hash(user.password, form.password.data):
           session['email'] = form.email.data 
           flash(f'Olá {form.email.data} você está logado', 'success')
           return redirect(request.args.get('next')or url_for ('admin'))
       else:
            flash('Usuário ou senha não correspondem.', 'danger')
   return render_template ('admin/login.html',form=form, title='Página de login')