# Generated by Django 2.1.2 on 2018-11-30 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0005_auto_20181126_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='triviaquestion',
            name='explanation',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='triviaquestion',
            name='text',
            field=models.CharField(max_length=255),
        ),
    ]