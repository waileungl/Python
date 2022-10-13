from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
db = "tv_shows_schema"

class Shows:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.description = data['description']
        self.network = data['network']
        self.date = data['date']
        self.owner_id = data['owner_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.liked_shows = []
    
    @classmethod
    def create_show(cls, data):
        query = "INSERT INTO shows(title, network, date, description, owner_id, created_at, updated_at) VALUES (%(title)s, %(network)s, %(date)s, %(description)s, %(owner_id)s, now(), now());"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def edit_show(cls, data):
        query = "UPDATE shows SET title = %(title)s, description = %(description)s, network = %(network)s, date = %(date)s WHERE shows.id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all_shows(cls, data):
        check_like_status = "SELECT * FROM likes WHERE user_id = %(id)s;"
        likedShows = connectToMySQL(db).query_db(check_like_status, data)
        liked_shows_list = []
        for row in likedShows:
            liked_shows_list.append(row["show_id"])

        query = "SELECT * FROM shows LEFT JOIN users ON users.id = shows.owner_id;"
        shows = []
        result = connectToMySQL(db).query_db(query)
        for row in result:
            shows.append(cls(row))

        info = []
        info.append(shows)
        info.append(liked_shows_list)
        return info

    @classmethod
    def liked_shows(cls, data):
        query = "SELECT * FROM likes WHERE user_id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        shows = cls(results[0])
        for row in results:
            data = {
                "id": row['show_id']
            }
        shows.
            
            
            liked_shows.append(row["show_id"])

    @classmethod
    def get_show_by_id(cls, show_id):
        query = f"SELECT COUNT(user_id) AS like_count FROM shows JOIN likes ON likes.show_id = shows.id LEFT JOIN users ON users.id = likes.user_id WHERE shows.id = {show_id};"
        num_of_like = connectToMySQL(db).query_db(query)[0]
        query = f"SELECT * FROM shows LEFT JOIN users ON shows.owner_id = users.id WHERE shows.id = {show_id};"
        show_info = connectToMySQL(db).query_db(query)[0]

        show_card = []
        show_card.append(num_of_like)
        show_card.append(show_info)
        return show_card

    @classmethod
    def delete_show(cls, data):
        query = "DELETE FROM shows WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)

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