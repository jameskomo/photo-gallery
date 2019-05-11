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

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_name(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html',{"message":message})
