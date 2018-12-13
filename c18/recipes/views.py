from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import F
from django.contrib.auth.models import User
from django.contrib.auth import PermissionDenied

from .models import QuizPage, Recipe, Response

from user.models import get_adjusted_name

from operator import itemgetter

import utilities


class ScoreboardView(View):
    template_name = 'recipes/scoreboard.html'

    def get(self, request):
        stats, next_quiz = self.get_stats(request.user)
        context = {'memory':utilities.get_random_memory(), 'stats':stats, 'next_quiz':next_quiz}
        return render(request, self.template_name, context)

    def get_stats(self, current_user):
        users = User.objects.all()
        temp = []
        for user in users:
            user_responses = Response.objects.filter(user=user)
            attempted_recipes = len(user_responses)
            if user == current_user:
                current_user_quizzes = 0
                next_quiz = None
                if attempted_recipes > 0:
                    for quiz in QuizPage.objects.all():
                        if len(user_responses.recipe.filter(quiz_page=quiz)) != 0:
                            current_user_quizzes += 1
            if len(QuizPage.objects.all()) > current_user_quizzes:
                next_quiz = current_user_quizzes + 1
            correct = len(user_responses.filter(correct=True))
            if attempted_recipes != 0:
                percent = '{:.1%}'.format(correct/attempted_recipes)
            else:
                percent = '0.0%'
            name = get_adjusted_name(user)
            if attempted_recipes > 0:
                temp.append( {'attempted_questions':attempted_recipes, 'correct':correct, 'percent':percent, 'name':name} )
        temp_sorted = sorted(temp, key = itemgetter('attempted_questions', 'correct'), reverse=True)
        stats = []
        attempt_group = -1
        total = len(Recipe.objects.all())
        for stat in temp_sorted:
            if stat['attempted_recipes'] == attempt_group:
                stats.append(dict(type='stat', value=stat))
            else:
                attempt_group = stat['attempted_recipes']
                stats.append(dict(type='heading', value='Completing ' + str(attempt_group) + '/' + str(total)))
                stats.append(dict(type='stat', value=stat))
        return stats, next_quiz




class QuizPageView(View):
    pass


class QuizResultsView(View):
    pass


class RecipeView(View):
    pass