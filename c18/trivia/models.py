from django.db import models
from django.conf import settings

from user.models import get_adjusted_name


class TriviaQuestion(models.Model):
    number = models.IntegerField(unique=True)
    text = models.CharField(max_length=255)
    attempted_count = models.IntegerField(default=0)
    correct_count = models.IntegerField(default=0)
    explanation = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['number']


class TriviaChoice(models.Model):
    question = models.ForeignKey(TriviaQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


    class Meta:
        ordering = ['pk']


class TriviaResponse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(TriviaQuestion, on_delete=models.CASCADE)
    response = models.ForeignKey(TriviaChoice, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)

    def __str__(self):
        text = get_adjusted_name(self.user) + ' responded ' + \
               str(self.response) + ' to question ' + str(self.question.number)
        return text


    class Meta:
        ordering = ['question']


class TriviaConversation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    entry = models.CharField(max_length = 300)

    def __str__(self):
        return get_adjusted_name(self.user) + ': ' + self.entry


class TriviaStats(models.Model):
    player = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    questions_attempted = models.SmallIntegerField(default=0)
    answers_correct = models.SmallIntegerField(default=0)

    def __str__(self):
        return get_adjusted_name(self.player) + ': ' + str(self.answers_correct) + \
               ' out of ' + str(self.questions_attempted)

    def get_next_trivia(self):
        return self.questions_attempted + 1

    def score(self):
        return '{:.1%}'.format(self.answers_correct / self.questions_attempted)
