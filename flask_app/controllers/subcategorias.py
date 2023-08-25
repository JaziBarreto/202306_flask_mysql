from flask import flash, redirect, request, session

from flask_app import app
from flask_app.models.subcategoria import Subcategoria

@app.route('/crear_subcategoria', methods=["POST"])
def crear_subcategoria():
    print("DATOS:", request.form)
    #la validacion se hace antes de guardar
    errores = Subcategoria.validar(request.form)

    if len(errores) > 0: #entra el error, si el largo de los errores es mayor a cero, quiere decir que hay errores
        for error in errores: #so, si vienen errores, necesito que los muestren
            flash(error, "error")
            return redirect("/ejemplo")

    id = Subcategoria.save(request.form)

    flash(f"la sub-categoria fue agregada exitosamente con el ID {id}", "success")
    return redirect("/ejemplo")
