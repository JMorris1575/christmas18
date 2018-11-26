from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User

from .models import TriviaResponse
from user.models import get_adjusted_name

from operator import itemgetter

import utilities

class ScoreboardView(View):
    template_name = 'trivia/scoreboard.html'

    def get(self, request):
        stats = self.stats()
        context = {'memory':utilities.get_random_memory(), 'stats':stats}
        return render(request, self.template_name, context)

    def stats(self):
        users = User.objects.all()
        temp = []
        for user in users:
            user_responses = TriviaResponse.objects.filter(user=user)
            attempts = len(user_responses)
            correct = len(user_responses.filter(correct=True))
            if attempts != 0:
                percent = '{:.1%}'.format(correct/attempts)
            else:
                percent = '0.0%'
            name = get_adjusted_name(user)
            if attempts > 0:
                temp.append( {'attempts':attempts, 'correct':correct, 'percent':percent, 'name':name} )
        temp_sorted = sorted(temp, key = itemgetter('attempts', 'correct'), reverse=True)
        stats = []
        attempt_group = -1
        for stat in temp_sorted:
            if stat['attempts'] == attempt_group:
                stats.append(dict(type='stat', value=stat))
            else:
                attempt_group = stat['attempts']
                stats.append(dict(type='heading', value='Players attempting ' + str(attempt_group) + ' questions:'))
                stats.append(dict(type='stat', value=stat))
        return stats
