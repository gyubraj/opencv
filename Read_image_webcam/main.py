import cv2

# img = cv2.imread('../resources/one.jpg')
# cv2.imshow("Bouddha", img)
# cv2.waitKey()

framewidth = 640
frameheight = 300

cap = cv2.VideoCapture("../resources/video.mp4")

# cap = cv2.VideoCapture(0)
# cap.set(3, framewidth)
# cap.set(4, frameheight)
while True:
    success, img = cap.read()
    img = cv2.resize(img, (framewidth, frameheight))
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
