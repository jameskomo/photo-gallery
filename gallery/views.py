from django.shortcuts import render, redirect
from .models import Image, Location, Category, tags

# Create your views here.
def home(request):
    return render (request, 'gallery/base.html')

def about(request):
    return render (request, 'gallery/about.html')