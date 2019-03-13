# Predicting All NBA Teams

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

I then analyzed the weights the model put on each feature. One could assume that features such as Player Efficiency Rating, Box Plus Minus, Win Shares, and other holistic statistics would have larger weights. However, when graphing feature weights, I found that this was not necessarily the case. 

![figure_1](https://user-images.githubusercontent.com/43687112/50879800-35d48900-13aa-11e9-9169-bbef41315e58.png)

While statistics such as Win Shares (WS) and Box Plus Minus (BPM) have relatively high coefficients, statistics such as Free Throws Attempted (FTA) and 3-Pointers Attempted (3PA) have high coefficients as well. I calcualted the odds ratios for the six statistics that had the highest absolute coefficients to determine how changes in each statistic individually affect a player's chances of being selected for the All NBA team.

```
Optimization terminated successfully.
         Current function value: 0.439132
         Iterations 7
FTA    0.422007
dtype: float64
Optimization terminated successfully.
         Current function value: 0.198077
         Iterations 8
STL%    0.122124
dtype: float64
Optimization terminated successfully.
         Current function value: 0.150885
         Iterations 8
TOV%    0.769919
dtype: float64
Optimization terminated successfully.
         Current function value: 0.438272
         Iterations 8
3PA    0.300711
dtype: float64
Optimization terminated successfully.
         Current function value: 0.549872
         Iterations 6
BPM    1.479616
dtype: float64
Optimization terminated successfully.
         Current function value: 0.541649
         Iterations 6
WS    0.666764
dtype: float64
```
As expected, statistics such as FTA, STL%, and 3PA have lower odds ratios than more holisitic statistics such as BPM and WS. Surprisingly, TOV% has a relatively high odds ratio.

```
Optimization terminated successfully.
         Current function value: 0.254573
         Iterations 7
PER    0.811768
dtype: float64
```
The odds ratio of PER confirms that the more holistic statistics have a greater impact on the selection of the All NBA teams.
