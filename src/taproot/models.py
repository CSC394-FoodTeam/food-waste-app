from django.db import models
from django.contrib.auth.models import Group

class User(models.Model):
    groups = models.ManyToManyField(Group, related_name='taproot_user_profiles')
    nickname = models.CharField(max_length=30)
    email = models.EmailField(unique=True, primary_key=True)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pantry_items')
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20,choices=PANTRY_TYPES, unique=True)
    expiry_date = models.DateField()
    quantity = models.IntegerField()


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fridge_items')
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20,choices=FRIDGE_TYPES, unique=True)
    expiry_date = models.DateField()
    quantity = models.IntegerField()


class Recipes(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='recipe_images/')