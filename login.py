from datetime import datetime

from flask import Flask, render_template, request, jsonify
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
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user_passwords = storeDB.process_user_passwords()
    if username in user_passwords.keys():
        print(user_passwords," ",user_passwords.get(username))
        if int(user_passwords.get(username)) == int(password):        # Authentication successful, render map.html
            return render_template('map.html')
        else:
            # Authentication failed, return error message
            return jsonify({'success': False, 'message': 'Invalid credentials'})
    else:
        print("theres no username")



@app.route('/map', methods=['POST'])

def map():
    print("Accessed /map route")  # Add this line to print a message when the route is accessed
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    mark_type = request.form.get('color')

    # Connect to the MySQL database
    connection = connect_to_database()

    if connection:
        try:
            cursor = connection.cursor()
            created_at = datetime.now().time()

            # Insert the mark into the 'marks' table
            cursor.execute(
                "INSERT INTO marks (latitude, longitude, mark_type, created_at) VALUES (%s, %s, %s,%s)",
                (latitude, longitude, mark_type, created_at )
            )
            connection.commit()
            cursor.close()
            connection.close()
            return render_template('map.html')
        except Error as e:
            print(f"Error saving mark to MySQL database: {e}")
            return jsonify({'error': 'Failed to save mark'}), 500
    else:
        return jsonify({'error': 'Failed to connect to database'}), 500

if __name__ == '__main__':
    app.run(debug=True)
