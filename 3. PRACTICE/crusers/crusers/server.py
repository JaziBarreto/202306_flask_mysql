import os
from flask import Flask, flash, render_template, redirect, request
from users import User #este es el del archivo en si y lo que pedimos que importe es el objeto de clase

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY_FLASK')

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/create_user', methods=["POST"])
def create_user():
#EL DICCIONARIO DE ABAJO SE ENCARGA DE INSERTAR EN FORMA DE DICT LOS DATOS DEL FORM AL DB
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # GUARDAMOS CON EL METODO SAVE DE USER
    User.save(data)
    return redirect('/users')

@app.route('/users/')
def users():
    users = User.get_all()
    print(users)
    return render_template("users.html", all_users = users)

#Obtener todos los datos del usuario a traves del id SHOW THE INFO
@app.route('/users/<int:id>')
def get_by_id(id):
    user = User.get_by_id(id)
    if user:
        return render_template("user_detalle.html", user=user)
    else:
        # Manejar el caso en el que no se encuentre el usuario por el ID
        flash("User not found", "danger")
        return redirect("/users")

#es para eliminar de forma segura
@app.route('/users/delete_user/<int:id>')
def delete_user(id):
    print("User who is going to be delete", id)
    User.delete(id)
    flash("The user has been  deleted", "success")
    return redirect("/users/")

#es para editar todos los datos del user a traves del id
@app.route('/users/edit_user/<int:id>')
def edit_user(id):
    edit_user = User.get_by_id(id)
    if edit_user:
        return render_template("edit_user.html", edit_user=edit_user)
    else:
        flash("User not found", "danger")
        return redirect("/users")
    
@app.route('/users/edit/<int:id>', methods=["POST"])
def edit_by_id(id):
    data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.update(data)
    flash("The user has been edited", "success")
    return redirect("/users/")
    

if __name__ == "__main__":
    app.run(debug=True)