import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="E:\ComputerVision\PyImageSearch\Opencv\opencv_basics\girl.png", help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
kernelSizes = [(3,3), (9,9), (15,15)]

for (Kx, Ky) in kernelSizes:
    blurred = cv2.blur(image, (Kx, Ky))
    cv2.imshow(f"Blurred ({Kx}, {Ky})", blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

for (Kx, Ky) in kernelSizes:
    blurred = cv2.GaussianBlur(image, (Kx, Ky), 0)
    cv2.imshow(f"Gaussian ({Kx}, {Ky}) blur", blurred)
    cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

for k in (3, 9, 15):
    blurred = cv2.medianBlur(image, k)
    cv2.imshow(f"Median blur {k}", blurred)
    cv2.waitKey(0)





