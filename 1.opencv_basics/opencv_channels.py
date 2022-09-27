import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="girl.png", help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Blue", B)
cv2.imshow("Green", G)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

zeros = np.zeros(image.shape[:2], dtype="uint8")
cv2.imshow("Red1", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green1", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue1", cv2.merge([B, zeros, zeros]))

cv2.waitKey(0)
