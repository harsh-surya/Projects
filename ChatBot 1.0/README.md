# Chat bot 1.0 

Here you can find a PyTorch implementation for a contextual chat bot.

The bot here is based on a soldier named Korosser. This is a basic bot and it consists of a limited number of replies.

This project was inspired by [this article](https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077)

## Description
This bot takes input from the user, classifies it into one of the tags given in the json file using a neural network and then it replies to the user by using a random function to choose from a list of predefined responses.
* Files contained in this project are:- 
  * nltk_utils.py
  * model.py
  * train.py
  * chat.py
  * intents.json
  * data.pth
 
 ### nltk_utils.py
 This python file is used for data preprocessing. Here we have used nltk implementation of word tokenisation and word stemming for preprocessing.
 
 ### model.py
 This file has Pytorch implementation of a feed forward neural network with 3 hidden layers.
 
 ### train.py
 This file is used for training of the model. We take the input from the json file and then preprocess it using the methods described in nltk_utils.py. The model is imported from model.py. Here we have used cross entropy loss and trained our model. In the end the model has been saved in the data.pth file.
  
  ![Image of trained model](https://i.ibb.co/rZKp7y1/train.png)
 
 ### chat.py 
 This is the file where the chat bot has been implemented.
 
 ![Image of Chat Bot](https://i.ibb.co/JxwBpCm/chat.png)
 
 ### intents.json
 This json file consists of the textual data for the bot. Here data has been divided on the basis of some tags. Each tag consists of the two parts patterns and responses. The pattern part is basically our training data and responses contain a number of hardcoded responses which our bot can use. The tags in this file are :-
 * greeting
 * goodbye
 * thanks
 * introduction
 * actions
 * facts
 * funny
 
 ### data.pth
 This file consists the trained model's parameters and is used by chat.py for to load our model.
