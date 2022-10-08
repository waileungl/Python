from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import books
class Authors:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_author(cls, data):
        query = "INSERT INTO authors ( name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return connectToMySQL('books_schema').query_db( query, data)

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('books_schema').query_db(query)
        authors = []
        for i in results:
            authors.append( cls(i) )
        return results

    @classmethod
    def showAuthor(cls, data):
        query = "SELECT * FROM authors JOIN favorites ON authors.id = favorites.user_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def add_author_favorite(cls, data):
        query = "INSERT INTO favorites (user_id, book_id) VALUES (%(id)s, %(bookid)s);"
        return connectToMySQL('books_schema').query_db(query, data)