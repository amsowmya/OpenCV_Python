import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="girl.png", help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (157, 133), (444, 759), 255, -1)
cv2.imshow("Rectangular mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask applied to image", masked)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (280, 281), (100), 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Circular mask", mask)
cv2.imshow("Mask applied", masked)

cv2.waitKey(0)

