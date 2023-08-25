from flask import flash, redirect, render_template, session


from flask_app.models.bodega import Bodega
from flask_app.models.categoria import Categoria
from flask_app import app
from flask_app.models.subcategoria import Subcategoria


@app.route('/ejemplo')
def ejemplo():
    if "user" not in session: #es decir, si el usuario no esta en session
        flash("usted no ha iniciado sesion", "error")
        return redirect("/login")

    return render_template(
        'ejemplo.html',
        bodegas=Bodega.get_all(),
        categorias=Categoria.get_all(),
        subcategorias=Subcategoria.get_all(),
    )