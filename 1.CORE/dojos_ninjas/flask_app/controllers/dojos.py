
from flask_app import app
from flask import redirect, render_template, request
from flask_app .models.dojos import Dojo
from flask_app .models.ninjas import Ninja

# to watch all the dojos
@app.route('/dojo/')
def dojo():
    # Obtenemos todos los dojos para mostrar
    dojos = Dojo.get_all()
    return render_template('dojo.html', dojos=dojos)

#to create a dojo
@app.route('/dojo/create/', methods=['POST'])
def dojo_create():
    # Asignamos a data el valor del campo nombre porque eso es lo editable
    data = {
        "name": request.form['name']
    }
    #se le pasa al objeto el nuevo nombre dado a data
    Dojo.create(data)

    return redirect('/dojo/')

# Shows all the ninjas from a dojo
@app.route('/dojo/<int:id>')
def dojo_id(id):
    # Agregamos a data el id recibido por parámetro
    data = {
        "id": id
    }
    # Enviamos data para consultar los ninjas
    ninjas = Ninja.get_ninjas(data)
    # Obtenemos el dojo
    dojo = Dojo.get_one(data)

    return render_template('show_dojos.html', ninjas=ninjas, dojo=dojo)