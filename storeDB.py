import firebase_admin
from firebase_admin import credentials, storage, db

passwords_array = {}  # Initialize list to store passwords

# Initialize Firebase app
cred = credentials.Certificate("soliderdetect-firebase-adminsdk-c1cuj-1d8a6eaf3c.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'gs://soliderdetect.appspot.com',
    'databaseURL': 'https://soliderdetect-default-rtdb.firebaseio.com/'
})

# Store Image URL in Realtime Database
def save_image_url_to_database(image_url, folder_name):
    ref = db.reference('images/' + folder_name)  # Reference the folder in the database
    ref.push({
        'imageURL': image_url
    })

# Example usage
def upload_images(image_urls, folder_name):
    for image_url in image_urls:
        save_image_url_to_database(image_url, folder_name)

# List of image URLs and corresponding folder names
image_urls_and_folders = [
    {'url': 'gs://soliderdetect.appspot.com/soliders/soldier1.jpg', 'folder': 'soliders'},
    {'url': 'gs://soliderdetect.appspot.com/soliders/soldier2.jpg', 'folder': 'soliders'},
    {'url': 'gs://soliderdetect.appspot.com/soliders/soldier3.jpg', 'folder': 'soliders'},
    {'url': 'gs://soliderdetect.appspot.com/soliders/soldier4.jpg', 'folder': 'soliders'},
    {'url': 'gs://soliderdetect.appspot.com/soliders/soldier5.jpg', 'folder': 'soliders'},
    {'url': 'gs://soliderdetect.appspot.com/soliders/soldier6.jpg', 'folder': 'soliders'},
    {'url': 'gs://soliderdetect.appspot.com/soliders/soldier7.jpg', 'folder': 'soliders'},
    {'url': 'gs://soliderdetect.appspot.com/soliders/soldier8.jpg', 'folder': 'soliders'},
    {'url': 'gs://soliderdetect.appspot.com/soliders/soldier9.jpg', 'folder': 'soliders'},
    {'url': 'gs://soliderdetect.appspot.com/soliders/soldier10.jpg', 'folder': 'soliders'},
    {'url': 'gs://soliderdetect.appspot.com/terrorists/terrorist1.jpg', 'folder': 'terrorists'},
    {'url': 'gs://soliderdetect.appspot.com/terrorists/terrorist2.jpg', 'folder': 'terrorists'},
    {'url': 'gs://soliderdetect.appspot.com/terrorists/terrorist3.jpg', 'folder': 'terrorists'},
    {'url': 'gs://soliderdetect.appspot.com/terrorists/terrorist4.jpg', 'folder': 'terrorists'},
    {'url': 'gs://soliderdetect.appspot.com/terrorists/terrorist5.jpg', 'folder': 'terrorists'},


    # Add more image URLs and folder names as needed
]

# Upload images to database
for item in image_urls_and_folders:
    upload_images([item['url']], item['folder'])


# Function to retrieve user passwords from Firebase
def get_user_passwords():
    users_ref = db.reference('users')  # Reference the node where user data is stored
    users_data = users_ref.get()  # Retrieve user data from Firebase


    if users_data:
        for user_id, user_info in users_data.items():
            # Assuming user_info is a dictionary containing user information
            # Assuming each user_info dictionary contains only 'password' key
            password = user_info.get('password')
            username = user_id
            if password:
                passwords_array[username]=password
    return passwords_array

# Main function to process user passwords
def process_user_passwords():
    passwords = get_user_passwords()  # Retrieve passwords
    # Process the passwords as needed
    print("Passwords:")
    for password in passwords:
        print(password)
    return passwords_array

# Call the main function to start processing passwords
process_user_passwords()