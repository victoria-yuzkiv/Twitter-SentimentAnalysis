# Data Processing course project

The main aim of the project is to apply data preparation techniques to the raw data and use this data for a certain purpose.

I desided to use [Sentiment140 dataset](http://help.sentiment140.com/for-students/) that contains tweets with labled polarity.

## Prerequisites 

```
pip install requirements.txt
```

Moreover, if you want to run the part with collecting tweets from Twitter Streaming API, you need to create an app that interacts with the Twitter API, create file config.py with your consumer key, consumer secret, access token and access token secret.

## Step 1: Data preparation

The code of this step can be found in *Preparing dataset.ipynb*.

Changes with data:
* HTML decoding
* Dealing with @mention
* Dealing with URL links
* BOM removing
* Removing non-numeric values
* Casting to lower-case
* Negation handling
* Tokenizing and joining

Cleaned data is being saved to cleaned_data.csv.

Moreover, in the file *tweet_preprocessing.py* I created a class PreprocessTweet that allows to perform all the operations listed above.

## Step 2:  Feature selection

The code of this step can be found in *Feature selection.ipynb*.

 Before training the model, I decided to compare feature extraction methods and choose the best one. I compared two methods: **Count Vectorizer** and 
**TFIDF Vectorizer**. Results:

![Feature selection](https://github.com/victoria-yuzkiv/Twitter-SentimentAnalysis/blob/master/FeatureSelection.PNG?raw=true)

To compare these methods, we should understand: Count Vectorizer just counts the word frequencies. Simple as that. But with the TFIDF Vectorizer the value increases proportionally to count, but is offset by the frequency of the word in the corpus.
From the graph above we can see that both bigram and trigram Count Vectorizer perform better for fewer features (less than 3000).

Trigram for TFIDF Vectorizer showed the best result, so I'll use it to train the model.


## Step 3: Using Twitter Streaming API

The code of this step can be found in *Receiving tweets from TwitterStreamingAPI.ipynb*.

I received 320 tweets about Ukraine (number of tweets user can receive per one time is limited because of run time limitation) and saved into *received_tweets.csv*. I took into account tweet's language and location (to be able to perform data analysis). 

## Step 4: Predicting polarity of tweets about Ukraine

I used logistic regression to train the model and then predicted polarity of received tweets. Experiment showed that 87% of tweets are positive and only 13% - negative.

As a result, using Twitter Streaming API we can get tweets about any topic we are interested in and using trained model we can get their polarity and make the statistics.