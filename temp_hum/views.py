from temp_hum.models import data_point
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.dateformat import DateFormat

def add_data(request, temp, hum):
    q =  data_point.objects.create(temp=temp, hum=hum)
    q.save
    return HttpResponse('1')


def temp_index(request):
    data_readings = data_point.objects.all()
    latest_reading = data_point.objects.latest()
    context = {'data_readings' : data_readings,
                'last_reading' : latest_reading}
    return render(request, 'temp_hum/temp_hum_index.html', context) 

#returns latest reading for ajax request, following http://www.tangowithdjango.com/book/chapters/ajax.html
def ajax_temp_index(request):
    latest_reading = data_point.objects.latest()
    formatted_date = DateFormat(latest_reading.created).format('N j, Y, H:i:s')
    jsonresponse = JsonResponse({'temp': latest_reading.temp, 'hum': latest_reading.hum, 'timestamp': formatted_date})
    return HttpResponse(jsonresponse) 
