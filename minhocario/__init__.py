from flask import Flask 
from flask_uploads import IMAGES, UploadSet, configure_uploads
from flask_sqlalchemy import SQLAlchemy
#from products.forms import Addprodutos
#from werkzeug.utils import secure_filename
#from werkzeug.datastructures import FileStorage
from flask_uploads import IMAGES, UploadSet, configure_uploads
from flask_bcrypt import Bcrypt
import os



basedir = os.path.abspath(os.path.dirname(__file__))



app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///minhocario.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'minhocario.db')
app.config['SECRET_KEY'] ='abcd'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.config ['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

from minhocario.admin import routes
from minhocario.products import routes