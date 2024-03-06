import face_recognition
import os, os.path
import cv2
from PIL import Image
import faceRecognitionAPI


def main():
    listPicsSoliders = list()
    listPicsTerrorists = list()
    lengthOfSoldDir = len([name for name in os.listdir('PICS\\soldiers') if (name.startswith("soldier"))])
    lengthOfTerDir = len([name for name in os.listdir('PICS\\terrorists') if (name.startswith("terrorist"))])
    for i in range(0, lengthOfSoldDir - 1):
        soldierPath = "PICS\\soldiers\\soldier" + str((i + 1)) + ".jpg"
        listPicsSoliders.append(cv2.imread(soldierPath))
        faceRecognitionAPI.feceRecog(listPicsSoliders, i)

    for i in range(0, lengthOfTerDir - 1):
        terroristPath = "PICS\\terrorists\\terrorist" + str((i + 1)) + ".jpg"
        listPicsTerrorists.append(cv2.imread(terroristPath))
        faceRecognitionAPI.feceRecog(listPicsTerrorists, i)

    print("All OK")


if __name__ == '__main__':
    main()
