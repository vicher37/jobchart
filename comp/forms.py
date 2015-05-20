__author__ = 'Vicky Zhang'
from django import forms

class NameForm(forms.Form):
    company_name = forms.CharField(label='Company name', max_length=100)