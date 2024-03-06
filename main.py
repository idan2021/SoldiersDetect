import face_recognition
import os, os.path
import cv2
from PIL import Image
import faceRecognitionAPI
import sys


def main():
    listPicsSoliders = list()
    listPicsTerrorists = list()
    lengthOfSoldDir = len([name for name in os.listdir('PICS\\soldiers') if (name.startswith("soldier"))])
    lengthOfTerDir = len([name for name in os.listdir('PICS\\terrorists') if (name.startswith("terrorist"))])
    for i in range(0, lengthOfSoldDir - 1):
        soldierPath = "PICS\\soldiers\\soldier" + str((i + 1)) + ".jpg"
        listPicsSoliders.append(cv2.imread(soldierPath))
        #faceRecognitionAPI.feceRecog(listPicsSoliders, i)

    for i in range(0, lengthOfTerDir - 1):
        terroristPath = "PICS\\terrorists\\terrorist" + str((i + 1)) + ".jpg"
        listPicsTerrorists.append(cv2.imread(terroristPath))
        #faceRecognitionAPI.feceRecog(listPicsTerrorists, i)

    known_image = face_recognition.load_image_file("PICS\\soldiers\\soldier2.jpg")
    unknown_image = face_recognition.load_image_file("PICS\\soldiers\\soldier8.jpg")

    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
    print(results)

    print("All OK")


if __name__ == '__main__':
    main()
