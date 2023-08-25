from flask import flash, redirect, render_template, request, session

from flask_app import app
from flask_app.models.bodega import Bodega


@app.route('/crear_bodega', methods=["POST"])
def crear_bodega():
    print("DATOS:", request.form)
    data = {
        'nombre': request.form['nombre']
    }
    id = Bodega.save(data)

    flash(f"la bodega fue agregada exitosamente con el ID {id}", "success")
    return redirect("/ejemplo")


@app.route('/eliminar_bodega/<id>')
def eliminar_bodega(id):

    print("BODEGA A ELIMINAR", id)

    bodega_a_eliminar = Bodega.get(id)
    bodega_a_eliminar.delete()

    # Bodega.eliminar(id)

    flash("Bodega eliminada", "success")
    return redirect("/ejemplo")

@app.route('/editar_bodega/<id>')
def editar_bodega(id):
    bodega = Bodega.get(id)

    return render_template(
        'editar_bodega.html',
        bodega=bodega
    )

@app.route('/procesar_editar_bodega/<id>', methods=["POST"])
def procesar_editar_bodega(id):
    print("DATOS:", request.form)

    bodega = Bodega.get(id)
    bodega.nombre = request.form['nombre']
    bodega.update()

    flash(f"la bodega fue actualizada exitosamente con el ID {id}", "success")
    return redirect("/ejemplo")
