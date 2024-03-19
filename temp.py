import urllib

import cv2
import face_recognition
import firebase_admin
import numpy as np
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
cred = credentials.Certificate("soliderdetect-firebase-adminsdk-c1cuj-1d8a6eaf3c.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://soliderdetect-default-rtdb.firebaseio.com/'
})

def download_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def main():
    # Retrieve image URLs from Realtime Database
    ref = db.reference('images/soliders')
    data = ref.get()
    image_urls = [item['imageURL'] for item in data.values()]

    # Download images and perform face comparison
    for i in range(len(image_urls) - 1):
        for j in range(i + 1, len(image_urls)):
            image1 = download_image(image_urls[i])
            image2 = download_image(image_urls[j])

            known_encoding = face_recognition.face_encodings(image1)[0]
            unknown_encoding = face_recognition.face_encodings(image2)[0]

            results = face_recognition.compare_faces([known_encoding], unknown_encoding)

            # Optionally, save the results to Realtime Database or use them as needed
            print(f"Comparison between {image_urls[i]} and {image_urls[j]}: {results}")

if __name__ == '__main__':
    main()