__author__ = 'Vicky'

from urllib.request import Request, urlopen
import urllib
import json
import pandas # as pd?
import main

#dict = {'name':[], 'like':[]}

def return_facebook_likes():

    #df = pandas.DataFrame()
    list_companies = ['walmart', 'cisco', 'pepsi', 'facebook', 'generalmotors',
                      'honda', 'ford', 'visa', 'vmware', 'realmassive']
    #main.getCompanies()


    graph_url = 'http://graph.facebook.com/'
    list_json = []

    with open('D:\\Python\\jobcharted\\jobcharted\\company\\fixtures\\fb.json', 'w') as outfile: # r for reading, w for writing (overwriting!), a for appending
        # you can use open(name, 'a'); this will create the file if the file does not exist, but will not truncate the existing file.
        for company in list_companies:
            # make graph api with company username
            current_page = graph_url + company

            # open public page in facebook api  (the most important part really. should memorize it -- open, read, loads)
            try:
                web_response = urllib.request.urlopen(current_page) # taking our URL string we created and storing the response
            except (RuntimeError, urllib.error.HTTPError):
                print('Error: There is no such company: ', company)
                break
            #readable_page = web_response.read() #  converts our response object into a readable 'html' like document that you can print to console
            readable_page = web_response.readall().decode('utf-8') # work-around for python 3
            json_fbpage = json.loads(readable_page) # taking our readable_page variable and converting it to a JSON object
            # This will allow us to refer to information within that original mess, by key value pairs, kind of like a Python dictionary.
            # json_fbpage is already a dict ob
            # ject at this time. If something goes wrong, check all object types again.
            list_json.append(json_fbpage) # if multiple json objects, you need to put them into a list first, and dump the whole list
            #print(json_fbpage)

        json.dump(list_json, outfile, indent=4)
        outfile.close()

        # read this new json file. from now on all operations are under 'r' mode
        with open(outfile.name, 'r') as infile: # outfile.name is used to solve the problem of 'need string or buffer, file found'
            json_test = json.load(infile)
            infile.seek(0)
            json_new = infile.read()

            # load and query this new json file
            json_new_query = json.loads(json_new)


            global dict
            dict = {'name':[], 'like':[], 'like_score':[]}
            for obj in json_new_query:
                dict['like'].append(obj['likes'])
                dict['name'].append(obj['name'])
            df_like = pandas.DataFrame(dict['like'], index=[dict['name']], columns=['FB_likes'])

            max_like = max(dict['like'])
            for obj in json_new_query :
                dict['like_score'].append(float(obj['likes'])/float(max_like) * 5)
            df_score = pandas.DataFrame(dict['like_score'], index=[dict['name']], columns=['FB_likes_score'])

            df = df_like.join(df_score, how='outer')
            #print(dict['name'])
            # for data parameter, only include the columns you want to include in the df (excluding indexes)!!

            #df1 = fb_df.append(df)
            #df2 = df.sort_index(by=['likes']) # most pandas methods return a new df, so has to assign it to a new df!!

            return df
            #return dict['name']


    outfile.close()

def return_fb_names():
    return dict['name']

if __name__ == '__main__':
    print(return_facebook_likes())
    return_fb_names()