from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from . import tweet

# Create your views here.


def index(request):
    template = "sentiment_app/Details.html"
    context = {}
    return render(request, template, context)


def show(request, terms, keyword):
    polarity, error, positive, wpositive, spositive, negative, wnegative, snegative, neutral = tweet.tweet(keyword, terms)
    template = "sentiment_app/sentiment_show.html"
    context = {"polarity": polarity, "keyword": keyword, "terms": terms, "error": error, 'positive': positive,
            'wpositive': wpositive, 'spositive': spositive, 'negative': negative, 'wnegative': wnegative,
                'snegative': snegative, 'neutral': neutral}
    return render(request, template, context)


def show1(request):
    template = "sentiment_app/pie.html"
    return render(request, template)
