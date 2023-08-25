from flask import render_template

from flask_app.models.bodega import Bodega
from flask_app.models.categoria import Categoria
from flask_app import app
from flask_app.models.subcategoria import Subcategoria


@app.route('/ejemplo')
def ejemplo():
    return render_template(
        'ejemplo.html',
        bodegas=Bodega.get_all(),
        categorias=Categoria.get_all(),
        subcategorias=Subcategoria.get_all(),
    )