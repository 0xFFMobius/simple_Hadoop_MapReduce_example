#!/usr/bin/env python
import sys
from sklearn.feature_extraction import text
import string
#import sklearn

sk_swords = text.ENGLISH_STOP_WORDS

stopwords = set(
    [s.lower() for s in sk_swords] + #from sklearn
    [s.lower() for s in nltk_swords] + #from nltk
#    [s.lower() for s in sp_swords] + #from spacy
    list(string.punctuation)         #and remove punctuation
)

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stopwords:
            print '%s\t%s' % (word, "1")
