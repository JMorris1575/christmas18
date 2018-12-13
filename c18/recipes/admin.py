from django.contrib import admin

from .models import QuizPage, Recipe, Response


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 5


class QuizPageAdmin(admin.ModelAdmin):
    inlines = [RecipeInline]


admin.site.register(QuizPage, QuizPageAdmin)
admin.site.register(Response)

