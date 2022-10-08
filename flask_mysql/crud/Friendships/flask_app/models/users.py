from flask_app.config.mysqlconnection import connectToMySQL

class Users:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_friendships(cls):
        query = "SELECT CONCAT(users.first_name, ' ', users.last_name) AS User, CONCAT(friends.first_name, ' ', friends.last_name) AS Friend, friendships.friend_id AS friend_id, friendships.user_id AS user_id FROM users LEFT JOIN friendships ON users.id = friendships.user_id LEFT JOIN users AS friends ON friends.id = friendships.friend_id;"
        return connectToMySQL('friendships_schema').query_db(query)

    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users(first_name, last_name, created_at, updated_at) VALUES(%(first_name)s, %(last_name)s, now(), now());"
        return connectToMySQL('friendships_schema').query_db(query, data)

    @classmethod
    def get_all_users(cls):
        query = "SELECT CONCAT(users.first_name, ' ', users.last_name) AS name, users.id FROM users;"
        return connectToMySQL('friendships_schema').query_db(query)

    @classmethod
    def create_friendship(cls, data):
        query = "INSERT INTO friendships(user_id, friend_id, created_at, updated_at) VALUES(%(user_id)s, %(friend_id)s, now(), now());"
        return connectToMySQL('friendships_schema').query_db(query, data)