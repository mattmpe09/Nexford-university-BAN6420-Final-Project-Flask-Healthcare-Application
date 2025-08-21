from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store
data_store = []

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    feedback = request.form.get('feedback')

    # Store the data
    data_store.append({
        'name': name,
        'email': email,
        'feedback': feedback
    })

    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return "<h2>Thank you for your submission!</h2>"

@app.route('/data')
def view_data():
    return {'submissions': data_store}

if __name__ == '__main__':
    app.run(debug=True)
