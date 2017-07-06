from django.db import models

# Create your models here.

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=50)
    restaurant_location = models.TextField()
    restaurant_image = models.ImageField(upload_to='', blank=True)