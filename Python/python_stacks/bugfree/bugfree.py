from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnections import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'Secretsss'

mysql = MySQLConnector(app,'emails')

@app.route('/')
def index():
    emails = mysql.query_db("SELECT * FROM emails")
    return render_template('bugfree.html')
@app.route('/success')
def create():
    emails = mysql.query_db("SELECT * FROM emails")
    print emails
    return render_template('results.html', all_emails=emails)

@app.route('/emails', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash('Email cannot be blank')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email address')
    else:
        flash('Success')
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
             'email': request.form['email'],
             'created_at': 'NOW()'
           }
        mysql.query_db(query, data)
        return redirect('/success')
    return redirect('/')
app.run(debug=True)
