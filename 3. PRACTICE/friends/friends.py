from mysqlconnection import connectToMySQL
import os

# modelar la clase después de la tabla friend de nuestra base de datos
class Friend: 
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
    # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(os.getenv('DATABASE')).query_db(query)
    # crear una lista vacía para agregar nuestras instancias de friends
        friends = []
    # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for friend in results:
            friends.append( cls(friend) )
        return friends
# metodo de clase para insertar datos a la BD desde el form, gralmente se usa un save
    @classmethod
    def save(cls, data):
        query = "INSERT INTO `friends` (`first_name`, `last_name`, `occupation`, `created_at`, `updated_at`) VALUES ( %(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW() );"
# data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL(os.getenv('DATABASE')).query_db(query, data)

