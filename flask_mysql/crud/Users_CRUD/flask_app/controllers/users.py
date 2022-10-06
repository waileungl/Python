# burgers.py
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.users import Users


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/create_new_user', methods=["POST"])
def create_new_user():
    #To prevent users submiting empty form
    if len(request.form["fname"]) == 0 or len(request.form["lname"]) == 0 or len(request.form["email"]) == 0:
        return redirect('/')
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Users.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/user_table')

@app.route("/user_table")
def userTable():
    return render_template("userTable.html", theUsers = Users.get_all())

@app.route("/userList", methods=["POST"])
def redirectHome():
    return redirect("/user_table")

@app.route("/show", methods=["POST"])
def userCard():
    session['user_id'] = request.form['user_card']
    return render_template("userCard.html", theUser = Users.get_one(session['user_id']))

@app.route('/edit_user', methods=["POST"])
def edit_user():
    if len(request.form["fname"]) == 0 or len(request.form["lname"]) == 0 or len(request.form["email"]) == 0:
        return redirect('/')
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        "id" : session['user_id']
    }
    Users.edit(data)
    return redirect('/user_table')

@app.route('/editNow', methods=["POST"])
def editNow():
    session['user_id'] = request.form['user_card']
    return render_template("edit.html")

@app.route('/deleteNow', methods=["POST"])
def deleteNow():
    session['user_id'] = request.form['user_card']
    data = {
        "id" : session['user_id']
    }
    Users.delete(data)
    return redirect("/user_table")
