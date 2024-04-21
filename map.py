from urllib import request
from flask import Flask, request, jsonify
import FigmaPy as figmapy
import pprint
from FigmaPy import FigmaPy
from flask import render_template, jsonify
import storeDB
import FigmaPy as figmapy
import pprint
from FigmaPy import FigmaPy
import pprint
import mysql.connector
from mysql.connector import Error
import psycopg2

token = 'figd_7HSUewq63aMivKOxxg3TEKHhzkVRhkEks1efByaN'  # can be found in your figma user profile page
file_key = 'UL63FTDcNng8ismP3nfp58'  # can be found in the URL of the file
figmaPy = FigmaPy(token)
file = figmaPy.get_file(file_key)
# Function to connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            database='SoloderDetect',
            user='root',
            password='Aa123456'
        )
        if connection.is_connected():
            print('Connected to MySQL database')
            return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

print([x.get('name') for x in file.document.get('children')])
# ['Page 1', 'Page 2']
app = Flask(__name__)
map()
page1 = file.document.get('children')
print(page1)
print([x.get('name') for x in page1])
# ['myArrow', 'myGroup', 'myImage']

ids = [x.get('id') for x in page1]
print(ids)
# ['7:2', '7:6', '21:4']

@app.route('/')
def login_page():
    return render_template('map.html')

# Define a route to handle saving marks from the map
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

            # Insert the mark into the 'marks' table
            cursor.execute(
                "INSERT INTO marks (latitude, longitude, mark_type) VALUES (%s, %s, %s)",
                (latitude, longitude, mark_type)
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







images = figmaPy.get_file_images(file_key=file_key, ids=ids)
pprint.pprint(images.images)
# {'21:4': 'https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/9bc9fdbd-REDACTED-2d1f31e9b57e',
#  '7:2': 'https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/de2afe63d-REDACTED-8abc-9ca5b5f88ac8',
#  '7:6': 'https://figma-alpha-api.s3.us-west-2.amazonaws.com/images/f56d5d8dd-REDACTED-af17-461010e0af14'}
