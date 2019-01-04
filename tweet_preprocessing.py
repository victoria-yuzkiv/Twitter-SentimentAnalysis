# A class for tweets pre-processing

from bs4 import BeautifulSoup
import re
from nltk.tokenize import WordPunctTokenizer


class PreprocessTweet:

    def __init__(self):
        self.name = 'PreprocessTweet'

    def decode_HTML(self, tweet):
        decoded_tweet = BeautifulSoup(tweet, 'html.parser')
        return decoded_tweet.get_text()

    def remove_mentions(self, tweet):
        return re.sub(r'@[A-Za-z0-9]+', '', tweet)

    def remove_links(self, tweet):
        return re.sub('((www.[^ ]+)|(https?://[A-Za-z0-9./]+))', '', tweet)

    def remove_BOM(self, tweet):
        try:
            bom_tweet = tweet.bytes(tweet, 'iso-8859-1').decode('utf-8-sig').replace("\ufffd", "?")
        except:
            bom_tweet = tweet
        return bom_tweet

    def remove_nonletter_characters(self, tweet):
        # including hashtag
        return re.sub('[^a-zA-Z]', ' ', tweet)

    def to_lower(self, tweet):
        return tweet.lower()

    def hadle_negations(self, tweet):
        negations = {"isn't": "is not", "aren't": "are not", "wasn't": "was not", "weren't": "were not",
                     "haven't": "have not", "hasn't": "has not", "hadn't": "had not", "won't": "will not",
                     "wouldn't": "would not", "don't": "do not", "doesn't": "does not", "didn't": "did not",
                     "can't": "can not", "couldn't": "could not", "shouldn't": "should not", "mightn't": "might not",
                     "mustn't": "must not"}
        neg_pattern = re.compile(r'\b(' + '|'.join(negations.keys()) + r')\b')
        without_negations = neg_pattern.sub(lambda x: negations[x.group()], tweet)
        return re.sub("[^a-zA-Z]", " ", without_negations)

    def tokenize(self, tweet):
        tok = WordPunctTokenizer()
        return (" ".join([x for x in tok.tokenize(tweet) if len(x) > 1])).strip()
