import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Path to input image")
ap.add_argument("-o", "--output", required=True, help="Path to the output image")
args = vars(ap.parse_args())

# load the input image from disk
image = cv2.imread(args["input"])

# convert the image to gray it, blur it, and threshold it
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7,7), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# extract contours from the image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# loop over the contours and draw them  on the input image
for c in cnts:
    cv2.drawContours(image, [c], -1, (0,255,0), 3)

# display the total num of shapes on images
text = f"I found total shape {len(cnts)}"
cv2.putText(image, text, (20, 70), cv2.FONT_HERSHEY_PLAIN, 8, (0,0,255), 8)

# write the output image to desk
cv2.imwrite(args["output"], image)



