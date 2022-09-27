import numpy as np
from skimage.exposure import is_low_contrast
from imutils.paths import list_images
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, default="E:\ComputerVision\PyImageSearch\Opencv\images", help="path to input directory or image")
ap.add_argument("-t", "--thresh", type=float, default=0.35, help="threshold for low contrast")
args = vars(ap.parse_args())

imagePaths = sorted(list(list_images(args["input"])))

for (i, imagePaths) in enumerate(imagePaths):
    print(f"[INFO] processing image {i+1, len(imagePaths)}")
    image = cv2.imread(imagePaths)
    image = imutils.resize(image, width=450)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (7,7), 0)
    edged = cv2.Canny(blurred, 30, 150)

    text = "Low contrast: No"
    color = (0, 255, 0)

    if is_low_contrast(gray, fraction_threshold=args["thresh"]):
        text = "Low contrast: Yes"
        color = (0,0,255)
    else:
        cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts, key=cv2.contourArea)

        cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        cv2.putText(image, text, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        cv2.imshow("Image", image)
        cv2.imshow("Edge", edged)
        cv2.waitKey(0)


