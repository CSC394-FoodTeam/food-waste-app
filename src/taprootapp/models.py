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
    item_name = models.CharField(max_length=100) #added primary key == True
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
    item_name = models.CharField(max_length=100) #added primary key == True
    category = models.CharField(max_length=20, choices=FRIDGE_TYPES, unique=False)   #throws Integrity error when same category exists in table
    expiry_date = models.DateField()
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.item_name


class Recipe(models.Model):
    DIETARY_RESTRICTIONS = [
        ('none', 'None'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('keto', 'Keto'),
        ('kosher', 'Kosher'),
        ('halal', 'Halal'),
        ('paleo', 'Paleo'),
        ('gluten-free', 'Gluten-free'),
        ('dairy-free', 'Dairy-free'),
        ('nut-free', 'Nut-free'),
        ('shellfish-free', 'Shellfish-free')
    ]
    CUISINE_TYPES = [
        ('none', 'None'),
        ('italian', 'Italian'),
        ('mexican', 'Mexican'),
        ('chinese', 'Chinese'),
        ('japanese', 'Japanese'),
        ('indian', 'Indian'),
        ('french', 'French'),
        ('greek', 'Greek'),
        ('thai', 'Thai'),
        ('brazilian', 'Brazilian'),
        ('korean', 'Korean'),
        ('middle Eastern', 'Middle Eastern'),
        ('mediterranean', 'Mediterranean'),
        ('caribbean', 'Caribbean'),
        ('african', 'African'),
        ('asian', 'Asian'),
        ('american', 'American'),
        ('australian', 'Australian'),
        ('european', 'European'),
        ('pacific Islander', 'Pacific Islander'),
        ('other', 'Other')
    ]
    FLAVOR_PROFILES = [
        ('none', 'None'),
        ('sweet', 'Sweet'),
        ('spicy', 'Spicy'),
        ('salty', 'Salty'),
        ('sour', 'Sour'),
        ('umami', 'Umami'),
        ('herbaceous', 'Herbaceous'),
        ('earthy', 'Earthy'),
        ('nutty', 'Nutty'),
        ('smoky', 'Smoky'),
        ('other', 'Other')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    restrictions = models.ManyToManyField(to='RecipeRestriction', choices=DIETARY_RESTRICTIONS, default='none', unique=False)
    cuisine = models.ManyToManyField(to='RecipeCuisine', choices=CUISINE_TYPES, default='none', unique=False)
    flavor_profile = models.ManyToManyField(to='RecipeFlavor', choices=FLAVOR_PROFILES, default='none', unique=False)
    ingredients = models.TextField()
    instructions = models.TextField()
    source = models.URLField(blank=True)
    image = models.ImageField(upload_to='recipe_images/', blank=True)

    def __str__(self):
        return self.title
    

class RecipeRestriction(models.Model):
    id = models.CharField(primary_key=True, max_length=50, choices=[(r[0], r[1]) for r in Recipe.DIETARY_RESTRICTIONS])

    def __str__(self):
        return self.id


class RecipeCuisine(models.Model):
    id = models.CharField(primary_key=True, max_length=50, choices=[(r[0], r[1]) for r in Recipe.CUISINE_TYPES])

    def __str__(self):
        return self.id


class RecipeFlavor(models.Model):
    id = models.CharField(primary_key=True, max_length=50, choices=[(r[0], r[1]) for r in Recipe.FLAVOR_PROFILES])

    def __str__(self):
        return self.id