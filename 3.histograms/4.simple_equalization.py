'''
Histogram-equalization will boost the quality of the image
'''
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="E:\ComputerVision\PyImageSearch\Opencv\images\car2.jpg", help="Path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=640)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

hist = cv2.equalizeHist(gray)
cv2.imshow("Histogram equalization", hist)

cv2.waitKey(0)