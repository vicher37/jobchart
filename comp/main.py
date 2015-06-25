__author__ = 'Vicky'

# reference: http://simplebeautifuldata.com/2014/08/25/simple-python-facebook-scraper-part-1/

from urllib.request import Request, urlopen
import urllib
import json
import pandas # as pd?
import facebook
import glassdoor
from django.core.management import call_command
import datetime
import time
from comp.models import ratings
from django import setup

list_companies = ['citi']

def ask_list():
    userInput = input('Please input the companies you are interested in and separate their names with one space.'
                      'If you want to go with the default list, just push enter to proceed.')
    if userInput == '':
        pass
    else:
        try:
            userInputParsed = userInput.split(sep = ' ')
        except ValueError:
            print('There\'s something wrong with the formatting of your input. Please read directions and try it again.')
        # could potentially be a separate block
        inputCompanies(list_companies = userInputParsed)

# def get_all_data():
#     return all_data

def return_rating():
    # print out the original data list
    facebook.return_facebook_likes()

    #global all_data
    all_data = glassdoor.add_glassdoor_rating()
    print(all_data)
    #cnx = connector.connect(user='root', password='mypw', database='jobcharted')
    #time.strftime('%m%d%y_%H%M%S')
    #all_data.to_sql(name='test3', con=cnx, flavor='mysql', schema='jobcharted', if_exists='replace')

    return all_data
    #all_data.to_sql('test1', con = SQLAlchemy, )
    # with open('D:\\Python\\jobcharted\\jobcharted\\company\\fixtures\\all.json', 'w') as outfile:
    #     all_json = all_data.to_json(orient=, )
    #     outfile.write(all_json)
    #     outfile.close()

    #call_command('loaddata', 'D:\\Python\\jobcharted\\jobcharted\\company\\data\\all.json')

def write_to_mysql():
    all_df = return_rating()
    for i in range(len(all_df.index)):
        # extract rating data from all_df as a list
        data_row = all_df.ix[i]
        row_value_list = data_row.values.tolist()

        # prepend company name
        index_name = all_df.index.values[i]
        row_value_list.insert(0, index_name)
        print(row_value_list)

        # initiate instance, save to mysql database
        setup()
        company_value = row_value_list[0]
        FB_likes_value = row_value_list[1]
        FB_likes_score_value = row_value_list[2]
        overall_rating_value = row_value_list[3]
        senior_leadership_rating_value = row_value_list[4]
        work_life_balance_rating_value = row_value_list[5]
        recommend_to_friend_rating_value = row_value_list[6]
        culture_and_values_rating_value = row_value_list[7]
        rating_instance = ratings(company = company_value,
                                 FB_likes = FB_likes_value,
                                 FB_likes_score = FB_likes_score_value,
                                 overall_rating = overall_rating_value,
                                 senior_leadership_rating = senior_leadership_rating_value,
                                 work_life_balance_rating = work_life_balance_rating_value,
                                 recommend_to_friend_rating = recommend_to_friend_rating_value,
                                 culture_and_values_rating = culture_and_values_rating_value)
        rating_instance.save()


def delete_objects(condition):
    ''' Just an example on how to clear none/default records. Make sure you imported django and ran django.setup()
    fist. For more info, refer to the screenshot in django folder.'''
    ratings.objects.filter(condition).delete()

def update_objects(condition):
    # replace with new conditions!!
    # Be very careful when you use it!!
    pass

def get_objects(condition):
    # returns a QuerySet
    return ratings.objects.filter(condition)


def sort_weight():
    # sorting and weighting
    input_next = input('You can sort this data frame, or weight it by percentages to generate your own rating. '
                       'Input s for sorting, w for weighting, p to pass. All lowercase without spaces.')
    if input_next == 's':
        print(glassdoor.sort_by())
    if input_next == 'w':
        print(glassdoor.return_weighted_df())
    if input_next == 'p':
        pass





def inputCompanies(listCompanies):
    list_companies = listCompanies

def getCompanies():
    return list_companies




if __name__ == '__main__':
        # only do write_to_my_sql here when you're starting off fresh new!!
        return_rating()


