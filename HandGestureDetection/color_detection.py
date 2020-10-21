import cv2 as cv
import numpy as np

def empty(a):
    pass

cap = cv.VideoCapture(0)

#creating trackbar to adjust hsv values for the mask
cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars",640,360)
cv.createTrackbar("Hue Min","TrackBars",0,179,empty)
cv.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv.createTrackbar("Sat Min","TrackBars",120,255,empty)
cv.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv.createTrackbar("Val Min","TrackBars",20,255,empty)
cv.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    _, img = cap.read()
    img = cv.resize(img, (480, 270))
    img = cv.flip(img, 1)
    
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv.getTrackbarPos("Val Max", "TrackBars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    #creating mask
    mask = cv.inRange(hsv_img, lower, upper)

    cv.imshow("Mask", mask)    
    cv.imshow("Image", img)
    if cv.waitKey(1) & 0xff == ord('q'):
        cv.destroyAllWindows()
        break