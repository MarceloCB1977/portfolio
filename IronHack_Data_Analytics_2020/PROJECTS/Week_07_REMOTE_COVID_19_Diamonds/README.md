# Diamonds Predictive Model

Project to develop a Machine Learning Model to predict a diamonds price

## Python libraries imported

for this project i used Pandas, Numpy, Seaborn, Matplotlib, Sklearn with LinearRegression, r2_score and mean_squared_error

### How i did it

We received a DataFrame with a lot of features about diamonds.
I researched and found out that i needed the 4 C's, Carat, Color, Clarity and Cut
These are the features used in the real world market to price diamonds.
Also following the real world market, i started to cluster those informations into groups.
after that, i trained and tested my model with those separate groups.

### Challenges

The challenge for me this time, was the "conventional way" of doing this, was very different from what
i found in my research about the market. I was supposed to follow a specifi order of steps, and at the time we haven't learned about clusterization yet.
I clustered it by hand, filtering the features, grouping them into clusters with pandas.
At the end, when all the models were tested against a new DataFrame, my model was the third more accurate.
I'm very proud of that.
