from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models import categoria

class Subcategoria:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.nombre = data['nombre']
        self.categoria = data.get("categoria")

    def __str__(self) -> str:
        return f"Instancia de Subcategoria {self.nombre} con ID {self.id}"
    
    #validación de los datos que se reciben
    @staticmethod
    def validar(datos_formulario):
        errores = []

        if len(datos_formulario['nombre']) == 0:
            errores.append("el nombre no tiene datos o algun caracter")


        if len(datos_formulario['nombre']) < 3:
            errores.append("el nombre debe tener mas de tres caracteres")

        return errores #retornaria solo la lista con los errores que existan

    @classmethod
    def get_all(cls):
        resultados_instancias = []
        query = "SELECT * FROM subcategorias JOIN categorias ON subcategorias.categoria_id = categorias.id"
        resultados = connectToMySQL('base_datos_productos').query_db(query)
        for resultado in resultados:
            
            instancia = cls(resultado)
            datos_categoria = {
                'id': resultado['categorias.id'],
                'nombre': resultado['categorias.nombre'],
            }
            instancia_categoria = categoria.Categoria(datos_categoria)
            instancia.categoria = instancia_categoria

            resultados_instancias.append(instancia)

        return resultados_instancias

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO subcategorias (nombre, categoria_id) VALUES (%(nombre)s, %(categoria_id)s);"
        return connectToMySQL('base_datos_productos').query_db( query, data )
