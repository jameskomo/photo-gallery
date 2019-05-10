from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render (request, 'gallery/base.html')

def about(request):
    return render (request, 'gallery/about.html')