from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.utils.expresiones_regulares import EMAIL_REGEX #desde flask app donde esta utils y dentro de las expresiones regulares, importa la que tiene que ver con bodegas


class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __str__(self) -> str:
        return f"Instancia de USUARIO {self.email} con ID {self.id}"

    @classmethod
    def validar(cls, formulario):

        errores = []
        if not EMAIL_REGEX.match(formulario['email']):
            errores.append("El correo que has introducido es invalido")

        if cls.get_by_email(formulario['email']): #si el correo existe en nuestra base de datos, entra en esta condicion
            errores.append("El correo que has introducido ya esta registrado")
        return errores

    @classmethod #por lo pronto no necesitamos el dato de todos los users
    def get_all(cls):
        resultados_instancias = []
        query = "SELECT * FROM user"
        resultados = connectToMySQL('base_datos_productos').query_db(query)
        for resultado in resultados:
            instancia = cls(resultado)
            resultados_instancias.append(instancia)

        return resultados_instancias

    @classmethod #para guardar los datos de los users
    def save(cls, data ):
        query = "INSERT INTO user (email, password, created_at, updated_at) VALUES (%(email)s, %(password)s, NOW(), NOW() );" #reminder: now() me da la fecha y hora exacta de cuando se inserta
        return connectToMySQL('base_datos_productos').query_db( query, data )
    
    @classmethod
    def get(cls, id ): #para obtener solo un usuario
        query = "SELECT * FROM user WHERE id = %(id)s;"
        data = { 'id': id }
        resultados = connectToMySQL('base_datos_productos').query_db( query, data )
        if resultados:
            return cls(resultados[0])
        
        return None
    
    @classmethod
    def get_by_email(cls, email): #para obtener solo un usuario desde el email
        query = "SELECT * FROM user WHERE email = %(email)s;"
        data = { 'email': email }
        resultados = connectToMySQL('base_datos_productos').query_db( query, data )
        if resultados:
            return cls(resultados[0])
        
        return None #si retorna none significa que el correo no se encuentra en la base de datos

    @classmethod
    def eliminar(cls, id ): #eliminar de tipo clase
        query = "DELETE FROM user WHERE id = %(id)s;"
        data = { 'id': id }
        connectToMySQL('base_datos_productos').query_db( query, data )
        return True

    def delete(self): #eliminar de tipo instancia
        query = "DELETE FROM user WHERE id = %(id)s;"
        data = { 'id': self.id }
        connectToMySQL('base_datos_productos').query_db( query, data )
        return True

    def update(self):
        query = "UPDATE user SET password = %(password)s, updated_at = NOW() WHERE id = %(id)s"
        data = {
            'id': self.id,
            'password': self.password
        }
        connectToMySQL('base_datos_productos').query_db( query, data )
        return True
