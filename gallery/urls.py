from . import views
from django.urls import path

urlpatterns=[
    path('', views.home, name='gallery-home'),
    path('about/', views.about, name='gallery-about'),
]