from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient



# Create your views here.


def index(request):
    # return HtttpResponse('Welcome to NUA News')
    newsapi = NewsApiClient(api_key='7bfb27f9a56e4ad7adcda1eb46820a6e')
    # /v2/top-headlines
    top_headlines = newsapi.get_top_headlines(sources='techcrunch')
    l = top_headlines['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
    return render(request, 'index.html', context={'mylist': mylist})
