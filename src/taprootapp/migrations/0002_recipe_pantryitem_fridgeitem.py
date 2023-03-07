# Generated by Django 4.1.6 on 2023-03-03 09:03

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$')])),
                ('restrictions', models.CharField(choices=[('vegetarian', 'Vegetarian')], max_length=20)),
                ('cuisine', models.CharField(choices=[('italian', 'Italian'), ('mexican', 'Mexican'), ('chinese', 'Chinese'), ('other', 'Other')], max_length=20)),
                ('ingredients', models.TextField(validators=[django.core.validators.RegexValidator('^[a-zA-Z ,]*$')])),
                ('instructions', models.TextField()),
                ('source', models.URLField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='recipe_images/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PantryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$')])),
                ('category', models.CharField(choices=[('grains', 'Grains'), ('canned foods', 'Canned Foods'), ('baking supplies', 'Baking Supplies'), ('spices', 'Spices'), ('snacks', 'Snacks'), ('sauces', 'Sauces'), ('oil and vinegars', 'Oil and Vinegars'), ('sweeteners', 'Sweeteners'), ('other', 'Other')], max_length=20)),
                ('expiry_date', models.DateField()),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FridgeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$')])),
                ('category', models.CharField(choices=[('fruits', 'Fruits'), ('vegetables', 'Vegetables'), ('grains', 'Grains'), ('dairy', 'Dairy'), ('meat', 'Meat'), ('seafood', 'Seafood'), ('dessert', 'Dessert'), ('snacks', 'Snacks'), ('beverages', 'Beverages'), ('other', 'Other')], max_length=20)),
                ('expiry_date', models.DateField()),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
