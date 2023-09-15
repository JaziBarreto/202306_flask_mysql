from flask import flash, redirect, render_template, request, session

from flask_app import app
from flask_app.models.usuarios import Usuario
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)  

@app.route('/login')
def registro():

    if 'usuario' in session:
        flash("Te haz registrado correctamente" + session['usuario']['first_name'], "info")
        return redirect("/")

    return render_template("inicio.html")

@app.route('/procesar_registro', methods=["POST"])
def procesar_registro():
    #validacion de los datos del formulario
    errores = Usuario.validar(request.form)
    if len(errores) > 0:
        for error in errores:
            flash(error, "error")
        return redirect ("/login")
    #coincidencia de contrasenhas
    if request.form["password"] != request.form["confirmar_password"]:
        flash("Lo sentimos, tus contraseñas no coinciden", "error")
        return redirect ("/login")
    #se crea un dict con los datos ingresados para que vayan a la db
    data= {
        'first_name': request.form["first_name"],
        'last_name': request.form["last_name"],
        'email': request.form["email"],
        'password': bcrypt.generate_password_hash(request.form["password"])
    }
    #guardar el dato del usuario bajo la instancia id en la db
    id= Usuario.save(data)
    #mensaje de exito para que puedan iniciar seison
    flash("Te registraste con éxito, bienvenido", "success")
    return redirect("/login")


@app.route('/procesar_inicio', methods=["POST"])
def procesar_inicio():
    usuario= Usuario.get_by_email(request.form['email'])
    if not usuario:
        flash("El correo o la contraseña que ingresaste, no son validos", "error")
        return redirect ("/login")
    resultado = bcrypt.check_password_hash(usuario.password, request.form['password'])
    if resultado:
        session['usuario'] = {
            'id': usuario.id,
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'email': usuario.email
        }
        return redirect("/inicio")
    flash("la contraseña o el correo no es válido", "error")
    return redirect("/login")

@app.route('/inicio')
def pagina_inicio():
    if 'usuario' not in session:
        flash("No estas logeado", "error")
        return redirect("/login")
    return render_template(
    'hola.html'
    )

@app.route('/salir')
def salir():
    session.clear()
    return redirect("/login")


