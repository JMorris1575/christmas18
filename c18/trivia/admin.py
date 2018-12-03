from django.contrib import admin

from .models import TriviaQuestion, TriviaChoice, TriviaResponse, TriviaConversation


class ChoiceInline(admin.StackedInline):
    model = TriviaChoice
    extra = 4


class TriviaQuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(TriviaQuestion, TriviaQuestionAdmin)
admin.site.register(TriviaResponse)                         # for use during development only
admin.site.register(TriviaConversation)