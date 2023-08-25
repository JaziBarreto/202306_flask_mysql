from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models import subcategoria

class Categoria:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.nombre = data['nombre'] #si no existe el dato, la pagina se cae
        self.sub_categorias = []

    def __str__(self) -> str:
        return f"Instancia de Categoria {self.nombre} con ID {self.id}"

    @classmethod
    def get_all(cls):
        resultados_instancias = []
        query = "SELECT * FROM categorias"
        resultados = connectToMySQL('base_datos_productos').query_db(query)
        for resultado in resultados:
            instancia = cls(resultado)
            resultados_instancias.append(instancia)

        return resultados_instancias

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO categorias (nombre) VALUES (%(nombre)s);"
        return connectToMySQL('base_datos_productos').query_db( query, data )

    @classmethod
    def get(cls, id ):
        query = "SELECT * FROM categorias WHERE id = %(id)s;"
        data = { 'id': id }
        resultados = connectToMySQL('base_datos_productos').query_db( query, data )
        if resultados:
            return cls(resultados[0])
        return None
    

    @classmethod
    def eliminar(cls, id ):
        query = "DELETE FROM categorias WHERE id = %(id)s;"
        data = { 'id': id }
        connectToMySQL('base_datos_productos').query_db( query, data )
        return True

    def delete(self):
        query = "DELETE FROM categorias WHERE id = %(id)s;"
        data = { 'id': self.id }
        connectToMySQL('base_datos_productos').query_db( query, data )
        return True

    def update(self):
        query = "UPDATE categorias SET nombre = %(nombre)s WHERE id = %(id)s"
        data = {
            'id': self.id,
            'nombre': self.nombre
        }
        connectToMySQL('base_datos_productos').query_db( query, data )
        return True

    @classmethod #pertenece a una consulta con relacion
    def get_categoria_con_subcategorias(cls, data):
        query = "SELECT * FROM categorias LEFT JOIN subcategorias ON categorias.id = subcategorias.categoria_id WHERE categorias.id = %(id)s"
        resultados = connectToMySQL('base_datos_productos').query_db( query, data )
        print("RESULTADOS", resultados)

        instancia_categoria = cls(resultados[0]) #como que se repetiran las categorias con varias subcategorias, solo pide el 1

        subcategorias = []
        for registro in resultados:
            print("REGISTRO", registro)
            data = {
                'id': registro['subcategorias.id'],
                'nombre': registro['subcategorias.nombre'],
                'categoria': instancia_categoria
            }
            instancia_subcategoria = subcategoria.Subcategoria(data)
            subcategorias.append(instancia_subcategoria)
        
        instancia_categoria.sub_categorias = subcategorias
        return instancia_categoria
