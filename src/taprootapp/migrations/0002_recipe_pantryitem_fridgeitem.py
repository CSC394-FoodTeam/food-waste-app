# Generated by Django 4.1.6 on 2023-02-25 20:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taprootapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('restrictions', models.CharField(choices=[('None', 'None'), ('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan'), ('Gluten-free', 'Gluten-free'), ('Dairy-free', 'Dairy-free'), ('Kosher', 'Kosher'), ('Halal', 'Halal')], default='None', max_length=20)),
                ('cuisine', models.CharField(choices=[('None', 'None'), ('Italian', 'Italian'), ('Mexican', 'Mexican'), ('Chinese', 'Chinese'), ('Indian', 'Indian'), ('French', 'French'), ('Greek', 'Greek'), ('Japanese', 'Japanese'), ('Thai', 'Thai'), ('Korean', 'Korean'), ('Middle Eastern', 'Middle Eastern'), ('Mediterranean', 'Mediterranean'), ('Caribbean', 'Caribbean'), ('African', 'African'), ('American', 'American')], default='None', max_length=20)),
                ('flavor_profile', models.CharField(choices=[('None', 'None'), ('Sweet', 'Sweet'), ('Sour', 'Sour'), ('Salty', 'Salty'), ('Bitter', 'Bitter'), ('Umami', 'Umami'), ('Spicy', 'Spicy'), ('Herbaceous', 'Herbaceous'), ('Nutty', 'Nutty'), ('Smoky', 'Smoky')], default='None', max_length=20)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('image', models.ImageField(upload_to='recipe_images/')),
            ],
        ),
        migrations.CreateModel(
            name='PantryItem',
            fields=[
                ('item_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Grains', 'Grains'), ('Canned Foods', 'Canned Foods'), ('Baking Supplies', 'Baking Supplies'), ('Spices', 'Spices'), ('Snacks', 'Snacks'), ('Sauces', 'Sauces'), ('Oil and Vinegars', 'Oil and Vinegars'), ('Sweeteners', 'Sweeteners')], max_length=20)),
                ('expiry_date', models.DateField()),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FridgeItem',
            fields=[
                ('item_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Fruits', 'Fruits'), ('Vegetables', 'Vegetables'), ('Grains', 'Grains'), ('Dairy', 'Dairy'), ('Meat', 'Meat'), ('Seafood', 'Seafood'), ('Dessert', 'Dessert'), ('Snacks', 'Snacks'), ('Beverages', 'Beverages')], max_length=20)),
                ('expiry_date', models.DateField()),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
