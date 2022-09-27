import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-o", "--output", required=True, help="path to the output")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w, c) = image.shape[:3]

print(f"width: {w}")
print(f"height: {h}")
print(f"channels: {c}")

cv2.imshow("Result", image)
cv2.waitKey(0)

print(args["output"])

cv2.imwrite(args["output"] + "/newimage3.png", image)