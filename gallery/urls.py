from . import views
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.home, name='gallery-home'),
    path('about/', views.about, name='gallery-about'),
    path('images/', views.images, name='gallery-images'),
    path('imagedetails/', views.imagedetails, name='gallery-imagedetails'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)