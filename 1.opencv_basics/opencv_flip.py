import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="girl.png", help="Path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original image", image)

flipped = cv2.flip(image, 1)
cv2.imshow("Horizontal flip", flipped)

flipped = cv2.flip(image, 0)
cv2.imshow("Vertical flip", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped both horizontal and vertical", flipped)
cv2.waitKey(0)