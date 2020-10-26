# Hand Gesture Detection using Neural Networks and Computer Vision

## About the project
This project implements a hand recognition and a hand gesture recognition system using neural networks and Computer Vision. The human hand gestures are detected using a classic CNN classification approach whereas the human hand itself is detected by creating binary masks using OpenCV. Also pyautogui has been used to control different mouse and keyboard operations using the different detected gestures.

## Requirements

* Python3
* Tensorflow version = 2.3.0
* Keras
* Opencv headless (cv2) for python3
* Pyautogui

## Description

### Masking
The "inRange()" function of OpenCV has been used here to create the masked image. Color detection was manually done to find the upper and lower bound of hsv values for human hand using the __color_detection.py__ file. These values were then recorded and used in other files for the same purpose.

### Dataset
The dataset has been created using the __Dataset_generator.py__ file. The dataset consists of 9 different classes:
* Fist
* Next
* None
* OneFinger
* Palm
* Previous
* Swing
* ThreeFinger
* TwoFinger

Each one of them consists of 1000 images which have been further split into train and test in a ratio of 9:1 using the __Test_Train_Split.py__ file.

### Model
The CNN model used here consists of 3 hidden convolution layers, 1 hidden fully connected layer and 1 softmax output layer. The detailed model summary is given below -

![Image of model summary](https://i.ibb.co/mBnz0Zq/model-summary.png)

This model can be found in __model.py__ file. This model was trained for a total of 10 epochs and its results were as follows -

![Image for training result](https://github.com/harsh-surya/Projects/blob/master/HandGestureDetection/Images/train.PNG)

The graphs for the accuracy and loss were also created -

Accuracy            |  Loss
:-------------------------:|:-------------------------:
![Image for accuracy](https://github.com/harsh-surya/Projects/blob/master/HandGestureDetection/Images/Accuracy_graph.png)  |  ![Image for loss](https://github.com/harsh-surya/Projects/blob/master/HandGestureDetection/Images/Loss_graph.png)

### Gesture detection and Pyautogui
__main_file.py__ and __Functions.py__ are the most important files in this project. These files are responsible for real-time hand gesture recognition and function allotment to the detected gestures.

#### _main_file.py_
This file loads the trained model (__HandGestureDetection_cnn.h5__) and then makes real-time prediction and displays the class name. It also detects the hand contour, its center and displays them. This file calls the action() function defined in the __Functions.py__ file.

#### _Functions.py_
This file uses pyautogui to perform different functions corresponding to the different detected gestures. The functions are as follows -

* movemouse() - triggered when 'Palm' or 'Fist' is detected
* movemouseslow() - triggered when 'Swing' is detected
* lclick() - triggered when 'OneFinger' is detected
* double_lclick() - triggered when 'TwoFinger' is detected
* rclick() - triggered when 'ThreeFinger' is detected
* change_window() - triggered when 'Previous' or 'Next' is detected
