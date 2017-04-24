from flask import Flask, request, redirect, render_template, session, flash
import re
import bcrypt
from mysqlconnection import MySQLConnector
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'dirtylittlesecret'

mysql = MySQLConnector(app,'login')

@app.route('/')
def index():
    login = mysql.query_db("SELECT * FROM registration")
    print login
    return render_template('login.html')

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
        query = "INSERT INTO registration (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt()),
        'created_at': 'NOW()'
        }
        mysql.query_db(query, data)
        return render_template('success.html')
    return redirect('/')
@app.route('/login', methods=['POST'])
def login():
    query = "SELECT email, password FROM registration WHERE email = :email"
    data = {'email': request.form['email']}
    result = mysql.query_db(query, data)
    hashed = result[0]['password']
    if len(result) != 0:
        if bcrypt.checkpw(request.form['password'].encode('utf8'), hashed.encode('utf8')):
            return render_template('success.html')
        else:
            flash("Password is incorrect")
            return redirect('/')
    else:
        flash('Email is incorrect')
        return redirect('/')
app.run(debug=True)




#
# @app.route('/success')
# def create():
#     login = mysql.query_db("SELECT * FROM registration")
#     print login
#     return render_template('success.html')
