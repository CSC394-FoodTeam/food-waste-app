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
        ('Grains','Grains'),
        ('Canned Foods','Canned Foods'),
        ('Baking Supplies','Baking Supplies'),
        ('Spices','Spices'),
        ('Snacks','Snacks'),
        ('Sauces','Sauces'),
        ('Oil and Vinegars','Oil and Vinegars'),
        ('Sweeteners','Sweeteners')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item_name = models.CharField(primary_key=True, max_length=100) #added primary key == True
    category = models.CharField(max_length=20,choices=PANTRY_TYPES, unique=False)
    expiry_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.item_name

    ###
    #def get_absolute_url(self):
        #return "list"
    ###

class FridgeItem(models.Model):
    FRIDGE_TYPES= [
        ('Fruits','Fruits'),
        ('Vegetables','Vegetables'),
        ('Grains','Grains'),
        ('Dairy','Dairy'),
        ('Meat','Meat'),
        ('Seafood','Seafood'),
        ('Dessert','Dessert'),
        ('Snacks','Snacks'),
        ('Beverages','Beverages')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item_name = models.CharField(primary_key=True, max_length=100) #added primary key == True
    category = models.CharField(max_length=20,choices=FRIDGE_TYPES,unique=False)   #throws Integrity error when same category exists in table
    expiry_date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.item_name
    
    ###
    #def get_absolute_url(self):
        #return "list"
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