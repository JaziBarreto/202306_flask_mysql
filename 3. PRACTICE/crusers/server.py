from flask import Flask, render_template, redirect, request
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

@app.route('/users')
def users():
    users = User.get_all()
    print(users)
    return render_template("users.html", all_users = users)

if __name__ == "__main__":
    app.run(debug=True)