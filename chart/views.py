from django.shortcuts import render
from .models import Chart

# Create your views here.


def home(request):
    data = Chart.objects.all()
    context = {
        'data': data
    }
    return render(request, 'chart/home.html', context)
