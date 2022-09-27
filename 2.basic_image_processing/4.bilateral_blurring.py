'''
Bilateral blur will maintain the edges
'''

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="E:\ComputerVision\PyImageSearch\Opencv\opencv_basics\girl.png", help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
params = [(11, 21, 6), (15, 43, 9), (9, 12, 7)]

for (diameter, sigmaColor, sigmaSpace) in params:
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)

    title = f"Blurred d={diameter}, sc={sigmaColor}, ss={sigmaSpace}"
    cv2.imshow(title, blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()


