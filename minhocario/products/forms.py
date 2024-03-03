from flask_wtf.file import FileAllowed, _FileField, FileRequired, DataRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators



class Addprodutos(Form):
    name = StringField('Nome:', [validators.DataRequired()])

    price = IntegerField('Preço:', [validators.DataRequired()])
    discount = IntegerField('Desconto:', [validators.DataRequired()])
    description = TextAreaField('Descrição:', [validators.DataRequired()])
    stock = IntegerField('Estoque:', [validators.DataRequired()])
    colors = TextAreaField('Cor:', [validators.DataRequired()])
    
    
    
    
    
    
    
    image_1 = _FileField('Image 1:' , validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    image_2 = _FileField('Image 2:' , validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    image_3 = _FileField('Image 3:' , validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    image_4 = _FileField('Image 4:' , validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    image_5 = _FileField('Image 5:' , validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    image_6 = _FileField('Image 6:' , validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    image_7 = _FileField('Image 7:' , validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    image_8 = _FileField('Image 8:' , validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])


