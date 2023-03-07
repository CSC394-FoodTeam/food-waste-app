from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MinValueValidator, RegexValidator
from django.contrib.postgres.fields import ArrayField

class User(AbstractUser):
    pass

class PantryItem(models.Model):
    PANTRY_TYPES=[
        ('grains','Grains'),
        ('canned foods','Canned Foods'),
        ('baking supplies','Baking Supplies'),
        ('spices','Spices'),
        ('snacks','Snacks'),
        ('sauces','Sauces'),
        ('oil and vinegars','Oil and Vinegars'),
        ('sweeteners','Sweeteners'),
        ('other', 'Other')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100, validators=[RegexValidator(r'^[a-zA-Z ]*$')]) 
    category = models.CharField(max_length=20,choices=PANTRY_TYPES, unique=False)
    expiry_date = models.DateField()
    quantity = models.IntegerField(validators=[MinValueValidator(1)], default=1)

    def __str__(self):
        return self.item_name.capitalize()


class FridgeItem(models.Model):
    FRIDGE_TYPES= [
        ('fruits','Fruits'),
        ('vegetables','Vegetables'),
        ('grains','Grains'),
        ('dairy','Dairy'),
        ('meat','Meat'),
        ('seafood','Seafood'),
        ('dessert','Dessert'),
        ('snacks','Snacks'),
        ('beverages','Beverages'),
        ('other', 'Other')
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100, validators=[RegexValidator(r'^[a-zA-Z ]*$')])
    category = models.CharField(max_length=20, choices=FRIDGE_TYPES, unique=False)   #throws Integrity error when same category exists in table
    expiry_date = models.DateField()
    quantity = models.IntegerField(validators=[MinValueValidator(1)], default=1)

    def __str__(self):
        return self.item_name.capitalize()

# Custom validator for ingredients field
def arrayfield_regex_validator(regex):
    regex_validator = RegexValidator(regex)
    def validator(value):
        for item in value:
            regex_validator(item)
    return validator

class Recipe(models.Model):
    DIETARY_RESTRICTIONS = [
        ('none', 'None'),
        ('vegetarian', 'Vegetarian'),
        # ('vegan', 'Vegan'),
        # ('keto', 'Keto'),
        # ('kosher', 'Kosher'),
        # ('halal', 'Halal'),
        # ('paleo', 'Paleo'),
        # ('gluten-free', 'Gluten-free'),
        # ('dairy-free', 'Dairy-free'),
        # ('nut-free', 'Nut-free'),
        # ('shellfish-free', 'Shellfish-free')
    ]
    CUISINE_TYPES = [
        # ('none', 'None'),
        ('italian', 'Italian'),
        ('mexican', 'Mexican'),
        ('chinese', 'Chinese'),
        # ('japanese', 'Japanese'),
        # ('indian', 'Indian'),
        # ('french', 'French'),
        # ('greek', 'Greek'),
        # ('thai', 'Thai'),
        # ('brazilian', 'Brazilian'),
        # ('korean', 'Korean'),
        # ('middle Eastern', 'Middle Eastern'),
        # ('mediterranean', 'Mediterranean'),
        # ('caribbean', 'Caribbean'),
        # ('african', 'African'),
        # ('asian', 'Asian'),
        # ('american', 'American'),
        # ('australian', 'Australian'),
        # ('european', 'European'),
        # ('pacific Islander', 'Pacific Islander'),
        ('other', 'Other')
    ]
    # FLAVOR_PROFILES = [
    #     ('none', 'None'),
    #     ('sweet', 'Sweet'),
    #     ('spicy', 'Spicy'),
    #     ('salty', 'Salty'),
    #     ('sour', 'Sour'),
    #     ('umami', 'Umami'),
    #     ('herbaceous', 'Herbaceous'),
    #     ('earthy', 'Earthy'),
    #     ('nutty', 'Nutty'),
    #     ('smoky', 'Smoky'),
    #     ('other', 'Other')
    # ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, validators=[RegexValidator(r'^[a-zA-Z -]*$')])
    restrictions = models.CharField(max_length=20, choices=DIETARY_RESTRICTIONS, unique=False, default='none')
    cuisine = models.CharField(max_length=20, choices=CUISINE_TYPES, unique=False)
    # flavor_profile = models.ManyToManyField(to='RecipeFlavor', choices=FLAVOR_PROFILES, default='none', unique=False)
    ingredients = ArrayField(models.CharField(max_length=100), default=list, validators=[arrayfield_regex_validator(r'^[a-z, -]*$')])
    instructions = models.TextField()
    source = models.URLField(blank=True)
    image = models.ImageField(upload_to='recipe_images/', blank=True)
    
    def __str__(self):
        return self.title.title()
    
    # @property
    # def ingredients(self):
    #     return set(self.ingredients)
    

# class RecipeRestriction(models.Model):
#     id = models.CharField(primary_key=True, max_length=50, choices=[(r[0], r[1]) for r in Recipe.DIETARY_RESTRICTIONS])

#     def __str__(self):
#         return self.id


# class RecipeCuisine(models.Model):
#     id = models.CharField(primary_key=True, max_length=50, choices=[(r[0], r[1]) for r in Recipe.CUISINE_TYPES])

#     def __str__(self):
#         return self.id


# class RecipeFlavor(models.Model):
#     id = models.CharField(primary_key=True, max_length=50, choices=[(r[0], r[1]) for r in Recipe.FLAVOR_PROFILES])

#     def __str__(self):
#         return self.id