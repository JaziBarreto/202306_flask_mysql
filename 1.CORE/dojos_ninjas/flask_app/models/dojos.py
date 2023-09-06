from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    #to get all the dojos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL("dojos_ninjas").query_db(query)

        # Creamos un objeto iterable de la clase dojo
        dojos: list = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    #to get one dojo
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL("dojos_ninjas").query_db(query, data)
        return cls(result[0])

    #to create a dojo
    @classmethod
    def create(cls, data):
        query = "INSERT INTO `dojos`(`name`, `created_at`, `updated_at`) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL("dojos_ninjas").query_db(query, data)
    
    #editar el dojo
    @classmethod
    def update(cls, data):
        query = """
                    UPDATE dojos SET 
                    name = %(name)s 
                    WHERE id = %(id)s;
                """ 
        return connectToMySQL("dojos_ninjas").query_db(query, data)
    
    #delete a dojo
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dojos where id = %(id)s;"
        return connectToMySQL("dojos_ninjas").query_db(query, data)