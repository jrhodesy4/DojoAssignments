from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
  return render_template("survey.html")

@app.route('/result', methods=['POST', 'GET'])
def result():
    if len(request.form['name']) < 1:
        flash("Name field cannot be empty")
        return redirect('/')
    elif len(request.form['location']) < 1:
        flash("Location field cannot be empty")
        return redirect('/')
    elif len(request.form['language']) < 1:
        flash("Language field cannot be empty")
        return redirect('/')
    elif len(request.form['comment']) < 1:
        flash("Comment field cannot be empty")
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash("Comments must be less than 120 characters")
        return redirect('/')
    else:
        return render_template('results.html', name=request.form['name'], location =request.form['location'], language=request.form['language'], comment=request.form['comment'])

@app.route('/process', methods=['GET'])
def process():
   return redirect('/')

app.run(debug=True)
