# Generated by Django 2.1.3 on 2018-11-27 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0003_triviaplayer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='triviaplayer',
            name='id',
        ),
        migrations.AlterField(
            model_name='triviaplayer',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
