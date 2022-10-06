from flask_app.config.mysqlconnection import connectToMySQL
class Ninjas:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_ninja(cls, data):
        query = "INSERT INTO ninjas ( first_name, last_name, age, dojo_id, created_at, updated_at ) VALUES ( %(fname)s, %(lname)s, %(age)s, %(dojo_id)s, NOW() , NOW() );"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data)

    @classmethod
    def get_all_ninjas(cls, data):
        query = "SELECT dojos.name AS dojos_name, ninjas.first_name, ninjas.last_name, ninjas.age FROM ninjas JOIN dojos ON dojos.id = ninjas.dojo_id WHERE dojo_id = %(dojo_id)s;"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)