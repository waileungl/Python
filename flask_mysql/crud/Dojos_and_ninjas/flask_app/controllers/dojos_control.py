from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojos import Dojos

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojo():
    return render_template("dojoTable.html", theDojos = Dojos.get_all_dojos())

@app.route('/addDojo', methods=["POST"])
def addDojo():
    if len(request.form["name"]) == 0:
        return redirect('/')
    data = {
        "name": request.form["name"]
    }
    Dojos.add_dojo(data)
    return redirect('/')

@app.route("/addNinja")
def addNinja():
    return render_template("addNinja.html", theDojos = Dojos.get_all_dojos())





