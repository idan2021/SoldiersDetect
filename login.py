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
            #map()
            return render_template('map.html')
        else:
            #return render_template('map.html')
            # Authentication failed, return error message
            return jsonify({'success': False, 'message': 'Invalid credentials'})
    else:
        print("theres no username")


@app.route('/map.html', methods=['GET'])
def map():
    # This route is for rendering the map.html template, it doesn't need any logic here
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
