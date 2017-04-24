from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("name.html")

@app.route('/process', methods=['POST'])
def process():
   name = request.form['name']
   print name
   return redirect('/')
app.run(debug=True)
