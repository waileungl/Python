from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.users import Users

@app.route("/")
def index():
    return redirect("/friendships")

@app.route("/friendships")
def friendships():
    return render_template("friendships.html", friendships = Users.get_all_friendships(), users = Users.get_all_users())

@app.route("/add_user", methods=["POST"])
def add_user():
    data = {
        "last_name": request.form["last_name"],
        "first_name": request.form["first_name"]
    }
    Users.add_user(data)
    return redirect("/friendships")

@app.route("/create_friendship", methods=["POST"])
def create_friendship():
    data = {
        "user_id": request.form["users"],
        "friend_id": request.form["friends"]
    }
    Users.create_friendship(data)
    return redirect("/friendships")
