from flask import flash, redirect, request, render_template

from flask_app import app
from flask_app.models.categoria import Categoria


@app.route('/crear_categoria', methods=["POST"])
def crear_categoria():
    print("DATOS:", request.form)
    data = {
        'nombre': request.form['nombre']
    }
    id = Categoria.save(data)

    flash(f"la categoria fue agregada exitosamente con el ID {id}", "success")
    return redirect("/ejemplo")

@app.route('/categoria/<id>')
def obtener_categoria(id):

    data = {
        'id': id
    }
    categoria = Categoria.get_categoria_con_subcategorias(data)

    return render_template("categoria_detalle.html", categoria=categoria)