from django.db import models
from django.contrib.auth.models import Group

class User(models.Model):
    groups = models.ManyToManyField(Group, related_name='taproot_user_profiles')
    nickname = models.CharField(max_length=30)
    email = models.EmailField(unique=True, primary_key=True)

class PantryItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pantry_items')
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    expiry_date = models.DateField()
    quantity = models.IntegerField()

class FridgeItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fridge_items')
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    expiry_date = models.DateField()
    quantity = models.IntegerField()

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='recipe_images/')