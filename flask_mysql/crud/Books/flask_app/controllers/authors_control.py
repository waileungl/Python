from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.authors import Authors
from flask_app.models.books import Books

@app.route("/")
def index():
    return redirect("/authors")

@app.route("/authors")
def authors():
    return render_template("authors.html", authors = Authors.get_all_authors())

@app.route('/addAuthor', methods=["POST"])
def addAuthor():
    print("Check!")
    if len(request.form["name"]) == 0:
        return redirect('/')
    data = {
        "name": request.form["name"]
    }
    Authors.add_author(data)
    return redirect('/authors')

@app.route("/showAuthor/<int:id>/<name>")
def showAuthor(id, name):
    data = {
        "id": id
    }
    return render_template('author_favorites.html', showAuthor = Authors.showAuthor(data), authorName = name, authorid = id, books = Books.get_all_books())

@app.route("/add_author_favorite", methods=["POST"])
def add_author_favorite():
    id = int(request.form["authorid"])
    name = request.form["authorName"]
    if (request.form["bookList"] == "0"):
        return redirect(f"/showAuthor/{id}/{name}")
    data = {
        "id": id,
        "bookid": int(request.form["bookList"])
    }
    Authors.add_author_favorite(data)
    return redirect(f"/showAuthor/{id}/{name}")





