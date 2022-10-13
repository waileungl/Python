from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.login import Users
db = "tv_shows_schema"

class Shows:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.network = data['network']
        self.date = data['date']
        self.owner_id = data['owner_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def create_show(cls, data):
        query = "INSERT INTO shows(title, network, date, description, owner_id, created_at, updated_at) VALUES (%(title)s, %(network)s, %(date)s, %(description)s, %(owner_id)s, now(), now());"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def edit_show(cls, data):
        query = "UPDATE shows SET title = %(title)s, description = %(description)s, network = %(network)s, date = %(date)s WHERE shows.id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all_info_for_dashboard(cls, data):
        #Get all shows that the logged-in user liked
        query1 = "SELECT show_id AS id, title, description, network, date, owner_id, shows.created_at AS created_at, shows.updated_at AS updated_at FROM users LEFT JOIN likes ON users.id = likes.user_id LEFT JOIN shows ON likes.show_id = shows.id WHERE users.id = %(id)s;"
        results = connectToMySQL(db).query_db(query1, data)
        liked_shows = []
        #Make class for all shows
        for row in results:
            liked_shows.append(cls(row))
        #Take show_id out from class
        liked_shows_id = []
        for row in liked_shows:
            liked_shows_id.append(row.id)

        #Get all shows info and their creater info from the database
        query2 = "SELECT * FROM shows LEFT JOIN users ON users.id = shows.owner_id;"
        shows = []
        result = connectToMySQL(db).query_db(query2)
        for row in result:
            shows.append(cls(row))

        dashboard_info_pack = []
        dashboard_info_pack.append(shows) #dashboard_info_pack[0]
        dashboard_info_pack.append(liked_shows_id) #dashboard_info_pack[1]
        return dashboard_info_pack

    @classmethod
    def get_show_info_pack_by_id(cls, data):
        #Calculate ( use count() ) and get the number of likes for the show by show_id
        query1 = "SELECT COUNT(user_id) AS like_count FROM shows JOIN likes ON likes.show_id = shows.id LEFT JOIN users ON users.id = likes.user_id WHERE shows.id = %(id)s;"
        results = connectToMySQL(db).query_db(query1, data)
        num_of_like = results[0]["like_count"]

        #Get all the info of the show by show_id
        query2 = "SELECT shows.id AS id, title, description, network, date, owner_id, shows.created_at, shows.updated_at FROM shows LEFT JOIN users ON shows.owner_id = users.id WHERE shows.id = %(id)s;"
        results = connectToMySQL(db).query_db(query2, data)
        show_info = cls(results[0])

        #Get all the info of the owner of the show by show_id
        query3 = "SELECT users.id AS id, first_name, last_name, email, hash, users.created_at AS created_at, users.updated_at AS updated_at FROM shows LEFT JOIN users ON shows.owner_id = users.id WHERE shows.id = %(id)s;"
        results = connectToMySQL(db).query_db(query3, data)
        owner_info = Users(results[0])

        show_info_pack = []
        show_info_pack.append(num_of_like) #show_info_pack[0]
        show_info_pack.append(show_info) #show_info_pack[1]
        show_info_pack.append(owner_info) #show_info_pack[2]
        return show_info_pack

    @classmethod
    def delete_show(cls, data):
        query1 = "DELETE FROM likes WHERE show_id = %(show_id)s;"
        connectToMySQL(db).query_db(query1, data)
        query2 = "DELETE FROM shows WHERE id = %(show_id)s;"
        return connectToMySQL(db).query_db(query2, data)

    @classmethod
    def like_show(cls, data):
        query = "INSERT INTO likes(show_id, user_id) VALUES(%(show_id)s, %(user_id)s);"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def unlike_show(cls, data):
        query = "DELETE FROM likes WHERE user_id = %(user_id)s and show_id = %(show_id)s;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def validate_show(cls, data):
        is_valid = True
        if len(data["title"]) == 0:
            flash("Name must not be blank.", "add_show")
            is_valid = False
        if len(data["description"]) == 0:
            flash("Description must not be blank.", "add_show")
            is_valid = False
        if len(data["network"]) == 0:
            flash("network must not be blank.", "add_show")
            is_valid = False
        if len(data["date"]) == 0:
            flash("Please choose the release date.", "add_show")
            is_valid = False
        return is_valid