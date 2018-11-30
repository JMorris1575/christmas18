from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.urls import reverse

from .models import TriviaQuestion, TriviaChoice, TriviaResponse
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
        total = len(TriviaQuestion.objects.all())
        for stat in temp_sorted:
            if stat['attempts'] == attempt_group:
                stats.append(dict(type='stat', value=stat))
            else:
                attempt_group = stat['attempts']
                stats.append(dict(type='heading', value='Completing ' + str(attempt_group) + '/' + str(total)))
                stats.append(dict(type='stat', value=stat))
        return stats, current_user_attempts


class NextQuestionView(View):

    def get(self, request):
        print("got to NextQuestionView")
        return redirect('trivia:display_question', get_next_question(request.user))


class DisplayQuestionView(View):
    template_name = 'trivia/trivia_question.html'

    def get(self, request, question_number):
        try:
            question = TriviaQuestion.objects.get(number=question_number)
        except:
            question_number = 1
            return redirect('trivia:display_question', question_number=question_number)
        else:
            response = TriviaResponse.objects.get(question=question).response
            if int(question_number) > get_next_question(request.user):      # prevents going beyond user's next question
                question_number = get_next_question(request.user)
                return redirect('trivia:display_question', question_number=question_number)
            if int(question_number) < get_next_question(request.user):      # prevents answering a quesstion twice
                return redirect('trivia:result', question_number=question.number, choice_id=response.id)
            choices = question.triviachoice_set.all()
            context = {'memory':utilities.get_random_memory(), 'question':question, 'choices':choices}
            return render(request, self.template_name, context)

    def post(self, request, question_number):
        question = TriviaQuestion.objects.get(number=question_number)
        choices = question.triviachoice_set.all()
        if int(question_number) < get_next_question(request.user):
            user_response = TriviaResponse.objects.get(user=request.user, question=question)
            choice = user_response.response
            return redirect('trivia:result', question_number=question_number, choice_id=choice.id)
        try:
            choice_id = request.POST['choice']
        except KeyError:
            context = {'question': question, 'choices': choices, 'display_memory': utilities.get_random_memory(),
                       'error_message': 'You must choose one of the responses below.'}
            return render(request, self.template_name, context)
        else:
            choice = choices.get(id=choice_id)
            user_response = TriviaResponse(user=request.user, question=question, response=choice)
            user_response.correct = choice.correct
            user_response.save()
        return redirect('trivia:result', question_number=question_number, choice_id = choice.id)


class DisplayResultView(View):
    template_name = 'trivia/trivia_result.html'

    def get(self, request, question_number, choice_id):
        question = TriviaQuestion.objects.get(number=question_number)
        user_choice = TriviaChoice.objects.get(id=choice_id)
        choices = question.triviachoice_set.all()
        correct_choice = question.triviachoice_set.get(correct=True)
        context = {'memory': utilities.get_random_memory(), 'question': question, 'choices': choices,
                   'user_choice': user_choice, 'correct_choice': correct_choice}
        return render(request, self.template_name, context)

def previous_question_view(request, question_number):
    previous = question_number - 1
    if previous < 1:
        previous = 1
    return redirect('trivia:display_question', previous)

def next_question_view(request, question_number):
    next = question_number + 1
    if next > len(TriviaQuestion.objects.all()):
        next = len(TriviaQuestion.objects.all())
    return redirect('trivia:display_question', next)

class EndOfQuestions(View):
    pass