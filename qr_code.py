# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:03:32 2021

@author: GONA
"""

import cv2 
from dronekit import connect

# Connect to the Vehicle
vehicle = connect('/dev/ttyTHS1', wait_ready=True, baud=57600)
 
cap = cv2.VideoCapture(0) 
  
hasFrame, frame = cap.read()
 
qrCodeDetector = cv2.QRCodeDetector()

while cv2.waitKey(1) < 0:
    #t = time.time()
    hasFrame, image = cap.read()
    decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
    
    if points is not None:
        nrOfPoints = len(points)
        print(decodedText)
        if decodedText == "TechTutorialsX!":
            for i in range(nrOfPoints):
                nextPointIndex = (i+1) % nrOfPoints
                cv2.line(image, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255,0,0), 5)
                image = cv2.rectangle(image, tuple(points[0, 0]), tuple(points[0, 2]), (0,0,0), 5)
        else:
            print("QR code not detected")    
     
    cv2.imshow("Image", image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
     

 

    
     