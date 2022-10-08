from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import authors
class Books:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_book(cls, data):
        query = "INSERT INTO books ( title, num_of_pages, created_at, updated_at ) VALUES ( %(title)s, %(num_of_pages)s, NOW() , NOW() );"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('books_schema').query_db(query)
        books = []
        for i in results:
            books.append( cls(i) )
        return results

    @classmethod
    def showBook(cls, data):
        query = "SELECT * FROM books JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.user_id WHERE books.id = %(id)s;"
        return connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def add_book_favorite(cls, data):
        query = "INSERT INTO favorites (user_id, book_id) VALUES (%(id)s, %(bookid)s);"
        return connectToMySQL('books_schema').query_db(query, data)