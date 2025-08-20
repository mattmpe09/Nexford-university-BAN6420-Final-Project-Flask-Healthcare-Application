from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Replace with your MongoDB connection string
client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority")
db = client['user_data_db']
collection = db['submissions']

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    feedback = request.form.get('feedback')
    expenses = {
        'food': request.form.get('food'),
        'transport': request.form.get('transport'),
        'entertainment': request.form.get('entertainment'),
        'utilities': request.form.get('utilities')
    }

    # Insert into MongoDB
    collection.insert_one({
        'name': name,
        'email': email,
        'feedback': feedback,
        'expenses': expenses
    })

    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return "<h2>Thank you for your submission!</h2>"

@app.route('/data')
def view_data():
    submissions = list(collection.find({}, {'_id': 0}))
    return {'submissions': submissions}

if __name__ == '__main__':
    app.run(debug=True)
