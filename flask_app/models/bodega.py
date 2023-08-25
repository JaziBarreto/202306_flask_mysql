from flask_app.config.mysqlconnections import connectToMySQL

class Bodega:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.nombre = data['nombre']

    def __str__(self) -> str:
        return f"Instancia de BODEGA {self.nombre} con ID {self.id}"

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
