import os
import json
import firebase_admin
from firebase_admin import credentials, db
from flask import Flask, jsonify

app = Flask(__name__)

# Get Firebase key & URL from environment variables
firebase_key = os.environ.get("FIREBASE_KEY")
firebase_url = os.environ.get("FIREBASE_URL")

if firebase_key and firebase_url:
    # Convert JSON string from env var to dict
    cred_dict = json.loads(firebase_key)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred, {"databaseURL": firebase_url})
else:
    raise ValueError("Firebase configuration missing! Set FIREBASE_KEY and FIREBASE_URL in Render environment.")

@app.route("/")
def home():
    return jsonify({"message": "Neuro-Waste Backend is Live "})

@app.route("/data")
def get_data():
    ref = db.reference("/")
    data = ref.get()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
