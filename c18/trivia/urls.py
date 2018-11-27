from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .views import ScoreboardView, NextQuestionView, DisplayQuestionView

app_name = 'trivia'

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('trivia:scoreboard'))),
    path('scoreboard', login_required(ScoreboardView.as_view()), name='scoreboard'),
    path('question', login_required(NextQuestionView.as_view()), name='next_question'),
    path('question/<int:question_number>', login_required(DisplayQuestionView.as_view()), name='display_question'),

]