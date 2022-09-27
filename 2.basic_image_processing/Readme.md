Morphological operations:
Erosion
Dilation
Opening
Closing
Morphological gradient
Black hat
Top hat (White hat)

1. Erosion: an erosion in an image "erods" the foreground object and makes it smaller. Simply put, pixels near the boundary of an object in an image will be discarded,'eroding' it away.

2. Dilation: dilation will grow the foreground pixels
3. Opening: opening is an erosion followed by dilation
4. Closing: closing is dilation followed by erosion
5. Morphological gradient: is the difference between dilation and erosion


6. Top hat/white hat: operation is used to reveal bright regions of an image on dark background
7. Black hat: is used to reveal dark regions of an image on bright background

Blur:
1. Bilateral blurring: Intension of our blurring methods have been reduce noise and derail in an image; however, as a side effect we have tended to lose edges in the image.
   To reduce noise while still maintaining edges, we can use bilateral blurring. 
   Bilateral blurring accomplishes this by introducing two Gaussian distributions
    cv2.bilateralFilter

IMP: Gaussian blur is removing the high frequency noise, and it's smoothing out the image

####################

Thresholding - General thresholding, OTSU, adaptive thresholding

Segmentation technique implies on every single pixel

Edge detection: instead of labeling every single pixel in a input image as forground and background, it just give the boundaries the contours of the object it self.
    Such that it segment the boundary between forground and background

Building block of edge detection is relay on 'Image gradients.'

Gradient Magnitude : is used to measure how strong the change in image intensity is

Gradient orientaion : is used to determine in which direction the change in intensity is pointing

----------------------

Kernels:
sharpen, laplacian, sobelx, sobely, schaar (varient of sobel kernel)
