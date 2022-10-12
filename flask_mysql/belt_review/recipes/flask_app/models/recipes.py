from unittest import result
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
db = "recipe_schema"

class Recipes:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date = data['date']
        self.under = data['under']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create_recipe(cls, data):
        query = "INSERT INTO recipes(name, description, instruction, date, under, user_id, created_at, updated_at) VALUES(%(name)s, %(description)s, %(instruction)s, %(date)s, %(under)s, %(user_id)s, now(), now());"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def edit_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, date = %(date)s, under = %(under)s WHERE recipes.id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id;"
        return connectToMySQL(db).query_db(query)

    @classmethod
    def get_recipe_by_id(cls, recipe_id):
        query = f"SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id = {recipe_id};"
        return connectToMySQL(db).query_db(query)[0]

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def validate_recipe(cls, data):
        is_valid = True
        if len(data["name"]) == 0:
            flash("Name must not be blank.", "add_recipe")
            is_valid = False
        if len(data["description"]) == 0:
            flash("Description must not be blank.", "add_recipe")
            is_valid = False
        if len(data["instruction"]) == 0:
            flash("Instruction must not be blank.", "add_recipe")
            is_valid = False
        if len(data["date"]) == 0:
            flash("Please choose the date.", "add_recipe")
            is_valid = False
        return is_valid