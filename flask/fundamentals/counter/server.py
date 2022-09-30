from itertools import count
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hello'


@app.route('/')
def index():
    if 'click' not in session.keys():
        session['click'] = 0
    if 'visit' not in session.keys():
        session['visit'] = 0
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def click():
    session['visit'] += 1
    if request.form['click'] == "0":
        session['click'] = 0
    elif (request.form['click'] == "-1"):
        session['click'] += 2
    else:
        session['click'] += 1
    return redirect('/')

@app.route('/input', methods=['POST'])
def form():
    session['visit'] += 1
    session['click'] += int(request.form['givenNum'])
    return redirect('/')

@app.route('/destroy_session')
def backhome():
    session['click'] = 0
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)    