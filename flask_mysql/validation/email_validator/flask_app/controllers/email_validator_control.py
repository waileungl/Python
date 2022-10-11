from flask_app import app
from flask import render_template,redirect,request, session, flash
from flask_app.models.email_validator import Email

@app.route('/')
def index():
    session.clear()
    return render_template('index.html', emails = Email.get_all_info())

@app.route('/submit', methods = ['POST'])
def submit():
    if not Email.validate_email(request.form):  
        return redirect('/')
    session['email'] = request.form['email']
    data = {
        "email": request.form['email']
    }
    Email.add_email(data)
    return redirect('/emails')

@app.route('/emails')
def emails():
    if not session:
        return redirect('/')
    flash(f"The email address you entered({session['email']}) is a VALID email address! Thank you!")
    return render_template('email.html', emails = Email.get_all_info())

@app.route('/delete/<email>')
def delete(email):
    print(email)
    Email.delete(email)
    flash(f"You have deleted ({email})!")
    return render_template('email.html', emails = Email.get_all_info())
