import matplotlib.pyplot as plt
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="E:\ComputerVision\PyImageSearch\Opencv\girl.png", help="Path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

chans = cv2.split(image)
colors = ('b', 'g', 'r')
plt.figure()
plt.title("Flattened color histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

# loop over the image channels
for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

# create a new figure and then plot a 2D color histogram for the green and blue channels
fig = plt.figure()
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D G and B")
plt.colorbar(p)

# plot 2D color histogram for green and red channels
ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D for G and R")
plt.colorbar(p)

# plot 2D histogram for blue and red
ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D for B and R")
plt.colorbar(p)

print(f"2D histogram shape: {hist.shape}, with {hist.flatten().shape[0]} values")

hist = cv2.calcHist([image], [0,1,2], None, [8,8,8], [0, 256, 0, 256, 0, 256])
print(f"3D histogram shape: {hist.shape}, with {hist.flatten().shape[0]}")

# display the original input image
plt.figure()
plt.axis("off")
plt.imshow(imutils.opencv2matplotlib(image))

plt.show()
