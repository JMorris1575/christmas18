# Generated by Django 2.1.2 on 2018-12-20 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20181213_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='guess',
            field=models.CharField(max_length=40),
        ),
    ]