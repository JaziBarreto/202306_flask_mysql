import os
from flask import session
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.usuarios import Usuario
from flask_app.utils.expresionesRegulares import COOKING_REGEX

class Receta:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date_cooked = data['date_cooked']
        self.cooking = data['cooking']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.usuario_id = data['usuario_id']
        self.author = data['author']

    def __str__(self) -> str:
        return f"{self.name}"

    @classmethod
    def validar(cls, formulario):
        errores = []
        if len(formulario['name']) < 2:
            errores.append("El nombre tiene que tener al menos tres caracteres")

        if len(formulario['instruction']) < 5:
            errores.append("La instruccion tiene que tener 5 caracters")

        if len(formulario['description']) < 5:
            errores.append("La descripción  tiene que tener al menos 5 caracters")

        if not COOKING_REGEX.match(formulario['cooking']):
            errores.append("Selecionar si o no")

        return errores

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recetas ( `name`, `description`, `instruction`, `date_cooked`, `cooking`,`created_at`,`updated_at`,`usuario_id`) VALUES(%(name)s, %(description)s, %(instruction)s, %(date_cooked)s, %(cooking)s, now(), now(), %(usuario_id)s);"
        return connectToMySQL(os.getenv('BASE_DATOS')).query_db(query, data)
    
    @classmethod
    def get_usuario_con_recetas(cls):
        query = """
        SELECT 
            recetas.id, 
            recetas.name, 
            recetas.cooking, 
            usuarios.first_name as author, 
            usuarios.id as usuario_id 
        FROM recetas
        LEFT JOIN usuarios 
        ON usuarios.id = recetas.usuario_id"""
        recetas = connectToMySQL(os.getenv('BASE_DATOS')).query_db(query)
        return recetas
    
    @classmethod
    def get_receta(cls, data):
        query = """
        SELECT 
            recetas.id, 
            recetas.name, 
            recetas.cooking, 
            recetas.date_cooked,
            recetas.description,
            recetas.instruction,
            recetas.created_at,
            recetas.updated_at,
            usuarios.first_name as author, 
            usuarios.id as usuario_id 
        FROM recetas
        LEFT JOIN usuarios 
        ON usuarios.id = recetas.usuario_id
        WHERE recetas.id = %(id)s;
        """
        result = connectToMySQL(os.getenv('BASE_DATOS')).query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = """
                    UPDATE recetas SET 
                    name= %(name)s, instruction = %(instruction)s, description = %(description)s, date_cooked = %(date_cooked)s, cooking = %(cooking)s, usuario_id = %(usuario_id)s
                    WHERE id = %(id)s;
                """ 
        return connectToMySQL(os.getenv('BASE_DATOS')).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM recetas where id = %(id)s;""" 
        return connectToMySQL(os.getenv('BASE_DATOS')).query_db(query, data)
