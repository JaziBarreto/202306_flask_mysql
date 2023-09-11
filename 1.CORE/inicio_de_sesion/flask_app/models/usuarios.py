import os

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.utils.expresionesRegulares import EMAIL_REGEX

# Definición de la clase Usuario
class Usuario:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __str__(self) -> str:
        return f"{self.email} ({self.id})"
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(os.getenv('BASE_DATOS')).query_db(query, data)
    
    @classmethod
    def validar (cls, infos):
        errores = []

        #validacion del correo
        if not EMAIL_REGEX.match(infos['email']):
            errores.append("El correo no es valido")
        #si ya existe en la bd
        if cls.get_by_email(infos['email']):
            errores.append("El correo ingresado ya existe")
        if len(infos['first_name']) < 2:
            errores.append("Tu nombre debe tener al menos 2 caracteres")
        if len(infos['last_name']) < 2:
            errores.append("Tu apellido debe tener al menos 2 caracteres")
        if len(infos['password']) < 8:
            errores.append("Tu contraseña debe tener al menos 8 caracteres")
        return errores
    
    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        data = {'email': email}
        resultados = connectToMySQL(os.getenv('BASE_DATOS')).query_db(query, data)

        if resultados:
            return cls(resultados[0])

        return None