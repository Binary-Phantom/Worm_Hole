from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, PasswordField, EmailField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, length, NumberRange
from flask_wtf.file import FileField, FileRequired


class SignUpForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    username = StringField('Apelido', validators=[DataRequired(), length(min=2)])
    password1 = PasswordField('Crie uma Senha', validators=[DataRequired(), length(min=6)])
    password2 = PasswordField('Confirme sua senha', validators=[DataRequired(), length(min=6)])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('senha', validators=[DataRequired()])
    submit = SubmitField('Login')


class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Senha atual', validators=[DataRequired(), length(min=6)])
    new_password = PasswordField('Nova Senha', validators=[DataRequired(), length(min=6)])
    confirm_new_password = PasswordField('Confirme a nova senha', validators=[DataRequired(), length(min=6)])
    change_password = SubmitField('Trocar Senhas')


class ShopItemsForm(FlaskForm):
    product_name = StringField('Nome do produto', validators=[DataRequired()])
    current_price = FloatField('Preço atual', validators=[DataRequired()])
    previous_price = FloatField('Preço anterior', validators=[DataRequired()])
    in_stock = IntegerField('Em estoque', validators=[DataRequired(), NumberRange(min=0)])
    product_picture = FileField('Foto Produto', validators=[DataRequired()])
    flash_sale = BooleanField('Promoção')

    add_product = SubmitField('Adicionar produto')
    update_product = SubmitField('Atualizar')


class OrderForm(FlaskForm):
    order_status = SelectField('Status pedido', choices=[('Pendente', 'Pendente'), ('Confirmado', 'Confirmado'),
                                                        ('Saiu para entrega', 'Saiu para entrega'),
                                                        ('Entregue', 'Entregue'), ('Cancelado', 'Cancelado')])

    update = SubmitField('Atualizar Status')





