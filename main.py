import csv
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('age')
    gender = request.form.get('gender')
    class_ = request.form.get('class')
    rating = request.form.get('rating')
    feedback = request.form.get('feedback')
    with open('submission.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([name, email, age, gender, class_, rating, feedback])
    return redirect(url_for('success', name=name))
    csvfile.close()
  
@app.route('/success/<name>')
def success(name):
    return render_template('success.html', name=name)


app.run(host='0.0.0.0', port=81)
    
