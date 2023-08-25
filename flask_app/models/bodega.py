from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.utils.expresiones_regulares import BODEGA_REGEX #desde flask app donde esta utils y dentro de las expresiones regulares, importa la que tiene que ver con bodegas

class Bodega:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.nombre = data['nombre']

    def __str__(self) -> str:
        return f"Instancia de BODEGA {self.nombre} con ID {self.id}"

    @staticmethod
    def validar(formulario):

        errores = []
        if not BODEGA_REGEX.match(formulario['nombre']):
            errores.append(
                "El nombre de la bodega es invalido, "
                "no cumple con lo requerido: "
                "Comenzar con mayuscula y al menos 10 caracteres" #usar las comillas asi hace que se vea en una sola linea pero no toda larga aqui en mi codigo, queda mas ordenado y bonito.
            )
        return errores


    @classmethod
    def get_all(cls):
        resultados_instancias = []
        query = "SELECT * FROM bodegas"
        resultados = connectToMySQL('base_datos_productos').query_db(query)
        for resultado in resultados:
            instancia = cls(resultado)
            resultados_instancias.append(instancia)

        return resultados_instancias

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO bodegas (nombre) VALUES (%(nombre)s);"
        return connectToMySQL('base_datos_productos').query_db( query, data )
    
    @classmethod
    def get(cls, id ):
        query = "SELECT * FROM bodegas WHERE id = %(id)s;"
        data = { 'id': id }
        resultados = connectToMySQL('base_datos_productos').query_db( query, data )
        if resultados:
            return cls(resultados[0])
        
        return None
    
    @classmethod
    def eliminar(cls, id ):
        query = "DELETE FROM bodegas WHERE id = %(id)s;"
        data = { 'id': id }
        connectToMySQL('base_datos_productos').query_db( query, data )
        return True

    def delete(self):
        query = "DELETE FROM bodegas WHERE id = %(id)s;"
        data = { 'id': self.id }
        connectToMySQL('base_datos_productos').query_db( query, data )
        return True

    def update(self):
        query = "UPDATE bodegas SET nombre = %(nombre)s WHERE id = %(id)s"
        data = {
            'id': self.id,
            'nombre': self.nombre
        }
        connectToMySQL('base_datos_productos').query_db( query, data )
        return True
