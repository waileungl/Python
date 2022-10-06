from flask import Flask, render_template, request, redirect
from users import Users
app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)