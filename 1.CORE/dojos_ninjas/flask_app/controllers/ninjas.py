from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route('/ninja/')
def ninja():
    # Obtenemos todos los dojos para poder enviar al ninja
    dojos = Dojo.get_all()
    
    return render_template('ninjas.html', dojos=dojos)

#to create a ninja
@app.route('/ninja/create/', methods=['POST'])
def ninja_create():

    data = {
        "dojoid": request.form['dojoid'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age']
    }

    # Enviamos data a la funcion de create ninja
    Ninja.create(data)

    # Una ves creado el ninja hacemos un redirect
    return redirect('/ninja/')

if __name__ == '__main__':
    app.run(debug=True)