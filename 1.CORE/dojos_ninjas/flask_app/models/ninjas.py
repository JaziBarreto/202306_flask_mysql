from flask_app.config.mysqlconnection import connectToMySQL


# modelar la clase después de la tabla friend de nuestra base de datos
class Ninja:
    def __init__(self, data) -> None:

        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data.get("age")
        self.dojoid = data.get("dojoid")
        self.created_at = data.get("created_at", None)
        self.updated_at = data.get("updated_at", None)

    #get all the ninjas
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL("dojos_ninjas").query_db(query)

        ninjas: list = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    #get a ninja by its id
    @classmethod
    def get_one(cls, data):

        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL("dojos_ninjas").query_db(query, data)
        return cls(result[0])
    
    #get the ninjas, related to a dojo for their id
    @classmethod
    def get_ninjas(cls, data):

        query = """
                    SELECT `ninjas`.`id`,`ninjas`.`first_name`,`ninjas`.`last_name`,`ninjas`.`age`,`ninjas`.`dojoid` 
                    FROM `dojos` LEFT JOIN ninjas ON dojos.id = ninjas.dojoid
                    WHERE dojos.id = %(id)s;
                """  
        results = connectToMySQL("dojos_ninjas").query_db(query, data)

        ninjas: list = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
        

    #create a new ninja
    @classmethod
    def create(cls, data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojoid) 
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojoid)s);""" 
        return connectToMySQL("dojos_ninjas").query_db(query, data)
    
    #edit a ninja
    @classmethod
    def update(cls, data):
        query = """
                    UPDATE ninjas SET 
                    first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, dojoid = %(dojoid)s 
                    WHERE id = %(id)s;
                """ 
        return connectToMySQL("dojos_ninjas").query_db(query, data)
    
    #to delete a ninja
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM ninjas where id = %(id)s;"""
        return connectToMySQL("dojos_ninjas").query_db(query, data)