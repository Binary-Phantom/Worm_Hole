from minhocario.products import forms
from minhocario import app, db
#from werkzeug.datastructures import FileStorage

#if __name__ == "__main__":
   # app.run(debug=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)