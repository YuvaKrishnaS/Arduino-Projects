import cv2
import os
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

cap = cv2.VideoCapture(0)
detector = FaceDetector()
arduino = SerialObject('COM4')

while True:
    success, img = cap.read()
    img, bBxoes = detector.findFaces(img)

    if bBxoes:
        arduino.sendData([1, 0])

    else:
        arduino.sendData([0,1])


    cv2.imshow("Video", img)
    cv2.waitKey(1)