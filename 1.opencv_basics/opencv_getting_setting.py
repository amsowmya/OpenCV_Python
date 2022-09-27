import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, default="girl.png", help="Path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["input"])
(h, w) = image.shape[:2]
cv2.imshow('Original', image)

(b, g, r) = image[0,0]
print(f"pixel at (0,0) - Red {r}, green {g}, and blue {b}")

(b, g, r) = image[50, 20]
print(f"pixel at (20, 50) - Red {r}, green {g}, and blue {b}")

image[50, 20] = (0,0,255)
(b, g, r) = image[50, 20]
print(f"pixel at (20, 50) - Red {r}, green {g}, and blue {b}")

(cX, cY) = (w // 2, h // 2)

tl = image[0:cY, 0:cX]
tr = image[0:cY, cX:w]
bl = image[cY:h, 0:cX]
br = image[cY:h, cX:w]

cv2.imshow('Top-Left corner', tl)
cv2.imshow('Top-right corner', tr)
cv2.imshow('Bottom-left corner', bl)
cv2.imshow('Bottom-right corner', br)

image[0:cY, 0:cX] = (0, 0, 255)

cv2.imshow('Updated image', image)
cv2.waitKey(0)