import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="E:\ComputerVision\PyImageSearch\Opencv\images\coin2.jpg", help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=640, height=400)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)
cv2.imshow("blurred", blurred)

(T, threshInv) = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh inverse", threshInv)

(T, thresh) = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("thresh", thresh)

(T, otsu) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("otus", otsu)
print(f"[INFO] threshold value is {T}")

masked = cv2.bitwise_and(image, image, mask=thresh)
cv2.imshow("masked", masked)

cv2.waitKey(0)

########### Adaptive threshold #################
# Instead of manually specifying the threshold value, we can use adaptive thresholding to examine neighborhoods
# of pixels and adaptively threshold each neighborhood
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)
cv2.imshow("Mean Adaptive threshold", thresh)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 4)
cv2.imshow("Gaussian adaptive threshold", thresh)

cv2.waitKey(0)