# Generated by Django 3.2.24 on 2024-02-24 16:21

from django.db import migrations, models
import recipe.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20240224_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=recipe.models.recipe_image_file_path),
        ),
    ]
