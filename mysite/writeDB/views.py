from django.shortcuts import render
from .models import ngo


def index(request):
    objects = ngo.objects.order_by('address')[:100]
    context = {'address': objects}
    #return render(request, 'writeDB/index.html', context)
    return render(request, 'writeDB/markers.html')

