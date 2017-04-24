from flask import Flask, request, redirect, render_template, session, flash
import re
import bcrypt
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'dirtylittlesecret'

mysql = MySQLConnector(app,'new_wall')

@app.route('/')
def index():
    if 'user' not in session:
        session['user'] = 0
    # login = mysql.query_db("SELECT * FROM people")
    # print login
    return render_template('loginwall.html')

@app.route('/register', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash('Email cannot be blank')
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email address')
        return redirect('/')
    if len(request.form['first_name']) < 2:
        flash('First Name has to be at least 2 characters long')
        return redirect('/')
    elif not NAME_REGEX.match(request.form['first_name']):
        flash('First Name has to be letters only')
        return redirect('/')
    if len(request.form['last_name']) < 2:
        flash('Last Name has to be at least 2 characters long')
        return redirect('/')
    elif not NAME_REGEX.match(request.form['last_name']):
        flash('Last Name has to be letters only')
        return redirect('/')
    if len(request.form['email']) < 8:
        flash('Password has to be at least 8 characters long')
        return redirect('/')
    if request.form['password'] != request.form['confirm']:
        flash('Confirmation does not match password')
        return redirect('/')
    else:
        password = request.form['password']
        query = "INSERT INTO people (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.hashpw(request.form['password'].encode('utf8'), bcrypt.gensalt()),
        'created_at': 'NOW()'
        }
        session['user'] = mysql.query_db(query, data)
        return redirect('/wall')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    query = "SELECT id, email, password FROM people WHERE email = :email"
    data = {'email': request.form['email']}
    results = mysql.query_db(query, data)
    hashed = result[0]['password']
    session['user'] = results[0]['id']
    if results:
        result = results[0]
        if bcrypt.checkpw(request.form['password'].encode('utf8'), hashed.encode('utf8')):
            return redirect('/wall')
        else:
            flash("Invalid login information")
            return redirect('/')
    else:
        flash('Invalid login information')
        return redirect('/')

@app.route('/message', methods=['POST'])
def message():
    query = "INSERT INTO messagings (message, created_at, updated_at, users_id) VALUES (:message, NOW(), NOW(), :users_id)"
    data = {
    'message': request.form['messagings'],
    'users_id': session['user']
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/wall')
def getmessage():
    print 6
    query = "SELECT message FROM messagings WHERE message = :message"
    data = {'message': request.form['messagings']}
    message = mysql.query_db(query, data)
    return render_template('wall.html', all_messages=message)
app.run(debug=True)
