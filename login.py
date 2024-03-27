from flask import Flask, render_template, request, jsonify

import storeDB

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
