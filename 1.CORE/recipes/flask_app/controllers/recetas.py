from flask import flash, redirect, request, session,  url_for, render_template
from flask_app.models.recetas import Receta
from flask_app.models.usuarios import Usuario

from flask_app import app

# Route para renderizar nueva receta form
@app.route('/create', methods=['GET', 'POST'])
def nueva_receta():
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "usuario_id": session['usuario']['id'],
            "description": request.form['description'],
            "instruction": request.form['instruction'],
            "cooking": request.form['cooking'],
            "date_cooked": request.form['date_cooked']
        }

        errores = Receta.validar(request.form)

        # Si se encuentran errores de validación, mostrarlos y redirigir al formulario de registro
        if len(errores) > 0:
            for error in errores:
                flash(error, "error")
            return redirect("/create")

        Receta.save(data)


        return redirect('/')
    return render_template('nueva_receta.html')

#renderizar recetas
@app.route('/recetas', methods=['GET'])
def recetas():
    if 'usuario' not in session:
        flash("No estás logeado", "error")
        return redirect("/login")
    recetas = Receta.get_usuario_con_recetas()
    return render_template('hola.html', recetas=recetas)

@app.route('/ver_receta/<int:id>')
def get_receta(id):
    data = {
        "id": id
    }
    receta = Receta.get_receta(data)
    return render_template("receta.html", receta=receta)

@app.route('/editar_receta/<int:id>/', methods=['GET', 'POST'])
def editar_receta(id):
    if request.method == 'GET':
        data = {"id": id}
        receta = Receta.get_receta(data)
        return render_template("editar.html", receta=receta)
    elif request.method == 'POST':
        data = {
            "id": id,
            "usuario_id": session["usuario"]["id"],
            "name": request.form['name'],
            "description": request.form['description'],
            "instruction": request.form['instruction'],
            "date_cooked": request.form['date_cooked'],
            "cooking": request.form['cooking'],
        }
        errors = Receta.validar(data)
        if len(errors) > 0:
            for error in errors:
                flash(error, 'danger')
            return render_template("editar.html", receta=data)  # Muestra el formulario con errores
        Receta.update(data)
        flash("Receta editada con éxito", "success")
        return redirect(url_for('recetas'))  # Redirige a la vista que muestra todas las recetas

    
@app.route('/eliminar_receta/<int:id>')
def eliminar_receta(id):
    data = {
        "id": id
    }
    receta = Receta.get_receta(data)

    # Verificar si el usuario actual tiene permiso para eliminar la receta
    if session["usuario"]["id"] == receta.usuario_id:
        Receta.delete(data)
        flash("La receta fue eliminada", "success")
    else:
        flash("No tienes permiso para eliminar la receta", "danger")

    return redirect('/recetas')  # Redirigir a la vista de mostrar recetas
