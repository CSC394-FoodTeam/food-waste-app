# Generated by Django 4.1.6 on 2023-02-21 06:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taprootapp', '0002_alter_fridgeitem_quantity_alter_pantryitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridgeitem',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='pantryitem',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
