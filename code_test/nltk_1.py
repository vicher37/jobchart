__author__ = 'Vicky Zhang'

import nltk
from nltk.tag import pos_tag, map_tag
from nltk.corpus import brown
import re

def tabulate():
    rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
    cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
    cfd = nltk.ConditionalFreqDist(cvs)
    cfd.tabulate()

def index():
    rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
    cv_word_pairs = [(cv, w) for w in rotokas_words
                             for cv in re.findall(r'[ptksvr][aeiou]', w)]
    cv_index = nltk.Index(cv_word_pairs)
    print(cv_index['su'])
    print(cv_index['po'])

def get_text(file):
    """read text from a file, normalizing whitespace and stripping HTML markup."""
    text = open(file).read()
    text = re.sub('\s+', ' ', text)
    text = re.sub(r'<.*?>', ' ', text)
    return text

def tagging():
    text = nltk.word_tokenize("And now for something completely different")
    print(nltk.pos_tag(text))

def auto_tag(company):
    """
    tag a given text using brown corpus and unigram tagger
    :param company: company whose reviews are tagged
    :return: a list of tagged words
    """
    brown_tagged_sents = brown.tagged_sents(categories = 'news', tagset='universal')
    brown_sents = brown.sents(categories = 'news')

    # open the review of a company, and print error message if company review doesn't exist
    try:
        text = open('D:\\Python\\chart\\code_test\\'+ company.capitalize() + '_review.txt').read()
    except FileNotFoundError:
        print('The system doesn\'t have a review for the company you entered. Please enter another company.')

    # normalize (tokenize and lowercase-ize) each word in the string
    text_token = nltk.word_tokenize(text)
    text_nrml = [w.lower() for w in text_token]

    # build unigram tagger based on brown corpus, and use it to tag the normalized text
    unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
    text_tagged = unigram_tagger.tag(text_nrml)
    return text_tagged

def common_tags(company):
    """
    return the most common tags and their frequencies
    :param company: company whose reviews are studied
    :return: a list of tuples of (tag, frequency)
    """
    text_tagged = auto_tag(company)
    tag_fd = nltk.FreqDist(tag for (word, tag) in text_tagged)
    return tag_fd.most_common()

def common_nouns(company):
    """
    return the most common nouns and their frequencies
    :param company: company whose reviews are studied
    :return: a list of tuples of (word, frequency)
    """
    text_tagged = auto_tag(company)
    noun_fd = nltk.FreqDist(word for (word, tag) in text_tagged if tag =='NOUN')
    return noun_fd.most_common(n=10)

def common_adjs(company):
    """
    return the most common adjectives and their frequencies
    :param company: company whose reviews are studied
    :return: a list of tuples of (word, frequency)
    """
    text_tagged = auto_tag(company)
    adj_fd = nltk.FreqDist(word for (word, tag) in text_tagged if tag =='ADJ')
    return adj_fd.most_common(n=10)

def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem

if __name__ == '__main__':
    common_adjs('walmart')