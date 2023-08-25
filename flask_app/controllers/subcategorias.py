from flask import flash, redirect, request, session

from flask_app import app
from flask_app.models.subcategoria import Subcategoria

@app.route('/crear_subcategoria', methods=["POST"])
def crear_subcategoria():
    print("DATOS:", request.form)

    id = Subcategoria.save(request.form)

    flash(f"la sub-categoria fue agregada exitosamente con el ID {id}", "success")
    return redirect("/ejemplo")
