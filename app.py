from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase app
cred = credentials.Certificate("soliderdetect-firebase-adminsdk-c1cuj-1d8a6eaf3c.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://soliderdetect-default-rtdb.firebaseio.com/'
})

app = Flask(__name__)

# Route for serving the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling login request
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Authenticate user using Firebase Realtime Database
    users_ref = db.reference('users')
    user_data = users_ref.child(username).get()

    if user_data and user_data.get('password') == password:
        # Authentication successful
        return jsonify({'success': True})
    else:
        # Authentication failed
        return jsonify({'success': False, 'message': 'Invalid credentials'})

if __name__ == '__main__':
    app.run(debug=True)
