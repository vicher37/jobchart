#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
#sys.setdefaultencoding("utf-8")
__author__ = 'Vicky Zhang'

from bs4 import BeautifulSoup
import requests
from django.utils.encoding import smart_str
from urllib import request


# get all reviews of a company
def get_review(url, count, company):
    print(url)
    #r = requests.get(url)
    r = request.urlopen(url)
    data = r.read()

#    for lines in open(data,'rb'):
#        decodedLine = lines.decode('UTF-8')
# commented out because it is unnecessary to print out 20+ htmls for each company, it would be two cluttered.
# can always uncomment it for debugging purposes.
#    with open('D:\\Python\\chart\\code_test\\'+ company + '_' + str(count) + '.html', 'w') as outfile:
#        #data_decoded = smart_str(data)
#        data_decoded = data.decode('utf-8')
#        data_encoded = data_decoded.encode("utf-8")
#        str_encoded = str(data_encoded)
#        outfile.write(str_encoded)
    #print(data)

    soup = BeautifulSoup(data)

    description_tag_list = soup.find_all("div", "description")

    # if the length of description list is only 1, that means all valid reviews have been extracted.
    # The only one left is
    #print(type(description_tag_list))
    print(len(description_tag_list))
    print(description_tag_list[1])
    if len(description_tag_list) < 20:
        print('All reviews have been extracted')
        sys.exit(0)
    else:
        skip_status = False
        for tag in description_tag_list:
            # skip the same first review on every page after the first , if it hasn't been skipped yet
            # This reflects another common problem:
            if count > 0 and skip_status == False:
                skip_status = True
                continue

            text = str(tag)

            # A common problem: does this function return a new object or modify the original one?
            text_new = text.replace(r'<br>', ' ')
            text_new_1 = text_new.replace(r'</br>', '')
            text_trim = text_new_1[25:-6]
            # for all possible text that could render encoding problems, include the following two lines.
            #text_trim_decoded = text_trim.decode('utf-8')
            text_trim_encoded = text_trim.encode("utf-8")
            text_encoded = (str(text_trim_encoded))[2:-1]

            # print(text_new_1[25:-6])

            # If the txt file doesn't exist yet, do the following.
            # If it does, either delete its contents or write into a new file
            with open('D:\\Python\\chart\\code_test\\' + company +'_review.txt', 'a') as outfile:

                  outfile.write(text_encoded)
                  outfile.write('\n')


def main():

    # ask for company name and generate urls for the first page and the pages after
    company = input("Enter a company you want to extract reviews about: ").capitalize()

    url_1 = 'http://www.indeed.com/cmp/' + company + '/reviews'
    url_2 = 'http://www.indeed.com/cmp/' + company + '/reviews' + '?fcountry=US&start='

    count = 0

    while count >= 0 :
        if count == 0:
            # initiate the txt file, or overwrites it with emptiness
            open('D:\\Python\\chart\\code_test\\' + company +'_review.txt', 'w').close()
            url = url_1
            get_review(url, count, company)
            print(url + ' has been extracted')
            count += 1
        elif count >= 20:
            print('The first 20 pages have been extracted')
            break
        else:
            print(count)
            url = url_2 + str(20 * count)
            #print(url)
            get_review(url, count, company)
            print(url + ' has been extracted, count = ' + str(count))
            count += 1


def clean_txt(company):
        open('D:\\Python\\chart\\code_test\\' + company +'_review.txt', 'w').close()


if __name__ == '__main__':
    main()
# www.glassdoor.com
# http://www.indeed.com/cmp/Indeed/reviews
# http://www.indeed.com/cmp/Indeed/reviews?fcountry=US&start=20