from flask import redirect, render_template, url_for, flash, request
from minhocario import db, app, photos
#from werkzeug.utils import secure_filename
#from flask_wtf import csrf
#from werkzeug.datastructures import FileStorage
#from flask_uploads import IMAGES, UploadSet, configure_uploads
import secrets
from .forms import Addprodutos
from .models import Marcas, Categoria, Additens



@app.route('/addmarca', methods=['GET', 'POST'])
def addmarca():
    if request.method == "POST":
        getmarca = request.form.get('marca')
        marca = Marcas(name=getmarca)
        db.session.add(marca)
        db.session.commit()
        flash(f'Marca {getmarca} cadastrada com sucesso.', 'success')
        return redirect(url_for('addmarca'))
    return render_template('/products/addmarca.html')

@app.route('/addcategoria', methods=['GET', 'POST'])
def addcategoria():
    if request.method == "POST":
        getcategoria = request.form.get('categoria')
        categoria = Categoria(name=getcategoria)
        db.session.add(categoria)
        db.session.commit()
        flash(f'Categoria {getcategoria} cadastrada com sucesso.', 'success')
        return redirect(url_for('addcategoria'))
    return render_template('/products/addcategoria.html')  

@app.route('/additem', methods=['GET', 'POST'])
def additem():
    produtos = Additens.query.all()
    marcas_list = Marcas.query.all()  
    categorias = Categoria.query.all()
    form = Addprodutos(request.form)

    if request.method == "POST" and form.validate():
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        description = form.description.data
        stock = form.stock.data
        color = form.color.data
        marca_id = request.form.get('marca')  
        categoria_id = request.form.get('categoria')  

        
        addpro = Additens(
            name=name, price=price, discount=discount, description=description,
            stock=stock, color=color, marca_id=marca_id, categoria_id=categoria_id
        )

        
        db.session.add(addpro)

        addpro.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        addpro.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        addpro.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        db.session.add(addpro)
        db.session.commit()
        flash(f'Item {name} cadastrado com sucesso!', 'success')
        return redirect(url_for('Login'))

    return render_template('/products/additem.html', title="Cadastrar Item", form=form, produtos=produtos, marcas=marcas_list, categorias=categorias)

