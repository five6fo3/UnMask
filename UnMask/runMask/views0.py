# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.http import HttpResponse
# Create your views here.

#def index(request):
    ##return HttpResponse("Hello there.")
from django.shortcuts import render
from django.http import HttpResponseRedirect
from deepmoji.finetuning import *

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            y_name = form.cleaned_data['your_name']

            #return HttpResponseRedirect('/thanks/')
            return render(request, 'name.html', {'form': y_name})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

#def return_name(request):
