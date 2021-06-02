from django.shortcuts import render
import requests


# Create your views here.
def news(request):
    url='http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=aa43349577ad4cf58c8fbdea021174c1'
    r= requests.get(url)
    data=r.json()
    return render(request,'myapp/index.html',data) 