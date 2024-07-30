from django.shortcuts import render
from django.contrib import messages
import requests
import datetime


# Create your views here.

def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'pune'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b325cc5930e701ae737b2b7185d157fb'
    PARAMS = {'units':'metric'}


    API_KEY = 'AIzaSyDFtHfwMu2V8bWmtGjPdRi704IXtXroJzo'
    SEARCH_ENGINE_ID = 'b5d77708aa06d4b89'

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']
    
    try :
        data =requests.get(url,params=PARAMS).json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day = datetime.date.today()

        return render(request,'weatherapp/index.html' ,{'description':description,'icon':icon,'temp':temp,'day':day,'city':city, 'exception_occured':False, 'image_url':image_url})
    except:
        exception_occured=True
        messages.error(request, 'enter data is not available to api')
        day=datetime.date.today()

        return render(request,'weatherapp/index.html' ,{'description':'clear sky','icon':'old','temp':25,'day':day,'city':'pune','exception_occured':True})
