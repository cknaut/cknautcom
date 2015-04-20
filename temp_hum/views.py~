from temp_hum.models import data_point
from django.shortcuts import render
from django.http import HttpResponse

def add_data(request, temp, hum):
    q =  data_point.objects.create(temp=temp, hum=hum)
    q.save
    return HttpResponse('1')


def temp_index(request):
    data_readings = data_point.objects.all()
    last_reading = data_point.objects.latest()
    context = {'data_readings' : data_readings,
                'last_reading' : last_reading}
    return render(request, 'temp_hum/temp_hum_index.html', context) 
