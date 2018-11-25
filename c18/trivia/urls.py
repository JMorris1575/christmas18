from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .views import ScoreboardView

app_name = 'trivia'

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('trivia:scoreboard'))),
    path('scoreboard', ScoreboardView.as_view(), name='scoreboard'),
]