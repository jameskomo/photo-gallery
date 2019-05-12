from django.test import TestCase
import datetime as dt
from .models import Image, Category,Location,tags

class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.food= Image(image_name = 'Nduma', image_description ='African Tastes', image_location ='Banglore', image_category ='Food', pub_date ='May 10, 2019, 5:28 p.m.', photo_image='media/images/food.jpg')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food,Image))
     # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

    def test_todays_images_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        images_by_date = Image.todays_images(date)
        self.assertTrue(len(images_by_date) == 0)
    

    def setUp(self):
        self.food= Image(image_name = 'Nduma', image_description ='African Tastes', image_location ='Banglore', image_category ='Food', pub_date ='May 10, 2019, 5:28 p.m.', photo_image='media/images/food.jpg')
        self.food.save_image()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

      

    def tearDown(self):
        Image.objects.all().delete()
        tags.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
    
   