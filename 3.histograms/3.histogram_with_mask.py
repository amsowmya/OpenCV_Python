from matplotlib import pyplot as plt
import numpy as np
import cv2

def plot_histogram(image, title, mask=None):
    chans = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

image = cv2.imread("E:\ComputerVision\PyImageSearch\Opencv\girl.png")
plot_histogram(image, "Histogram of original image")
cv2.imshow("original", image)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (151, 101), (371, 365), 255, -1)
cv2.imshow("mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Applying mask", masked)

plot_histogram(image, "Histogram for masked img", mask=mask)

plt.show()

