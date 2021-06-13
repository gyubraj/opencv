import cv2
import numpy as np

img = cv2.imread('../resources/one.jpg')

width, height = 250, 250

pts1 = np.float32([
    [111, 219],
    [287, 180],
    [100, 200],
    [100, 300]
])

for x in range(0, 4):
    print(x)
    cv2.circle(img, (pts1[x][0], pts1[x][1]), 5, (0, 0, 255), cv2.FILLED)
    cv2.imshow("Image", img)

pts2 = np.float32([
    [0, 0],
    [width, 0],
    [0, height],
    [width, height]
])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

output = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", output)


cv2.waitKey()
