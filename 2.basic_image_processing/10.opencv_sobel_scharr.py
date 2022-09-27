import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="E:\ComputerVision\PyImageSearch\Opencv\images\coin4.jpg", help="Path to image")
ap.add_argument("-s", "--scharr", type=int, default=0, help="If you want scharr enter the value greater than 0")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, height=640, width=400)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

ksize = -1 if args["scharr"] > 0 else 3
gX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
gY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)

# the gradient magnitude images are now of the floating point data type, so we need to take care
# to convert them back a to unsigned 8-bit integer representation so other OpenCV functions can
# operate on them and visualize them
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

# combine the gradient representations into a single image
combined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

cv2.imshow("Sobel/Scharr X", gX)
cv2.imshow("Sobel/Scharr", gY)
cv2.imshow("Soble/Scharr Combined", combined)
cv2.waitKey(0)
