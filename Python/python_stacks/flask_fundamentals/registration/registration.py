from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')
def index():
  return render_template("registration.html")

@app.route('/result', methods=['POST', 'GET'])
def result():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
    elif len(request.form['first']) < 1:
        flash("First Name field cannot be empty")
    elif not NAME_REGEX.match(request.form['first']):
        flash("Error: First Name cannot contain any numbers")
    elif len(request.form['last']) < 1:
        flash("Last Name field cannot be empty")
    elif not NAME_REGEX.match(request.form['last']):
        flash("Error: Last Name cannot contain any numbers")
    elif len(request.form['password']) < 1:
        flash("Password field cannot be empty")
    elif len(request.form['password']) < 9:
        flash("Password must be more than 8 characters ")
    elif len(request.form['confirm']) < 1:
        flash("Confirmation field cannot be empty")
    elif request.form['confirm'] != request.form['password']:
        flash('Passwords do not match')
    else:
        flash('Thanks for submitting your information')
    return redirect('/')


app.run(debug=True)
