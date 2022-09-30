from telnetlib import STATUS
import time
from itertools import count
import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hello'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gaming')
def gaming():
    return render_template('gaming.html')

@app.route('/input', methods=['POST'])
def form():
    if 'answer' not in session.keys():
        session['answer'] = 0
        answer = random.randint(1, 100)
        session['answer'] = answer
    if 'color' not in session.keys():
        session['color'] = ''
    if 'attempt' not in session.keys():
        session['attempt'] = 0
    if 'left' not in session.keys():
        session['left'] = 6
    result = session['answer']
    session['left'] -= 1
    session['attempt'] += 1
    if session['left'] <= 0:
        session['response'] = f"YOU LOSE, <br> {result} was the number"
        session['color'] = 'red'
        return render_template('lose.html')
    if int(request.form['givenNum']) > session['answer']:
        session['response'] = "Too high"
        session['color'] = 'red'
    elif int(request.form['givenNum']) < session['answer']:
        session['response'] = "Too low"
        session['color'] = 'red'
    else:
        session['response'] = f"Congratulation! <br>{result} was the number"
        session['color'] = 'green'
        return render_template('win.html')
    return redirect('/gaming')

@app.route('/record', methods=['POST'])
def record():
    now = time.localtime()
    date = time.strftime("%D", now)
    session.clear()
    session['status'] = 'win'
    return render_template('index.html', player = request.form["player"], attempt = request.form["attempt"], date = str(date))

@app.route('/again', methods=['POST'])
def again():
    session.clear()
    session['status'] = 'lose'
    return render_template('index.html')

#why cannot directly redirect the page to here and clear the session
@app.route('/restart') 
def restart():
    session.clear()
    session['status'] = 'lose'
    return render_template('index.html')


if __name__=="__main__":   
    app.run(debug=True)    