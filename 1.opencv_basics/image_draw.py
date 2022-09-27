import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="girl.png", help="Path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.circle(image, (301, 288), 140, (0, 0, 255))
cv2.circle(image, (235, 246), 10, (0, 0, 255), -1)
cv2.circle(image, (326, 250), 10, (0, 0, 255), -1)
cv2.rectangle(image, (247, 330), (327, 356), (0, 0, 255), -1)

cv2.imshow('image', image)
cv2.waitKey(0)