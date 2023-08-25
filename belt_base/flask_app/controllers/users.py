from flask import flash, redirect, render_template, request, session

from flask_app import app
from flask_app.models.users import User

from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)  

@app.route('/login') #para que muestre login y sign up, dependiendo del action ira a register o a login
def registro():

    if User in session: #es decir, si el usuario esta logueado
        flash("Ya te encuentras logueado, eres " + session['user']['email'], "info")
        return redirect("/inicio")

    return render_template("login.html")

@app.route('/procesar_login', methods=["POST"])
def procesar_login():
    print(request.form)

    user = User.get_by_email(request.form['login_email'])
    if not user:
        flash("El correo o la contraseña introducidos no son válidos", "error")
        return redirect("/login")

    resultado = bcrypt.check_password_hash(user.password, request.form['login_password'])
    if resultado:
        session['users'] = {
            'id': user.id,
            'email': user.email
        }
        return redirect ("/inicio")
    
    flash("La contraseña o el correo introducidos no son válidos", "error")
    return redirect("/login")

@app.route('/procesar_registro', methods=["POST"])
def procesar_sign_up():
    print(request.form)

    errores = User.validar(request.form) #valida si el correo es correcto
    if len(errores) > 0:
        for error in errores:
            flash(error, "error")
        return redirect("/login") #so, si el correo no se encuentra en la base de datos, les manda en el login

    if request.form["password"] != request.form["confirm_password"]:
        flash("Las contraseñas no coinciden", "error")
        return redirect("/login")

    data = {
        'email': request.form["email"],
        'password': bcrypt.generate_password_hash(request.form['password']) #se hace un hash de lo que el user esta enviando
    }
    id = User.save(data) #es el data del diccionario que se debe guardar en nuestra base de datos
    flash("Usuario registrado correctamente", "success")
    return redirect("/inicio")

@app.route('/inicio')
def inicio_sesion():
    flash("Bienvenido otra vez", "info")
    return render_template("inicio.html")

@app.route('/salir') 
def salir():

    session.clear()
    return redirect("/login")