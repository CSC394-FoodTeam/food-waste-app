# Generated by Django 4.1.6 on 2023-02-08 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taproot', '0002_alter_fridgeitem_category_alter_pantryitem_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridgeitem',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pantryitem',
            name='category',
            field=models.CharField(max_length=50),
        ),
    ]
