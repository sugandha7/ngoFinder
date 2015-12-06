from django.shortcuts import render
from .models import ngo
from django.db.models import Avg
import simplejson


def index(request):
    objects = ngo.objects.order_by('id')[:100]
    location = []
    for entry in objects:
    	loc = []
    	loc.append(entry.name)
    	loc.append(entry.latitude)
    	loc.append(entry.longitude)
    	loc.append(entry.id)
    	location.append(loc)
    avg_lat = objects.aggregate(Avg('latitude'))
    avg_lng = objects.aggregate(Avg('longitude'))
    json_loc = simplejson.dumps(location)
    context = {'location': json_loc, 'avg_lat': avg_lat['latitude__avg'], 'avg_lng': avg_lng['longitude__avg']}
    return render(request, 'writeDB/markers.html', context)

