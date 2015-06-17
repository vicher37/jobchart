from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from comp.models import ratings, review_summary
import comp.review_summary
from django.template import RequestContext, loader
import os
import django
from .forms import NameForm
# this file connects data model with html

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chart.settings")

def index(request):
    rating_list = ratings.objects.order_by('id')
    context = {'rating_list' : rating_list}
    return render(request, 'comp/index.html', context)

def rating_page(request, company_id):
    try:
        # chose to call id as company_id because id is unique to the company, not necessarily to the rating
        # however, the return object is called rating because it includes all the detailed ratings of the company
        rating = ratings.objects.get(pk = company_id)
    except ratings.DoesNotExist:
        raise Http404("Company does not exist")
    return render(request, 'comp/rating_page.html', {'rating' : rating})

def review_summaries(request, company_id):
    # common_nouns = comp.review_summary.common_nouns(company)
    # common_adjs = comp.review_summary.common_adjs(company)
    # common_tags = comp.review_summary.common_tags(company)
    # print(common_adjs)
    # filter for more than one result
    django.setup()
    words = review_summary.objects.filter(company_id = company_id)
    # words_list = []
    # for word in words:
    #     word_split = word.__str__().split(',')
    #     words_list.append(word_split)
    #word_list = []
    #for word in words:
        # print(word)
    #    word_list.append(word)
    #word_list_str = str(word_list)
    #print(word_list_str)
    #print(type(word_list))

    # comment for review_summary.html : use attribute to retrieve attributes, not string method! The reason why we use
    # models is that we can retrieve attributes easily!!
    return render(request, 'comp/review_summary.html', {'common_words' : words})
# The review summary for this company is not available.

def company(request, company_id):
    rating = ratings.objects.get(id=company_id)
    return render(request, 'comp/company.html', {'rating': rating})

def about(request):
    return render(request, 'comp/about.html')

def methodology(request):
    return render(request, 'comp/methodology.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data
            #name = str(name)

            # One difficulty of Django debugging is you can only see the end result. So sometimes have to
            # tweak the webpage output so that you can see interim outputs to, in order to debug.
            # Here, name actually is {'company_name' : 'Cisco'}, so if you directly put that into a string, of course
            # you can't find the object in ratings table!
            # Also, tell table structure from dict! They use different syntax to retrieve values! Dict uses name['foo']
            # whereas table uses name.foo!
            name_str = name['company_name']

            # Do some processing for the special cases (aka abbreviations)
            if name_str == 'GM':
                name_str = 'General Motors'

            # has to put it into string to pass to the page!
            # name_1 = str(name)
            obj_list = ratings.objects.filter(company__icontains=name_str)

            # redirect to a new URL:
            return render(request, 'comp/search_result.html', {'obj_list' : obj_list})

    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = NameForm()
    #     return render(request, 'search_result.html', {'form': form})

if __name__ == '__main__':
    review_summaries('Walmart')
