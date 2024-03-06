import face_recognition
import os, os.path


def main():
    listPicsSoliders=list()
    listPicsTerrorists=list()
    lengthOfSoldDir = len([name for name in os.listdir('PICS\\soldiers') if (name.startswith("soldier"))])
    lengthOfTerDir = len([name for name in os.listdir('PICS\\terrorists') if (name.startswith("terrorist"))])
    for i in range(0, lengthOfSoldDir-1):
        soldierPath="PICS\\soldiers\\soldier" + str((i + 1)) + ".jpg"
        listPicsSoliders.append(face_recognition.load_image_file(soldierPath))
    for i in range(0,lengthOfTerDir-1):
        terroristPath="PICS\\terrorists\\terrorist" + str((i + 1)) + ".jpg"
        listPicsTerrorists.append(face_recognition.load_image_file(terroristPath))

    print("All OK")



if __name__ == '__main__':
    main()
