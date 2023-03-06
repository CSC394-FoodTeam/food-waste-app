# Generated by Django 4.1.6 on 2023-03-06 23:28

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taprootapp', '0002_recipe_pantryitem_fridgeitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pantryitem',
            name='item_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-z ]*$')]),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='restrictions',
            field=models.CharField(choices=[('none', 'None'), ('vegetarian', 'Vegetarian')], default='none', max_length=20),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z -]*$')]),
        ),
    ]