# Generated by Django 2.1.2 on 2018-12-13 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_recipe_image_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizpage',
            name='title',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
