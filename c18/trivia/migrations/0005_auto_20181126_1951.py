# Generated by Django 2.1.3 on 2018-11-27 00:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trivia', '0004_auto_20181126_1939'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TriviaPlayer',
            new_name='TriviaStats',
        ),
    ]
