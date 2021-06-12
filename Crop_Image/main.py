import cv2

img = cv2.imread("../resources/one.jpg")

# Current image shape
print(img.shape)

width, height = 400, 400

imgResize = cv2.resize(img, (width, height))

print(imgResize.shape)

# image cropped
imgCropped = img[300:720, :]

cv2.imshow("Image", img)

cv2.imshow("Image Resize", imgResize)

cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey()
