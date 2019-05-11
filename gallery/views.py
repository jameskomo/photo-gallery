from django.shortcuts import render, redirect
from django.http import Http404
import datetime as dt
from .models import Image, Location, Category, tags

# Create your views here.
def home(request):
    return render (request, 'gallery/base.html')

def about(request):
    return render (request, 'gallery/about.html')

def images(request):
    context = {
        'images':Image.objects.all()
    }
    return render (request, 'gallery/images.html', context)

def imagedetails(request):
    return render (request, 'gallery/imagedetails.html')
