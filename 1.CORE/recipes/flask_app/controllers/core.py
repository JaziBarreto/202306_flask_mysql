from flask import render_template, flash, redirect, session
from flask_app import app
from flask_app.models.recetas import Receta

@app.route('/')
def inicio():
    if 'usuario' not in session:
        flash("No estás logeado", "error")
        return redirect("/login")

    recetas = Receta.get_usuario_con_recetas()
    
    return render_template('hola.html', recetas=recetas)
