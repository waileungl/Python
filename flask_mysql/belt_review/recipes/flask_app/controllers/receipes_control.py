from flask_app import app
from flask import render_template,redirect,request, session, flash
from flask_app.models.recipes import Recipes
from flask_app.controllers import login_control
from flask_app.models.login import Users

@app.route('/recipes/new')
def add_recipe():
    if 'id' not in session:
        return redirect('/')
    return render_template("add_recipes.html")


@app.route('/create_recipe', methods = ['POST'])
def create_recipe():
    recipe_validation = Recipes.validate_recipe(request.form)
    if not recipe_validation:
        return redirect('/recipes/new')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instruction": request.form["instruction"],
        "date": request.form["date"],
        "under": request.form["under"],
        "user_id": session["id"]
    }
    Recipes.create_recipe(data)
    return redirect("/dashboard")


@app.route('/recipes/edit/<int:recipe_id>')
def edit_recipe(recipe_id):
    if 'id' not in session:
        return redirect('/')
    return render_template("edit_recipes.html", recipe_id = Recipes.get_recipe_by_id(recipe_id))

@app.route('/edit_recipe', methods = ['POST'])
def edit_recipe_submit():
    data = {
        "id": request.form["recipe_id"],
        "name": request.form["name"],
        "description": request.form["description"],
        "instruction": request.form["instruction"],
        "date": request.form["date"],
        "under": request.form["under"],
        "user_id": session["id"]
    }
    Recipes.edit_recipe(data)
    return redirect("/dashboard")

@app.route('/recipes/show/<int:recipe_id>')
def show_recipe(recipe_id):
    if 'id' not in session:
        return redirect('/')
    return render_template("show_recipes.html", recipe_id = Recipes.get_recipe_by_id(recipe_id))

@app.route('/recipes/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    if 'id' not in session:
        return redirect('/')
    data = {
        "id":recipe_id
    }
    Recipes.delete_recipe(data)
    return redirect("/dashboard")
