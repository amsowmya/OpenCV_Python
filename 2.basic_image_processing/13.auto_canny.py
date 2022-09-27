import argparse
import cv2
import glob
import imutils
import numpy as np

def auto_canny(image, sigma=0.33):
    v = np.median(image)

    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    return edged

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="E:\ComputerVision\PyImageSearch\Opencv\images\img13.jpg", help="Path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=400)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)

wide = cv2.Canny(blurred, 10, 200)
tight = cv2.Canny(blurred, 225, 250)
auto = auto_canny(blurred)

cv2.imshow("Original", image)
# cv2.imshow("Edges", np.hstack([wide, tight, auto]))
cv2.imshow("wide", wide)
cv2.imshow("tight", tight)
cv2.imshow("auto", auto)
cv2.waitKey(0)