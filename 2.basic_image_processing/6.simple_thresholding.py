import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="E:\ComputerVision\PyImageSearch\Opencv\images\coin2.jpg", help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=640, height=400)
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)

# apply basic thresholding -- the first parameter is the image we want to threshold,
# the secong value is out threshold check; if a pixel value is greater than our threshold
# (in this case 150), we set it to be *black, otherwise it is *white* (255)

(T, threshInv) = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh binary inverse", threshInv)

(T, thresh) = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresh binary", thresh)
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Output", masked)
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask=thresh)
cv2.imshow("mask", masked)
cv2.waitKey(0)