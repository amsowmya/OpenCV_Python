from imutils.perspective import four_point_transform
from skimage import exposure
import numpy as np
import argparse
import imutils
import cv2
import sys

def find_color_card(image):
    # load the ArUCo dictionary, grab the ArUCo parameters, and detect the markers in the input image
    arucoDict =  cv2.aruco.Dictionary_get(cv2.aruco.DICT_ARUCO_ORIGINAL)
    arucoParams = cv2.aruco.DetectorParameters_create()

    (corners, ids, rejected) = cv2.aruco.detecMarkers(image, arucoDict, parameters=arucoParams)

    try:
        ids = ids.flatten()

        i = np.squeeze(np.where(ids==923))
        topLeft = np.squeeze(corners[i])[0]

        i = np.squeeze(np.where(ids == 1001))
        topRight = np.squeeze(corners[i])[1]

        i = np.squeeze(np.where(ids == 241))
        bottomRight = np.squeeze(corners[i])[2]

        i = np.squeeze(np.where(ids == 1007))
        bottomLeft = np.squeeze(corners[i])[3]

    except:
        return None

    cardCoords = np.array([topLeft, topRight, bottomRight, bottomLeft])
    card = four_point_transform(image, cardCoords)

    return card

ap = argparse.ArgumentParser()
ap.add_argument("-r", "--reference", required=True, help="path to the input reference image")
ap.add_argument("-i", "--input", required=True, help="path to the input image to apply color correction to")
args = vars(ap.parse_args())

ref = cv2.imread(args["reference"])
image = cv2.imread(args["input"])

ref = imutils.resize(ref, width=600)
image = imutils.resize(image, width=600)

cv2.imshow("Reference", ref)
cv2.imshow("Input", image)

refCard = find_color_card(ref)
imageCard = find_color_card(image)

if refCard is None or imageCard is None:
    print("[INFO] could not find color matching card in both images")
    sys.exit(0)

cv2.imshow("Reference color card", refCard)
cv2.imshow("Input color card", imageCard)

print("[INFO] matching images...")
imageCard = exposure.match_histograms(imageCard, refCard, multichannel=True)

cv2.imshow("Inout color card after matching", imageCard)
cv2.waitKey(0)



