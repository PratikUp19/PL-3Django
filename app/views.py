from django.shortcuts import render
import requests
import json
# Create your views here.
def home(request):
    api_request = requests.get("http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=d33f23a0acd54247b78e718931c48038")
    print (api_request)
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api' : api})
