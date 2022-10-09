from flask_app import app
from flask import render_template,redirect,request, session, flash
from flask_app.models.dojo_survey import Survey

@app.route('/')
def index():
    return render_template('index.html', users = Survey.get_all_user() )

@app.route('/submit', methods = ['POST'])
def submit():
    if not Survey.validate_survey(request.form):
        return redirect('/')
    session["name"] = request.form["fullname"]
    data = {
        "name": request.form['fullname'],
        "location": request.form['location'],
        "language": request.form['language'],
        "pokemon": request.form['pokemon'],
        "comment": request.form['commentBox']
    }
    Survey.add_survey(data)
    return redirect('/user')

@app.route('/user')
def user():
    data = {
        "name": session["name"]
    }
    return render_template('usercard.html', info = Survey.get_info(data))

@app.route('/get_info/<name>')
def get_user(name):
    data = {
        "name": name
    } 
    return render_template('usercard.html', info = Survey.get_info(data))