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
        return connectToMySQL(os.getenv('DATABASE')).query_db(query, data)
    
#Obtener todos los datos del usuario a traves del id SHOW THE INFO
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {'id': id}
        resultados = connectToMySQL(os.getenv('DATABASE')).query_db(query, data)
        if resultados:
            return cls(resultados[0])  # Devolver el primer resultado como instancia de User
        return None
    
#Obtener todos los datos de un usuario a traves de su 'Email'
    @classmethod
    def get_by_email(cls, email ):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data = { 'email': email }
        resultados = connectToMySQL(os.getenv('DATABASE')).query_db( query, data )
        if resultados:
            return cls(resultados[0])
        
        return None

#es para editar todos los datos del user a traves del id
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s"
        connectToMySQL(os.getenv('DATABASE')).query_db(query, data)
        return True

#es para eliminar de forma segura
    @classmethod
    def delete(cls, id ):
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = { 'id': id }
        connectToMySQL(os.getenv('DATABASE')).query_db(query, data)
        return True
    
