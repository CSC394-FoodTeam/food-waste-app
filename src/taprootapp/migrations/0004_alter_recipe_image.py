# Generated by Django 4.1.6 on 2023-03-03 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taprootapp", "0003_alter_recipe_ingredients_alter_recipe_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="image",
            field=models.ImageField(upload_to="files/covers"),
        ),
    ]
