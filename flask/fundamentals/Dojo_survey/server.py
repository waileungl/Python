from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "hello"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    form = dict(request.form)
    for key in form:
        session[key] = form[key]
        print(session[key])
    return redirect('/user')

@app.route('/back', methods = ['POST'])
def back():
    session.clear()
    return redirect('/')

@app.route('/user')
def user():
    return render_template('usercard.html')

if __name__ == "__main__":
    app.run(debug=True)