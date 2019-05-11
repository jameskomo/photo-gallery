from . import views
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.images, name='gallery-home'),
    path('about/', views.about, name='gallery-about'),
    path('images/', views.images, name='gallery-images'),
    url(r'^search/', views.search_results, name='search_results'),
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)