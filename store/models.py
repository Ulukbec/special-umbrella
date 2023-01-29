from django.db import models


# Create your models here.

class Product(models.Model):
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=100)
    descriptions = models.TextField(blank=True)
    create_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now_add=True)

