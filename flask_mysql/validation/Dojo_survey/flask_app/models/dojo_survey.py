from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.pokemon = data['pokemon']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_survey(data):
        is_valid = True
        agree = True
        if len(data['fullname']) < 3:
            flash("Name must be at least 3 character.")
            is_valid = False
        if data['location'] == "placeholder":
            flash("A location must be selected.")
            is_valid = False
        if data['language'] == "placeholder":
            flash("A language must be selected.")
            is_valid = False
        if data['pokemon'] == "placeholder":
            flash("Please select your starter pokemon!")
            is_valid = False
        if [i for i in data if i =='agreeBox'] != ['agreeBox']:
            flash("Please tick the agree box.")
            is_valid = False
        return is_valid

    @classmethod
    def add_survey(cls, data):
        query = "INSERT INTO users(name, location, language, pokemon, comment, created_at, updated_at) VALUES(%(name)s, %(location)s, %(language)s, %(pokemon)s, %(comment)s, now(), now());"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)

    @classmethod
    def get_info(cls, data):
        query = "SELECT * FROM users WHERE name = %(name)s;"
        return connectToMySQL('dojo_survey_schema').query_db(query, data)[0]

    @classmethod
    def get_all_user(cls):
        query = "SELECT name FROM users;"
        return connectToMySQL('dojo_survey_schema').query_db(query)
