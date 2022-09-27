import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="girl.png", help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

face = image[148:406, 184:375]
cv2.imshow("face", face)
cv2.waitKey(0)

body = image[388:763 , 50:521]
cv2.imshow("body", body)
cv2.waitKey(0)



