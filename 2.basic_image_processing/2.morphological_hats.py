import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="E:/ComputerVision/PyImageSearch/Opencv/images/car1.jpg", help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=640, height=400)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("original", image)

rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (50, 50))
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

cv2.imshow("gray", gray)
cv2.imshow("blackhat", blackhat)
cv2.imshow("tophat", tophat)
cv2.waitKey(0)