# Generated by Django 4.1.6 on 2023-02-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taproot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridgeitem',
            name='category',
            field=models.CharField(choices=[('1', 'Fruits'), ('2', 'Vegetables'), ('3', 'Grains'), ('4', 'Dairy'), ('5', 'Meat'), ('6', 'Seafood'), ('7', 'Deseert'), ('8', 'Snacks'), ('9', 'Beverages')], max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='pantryitem',
            name='category',
            field=models.CharField(choices=[('1', 'Grains'), ('2', 'Canned Foods'), ('3', 'Baking Supplies'), ('4', 'Spices'), ('5', 'Snacks'), ('6', 'Sauces'), ('7', 'Oil and Vinegars'), ('8', 'Sweetners')], max_length=20, unique=True),
        ),
    ]
