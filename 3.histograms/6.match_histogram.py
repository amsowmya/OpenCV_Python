from skimage import exposure
import argparse
import cv2
import imutils
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", type=str, default="E:\ComputerVision\PyImageSearch\Opencv\images\girl.png", help="Path to source image")
ap.add_argument("-r", "--reference", type=str, default="E:\ComputerVision\PyImageSearch\Opencv\images\img11.jpg", help="Path to reference image")
args = vars(ap.parse_args())

src = cv2.imread(args["source"])
src = imutils.resize(src, width=640)
ref = cv2.imread(args["reference"])
ref = imutils.resize(ref, width=640)

multi = True if src.shape[-1] > 1 else False
matched = exposure.match_histograms(src, ref, multichannel=multi)

cv2.imshow("Source", src)
cv2.imshow("Reference", ref)
cv2.imshow("Matched", matched)
cv2.waitKey(0)

(fig, axs) = plt.subplots(nrows=3, ncols=3, figsize=(8,8))

for (i, image) in enumerate((src, ref, matched)):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for(j, color) in enumerate(("red", "green", "blue")):
        (hist, bins) = exposure.histogram(image[..., j], source_range="dtype")
        # normalizing
        axs[j, i].plot(bins, hist / hist.max())

        (cdf, bins) = exposure.cumulative_distribution((image[..., j]))
        axs[j, i].plot(bins, cdf)

        axs[j, 0].set_ylabel(color)

axs[0,0].set_title("Source")
axs[0,1].set_title("Reference")
axs[0,2].set_title("Matched")

plt.tight_layout()
plt.show()
cv2.waitKey(0)
