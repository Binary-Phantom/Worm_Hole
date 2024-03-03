from flask import redirect, render_template, url_for, flash, request
from minhocario import db, app, photos
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from flask_uploads import IMAGES, UploadSet, configure_uploads
import secrets
from .forms import Addprodutos
from .models import Produto, Categoria, Additens



@app.route('/addproduto', methods=['GET', 'POST'])
def addproduto():
    if request.method == "POST":
        getproduto = request.form.get('produto')
        produto = Produto(name=getproduto)
        db.session.add(produto)
        db.session.commit()
        flash(f'Produto {getproduto} cadastrado com sucesso.', 'success')
        return redirect(url_for('addproduto'))
    return render_template('/products/addproduto.html', produto='produto')

@app.route('/addcategoria', methods=['GET', 'POST'])
def addcategoria():
    if request.method == "POST":
        getcategoria = request.form.get('categoria')
        categoria = Categoria(name=getcategoria)
        db.session.add(categoria)
        db.session.commit()
        flash(f'Categoria {getcategoria} cadastrada com sucesso.', 'success')
        return redirect(url_for('addcategoria'))
    return render_template('/products/addcategoria.html')  # Certifique-se de criar o template addcategoria.html

@app.route('/additem', methods=['GET', 'POST'])
def additem():
    produtos = Additens.query.all()
    categorias = Categoria.query.all()
    form = Addprodutos(request.form)  # Certifique-se de usar o formulário correto (Addprodutos)
    
    if request.method == "POST" and form.validate():
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        description = form.description.data
        stock = form.stock.data
        color = form.color.data
        produto = request.form.get('produto')
        categoria = request.form.get('categoria')

        addpro = Additens(
            name=name, price=price, discount=discount, description=description,
            stock=stock, color=color, produto_id=produto, categoria_id=categoria
        )

        db.session.add(addpro)
        db.session.commit()

        
        addpro.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        addpro.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        addpro.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        db.session.commit()

        flash(f'Produto {name} cadastrado com sucesso!')
        return redirect(url_for('admin'))

    return render_template('/products/additem.html', title="Cadastrar Item", form=form, produtos=produtos, categorias=categorias)
