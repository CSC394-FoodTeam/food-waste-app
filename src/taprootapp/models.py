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
        ('Keto', 'Keto'),
        ('Kosher', 'Kosher'),
        ('Halal', 'Halal'),
        ('Paleo', 'Paleo'),
        ('Gluten-free', 'Gluten-free'),
        ('Dairy-free', 'Dairy-free'),
        ('Nut-free', 'Nut-free'),
        ('Shellfish-free', 'Shellfish-free')
    ]
    CUISINE_TYPES = [
        ('None', 'None'),
        ('Italian', 'Italian'),
        ('Mexican', 'Mexican'),
        ('Chinese', 'Chinese'),
        ('Japanese', 'Japanese'),
        ('Indian', 'Indian'),
        ('French', 'French'),
        ('Greek', 'Greek'),
        ('Thai', 'Thai'),
        ('Brazilian', 'Brazilian'),
        ('Korean', 'Korean'),
        ('Middle Eastern', 'Middle Eastern'),
        ('Mediterranean', 'Mediterranean'),
        ('Caribbean', 'Caribbean'),
        ('African', 'African'),
        ('Asian', 'Asian'),
        ('American', 'American'),
        ('Australian', 'Australian'),
        ('European', 'European'),
        ('Pacific Islander', 'Pacific Islander'),
        ('Other', 'Other')
    ]
    FLAVOR_PROFILES = [
        ('None', 'None'),
        ('Sweet', 'Sweet'),
        ('Spicy', 'Spicy'),
        ('Salty', 'Salty'),
        ('Sour', 'Sour'),
        ('Umami', 'Umami'),
        ('Herbaceous', 'Herbaceous'),
        ('Earthy', 'Earthy'),
        ('Nutty', 'Nutty'),
        ('Smoky', 'Smoky'),
        ('Other', 'Other')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # restrictions = models.ManyToManyField(to='RecipeRestriction', choices=DIETARY_RESTRICTIONS, default='None', unique=False)
    # cuisine = models.ManyToManyField(to='RecipeCuisine', choices=CUISINE_TYPES, default='None', unique=False)
    # flavor_profile = models.ManyToManyField(to='RecipeFlavor', choices=FLAVOR_PROFILES, default='None', unique=False)
    restrictions = models.ManyToManyField(to='RecipeRestriction', related_name='recipes', blank=True)
    cuisine = models.ManyToManyField(to='RecipeCuisine', related_name='recipes', blank=True)
    flavor_profile = models.ManyToManyField(to='RecipeFlavor', related_name='recipes', blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    source = models.URLField(blank=True)
    image = models.ImageField(upload_to='recipe_images/', blank=True)

    def __str__(self):
        return self.title
    

class RecipeRestriction(models.Model):
    id = models.CharField(primary_key=True, choices=Recipe.DIETARY_RESTRICTIONS, max_length=50)
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class RecipeCuisine(models.Model):
    id = models.CharField(primary_key=True, choices=Recipe.CUISINE_TYPES, max_length=50)
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class RecipeFlavor(models.Model):
    id = models.CharField(primary_key=True, choices=Recipe.FLAVOR_PROFILES, max_length=50)
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name