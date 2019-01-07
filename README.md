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
 Before training the model, I decided to compare feature extraction methods and choose the best one. I compared two methods: **Count Vectorizer** and 
**TFIDF Vectorizer**. Results:

![Feature selection](https://github.com/victoria-yuzkiv/Twitter-SentimentAnalysis/blob/master/FeatureSelection.PNG?raw=true)

