from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    username = StringField('Nome', [validators.Length(min=4, max=25)])
    nickname = StringField('Usuario', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('Crie sua senha', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='As senhas devem ser iguais')
    ])
    confirm = PasswordField('Digite sua senha novamente')
    

class LoginFormulario (Form):
    email = StringField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField ('Senha', [validators.DataRequired()])
    