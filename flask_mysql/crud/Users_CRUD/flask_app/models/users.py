# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Users:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query)
        print("This is the result of 'SELECT * FROM users'", results)
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for name in results:
            users.append( cls(name) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users').query_db( query, data)

    @classmethod
    def get_one(cls, id):
        query = f"SELECT * FROM users WHERE users.id = {id}"
        results = connectToMySQL('users').query_db(query)
        user = []
        for name in results:
            user.append( cls(name) )
        return user

    @classmethod
    def edit(cls, data):
        query = "UPDATE users SET first_name = %(fname)s, last_name = %(lname)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL('users').query_db( query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE users FROM users WHERE id = %(id)s;"
        return connectToMySQL('users').query_db( query, data)