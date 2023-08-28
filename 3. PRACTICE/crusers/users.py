from mysqlconnection import connectToMySQL
import os

# modelar la clase después de la tabla friend de nuestra base de datos
class User: 
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# METODO DE CLASE PARA CONSULTAS DE TODOS LOS USERS
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(os.getenv('DATABASE')).query_db(query)
    #LISTA PARA LA INSTANCIA DE USERS
        users = []
    #ITERACION PARA CREAR INSTANCIAS DE USERS CON LOS DATOS QUE HAYA CON CLS
        for user in results:
            users.append( cls(user) )
        return users
# INSERTAR Y GUARDAR DATOS EN EL DB
    @classmethod
    def save(cls, data):
        query = "INSERT INTO `users` (`first_name`, `last_name`, `email`, `created_at`, `updated_at`) VALUES ( %(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() );"
# data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL(os.getenv('DATABASE')).query_db(query, data)