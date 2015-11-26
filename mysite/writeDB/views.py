from django.shortcuts import render
from .models import ngo


def index(request):
    address = ngo.objects.order_by('address')[:100]
    context = {'address': address}
    return render(request, 'writeDB/index.html', context)

