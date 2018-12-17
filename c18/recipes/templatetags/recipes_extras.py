from django import template

register = template.Library()

@register.filter(name='recipe_name')
def recipe_name(value, recipe):
    return value.get(recipe.name, '')
