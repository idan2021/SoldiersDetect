import face_recognition
import cv2


def feceRecog(listOfObjects, index):
    face_locations = face_recognition.face_locations(listOfObjects[index])
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(listOfObjects[index], (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(listOfObjects[index], str(index), (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow("Face Recognition", listOfObjects[index])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
