# for recording or capturing feed from web cam
import cv2  

#need for our hand detection
from cvzone.HandTrackingModule import HandDetector

from cvzone.SerialModule import SerialObject

# initialize our camera
cap = cv2.VideoCapture(0)

# set our hand tracking object
detector = HandDetector(detectionCon=0.8)
arduino = SerialObject("COM5")    # Select your own com port here


# start our while loop
while True:
    success, image = cap.read()
    hands, bboxInfo = detector.findHands(image)
    if len(hands)==1:
        print(detector.fingersUp(hands[0]))       
        if detector.fingersUp(hands[0]) == [1,1,1,1,1]:    
            arduino.sendData([181])               
        else:
            arduino.sendData([0])                        
    cv2.imshow('image',image)      
    cv2.waitKey(1)==ord("q")      