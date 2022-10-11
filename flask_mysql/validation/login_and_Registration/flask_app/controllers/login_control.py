from flask_app import app
from flask import render_template,redirect,request, session, flash
from flask_app.models.login import Users
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['POST'])
def register():
    if not Users.validate_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "location": request.form['location'],
        "language": request.form['language'],
        "birthday": request.form['birthday'],
        "pokemon": request.form['pokemon'],
        "email": request.form['email'],
        "password": pw_hash
    }
    session["id"] = Users.register(data)
    return redirect('/user_profile')

@app.route('/login', methods = ['POST'])
def login():
    data = {
        "email": request.form['login_email']
    }
    user = Users.validate_login(data)
    if not user:
        flash("Invalid Email/Password", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.hash, request.form['login_password']):
        flash("Invalid Email/Password", "login")
        return redirect('/')
    session["id"] = user.id
    return redirect("/user_profile")

@app.route('/user_profile')
def profile():
    if not len(session):
        return redirect('/')
    data = {
        "id": session["id"]
    }
    return render_template('profile.html', info = Users.get_user_by_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')