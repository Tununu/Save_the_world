import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = None
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('age')
    gender = request.form.get('gender')
    class_ = request.form.get('class')
    rating = request.form.get('rating')
    feedback = request.form.get('feedback')

    if(feedback == 'Easter egg'):
		    data = 'egg'
  
    with open('submission.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([name, email, age, gender, class_, rating, feedback])
    return redirect(url_for('success', name=name, data=data))
    csvfile.close()
  
@app.route('/success/<name>, <data>')
def success(name, data):
    return render_template('success.html', name=name, data=data)


app.run(host='0.0.0.0', port=81)
