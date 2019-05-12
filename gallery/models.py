from django.db import models
import datetime as dt 

# Create your models here.
class Image(models.Model):    
    image_name=models.CharField(max_length=60)
    image_description = models.TextField()
    image_location = models.CharField(default="", max_length = 30) 
    image_category = models.CharField(default="", choices=[('Music', 'Music'), ('Travel', 'Travel'), ('Food', 'Food')], max_length = 30)
    pub_date = models.DateTimeField(auto_now_add=True)
    photo_image = models.ImageField(default="", upload_to = 'images/')

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()
    def save_image(self):
        self.save()
    class Meta:
        ordering = ['image_name']    

    @classmethod
    def search_by_image_category(cls,search_term):
        images = cls.objects.filter(image_category__icontains=search_term)
        return images
    @classmethod
    def todays_images(cls,date):
        images = cls.objects.filter(pub_date__date = date)
        return images

    

class Category(models.Model):
    image_category =  models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_category

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Location(models.Model):
    image_location = models.ForeignKey(Image, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)

    def __str__(self):
        return self.image_location

