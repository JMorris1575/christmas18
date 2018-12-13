from django.db import models
from django.conf import settings

import os


class QuizPage(models.Model):
    page_number = models.SmallIntegerField(unique=True)
    title = models.CharField(max_length=40)


    def __str__(self):
        return 'Quiz Page: ' + self.title


class Recipe(models.Model):
    name = models.CharField(max_length=40, unique=True)
    ingredients = models.TextField()
    quiz_page = models.ForeignKey(QuizPage, on_delete=models.CASCADE)
    recipe_image_filename = models.CharField(max_length=60, default="", blank=True)

    def __str__(self):
        return 'Recipe for ' + self.name

    def get_recipe_image_filename(self):
        return os.path.join('recipes', 'images', 'Recipe' + str(self.number))


class Response(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    guess = models.SmallIntegerField()
    correct = models.BooleanField()

    def __str__(self):
        return self.user.username + "'s guess on " + str(self.recipe)
