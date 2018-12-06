from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Object, Description

import utilities


class ObjectListView(View):
    template_name = 'whatsit/object_list.html'

    def get(self, request):
        objects = Object.objects.filter(publish=True)
        context = {'memory':utilities.get_random_memory(), 'objects': objects}
        return render(request, self.template_name, context)



