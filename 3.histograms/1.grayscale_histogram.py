import matplotlib.pyplot as plt
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default = "E:\ComputerVision\PyImageSearch\Opencv\girl.png", help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=640)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

'''
compute grayscale histogram
[gray] - grayscale image, [0] - 0th channel of the image (this is gray scale image so 0), mask = None,
[256] - no. of bins in histogram (256 values in the image)
[0, 256] - range of pixel values
if we have a mask, it will compute the histogram for only masked region
'''
# calcHist(image, channel, mask, bins, pixel range)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

# matplotlib expects RGB images so convert and then display the image with matplotlib
plt.figure()
plt.axis("off")
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB))

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

