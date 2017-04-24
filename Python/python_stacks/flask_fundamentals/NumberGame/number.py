from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
import random

@app.route('/')
def index():
    if 'number' in session:
        pass
    elif 'number' not in session:
        session['number'] = random.randrange(0,101)
    print session['number']
    return render_template('number.html')
#
#
@app.route('/result', methods=['POST', 'GET'])
def result():
    if int(request.form['guess']) == session['number']:
        session['response'] = 'Correct! Would you like to play again?'
    elif int(request.form['guess']) > session['number']:
        session['response'] = 'Too high, keep guessing!'
    elif int(request.form['guess']) < session['number']:
        session['response'] = 'Too low, guess again...'
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.pop('number')
    session['response'] = ''
    return redirect('/')

app.run(debug=True)
