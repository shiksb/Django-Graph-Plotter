from django.shortcuts import render
from django.http import HttpResponse
from .models import Data, Pi
from .reports import ChartData
import simplejson

def plot(request) :
    return render(request, 'plot/plot.html', {})

def stocks(request) :
    return render(request, 'plot/index.html', {})

def chart_data_json(request):
    data = {}
    params = request.GET

    days = params.get('days', 0)
    print(days)

    # data['chart_data'] = ChartData.get_avg_by_day(10)
    # data = ChartData.get_avg_by_day(10)

    dataObjects = Data.objects.all()
    data = []

    for datum in dataObjects:
        data.append([int((datum.date_time.timestamp() - 14400) * 1000),
                     datum.vol])

    return HttpResponse(simplejson.dumps(data),content_type='application/json')