__author__ = 'Vicky'

from urllib.request import Request, urlopen
import json

from pandas import *

import facebook
import main

import random

def add_glassdoor_rating():
    list_companies = main.getCompanies()
    list_json = []
    #print(list_companies)

    with open('D:\\Python\\jobcharted\\jobcharted\\company\\fixtures\\glassdoor.json', 'w') as outfile: # r for reading, w for writing (overwriting!), a for appending
        # you can use open(name, 'a'); this will create the file if the file does not exist, but will not truncate the existing file.
        for company in list_companies:
            # open public page in facebook api  (the most important part really. should memorize it -- open, read, loads)
            #try:
            #web_response = urllib.request.urlopen(current_page) # taking our URL string we created and storing the response
            req = Request('http://api.glassdoor.com/api/api.htm?t.p=30341&t.k=huBJAV6WueU&'
                                         'userip=70.115.159.41&useragent=chrome&format=json&v=1&action=employers'
                                         '&q=' + company + '&state=texas&city=austin',
                                         headers={'User-Agent': 'chrome'})
            web_response = urlopen(req)
            #print(type(web_response))
            #except (RuntimeError, urllib.error.HTTPError) as e:
             #   print('Error: There is no such company: ', company)
              #  print(e.errno)
               # continue
            #readable_page = web_response.read() #  converts our response object into a readable 'html' like document that you can print to console
            readable_page = web_response.read() # work-around for python 3
            #print(readable_page)
            json_fbpage = json.loads(readable_page.decode('utf-8')) # taking our readable_page variable and converting it to a JSON object
            # This will allow us to refer to information within that original mess, by key value pairs, kind of like a Python dictionary.
            # json_fbpage is already a dict ob
            # ject at this time. If something goes wrong, check all object types again.
            #print(json_fbpage)
            #print(type(json_fbpage))
            list_json.append(json_fbpage) # if multiple json objects, you need to put them into a list first, and dump the whole list
            #print(json_fbpage)

        #print(list_json)
        #print(type(list_json))

        text = json.dumps(list_json, outfile) # why it cannot do indent = 4?
        outfile.write(text)
        outfile.close()

        # read this new json file. from now on all operations are under 'r' mode
        with open(outfile.name, 'r') as infile: # outfile.name is used to solve the problem of 'need string or buffer, file found'
            json_test = json.load(infile)
            infile.seek(0)
            json_new = infile.read()

            # load and query this new json file. The point of this phase is to observe data structure (each API generates
            # different structure) and adjust the code accordingly (according to whether it's list/dict!)
            json_new_query = json.loads(json_new)

            global dict
            dict = {'name':[], 'overall_rating':[], 'senior_leadership_rating':[], 'work_life_balance_rating':[],
                    'recommend_to_friend_rating':[], 'culture_and_values_rating':[]}

            for obj in json_new_query:
                comp = obj['response']['employers'][0]
                #print(comp)
                dict['name'].append(comp['name'])
                dict['overall_rating'].append(comp['overallRating'])
                #print(comp['overallRating'])
                dict['senior_leadership_rating'].append(comp['seniorLeadershipRating'])

                dict['work_life_balance_rating'].append(comp['workLifeBalanceRating'])
                dict['recommend_to_friend_rating'].append(comp['recommendToFriendRating'])
                dict['culture_and_values_rating'].append(comp['cultureAndValuesRating'])

            #print(dict)
            global df
            df = facebook.return_facebook_likes()
            column_names = ['overall_rating', 'senior_leadership_rating', 'work_life_balance_rating',
                    'recommend_to_friend_rating', 'culture_and_values_rating']
            for name in column_names:
                df1 = DataFrame(data=dict.get(name),
                                       index=[get_min_names()],
                                       columns=[name])
                df = df.join(df1, how='outer')

            return df



def sort_by():
        df = add_glassdoor_rating('df')
        sort_by = input('Please choose which parameter you want to sort by from this list, '
                    'and type its full name as shown, without spaces: ' +
                    str(df.columns.values))
        df_sort = df.sort_index(by=sort_by, ascending=False) # most pandas methods return a new df, so has to assign it to a new df!!
        return df_sort

def weight_input ():
    weight_input = input('Please input the weight of each element, in the form of score (out of 100) '
                       '(e.g. 20), in the following sequence: ' +
                        str(df.columns.values) +
                       ' Also, please use space as the separator.'
                       ' Like this: 10 20 30 20 10 10'
                       '. They don\'t have to sum up to 100% since '
                       'we will do the conversion. Just indicate your relative preference for each element.'
                       'For testing, press enter to go with randomly generated parameters.')
    if weight_input == '':
        weight_input = []
        for i in range(len(df.columns.values)-1):
            num = random.randrange(0, 100, 10)
            weight_input.append(num)
        # return marks the end of this function!!

    #try:
        weight_int_list = []
        for weight in weight_input:
            weight_int = int(weight)
            weight_int_list.append(weight_int)

        weightNum_list = []
        for weight in weight_int_list:
            weightNum = int(weight)/sum(weight_int_list)
            weightNum_list.append(weightNum)
            print(weightNum)

    print('weight int list',weight_int_list)
    print('weight num list', weightNum_list)
    return weightNum_list

def return_weighted_df():
    # convert user input into percentages

    df_small = df.ix[:, 1:]
    weight_num_list = weight_input()
    print(weight_num_list)
    sum_list = []
    j = 0
    sum = 0
    for index in df_small.index.values:
        for column in df_small.columns.values:
            product = float(df_small.get_value(index, column)) * weight_num_list[j]
            sum += product
            j += 1
            if j == len(df_small.columns.values): # You check this condition after incrementing the counter, so do not need to substract 1!
                sum_list.append(sum)
                j = 0
                sum = 0 # update both counters/status indicators!
    df_sum = DataFrame(data=sum_list, index=df.index.values, columns=['YourRating'])
    df_weighted = df.join(df_sum, how='outer')
    print(df_weighted)
    return df_weighted


def return_gd_names():
    return dict['name']

def get_min_names():
    # import the lists and make sure they are of equal length
    fb_list = facebook.return_fb_names()
    gd_list = return_gd_names()
    assert len(fb_list) == len(gd_list)

    # go through both lists, compare each element, choose the shorter one
    global min_list
    min_list =[]
    for i in range(len(fb_list)):
        if len(fb_list[i]) > len(gd_list[i]):
            min_list.append(gd_list[i])
        else :
            min_list.append(fb_list[i])
    return min_list


if __name__ == '__main__':
    print(add_glassdoor_rating())
