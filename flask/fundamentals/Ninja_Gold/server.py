from array import array
from datetime import datetime
from random import randint

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "hello"

@app.route('/')
def index():
    if 'count' not in session.keys():
        session['count'] = 0
        session['list'] = ''
        session['output'] = ''
        session['left'] = 15
    return render_template('index.html')

@app.route('/findGold', methods = ['POST'])
def calculate():
    session['left'] -= 1
    date = datetime.now().strftime('%Y/%m/%d %H:%M %p')
    gold = eval(request.form['dig'])
    place = request.form['place']
    session['count'] += eval(request.form['dig'])
    if gold < 0:
        loss = abs(gold)
        session['list'] = f"<p class = 'loss'>Entered {place} and lost {loss} golds... Ouch.. ({date})</p>" + session['list']
    else:
        session['list'] = f"<p class = 'win'>Earned {gold} golds from the {place}! ({date})</p>" + session['list']
    if session['count'] >= 500:
        return redirect("/win")
    if session['left'] <= 0:
        return redirect("/lose")
    return redirect('/')

@app.route('/win', methods = ['POST'])
def win():
    return render_template(win.html)

@app.route('/lose', methods = ['POST'])
def lose():
    return render_template(lose.html)

@app.route('/reset', methods = ['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)




# @app.route('/findGold', methods = ['POST'])
# def calculate():
#     date = datetime.now().strftime('%Y/%m/%d %H:%M %p')
#     if 'farm' in request.form['dig']:
#         gold = randint(10,20)
#         place = 'farm'
#         session['count'] += gold
#     elif 'cave' in request.form['dig']:
#         gold = randint(5,10)
#         place = 'cave'
#         session['count'] += gold
#     elif 'house' in request.form['dig']:
#         gold = randint(2,5)
#         place = 'house'
#         session['count'] += gold
#     elif 'casino' in request.form['dig']:
#         gold = randint(-50,50)
#         place = 'casino'
#         session['count'] += gold
#         if gold < 0:
#             loss = abs(gold)
#             session['list'] = f"<p class = 'loss'>Entered {place} and lost {loss} golds... Ouch.. ({date})</p>" + session['list']
#             return redirect('/')
#     session['list'] = f"<p class = 'win'>Earned {gold} golds from the {place}! ({date})</p>" + session['list']
    
#     return redirect('/')