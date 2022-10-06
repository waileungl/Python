from flask_app.config.mysqlconnection import connectToMySQL
class Dojos:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data)

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for name in results:
            dojos.append( cls(name) )
        return dojos