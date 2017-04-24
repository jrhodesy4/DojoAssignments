from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
  # return render_template("survey.html")
  return 'No ninjas here!'

@app.route('/ninja')
def all():
    return render_template('pics1.html')

@app.route('/ninja/<color>')
def one(color):
    if color == 'blue':
        color = '/static/leonardo.jpg'
    elif color == 'orange':
        color = '/static/michelangelo.jpg'
    elif color == 'red':
        color = '/static/raphael.jpg'
    elif color == 'purple':
        color = '/static/donatello.jpg'
    else:
        color = '/static/notapril.jpg'
    return render_template('pics.html', color = color)

app.run(debug=True)
