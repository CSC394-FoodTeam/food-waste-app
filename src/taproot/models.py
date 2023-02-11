from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings

class User(AbstractUser):
    
    email = models.EmailField(primary_key=True, max_length=254, verbose_name='email address', default='welcome@example.com', unique=True)
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class PantryItem(models.Model):
    PANTRY_TYPES=[
        ('1','Grains'),
        ('2','Canned Foods'),
        ('3','Baking Supplies'),
        ('4','Spices'),
        ('5','Snacks'),
        ('6','Sauces'),
        ('7','Oil and Vinegars'),
        ('8','Sweeteners')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20,choices=PANTRY_TYPES, unique=True)
    expiry_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.item_name


class FridgeItem(models.Model):
    FRIDGE_TYPES= [
        ('1','Fruits'),
        ('2','Vegetables'),
        ('3','Grains'),
        ('4','Dairy'),
        ('5','Meat'),
        ('6','Seafood'),
        ('7','Dessert'),
        ('8','Snacks'),
        ('9','Beverages')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20,choices=FRIDGE_TYPES, unique=True)
    expiry_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.item_name
    
    ###
    def get_absolute_url(self):
        return "list"
    ###


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='recipe_images/')

    def __str__(self):
        return self.name

class Test(models.Model):
    name = models.CharField(max_length=20)