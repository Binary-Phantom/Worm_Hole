from minhocario import db
from werkzeug.datastructures import FileStorage
from datetime import datetime



class Additens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    discount = db.Column(db.Integer, default=0)
    description = db.Column(db.Text, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    color = db.Column(db.Text, nullable=False)
    
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    
    
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'),
        nullable=False)

    produto = db.relationship('Produto', 
        backref=db.backref('produtos', lazy=True))
    




    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'),
        nullable=False)

    categoria = db.relationship('Categoria', 
        backref=db.backref('categorias', lazy=True))
    


    image_1 = db.Column(db.String(180), nullable=False, default = 'image.jpg')
    image_2 = db.Column(db.String(180), nullable=False, default = 'image.jpg')
    image_3 = db.Column(db.String(180), nullable=False, default = 'image.jpg')





    def __repr__(self):
        return '<Additens %r>' % self.name




class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False, unique=True)


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False, unique=True)  

