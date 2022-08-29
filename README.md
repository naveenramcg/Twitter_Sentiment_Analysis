# Twitter_Sentiment_Analysis

## What is this ?
Twitter Sentiment Analysis is a data science project using python to analyze the sentiments behind tweets. The tweets can be positive, negative or neutral corresponding to a query(a topic).

## Packages used
In this project, the packages used are 
  1. tweepy : https://docs.tweepy.org/en/stable/#
  2. textblob : https://textblob.readthedocs.io/en/dev/
  3. nltk : https://www.nltk.org/
  4. matplotlib : https://matplotlib.org/3.6.0/users/index.html

## What we do ?
First of all, it is required to create a developer account with twitter to access the API. This can be done using : https://developer.twitter.com/en
After creating an account in twitter developer portal, unique consumer_key, consumer_secret, access_token, acces_token_secret, bearer_token are generated to acces the API. Using the tweepy package, the API is accessed and a tweets are retrieved, according to the search query provided.
A text processing package called textblob is used to get the subjectivity and polarity of the tweets with the help of nltk (Natural Language Tool Kit). Thus, the nature of tweets can be found out.
With pandas, the polarity and subjectivity are stored in a dataframe. Then, it is plotted as a scatter plot. The points on the left side of y-axis shows the negative tweets, on the right side of y-axis shows the positive tweets and points on the y-axis shows neutral tweets.


## Result
Sample output 

![image](https://user-images.githubusercontent.com/76693387/187238251-ae064170-a1a1-4ca3-9f1d-0451d8f3bb93.png)
