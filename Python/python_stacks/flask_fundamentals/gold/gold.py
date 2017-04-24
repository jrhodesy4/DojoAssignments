from flask import Flask, render_template, request, redirect, session
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
import random

@app.route('/')
def index():
    if 'totalgold' not in session:
        session['totalgold'] = 0

    return render_template('gold.html')

@app.route('/process_money', methods=['POST'])
def goldilocks():
    if 'log' not in session:
        session['log'] = ''
    farmgold = random.randrange(10,21)
    cavegold = random.randrange(5,11)
    housegold = random.randrange(2,6)
    casinogold = random.randrange(0,51)
    now = datetime.now().strftime("%Y/%m/%d %H:%M")
    if request.form['building'] == 'farm':
        session['totalgold'] += farmgold
        session['log'] += '<p class="win">You won ' + str(farmgold) + ' golds at the ' + request.form['building'] + ' ' + '(' + str(now) + ')</p>'

    elif request.form['building'] == 'cave':
        session['totalgold'] += cavegold
        session['log'] += '<p class="win">You won ' + str(cavegold) + ' golds at the ' + request.form['building'] + ' ' + '(' + str(now) + ')</p>'

    elif request.form['building'] == 'house':
        session['totalgold'] += housegold
        session['log'] += '<p class="win">You won ' + str(housegold) + ' golds at the ' + request.form['building'] + ' ' + '(' + str(now) + ')</p>'

    elif request.form['building'] == 'casino':
        result = random.randint(0, 1)
        if result == 0:
            session['totalgold'] -= casinogold
            session['response'] = 'Loser'
            session['log'] += '<p class="lose">You lost ' + str(casinogold) + ' at the ' + request.form['building'] + ' ' + '(' + str(now) + ')</p>'
            print session['log']
        else:
            session['totalgold'] += casinogold
            session['response'] = 'Winner'
            session['log'] += '<p class="win">You won ' + str(casinogold) + ' golds at the ' + request.form['building'] + ' ' + '(' + str(now) + ')</p>'
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['totalgold'] = 0
    session['log'] = ''
    return redirect('/')


app.run(debug=True)
