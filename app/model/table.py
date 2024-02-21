from app import db


class User(db.Model):
    __tablename = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)  #olhar depois para ver se precisa ser unique
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)


    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
    def __repr__(self):
        return "<User %r>" %self.username
    
class Item(db.Model):
    __tablename = "itens"

    id = db.Column(db.integer, primary_key=True)
    content = db.Column (db.Text)
     