import cv2 as cv
import numpy as np
import operator
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"  #to disable gpu
import tensorflow as tf
from tensorflow import keras
from keras import models as K
from Functions import action

#boolean to enable/disable gesture controls
controls = True         

cap = cv.VideoCapture(0)

# lower and upper bound for the mask (to be manually adjusted for hand detection)
lower = np.array([129,0,39])
upper = np.array([169,169,255])

while True:
    _, img = cap.read()
    #optional step (depends on the input)
    img = cv.flip(img, 1)       
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(img_hsv, lower, upper)
    
    #loading trained model
    model = K.load_model("HandGestureDetection_cnn.h5")     
    cp_mask = mask.copy()
    cp_mask = cv.resize(cp_mask, (256,256))
    #resizing image for prediction
    in_img = cp_mask.reshape(-1,256,256,1)              
    prediction = model.predict(in_img)
    
    #To convert one hot vector prediction to text(class name)
    predictor = {"Fist": prediction[0][0],
                 "Next": prediction[0][1],
                 "None": prediction[0][2],
                 "OneFinger": prediction[0][3],
                 "Palm": prediction[0][4],
                 "Previous": prediction[0][5],
                 "Swing": prediction[0][6],
                 "ThreeFinger": prediction[0][7],
                 "TwoFinger": prediction[0][8]
                 }
    predictor = sorted(predictor.items(), key = operator.itemgetter(1), reverse = True)
    
    #Putting class name on the original image
    img = cv.putText(img, predictor[0][0], (100,100), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2, cv.LINE_AA )
    
    #Finding contours in the mask image
    contours, heirarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) 
    if len(contours)!=0:
        valid_contours = []
        maxarea = 0
        bigcvt = contours[0]
        
        #Isolating the biggest contour
        for cvt in contours:
            area = cv.contourArea(cvt)
            if area> maxarea:
                maxarea = area
                bigcvt = cvt
                
        #condition for granting controls        
        if maxarea>500 and controls == True:
            valid_contours.append(bigcvt)
            M = cv.moments(bigcvt)
            if M['m00'] != 0:
                #Finding the center of the contour
                cx = int(M['m10']/(M['m00']))
                cy = int(M['m01']/(M['m00']))
                action(predictor[0][0] ,cx, cy, img.shape[1], img.shape[0])
            
            #drawing the contour and it's center on the original image
            img = cv.circle(img, (cx,cy), 1, (0,0,255), 2)
            img = cv.drawContours(img, valid_contours, -1, (0,255,0), 3)
    
    
    cv.imshow("Image", img)
    cv.imshow("Mask", mask)
    if cv.waitKey(1) & 0xFF ==ord('q'):
        cv.destroyAllWindows()
        break