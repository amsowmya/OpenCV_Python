import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="E:/ComputerVision/PyImageSearch/Opencv/images/text1.jpg", help="Path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width=640, height=400)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# apply a series of erosions
for i in range(0, 5):
    eroded = cv2.erode(gray.copy(), None, iterations=i+1)  # by default kernal size is 3x3
    cv2.imshow(f'Eroded {i+1} times', eroded)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

# apply a series of dilation
for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i+1)  # by default kernal size is 3x3
    cv2.imshow(f"Dilated {i+1} times", dilated)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

# loop over the kernal sizes
# constuct a rectangular kernal from the current size and then apply an "opening" operation
kernelSizes = [(3,3), (5,5), (7,7)]

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow(f"Opening: ({kernelSize[0], kernelSize[1]})", opening)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow(f"Closing: ({kernelSize[0], kernelSize[1]})", closing)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow(f"Gradient ({kernelSize[0]} {kernelSize[1]})", gradient)
    cv2.waitKey(0)

cv2.destroyAllWindows()