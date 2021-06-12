import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)

# img[:100, :] = 255, 0, 0

# img[:] = 255, 0, 0

cv2.line(img, (0, 0), (100, 100), (0, 255, 0), thickness=2)

# create rectangel
cv2.rectangle(img, (350, 100), (450, 200), (0, 0, 255), cv2.FILLED)


# create circle
cv2.circle(img, (100, 100), 100, (100, 100, 100), thickness=2)


# text

cv2.putText(img, "Draw Shapes", (255, 255), cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1, color=(255, 255, 255), thickness=2)
cv2.imshow("Image", img)

cv2.waitKey()
