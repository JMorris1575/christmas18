from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import PermissionDenied

from .models import QuizPage, Recipe, Response

import utilities


class ScoreboardView(View):
    pass


class QuizPageView(View):
    pass


class QuizResultsView(View):
    pass


class RecipeView(View):
    pass
