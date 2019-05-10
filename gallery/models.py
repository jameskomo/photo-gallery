from django.db import models

# Create your models here.
class Image(models.Model):
    image_name=models.CharField(max_length=60)
    image_description = models.TextField()
    image_location = models.CharField(default="", max_length = 30) 
    image_category = models.CharField(default="", max_length = 30) 

class Category(models.Model):
    image_category =  models.ForeignKey(Image, on_delete=models.CASCADE)

class Location(models.Model):
    image_location = models.ForeignKey(Image, on_delete=models.CASCADE)
