from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.urls import reverse

from .models import TriviaQuestion, TriviaResponse
from user.models import get_adjusted_name

from operator import itemgetter

import utilities

def get_next_question(user):
    return len(TriviaResponse.objects.filter(user=user)) + 1

class ScoreboardView(View):
    template_name = 'trivia/scoreboard.html'

    def get(self, request):
        stats, current_user_attempts = self.get_stats(request.user)
        context = {'memory':utilities.get_random_memory(), 'stats':stats, 'user_attempts':current_user_attempts}
        return render(request, self.template_name, context)

    def get_stats(self, current_user):
        users = User.objects.all()
        temp = []
        for user in users:
            user_responses = TriviaResponse.objects.filter(user=user)
            attempts = len(user_responses)
            if user == current_user:
                current_user_attempts = attempts
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
        return stats, current_user_attempts


class NextQuestionView(View):

    def get(self, request):
        print("got to NextQuestionView")
        return redirect(reverse('trivia:display_question', args=[get_next_question(request.user)]))


class DisplayQuestionView(View):
    template_name = 'trivia/trivia_question.html'

    def get(self, request, question_number):
        if int(question_number) > get_next_question(request.user):
            question_number = get_next_question(request.user)
            return redirect(reverse('trivia:display_question', kwargs={'question_number':question_number}))
        if int(question_number) > len(TriviaQuestion.objects.all()):
            return redirect(reverse('end_of_questions'))
        question = TriviaQuestion.objects.get(number=question_number)
        choices = question.triviachoice_set.all()
        context = {'memory':utilities.get_random_memory(), 'question':question, 'choices':choices}
        return render(request, self.template_name, context)

    def post(self, request, question_number):
        question = TriviaQuestion.objects.get(number=question_number)
        choices = question.triviachoice_set.all()
        if int(question_number) < get_next_question(request.user):
            user_response = TriviaResponse.objects.get(user=request.user, question=question)
            choice = user_response.choice
            return redirect('trivia_result', question_number=question_number, choice_number=choice.number)
        try:
            choice_index = request.POST['choice']
        except KeyError:
            context = {'question': question, 'choices': choices, 'display_memory': utilities.get_random_memory(),
                       'error_message': 'You must choose one of the responses below.'}
            return redirect('trivia:display_question', question_number=question_number)
        else:
            choice = choices.get(number=choice_index)
            user_response = TriviaResponse(user=request.user, question=question, response=choice)
            user_response.correct = choice.correct
            user_response.save()
        return redirect('trivia:trivia_result', question_number=question_number, choice_number = choice.number)




class EndOfQuestions(View):
    pass