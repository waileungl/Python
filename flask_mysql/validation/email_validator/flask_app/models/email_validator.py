from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_email(data):  
        is_valid = True
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def add_email(cls, data):
        query = "INSERT INTO email(email, created_at, updated_at) VALUES(%(email)s, now(), now());"
        return connectToMySQL('email_validator_schema').query_db(query, data)

    @classmethod
    def get_all_info(cls):
        query = "SELECT * FROM email;"
        return connectToMySQL('email_validator_schema').query_db(query)
