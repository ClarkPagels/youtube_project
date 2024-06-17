import nltk
nltk.download('dot')
import spacy
from textblob import TextBlob
from collections import Counter

def fileToText(text):
    with open(text) as f:
         text = f.read()
    return text
def tokenize(text):
    text = fileToText(text)
    tokens = nltk.word_tokenize(text)
    return tokens
def wordCounter(text):

    text = fileToText(text)
    array = text.split()
    return len(array)
def lemmanize(text):

    nlp = spacy.load('en_core_news_sm')
    lemanized_tokens= [token.lemma_ for token in nlp(text)]
    return lemanized_tokens
def sentiment(text):
    text = fileToText(text)
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    sentiment_subjectivity = blob.sentiment.subjectivity
    print(f"Sentiment Polarity: {sentiment_polarity}")
    print(f"Sentiment Subjectivity: {sentiment_subjectivity}")
def most_common_words(text):
    text = fileToText(text)
    split_it = text.split()
    # Pass the split_it list to instance of Counter class.
    counter = Counter(split_it)
    # most_common() produces k frequently encountered
    # input values and their respective counts.
    most_occur = counter.most_common(4)