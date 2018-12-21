from django.db import models
from django.conf import settings

import os


class QuizPage(models.Model):
    quiz_number = models.SmallIntegerField(unique=True)
    title = models.CharField(max_length=40)

    def __str__(self):
        return 'Quiz Page ' + str(self.quiz_number) + ': ' + self.title

    def is_next_quiz(self):
        if self.quiz_number < len(QuizPage.objects.all()):
            return True
        else:
            return False

        class Meta:
            ordering = ['quiz_number']


class Recipe(models.Model):
    name = models.CharField(max_length=40, unique=True)
    ingredients = models.TextField()
    quiz_page = models.ForeignKey(QuizPage, on_delete=models.CASCADE)
    recipe_image_filename = models.CharField(max_length=60, default="", blank=True)

    def __str__(self):
        return 'Recipe for ' + self.name

    def get_recipe_image_filename(self):
        return os.path.join('recipes', 'images', 'recipe_images', self.recipe_image_filename)

    class Meta:
        ordering = ['pk']


class Response(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    guess = models.CharField(max_length=40)
    correct = models.BooleanField()

    def __str__(self):
        return self.user.username + "'s guess on " + str(self.recipe)

    def quiz_number(self):
        return self.recipe.quiz_page.page_number
