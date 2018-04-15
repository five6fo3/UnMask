### nn2profile.py description
### This function will receive data from the deepmoji and hate speech id neural nets
### Deepmoji will provide:
### emoji ids (0-63) corresponding mapping in emoji_overview

from __future__ import division
import csv
import numpy

hateValsRaw = []
hateValsTrimmed = []
deepAnalysisRaw = []
deepAnalysisTrimmed = []
sentimentTracker = []

def deepmojiTokenizer():
    with open("runMask/examples/test_sentences.csv") as csvfile:
        reader2 = csv.reader(csvfile) # change contents to floats
        for row in reader2: # each row is a list
            deepAnalysisRaw.append(row)

    for i in range(len(deepAnalysisRaw)-1):

        segment = []

        segment.append(deepAnalysisRaw[i+1][2])
        segment.append(deepAnalysisRaw[i+1][3])
        segment.append(deepAnalysisRaw[i+1][4])
        segment.append(deepAnalysisRaw[i+1][5])
        segment.append(deepAnalysisRaw[i+1][6])

        deepAnalysisTrimmed.append(segment)

    print (deepAnalysisTrimmed)

    for i in range(len(deepAnalysisTrimmed)):
        if '1' in deepAnalysisTrimmed[i]:
            sentimentTracker.append("Sarcasm")
        else:
            sentimentTracker.append("None")
    print (sentimentTracker)




def hateSpeechTokenizer():
    with open("runMask/HS_Input.csv") as csvfile:
        reader = csv.reader(csvfile) # change contents to floats
        for row in reader: # each row is a list
            hateValsRaw.append(row)

    ##print (hateValsRaw)

    for i in range(len(hateValsRaw)):
        hateValsTrimmed.append(hateValsRaw[i][1])

    print (hateValsTrimmed)

def wrap():
    strikes = 0;
    totalTweets = len(hateValsTrimmed)
    for i in range(len(deepAnalysisTrimmed)):
        if ((hateValsTrimmed[i] == 'racism' or hateValsTrimmed[i] == 'sexism') and sentimentTracker[i] == 'None'):
            strikes = strikes + 1
    avg = strikes / totalTweets
    print (avg)
    return avg
    ##for i in sentimentVals to end_main_loop
        ##TODO: combine elements of sentimentVals with their respective elements
        ##in hateVals in the 2d array wrapper.

    ##iterate through new array and output a raw percentage of indices with
    ##non-sarcastic racist or sexist content compared to entire dataset.


#deepmojiTokenizer()

#hateSpeechTokenizer()

#wrap()

##TODO: testing to determine how to treat raw evaluation

##TODO: figure out how to return final profile coefficient to front end
