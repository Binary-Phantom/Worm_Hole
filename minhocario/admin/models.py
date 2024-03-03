from minhocario import app, db
from werkzeug.utils import secure_filename

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    nickname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    profile = db.Column(db.String(200), unique=False, nullable=False, default='profile.jpg')

    def __repr__(self):
        return f'<User {self.username}>'

# lembrar que o alchemy precisa de ordem certa para iniciar o db

# A criação de tabelas deve ser realizada no script principal do aplicativo.
# Ex: run.py
# não criar a inicialização do db aq, e sim no run.py
#if __name__ == '__main__':
   # with app.app_context():
        # Cria todas as tabelas definidas nos modelos
       # db.create_all()