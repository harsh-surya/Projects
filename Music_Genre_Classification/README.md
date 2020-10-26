# Music Genre Classification

## About the project
In this project different deep learning architectures have been used to perform music genre classification.

## Requirements

* Python3
* Tensorflow version = 2.3.0
* Keras
* Librosa 0.8.0

## Description

### Dataset
The dataset can be downloaded from [this link](https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification). The dataset consists of 10 music genres:

 * blues
 * classical
 * country
 * disco
 * hiphop
 * jazz
 * metal
 * pop
 * reggae
 * rock

Each Genre has 50 audio files. All audio files are 30 seconds long and have a .wav extension.
The dataset has been processed using the __processData.py__ file. This file creates 10 segments from each audio file converts it into it's corresponding mfcc vector using the __librosa__ library. These vectors are stored in a dictionary along with the right labels. This dictionary is futhur converted into a json file.

### Models
This project consists of 3 models:
* Multi layered perceptron network
* Convolutional neural network
* Recurrent neural network using LSTMs

#### MLP model
This model is given in the __MLPModel.py__ file and it's trained parameters are saved in __Multi_layer_Perceptron_Model.h5__. The model summary is given below: 

![MLP Summary](https://github.com/harsh-surya/Projects/blob/master/Music_Genre_Classification/MLP_Images/Model_Summary.png)

The training results were as follows:

![MLP Training](https://github.com/harsh-surya/Projects/blob/master/Music_Genre_Classification/MLP_Images/Training.png)

The curves for loss and accuracy for the training and validation sets were:

![MLP Curves](https://github.com/harsh-surya/Projects/blob/master/Music_Genre_Classification/MLP_Images/Curve.png)

#### CNN model
This model is given in the __CNNModel.py__ file and it's trained parameters are saved in __CNN_Model.h5__. The model summary is given below: 

![CNN Summary](https://github.com/harsh-surya/Projects/blob/master/Music_Genre_Classification/CNN_Images/Model_Summary.png)

The training results were as follows:

![CNN Training](https://github.com/harsh-surya/Projects/blob/master/Music_Genre_Classification/CNN_Images/Training.png)

The curves for loss and accuracy for the training and validation sets were:

![CNN Curves](https://github.com/harsh-surya/Projects/blob/master/Music_Genre_Classification/CNN_Images/Curve.png)

#### RNN-LSTM model
This model is given in the __RNN-LSTM_Model.py__ file and it's trained parameters are saved in __RNN_LSTM_Model.h5__. The model summary is given below: 

![RNN-LSTM Summary](https://github.com/harsh-surya/Projects/blob/master/Music_Genre_Classification/RNN_LSTM_Images/Model_Summary.png)

The training results were as follows:

![RNN-LSTM Training](https://github.com/harsh-surya/Projects/blob/master/Music_Genre_Classification/RNN_LSTM_Images/Training.png)

The curves for loss and accuracy for the training and validation sets were:

![RNN-LSTM Curves](https://github.com/harsh-surya/Projects/blob/master/Music_Genre_Classification/RNN_LSTM_Images/Curve.png)
