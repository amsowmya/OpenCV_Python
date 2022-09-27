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
cv2.imshow("Blurred", blurred)

(T, thresholdInv) = cv2.threshold(blurred, 130, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshinv", thresholdInv)
print(f"[INFO] otsu's thresholding value: {T}")

(T, threshold) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("Thresh binary", threshold)
print(f"[INFO] otsu's thresholding value {T}")

masked = cv2.bitwise_and(image, image, mask=thresholdInv)
cv2.imshow("Masked", masked)

masked = cv2.bitwise_and(image, image, mask=threshold)
cv2.imshow("thresh masked", masked)
cv2.waitKey(0)