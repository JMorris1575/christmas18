from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .views import ScoreboardView, QuizPageView, QuizResultsView, RecipeView, next_quiz_results, previous_quiz_results

app_name = 'recipes'

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('recipes:scoreboard'))),
    path('scoreboard/', login_required(ScoreboardView.as_view()), name='scoreboard'),
    path('quiz/<int:quiz_number>/', login_required(QuizPageView.as_view()), name='quiz_page'),
    path('results/<int:quiz_number>/', login_required(QuizResultsView.as_view()), name='quiz_results'),
    path('view/<int:recipe_id>/', login_required(RecipeView.as_view()), name='recipe_view'),
    path('next/<int:quiz_number>/', login_required(next_quiz_results), name='next_results'),
    path('previous/<int:quiz_number>/', login_required(previous_quiz_results), name='previous_results')
]