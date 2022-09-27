from skimage.exposure import rescale_intensity
import argparse
import cv2
import numpy as np
import imutils

def convolve(image, kernel):
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]

    # allocate memory for the output image, taking care to "pad" the borders of the input image so the
    # spatial size (i,e. width and height) are not reduced
    pad = (kW - 1) // 2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float32")

    # loop over the input image, 'sliding' the kernel accross each (x, y)-coordinate from left-to-right
    # and top to bottom
    for y in np.arange(pad, iH+pad):
        for x in np.arange(pad, iW+pad):
            # extract the ROI of the image by extracting the *center* region of the current (x, y)-coordinates
            roi = image[y-pad : y+pad+1, x-pad : x+pad+1]

            #perform the actual convolution by taking the element-wise multiplicaite between the ROI and the
            # kernel, then summing the matrix
            k = (roi * kernel).sum()

            # store the convolved value in the output (x,y)-coordinate of the output image
            output[y-pad, x-pad] = k

    # rescale the output image to be in the range [0, 255]
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")

    # return the output image
    return output

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="E:\ComputerVision\PyImageSearch\Opencv\images\img11.jpg", help="Path to input image")
args= vars(ap.parse_args())

# construct average blurring kernels used to smooth an image
smallBlur = np.ones((7,7), dtype="float") * (1.0 / (7 * 7))
largeBlur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))

# construct a sharpening filter
sharpen = np.array((
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]), dtype="int")

# construct the Laplacian kernel used to detect edge-like regions of an image
laplacian = np.array((
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]), dtype="int")

# construct the Sobel x-axis kernel
sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype="int")

# construct the Sobel y-axis kernel
sobelY = np.array((
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]), dtype="int")

scharrX = np.array((
    [3, 0, -3],
    [10, 0, -10],
    [3, 0, -3]), dtype="int")

scharrY = np.array((
    [3, 10, 3],
    [0, 0, 0],
    [-3, -10, -3]), dtype="int")

# construct the kernel bank, a list of kernels we are going to apply using both our custom 'convole' function and
# Opencv's 'filter2D' function
kernelBank = (
    ("small_blur", smallBlur),
    ("large_blur", largeBlur),
    ("sharpen", sharpen),
    ("laplacian", laplacian),
    ("sobel_x", sobelX),
    ("sobel_y", sobelY),
    ("scharr_x", scharrX),
    ("scharr_y", scharrY)
)

image = cv2.imread(args["image"])
image = imutils.resize(image, width=640, height=400)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for (kernelName, kernel) in kernelBank:
    print(f"[INFO] applying {kernelName} kernel")
    convoleOutput = convolve(gray, kernel)
    opencvOutput = cv2.filter2D(gray, -1, kernel)

    cv2.imshow("Original", gray)
    cv2.imshow(f"{kernelName} - convolve", convoleOutput)
    cv2.imshow(f"{kernelName} - opencv", opencvOutput)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




