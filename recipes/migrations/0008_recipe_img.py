# Generated by Django 4.1 on 2022-08-27 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_rename_name_recipeingredient_ingredient_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]