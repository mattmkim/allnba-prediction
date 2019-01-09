# Predicting AllNBA Teams

### Description

Every season, a panel of sportswriters and broadcasters selected the 15 best NBA players to be on the All NBA team. Using data on All NBA teams and season statistics of every NBA player from 1998, I created a model that would predict the players that would be selected to be on the All NBA team. 

### Model

Using the sklearn package, I trained a support vector machine using season statistics of players from 1998 - 2012, and tested data from 2013 - 2017. Using cross-validated grid search, I was able to determine the optimal kernel and parameters to use for the support vector machine, and my model ended up predicting all 75 players who were selected to be on the All NBA teams from 2013 - 2017.

``` 
              precision    recall  f1-score   support

 Not All NBA       1.00      1.00      1.00      2296
     All NBA       1.00      1.00      1.00        75

   micro avg       1.00      1.00      1.00      2371
   macro avg       1.00      1.00      1.00      2371
weighted avg       1.00      1.00      1.00      2371

[[2296    0]
 [   0   75]]
```
### Feature Weights

I then analyzed the weights the model put on each feature. One could assume that features such as Player Efficiency Rating, Box Plus Minus, and other holistic statistics would have larger weights. However, when graphing feature weights, I found that this was not necessarily the case. 

![Alt](Users/matthew/Desktop/Figure_1.png)


