import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red)
cv2.imshow('canvas',canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (10, 10), (60, 60), red, 3)
cv2.imshow('canvas', canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (80, 50), (180, 100), (255, 0, 0), -1)
cv2.imshow('canvas', canvas)
cv2.waitKey(0)

# re-initialize the canvas with empty array
canvas = np.zeros((300, 300, 3), dtype="uint8")

(centerX, centerY) = (canvas.shape[1] //2, canvas.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

cv2.imshow('canvas', canvas)
cv2.waitKey(0)

# re-initialize our canvas once again
canvas = np.zeros((300, 300, 3), dtype="uint8")



# let's draw random 25 circles
for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=255, size=(3,)).tolist()
    print(color)
    pt = np.random.randint(0, high=300, size=(2,))
    print(pt)

    cv2.circle(canvas, tuple(pt), radius, color, -1)


cv2.imshow('canvas', canvas)
cv2.waitKey(0)