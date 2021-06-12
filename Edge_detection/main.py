import cv2
import numpy as np

kernel = np.ones((5, 5), np.int8)

img = cv2.imread('../resources/one.jpg')

# Edge Detection
imgCanny = cv2.Canny(img, 100, 200)

# Image Dilation
imgdilation = cv2.dilate(imgCanny, kernel, iterations=1)

# Image Eroson
imgeroson = cv2.erode(imgdilation, kernel, iterations=1)


cv2.imshow("CannyImage", imgCanny)

cv2.imshow("Dilation Image", imgdilation)

cv2.imshow("Eroson Image", imgeroson)

cv2.waitKey()
