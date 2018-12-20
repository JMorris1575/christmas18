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
                        if len(user_responses.filter(recipe__quiz_page=quiz)) != 0:
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
                temp.append({'attempted_recipes':attempted_recipes, 'correct':correct, 'percent':percent, 'name':name})
        temp_sorted = sorted(temp, key = itemgetter('attempted_recipes', 'correct'), reverse=True)
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
    template_name = 'recipes/quiz_page.html'

    def get(self, request, quiz_number):
        quiz = QuizPage.objects.get(quiz_number=quiz_number)
        recipes = Recipe.objects.filter(quiz_page=quiz)
        recipe_names = []
        for recipe in recipes:
            recipe_names.append(recipe.name)
        recipe_names.sort()
        context = {'memory':utilities.get_random_memory(), 'quiz':quiz, 'recipes':recipes, 'recipe_names': recipe_names}
        return render(request, self.template_name, context)

    def post(self, request, quiz_number):
        quiz = QuizPage.objects.get(quiz_number=quiz_number)
        recipes = Recipe.objects.filter(quiz_page=quiz)
        guesses = {}
        recipe_names = []
        for recipe in recipes:
            guesses[recipe.name] = request.POST[recipe.name]
            recipe_names.append(recipe.name)
        recipe_names.sort()
        if "" in guesses.values():
            context = {'memory': utilities.get_random_memory(), 'quiz': quiz, 'recipes': recipes, 'guesses': guesses,
                       'recipe_names': recipe_names, 'error': 'You must guess a recipe for each set of indredients.'}
            return render(request, self.template_name, context)

        for recipe in recipes:
            response = Response(user=request.user, recipe=recipe, guess=request.POST[recipe.name])
            if recipe.name == request.POST[recipe.name]:
                response.correct = True
            else:
                response.correct = False
            response.save()
        return redirect('recipes:quiz_results', quiz_number=quiz_number)


class QuizResultsView(View):
    template_name = 'recipes/quiz_results.html'

    def get(self, request, quiz_number):
        quiz = QuizPage.objects.get(quiz_number=quiz_number)
        recipes = Recipe.objects.filter(quiz_page=quiz)
        guesses = []
        for response in Response.objects.filter(recipe__quiz_page=quiz):
            guesses.append(response.guess)
        context = {'memory':utilities.get_random_memory(), 'quiz': quiz, 'recipes': recipes, 'guesses': guesses}
        return render(request, self.template_name, context)


class RecipeView(View):
    pass
