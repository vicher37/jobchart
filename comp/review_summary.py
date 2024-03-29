__author__ = 'Vicky Zhang'
import nltk
from nltk.corpus import brown
from django import setup
from comp.models import review_summary, ratings
import os
from pandas import *
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chart.settings")

def auto_tag(company):
    """
    tag a given text using brown corpus and unigram tagger
    :param company: company whose reviews are tagged
    :return: a list of tagged words
    """
    brown_tagged_sents = brown.tagged_sents(categories = 'news', tagset='universal')
    brown_sents = brown.sents(categories = 'news')

    # open the review of a company, and print error message if company review doesn't exist
    # first deal with unique cases such as General Motors => GM
    if company == 'General Motors':
        company = 'GM'
    elif company == 'Ford Motor Company':
        company = 'Ford'
    try:
        text = open('/Users/vickyzhang/Documents/Python/chart/comp/review/'+ company.capitalize() + '_review.txt').read()
    except FileNotFoundError:
        print('The system doesn\'t have a review for the company you entered. Please enter another company.')

    # normalize (tokenize and lowercase-ize) each word in the string
    text_token = nltk.word_tokenize(text)
    text_normal = [w.lower() for w in text_token]

    # build unigram tagger based on brown corpus, and use it to tag the normalized text
    unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
    text_tagged = unigram_tagger.tag(text_normal)
    return text_tagged

def get_length(company):
    try:
        text = open('/Users/vickyzhang/Documents/Python/chart/comp/review/'+ company.capitalize() + '_review.txt').read()
    except FileNotFoundError:
        print('The system doesn\'t have a review for the company you entered. Please enter another company.')
    return len(text)

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
    noun_fd_list = noun_fd.most_common(n=10)

    noun_fd_long_list = []
    for noun_tuple in noun_fd_list:
        noun_list = list(noun_tuple)
        noun_list.insert(1, 'NOUN')
        noun_list.insert(3, company)
        noun_fd_long_list.append(noun_list)
    return noun_fd_long_list

def common_phrases(company):
    """
    return the most common phrases and their frequencies
    :param company: company whose reviews are studied
    :return: a list of tuples of (phrases, frequency)
    """
    text_tagged = auto_tag(company)

    phrase_list = []
    i = 0
    for i in range(len(text_tagged) - 1):
        (word1, tag1) = text_tagged[i]
        (word2, tag2) = text_tagged[i+1]
        if tag1 == 'ADJ' and tag2 == 'NOUN':
            word_list = [word1, word2]
            phrase = ' '.join(word_list)
            phrase_list.append(phrase)
    phrase_series = Series(phrase_list)
    phrase_counts = phrase_series.value_counts()
    return phrase_counts
    #phrase_fd = nltk.FreqDist


def write_words(company):
    long_list = common_nouns(company=company)
    adj_long_list = common_adjs(company=company)
    for adj_item in adj_long_list:
        long_list.append(adj_item)
    setup()
    for noun_list in long_list:
        # remember: bad design if you use company name as key arg in any url/code!
        id_num_obj = ratings.objects.get(company=company)
        id_num = id_num_obj.id
        review_summary_instance = review_summary(company=noun_list[3],
                                                 word=noun_list[0],
                                                 part_of_speech=noun_list[1],
                                                 frequency=noun_list[2],
                                                 company_id = id_num)
        review_summary_instance.save()


def delete_all_records():
    setup()
    s = review_summary.objects.all()
    s.delete()

def common_adjs(company):
    """
    return the most common adjectives and their frequencies
    :param company: company whose reviews are studied
    :return: a list of tuples of (word, frequency)
    """
    text_tagged = auto_tag(company)
    adj_fd = nltk.FreqDist(word for (word, tag) in text_tagged if tag =='ADJ')
    adj_fd_list = adj_fd.most_common(n=10)

    adj_fd_long_list = []
    for adj_tuple in adj_fd_list:
        adj_list = list(adj_tuple)
        adj_list.insert(1, 'ADJ')
        adj_list.insert(3, company)
        adj_fd_long_list.append(adj_list)
    return adj_fd_long_list

def summary_json():
    setup()
    file = {}
    comp_dict = {}
    for r in ratings.objects.raw('SELECT * FROM comp_ratings'):
        words = review_summary.objects.filter(company_id = r.id)
        words_list = words.values()
        # print(words.values()[0])
        # print(type(words))

        node_list = []
        for word in words_list:
            node = {}
            node["label"] = word["word"]
            node["n"] = word["frequency"]
            node_list.append(node)
        comp_dict[r.id] = node_list
        print(comp_dict)
    comp_dict = json.dumps(comp_dict, indent=4)
    with open('/Users/vickyzhang/Documents/python/chart/jobchart/comp/static/comp/summary.json', 'a') as outfile:
        outfile.write(str(comp_dict))

def rating_json():
    setup()
    comp_dict = {}
    for r in ratings.objects.raw('SELECT * FROM comp_ratings'):
        print(r.id)
        rating = ratings.objects.filter(id = r.id)
        rating_values = rating.values()
        print(rating_values)
        fields = ratings._meta.get_all_field_names()
        node_list = []
        for field in ratings._meta.get_all_field_names():
            if field == "id": continue
            elif field == "company" : continue
            elif field == "FB_likes" : continue
            elif field == "FB_likes_score": continue
            elif field == "recommend_to_friend_rating": continue
            node = {}
            node["label"] = field
            node["n"] = float(rating_values[0][field])
            node_list.append(node)
        comp_dict[r.id] = node_list
        print(comp_dict)
    comp_dict = json.dumps(comp_dict, indent=4)
    with open('/Users/vickyzhang/Documents/python/chart/jobchart/comp/static/comp/rating.json', 'w') as outfile:
        outfile.write(str(comp_dict))

def for_bubble_chart():
    setup()
    wrapper_dict = {}
    wrapper_dict["name"] = "companies"
    wrapper_dict["children"] = []
    for r in ratings.objects.raw('SELECT * FROM comp_ratings'):
        words = review_summary.objects.filter(company_id = r.id)
        words_list = words.values()
        comp_dict = {}
        print(words_list)
        try:
            comp_dict["name"] = words_list[0]["company"]
        except:
            continue
        comp_dict["children"] = []
        for word in words_list:
            node_dict = {}
            node_dict["name"] = word["word"]
            node_dict["size"] = word["frequency"]
            comp_dict["children"].append(node_dict)
        wrapper_dict["children"].append(comp_dict)
    print(wrapper_dict)
    wrapper_dict = json.dumps(wrapper_dict, indent=4)
    with open('/Users/vickyzhang/Documents/python/chart/jobchart/comp/static/comp/for_bubble.json', 'w') as outfile:
        outfile.write(str(wrapper_dict))








if __name__ == '__main__':
    rating_json()
    # table1 = common_phrases('Cisco')
    # print(table1)
    # print(len(table1))
    # print(get_length('Cisco'))
    # print(table1.ix[0, 1]/get_length('Cisco'))
    # table2 = common_phrases('Pepsi')
    # print(table2)
    # print(len(table2))
    # print(get_length('Pepsi'))
    # print(table2.ix[0, 1]/get_length('Pepsi'))
    # # TODO: still need to read info extraction chapter in the book
