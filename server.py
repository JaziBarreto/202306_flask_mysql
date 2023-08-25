from flask_app import app
from flask_app.controllers import bodegas, categorias, subcategorias, core

if __name__=="__main__":
    app.run(debug=True)