import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="E:\ComputerVision\PyImageSearch\Opencv\images\car2.jpg", help="path to input image")
# by default opencv having value 20, but we shld keep it 2 to 8
ap.add_argument("-c", "--clip", type=float, default=2.0, help="threshold for contrast limiting")
# we shld keep this value between 4 to 10
ap.add_argument("-t", "--tile", type=int, default=8, help="tile grid size -- devides image into tile x tile cells (8x8)")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=640)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
clahe = cv2.createCLAHE(clipLimit=args["clip"], tileGridSize=(args["tile"], args["tile"]))
equalized = clahe.apply(gray)

cv2.imshow("Input", gray)
cv2.imshow("Output", equalized)
cv2.waitKey(0)