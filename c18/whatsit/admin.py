from django.contrib import admin

from .models import Object, Description, Contribution

admin.site.register(Object)
admin.site.register(Description)
admin.site.register(Contribution)
