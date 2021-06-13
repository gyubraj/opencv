import cv2
import numpy as np

kernel = np.ones((5, 5), np.int8)

# img = cv2.imread('../resources/one.jpg')


def stackImage(windowWidth, windowHeight, scale, images):
    rows = len(images)
    cols = len(images[0])
    width = int(windowWidth/cols)
    height = int(windowHeight/rows)
    ver = None
    for img in images:
        hor = None
        for i in img:
            # if i.shape[:2] == images[0][0].shape[:2]:
            #     i = cv2.resize(i, (0, 0), None, scale, scale)
            # else:
            i = cv2.resize(i, (width, height), None, scale, scale)

            if len(i.shape) == 2:
                i = cv2.cvtColor(i, cv2.COLOR_GRAY2BGR)

            if hor is not None:
                hor = np.hstack((hor, i))
            else:
                hor = i
        if ver is not None:
            ver = np.vstack((ver, hor))
        else:
            ver = hor
    return ver


cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    # Edge Detection
    imgCanny = cv2.Canny(img, 100, 200)

    # Image Dilation
    imgdilation = cv2.dilate(imgCanny, kernel, iterations=1)

    # Image Eroson
    imgeroson = cv2.erode(imgdilation, kernel, iterations=1)

    displayImage = stackImage(1000, 500,
                              0.5, [[img, imgdilation],
                                    [imgeroson, imgCanny],
                                    [imgeroson, imgCanny],
                                    [img, imgdilation]
                                    ])

    cv2.imshow("Image", displayImage)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cv2.imshow("CannyImage", imgCanny)

# cv2.imshow("Dilation Image", imgdilation)

# cv2.imshow("Eroson Image", imgeroson)

cv2.waitKey()
