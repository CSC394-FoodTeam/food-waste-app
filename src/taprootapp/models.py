from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator

class User(AbstractUser):
    pass

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
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.item_name


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
    category = models.CharField(max_length=20, choices=FRIDGE_TYPES, unique=False)   #throws Integrity error when same category exists in table
    expiry_date = models.DateField()
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.item_name


class Recipe(models.Model):
    DIETARY_RESTRICTIONS = [
        ('None', 'None'),
        ('Vegetarian', 'Vegetarian'),
        ('Vegan', 'Vegan'),
        ('Gluten-free', 'Gluten-free'),
        ('Dairy-free', 'Dairy-free'),
        ('Kosher', 'Kosher'),
        ('Halal', 'Halal'),
    ]
    CUISINE_TYPES = [
        ('None', 'None'),
        ('Italian', 'Italian'),
        ('Mexican', 'Mexican'),
        ('Chinese', 'Chinese'),
        ('Indian', 'Indian'),
        ('French', 'French'),
        ('Greek', 'Greek'),
        ('Japanese', 'Japanese'),
        ('Thai', 'Thai'),
        ('Korean', 'Korean'),
        ('Middle Eastern', 'Middle Eastern'),
        ('Mediterranean', 'Mediterranean'),
        ('Caribbean', 'Caribbean'),
        ('African', 'African'),
        ('American', 'American')
    ]
    FLAVOR_PROFILES = [
        ('None', 'None'),
        ('Sweet', 'Sweet'),
        ('Sour', 'Sour'),
        ('Salty', 'Salty'),
        ('Bitter', 'Bitter'),
        ('Umami', 'Umami'),
        ('Spicy', 'Spicy'),
        ('Herbaceous', 'Herbaceous'),
        ('Nutty', 'Nutty'),
        ('Smoky', 'Smoky')
    ]
    recipe_id = models.AutoField(primary_key=True, default=0)
    name = models.CharField(max_length=100)
    restrictions = models.CharField(max_length=20, choices=DIETARY_RESTRICTIONS, default='None', unique=False)
    cuisine = models.CharField(max_length=20, choices=CUISINE_TYPES, default='None', unique=False)
    flavor_profile = models.CharField(max_length=20, choices=FLAVOR_PROFILES, default='None', unique=False)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipe_images/')

    def __str__(self):
        return self.name