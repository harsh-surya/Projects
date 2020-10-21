import numpy as np
import cv2 as cv

#boolean to enable/disable writing
write = False

#mask values for hand detection
lower_skin = np.array([0,60,20])
upper_skin = np.array([100,187,255])

#val starts from 0 and reaches 999 to give us a total of 1000 images
val = 0
cap = cv.VideoCapture(0)

while True:
    _, img = cap.read()
    img = cv.flip(img, 1)
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
    mask = cv.inRange(img_hsv, lower_skin, upper_skin)
    
    cv.imshow("normal image", img)
    #cv.imshow("hsv image", img_hsv)
    cv.imshow("mask image", mask)
    
    if val<1000 and write == True:
        cv.imwrite("Dataset/Training/None/none" + str(val) + ".jpg", mask)
        print(val)
        
    val = val + 1
    
    if cv.waitKey(1) & 0xff == ord('q'):
        cv.destroyAllWindows()
        break