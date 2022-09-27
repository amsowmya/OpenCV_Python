import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="girl.png", help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original image", image)

# let's resize our image to be 150 pixels wide, but in order to prevent our resized image from
# being skewed/distorted, we must first calculate the ratio of the *new* width to the *old* width
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))

# perform actual resize of the image
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized width", resized)

cv2.resize(image, (int(image.shape[0] * (100 / image.shape[1])), 100))

# let's resize the image to have a width of 50 pixels, again keeping in mind the aspect ratio
r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized height", resized)
cv2.waitKey(0)

# calculating the ratio each and every time we want to resize an image is a real pain, so let's
# use the imutils convenience function which will *automatically* maintain our aspect ratio for us
resized = imutils.resize(image, width=100)
cv2.imshow("Resized via imutils", resized)
cv2.waitKey(0)

resized = imutils.resize(image, height=50)
cv2.imshow("Resized height via imutils", resized)
cv2.waitKey(0)

methods = [
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST), # large to small
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR), # large to small
    ("cv2.INTER_AREA", cv2.INTER_AREA), # large to small
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC), # small to large
    ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)] # small to large

for (name, method) in methods:
    print(f"[INFO] {name}")
    resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
    cv2.imshow(f"method: {name}", resized)
    cv2.waitKey(0)