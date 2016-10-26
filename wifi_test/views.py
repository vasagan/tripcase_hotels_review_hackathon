from django.shortcuts import render
from django.conf import settings
import requests
from .serializer import WifiSerializer
from .forms import SubmitWifiRatings

# Create your views here.


def save_wifi_ratings(request):
#    r = requests.get('http://api.embed.ly/1/oembed?key=' + settings.WIFI_KEY)
    r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    json = r.json()
    wifi_details = {'id' : json['id'], 'name' : json['title'], 'body' : json['body']}
    return render(request, 'fetch_response.html', {'wifi_details': wifi_details})
#    serializer = WifiSerializer(data=json)
#    if serializer.is_valid():
#        wifi_details = serializer.save()
#        return render(request, 'fetch_response.html', {'wifi_details': wifi_details })
#    else:
#        return render(request, 'fetch_response.html')


def show_home(request):
    return render(request, 'index.html')