from django.http import HttpResponse
from django.shortcuts import render
import operator

def count(request):
    wordcount = request.GET['wordcount']
    wordlist = wordcount.split()

    #Counting word frequency
    freqword = {}
    for word in wordlist:
        if word in freqword:
            freqword[word] += 1
        else:
            freqword[word] = 1

    # converting dic into list so we can sort
    freqlist = freqword.items()

    # SORTING THE CONVERTED list from dic

    sortedfreq = sorted(freqlist, key=operator.itemgetter(0),reverse=False)
    


    return render(request, 'count.html',{'wordcount':wordcount,'wordlist':len(wordlist),'freqword':freqword,'sortedfreq':sortedfreq }) 
    # passing arg dictionary
    
def home(request):
    return render(request, 'home.html')