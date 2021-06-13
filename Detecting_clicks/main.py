import cv2
import numpy as np

img = cv2.imread('../resources/one.jpg')


# def setCircle(x, y):
#     print(x, y)
#     cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
#     cv2.imshow("Image", img)


circles = np.zeros((4, 2), np.int)
counter = 0


def mousePoints(event, x, y, flags, parameters):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter += 1
        if counter == 4:
            counter = 0
            showImage()


def showImage():
    width, height = 250, 250
    pts1 = np.float32([
        circles[0],
        circles[1],
        circles[2],
        circles[3]
    ])
    print(pts1)
    pts2 = np.float32([
        [0, 0],
        [width, 0],
        [0, height],
        [width, height]
    ])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    print(matrix)
    output = cv2.warpPerspective(img, matrix, (width, height))
    # for x in range(0, 4):
    #     cv2.circle(img, (circles[x][0], circles[x][1]),
    #                5, (0, 0, 255), cv2.FILLED)
    cv2.imshow("New Image", output)


cv2.imshow("Image", img)

cv2.setMouseCallback("Image", mousePoints)

cv2.waitKey()
