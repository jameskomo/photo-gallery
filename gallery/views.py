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
def categories(request):
    context = {
        'categories':Category.objects.all()
    }
    return render (request, 'gallery/images.html', context)

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_image_category(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html',{"message":message})

def images_by_location(request,image_location):
    try:
        image = Image.objects.get(location = image_location)
    except DoesNotExist:
        raise Http404()
    return render(request,"gallery/images_by_location.html", {"image":image})


