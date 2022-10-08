from multiprocessing import Condition
from flask_app import app
from flask import render_template,redirect,request,flash
from flask_app.models.users import Users

@app.route("/")
def index():
    return redirect("/friendships")

@app.route("/friendships")
def friendships():
    return render_template("friendships.html", friendships = Users.get_all_friendships(), users = Users.get_all_users())

@app.route("/add_user", methods=["POST"])
def add_user():
    if len(request.form["last_name"]) == 0 or len(request.form["first_name"]) == 0:
        return redirect("/friendships")
    data = {
        "last_name": request.form["last_name"],
        "first_name": request.form["first_name"]
    }
    Users.add_user(data)
    return redirect("/friendships")

@app.route("/create_friendship", methods=["POST"])
def create_friendship():

    friendships = eval(request.form["friendships"])
    for i in friendships:
        Condition0 =  str(request.form["friends"]) == str(request.form["users"])
        Condition1 = str(i["user_id"]) == str(request.form["friends"])
        Condition2 = str(i["friend_id"]) == str(request.form["users"])
        Condition3 = str(i["user_id"]) == str(request.form["users"])
        Condition4 = str(i["friend_id"]) == str(request.form["friends"])
        if (Condition1 and Condition3) or Condition0:
            flash("You can't friend youself!")  
            return redirect("/friendships")
        elif (Condition1 and Condition2) or (Condition3 and Condition4):
            flash("They are already friend!")  
            return redirect("/friendships")

    data = {
        "user_id": request.form["users"],
        "friend_id": request.form["friends"],
    }
    Users.create_friendship(data)
    return redirect("/friendships")
