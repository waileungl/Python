import string
from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.books import Books
from flask_app.models.authors import Authors

@app.route('/books')
def books():
    return render_template('books.html', books = Books.get_all_books())

@app.route('/addBook', methods=["POST"])
def addBook():
    if len(request.form["title"]) == 0 or len(request.form["page"]) == 0:
        return redirect('/books')
    data = {
        "title": request.form["title"],
        "num_of_pages": int(request.form["page"])
    }
    Books.add_book(data)
    return redirect('/books')


@app.route("/showBook/<int:id>/<name>")
def showBook(id, name):
    data = {
        "id": id
    }
    return render_template('book_favorites.html', showBook = Books.showBook(data), bookName = name, bookid = id, authors = Authors.get_all_authors())

@app.route("/add_book_favorite", methods=["POST"])
def add_book_favorite():
    id = int(request.form["bookid"])
    name = request.form["bookName"]
    if (request.form["authorList"] == "0"):
        return redirect(f"/showBook/{id}/{name}")
    data = {
        "id": int(request.form["authorList"]),
        "bookid": id
    }
    Books.add_book_favorite(data)
    return redirect(f"/showBook/{id}/{name}")