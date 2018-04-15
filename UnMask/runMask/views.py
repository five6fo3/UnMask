# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.http import HttpResponse
# Create your views here.

#def index(request):
    ##return HttpResponse("Hello there.")
import csv
import codecs, json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from examples.score_texts_emojis import *
from nn2profile import *
#from twitter_scraper import get_tweets
from twitterscraper import query_tweets

from .forms import NameForm

def get_name(request):
    tweetList = []
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

            for tweet in query_tweets("from:%s"%y_name, 7)[:7]:
                print(tweet.text.encode('utf-8'))
                tweetList.append(unicode(tweet.text).replace("'",""))

            scoreboard(tweetList)
            with open('test_sentences.csv','rb') as f:
                reader = csv.reader(f)
                your_list = list(reader)
            deepmojiTokenizer()
            hateSpeechTokenizer()
            average = wrap()

            #return HttpResponseRedirect('/thanks/')
            return render(request, 'name.html', {'form': average})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

#def return_name(request):
