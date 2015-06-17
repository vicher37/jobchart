__author__ = 'Vicky Zhang'

from django.conf.urls import patterns, url
from comp import views
from django.views.generic.base import RedirectView

# This file connects url with view, which connects data model with html
urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<company_id>\d+)/ratings/$', views.rating_page, name='rating_page'),
                       url(r'^(?P<company_id>\d+)/review_summary/$', views.review_summaries, name='review_summary'),
                       url(r'^(?P<company_id>\d+)/company/$', views.company, name='company'),
                       url(r'^search_result/$', views.get_name, name='search_result'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^methodology/$', views.methodology, name='methodology'),)
