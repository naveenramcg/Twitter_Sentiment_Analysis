# import required modules
import tweepy
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

# natural language toolkit 
import nltk
nltk.download('brown')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# authentication details
consumer_key = 'CONSUMER KEY'
consumer_secret = 'CONSUMER SECRET'
access_token = 'ACCESS TOKEN'
access_token_secret = 'ACCESS TOKEN SECRET'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# initialising api and processing tweets
api = tweepy.API(auth)
topic = 'football'
a = api.search(topic, count = 100)   # search for a particular topic - set a count
x = []
for tweet in a:
  analysis = TextBlob(tweet.text)        # get every tweet text
  x.append(' '.join(analysis.words))     # clean the text - remove symbols and extract words

# getting values of polarity and subjectivity - it can be done in the above loop also
polarity = []
subjectivity = []
for tweet in x:
  analysis = TextBlob(tweet)
  polarity.append(analysis.sentiment.polarity)
  subjectivity.append(analysis.sentiment.subjectivity)

# creating a pandas a dataframe work to store data
data = {'polarity': polarity, 'subjectivity': subjectivity}
df = pd.DataFrame(data)
print(df)

# plotting the data - left side of x- axis shows negative tweets, right side shows positive tweets 
# the points on y-axis shows neutral comments
fig, ax = plt.subplots(facecolor='white')
df.plot(x = 'polarity', y='subjectivity', kind ='scatter', color = "purple", ax= ax)
