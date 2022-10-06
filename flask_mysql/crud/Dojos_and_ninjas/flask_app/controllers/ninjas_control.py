from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.ninjas import Ninjas

@app.route('/create_new_ninja', methods=["POST"])
def create_new_ninja():
    if len(request.form["fname"]) == 0 or len(request.form["lname"]) == 0 or len(request.form["age"]) == 0:
        return redirect('/addNinja')
    data = {
        "dojo_id": int(request.form["dojo"]),
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "age" : int(request.form["age"])
    }
    Ninjas.add_ninja(data)
    return redirect('/')

@app.route("/ninjaTable/<int:id>/<name>")
def ninjaTable(id, name):
    data = {
        "dojo_id": id
    }
    
    return render_template("ninjaTable.html", theNinjas = Ninjas.get_all_ninjas(data), dojoName = name)