# import the necessary packages

import argparse
import imutils
import cv2
from PIL import Image 
import numpy as np

# construct the argument parse and parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required=True,
	            help="path to the input image")
args = vars(parser.parse_args())

# load the image, convert it to grayscale, blur it slightly,
# and threshold it
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 12, 13, cv2.THRESH_BINARY)[1]
print np.unique(thresh)
# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if imutils.is_cv2() else cnts[1]
cnts = cnts[0] if cv2.__version__.startswith("2.")  else cnts[1]
cnts = sorted(cnts, key=lambda c: c.shape[0], reverse=True)
print "&&&&&&&", len(cnts)
# loop over the contours
for c in cnts:
    print "typetype"
    print c.shape
    # compute the center of the contour
    M = cv2.moments(c)
    print M
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    print cX, cY
    # draw the contour and center of the shape on the image
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.circle(image, (cX, cY), 7, (255, 0, 255), -1)
    cv2.putText(image, "center", (cX - 20, cY - 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    # show the image
    cv2.imshow("Image", image*19)
    cv2.waitKey(0)
