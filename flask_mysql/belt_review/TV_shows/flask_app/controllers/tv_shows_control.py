from flask_app import app
from flask import render_template,redirect,request, session, flash
from flask_app.models.tv_shows import Shows
from flask_app.controllers import login_control
from flask_app.models.login import Users

@app.route('/shows/new')
def add_show():
    if 'id' not in session:
        return redirect('/')
    return render_template("add_shows.html")

@app.route('/create_show', methods = ['POST'])
def create_show():
    show_validation = Shows.validate_show(request.form)
    if not show_validation:
        return redirect('/shows/new')
    data = {
        "title": request.form["title"],
        "description": request.form["description"],
        "network": request.form["network"],
        "date": request.form["date"],
        "owner_id": session["id"]
    }
    Shows.create_show(data)
    return redirect("/shows")

@app.route('/shows/<int:show_id>')
def show_show(show_id):
    if 'id' not in session:
        return redirect('/')
    return render_template("show_shows.html", show_id = Shows.get_show_by_id(show_id))

@app.route('/shows/edit/<int:show_id>')
def edit_show(show_id):
    if 'id' not in session:
        return redirect('/')
    return render_template("edit_shows.html", show_id = Shows.get_show_by_id(show_id))

@app.route('/edit_show', methods = ['POST'])
def edit_show_submit():
    id = request.form["show_id"]
    show_validation = Shows.validate_show(request.form)
    if not show_validation:
        return redirect(f'/shows/edit/{id}')
    data = {
        "id": request.form["show_id"],
        "title": request.form["title"],
        "description": request.form["description"],
        "network": request.form["network"],
        "date": request.form["date"],
        "owner_id": session["id"]
    }
    Shows.edit_show(data)
    return redirect("/shows")

@app.route('/shows/delete/<int:show_id>')
def delete_show(show_id):
    if 'id' not in session:
        return redirect('/')
    data = {
        "id":show_id
    }
    Shows.delete_show(data)
    return redirect("/shows")

@app.route('/shows/like/<int:show_id>')
def like_show(show_id):
    if 'id' not in session:
        return redirect('/')
    data = {
        "show_id": show_id,
        "user_id": session["id"]
    }
    Shows.like_show(data)
    return redirect("/shows")

@app.route('/shows/unlike/<int:show_id>')
def unlike_show(show_id):
    if 'id' not in session:
        return redirect('/')
    data = {
        "show_id": show_id,
        "user_id": session["id"]
    }
    Shows.unlike_show(data)
    return redirect("/shows")
