import os
import os.path

import cv2
import face_recognition

import faceRecognitionAPI


image1 = "PICS\\soldiers\\soldier2.jpg"
image2 = "PICS\\soldiers\\soldier3.jpg"


def main():
    '''
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
    '''

    known_image = face_recognition.load_image_file(image1)
    unknown_image = face_recognition.load_image_file(image2)

    known_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([known_encoding], unknown_encoding)

    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)
    img_h_resize = hconcat_resize([img1, img2])
    image = faceRecognitionAPI.feceRecog(img_h_resize, results)
    cv2.imshow('Image_Comparison.jpg', image)
    print(results)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("All OK")


def hconcat_resize(img_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(img.shape[0]
                for img in img_list)
    im_list_resize = [cv2.resize(img, (int(img.shape[1] * h_min / img.shape[0]), h_min), interpolation=interpolation)
                      for img in img_list]
    return cv2.hconcat(im_list_resize)


if __name__ == '__main__':
    main()
