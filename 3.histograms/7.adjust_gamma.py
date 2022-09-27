'''
If gamma value is less than 1 - shift the image towards the darker
If gamma value is greater than 1 - shift the image towards the lighter
'''

from __future__ import print_function
import argparse
import cv2
import imutils
import numpy as np

def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="E:\ComputerVision\PyImageSearch\Opencv\images\girl.png", help="Path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("image", image)

for gamma in np.arange(0.0, 3.5, 0.5):
    if gamma == 1:
        continue

    gamma = gamma if gamma > 0 else 0.1
    adjusted = adjust_gamma(image, gamma)
    cv2.putText(adjusted, f'Gamma: {gamma}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    cv2.imshow("IMAGES", np.hstack([image, adjusted]))
    cv2.waitKey(0)
