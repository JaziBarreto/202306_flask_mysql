from flask import Flask, render_template, request, redirect, session, flash
from flask_app.config.mysqlconnections import connectToMySQL
app = Flask(__name__)
app.secret_key = 'cualquier cosa'

class Bodega:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.nombre = data['nombre']

@app.route('/ejemplo')
def ejemplo():
    query = "SELECT * FROM productos p JOIN subcategorias s ON p.subcategoria_id = s.id JOIN imagenes i ON p.imagen_id = i.id;"
    resultados = connectToMySQL('base_datos_productos').query_db(query) #para que me devuelva los datos de la consulta, debe estar en una variable
    if resultados:
        for resultado in resultados:
            print("RESULTADO: ", resultado)
        instancia_bodega = Bodega(resultado)
        print(instancia_bodega)

    else:
        flash("Error en la consulta SQL")  # Esto podría ser útil para mostrar un mensaje de error en la interfaz web

    return render_template('ejemplo.html')


if __name__=="__main__":
    app.run(debug=True)

