from django.test import TestCase
from .models import Image, Category,Location,tags

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.food= Image(image_name = 'Nduma', image_description ='African Tastes', image_location ='Banglore', image_category ='Food', pub_date ='May 10, 2019, 5:28 p.m.', photo_image='media/images/food.jpg')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food,Image))
    # Testing Save Method
    def test_save_method(self):
        self.food.image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)