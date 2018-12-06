# Generated by Django 2.1.2 on 2018-12-06 02:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TriviaChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=255)),
                ('correct', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='TriviaConversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.CharField(max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TriviaQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('text', models.CharField(max_length=255)),
                ('publish', models.BooleanField(default=False)),
                ('attempted_count', models.IntegerField(default=0)),
                ('correct_count', models.IntegerField(default=0)),
                ('explanation', models.CharField(default='', max_length=255)),
                ('link', models.URLField(default='')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='TriviaResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trivia.TriviaQuestion')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trivia.TriviaChoice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['question'],
            },
        ),
        migrations.AddField(
            model_name='triviachoice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trivia.TriviaQuestion'),
        ),
    ]
