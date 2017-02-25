from django.shortcuts import render, render_to_response
from chartit import DataPool, Chart
from .models import MonthlyWeatherByCity
import json, urllib
from django.http import JsonResponse, HttpResponse


# Create your views here.
def weather_chart_view(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': MonthlyWeatherByCity.objects.all()},
              'terms': [
                'month',
                'houston_temp',
                'boston_temp']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'boston_temp',
                    'houston_temp']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Weather Data of Boston and Houston'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response('plot/plot.html',{'weatherchart': cht})

def plot(request) :
    url = 'https://www.highcharts.com/samples/data/jsonp.php?filename=aapl-c.json&callback=?'
    # response = JsonResponse({1: 5})
    # response = urllib.urlopen(url)
    # data = json.loads(response.read())
    # js = response.content
    # 'https://www.highcharts.com/samples/data/jsonp.php?filename=aapl-c.json&callback=?'
    jstring = '{"chart_data": {"dates": [1396310400, 1396396800, 1396483200, 1396569600], "values": [2, 3, 2, 4]}}'
    js = json.loads(jstring)
    return render(request, 'plot/index.html', {'js':js})
    # return HttpResponse(json.dumps(json.loads(jstring)))

def disp(request) :
    if request.method == "GET":
        print("got")

        data = {
            "chart_data": {
                "dates": [1396310400, 1396396800, 1396483200, 1396569600],
                "values": [2, 3, 2, 4]
            }
        }
        data = [
        [1267401600000, 29.86],
        [1267488000000, 29.84],
        [1267574400000, 29.90],
        [1267660800000, 30.10]
        ]

    return JsonResponse(data)
