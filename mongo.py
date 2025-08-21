from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["user_data"]
collection = db["users"]

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()

    expenses = {}
    for category in ["utilities", "entertainment", "school_fees", "shopping", "healthcare"]:
        if data.get(category):
            amount_key = f"{category}_amount"
            expenses[category] = float(data.get(amount_key, 0))

    user_record = {
        "age": int(data["age"]),
        "gender": data["gender"],
        "income": float(data["income"]),
        "expenses": expenses
    }

    collection.insert_one(user_record)
    return jsonify({"message": "User data saved successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
