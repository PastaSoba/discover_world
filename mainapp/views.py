from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import TouristSpot

# Create your views here.
def index(request):
    touristSpots = TouristSpot.objects.all().order_by('-created_datetime')
    return render(request, 'mainapp/index.html', {'touristSpots':touristSpots})

def exploreplan(request):
    touristSpots = TouristSpot.objects.all().order_by('-created_datetime')
    return render(request, 'mainapp/exploreplan.html', {'touristSpots':touristSpots})

def aboutus(request):
    return render(request, 'mainapp/aboutus.html')