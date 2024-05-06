from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for
import mysql.connector
from mysql.connector import Error
import storeDB

app = Flask(__name__)

# Function to connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            database='soliderdetect',
            user='root',
            password='Aa123456'
        )
        if connection.is_connected():
            print('Connected to MySQL database')
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

# Dummy user data (replace with Firebase authentication)
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/')
def login_page_route():  # Renamed from login_page to login_page_route
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user_passwords = storeDB.process_user_passwords()
    if username in user_passwords.keys():
        if int(user_passwords.get(username)) == int(password):        # Authentication successful, redirect to /map
            return redirect(url_for('map'))
        else:
            # Authentication failed, return error message
            return jsonify({'success': False, 'message': 'Invalid credentials'})
    else:
        print("theres no username")

# Function to save a mark to the database
def save_mark(latitude, longitude, mark_type):
    connection = connect_to_database()

    if connection:
        try:
            cursor = connection.cursor()
            created_at = datetime.now().time()

            # Insert the mark into the 'marks' table
            cursor.execute(
                "INSERT INTO marks (latitude, longitude, mark_type, created_at) VALUES (%s, %s, %s, %s)",
                (latitude, longitude, mark_type, created_at)
            )
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except Error as e:
            print(f"Error saving mark to MySQL database: {e}")
            return False
    else:
        return False

# Function to fetch all marks from the database
# Function to fetch all marks from the database
def get_marks():
    connection = connect_to_database()

    if connection:
        try:
            cursor = connection.cursor(dictionary=True)

            # Fetch all marks from the 'marks' table
            cursor.execute("SELECT * FROM marks")
            marks = cursor.fetchall()

            # Convert timedelta objects to string representation
            for mark in marks:
                mark['created_at'] = str(mark['created_at'])

            cursor.close()
            connection.close()

            return marks
        except Error as e:
            print(f"Error fetching marks from MySQL database: {e}")
            return []
    else:
        return []

@app.route('/map', methods=['GET', 'POST'])
def map():
    if request.method == 'POST':
        print("Accessed /map route")  # Add this line to print a message when the route is accessed
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        mark_type = request.form.get('color')

        # Save the mark to the database
        if not save_mark(latitude, longitude, mark_type):
            return jsonify({'error': 'Failed to save mark'}), 500

    # Fetch all marks from the database
    marks = get_marks()

    return render_template('map.html', marks=marks)

if __name__ == '__main__':
    app.run(debug=True)
