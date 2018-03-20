"""Data cleaning for movie text data.

The overall data cleaning process invloves removing punctuation, 
making everything lower case, and tokenizing the text from titles and the actual reviews themselves. 
num_helpful_yes gets rid of commas and numbers and replace with empty character. 
This is because the numerical values sometimes have commas in them.
Cleaner word tokenizes the entire text with NLTK 
and then filters out all the tokens that are alphabetic. 
We then convert everything to lowercase and then join all the tokens together
to one string separated by spaces. 

"""


__version__ = '0.1'
__date__ = '3/19/2018'


import json
# import nltk
# nltk.download()
from nltk.tokenize import word_tokenize

from helper import export_to_csv
from helper import export_to_json


def clean(reviews, debug=False):
    """Clean the provided list of reviews.

    Mutates the list passed as a parameter.

    """
    for k, review in enumerate(reviews):
        # get rid of commas in numeric values
        review['num_helpful_yes'] = review['num_helpful_yes'].replace(',', '')
        review['num_helpful_total'] = review['num_helpful_yes'].replace(',', '')
        # tokenize title and remove punctuation
        title_tokens = word_tokenize(review['title'])
        title_words = [word.lower() for word in title_tokens if word.isalpha()]
        review['title'] = ' '.join(title_words)
        # tokenize text and remove stopwords
        text_tokens = word_tokenize(review['text'])
        text_words = [word.lower() for word in text_tokens if word.isalpha()]
        review['text'] = ' '.join(text_words)

        if debug and (k + 1) % 100 == 0:
            print('Finished cleaning %d reviews' % (k + 1))


if __name__ == '__main__':
    with open('reviews_raw.json', 'r') as input_file:
        reviews = json.load(input_file)
    clean(reviews, debug=True)
    export_to_csv(reviews, 'reviews_clean.csv')
    export_to_json(reviews, 'reviews_clean.json')
