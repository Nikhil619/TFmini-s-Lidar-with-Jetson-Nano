from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2

# Step.2
# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# open the output CSV file for writing and initialize the set of
# barcodes found thus far
#csv = open(args["output"], "w")
found = set()
x = 0
y= 0 
w = 0
h = 0

# Step.3
# loop over the frames from the video stream
while cv2.waitKey(1) < 0:
    # grab the frame from the threaded video stream and resize it to
    # have a maximum width of 400 pixels
    frame = vs.read()    
    frame = imutils.resize(frame, width=400)
    #thandri = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # find the barcodes in the frame and decode each of the barcodes
    barcodes = pyzbar.decode(frame)
    frame_count = 1
    # Step.4
    # loop over the detected barcodes
    for barcode in barcodes:
        print("[Barcode] starting analyze barcode %d ..." % frame_count)
        frame_count = frame_count + 1
        
        # extract the bounding box location of the barcode and draw
        # the bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        

        # the barcode data is a bytes object so if we want to draw it
        # on our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
    cv2.imshow("csv", frame)
print("[INFO] cleaning up...")
#csv.close()
cv2.destroyAllWindows()
vs.stop()