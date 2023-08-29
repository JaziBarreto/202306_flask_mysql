from flask import Flask, flash, render_template, redirect, request
from users import User #este es el del archivo en si y lo que pedimos que importe es el objeto de clase

app = Flask(__name__)

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


#ESTE ES PARA MOSTRAR TODA LA INFO DEL USER DE ACUERDO AL ID
@app.route('/users/<id>')
def get_user(id):
    data = {
        'id': id
    }
    user= User.get(data)
    return render_template("user_detalle.html", user=user)

#este es para eliminar user segun id
@app.route('/delete_user/<id>')
def delete_user(id):
    print("User who is going to be delete", id)

    user_to_delete = User.get(id)
    user_to_delete.delete()
    User.eliminar(id)
    flash("The user has been  deleted", "success")
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)