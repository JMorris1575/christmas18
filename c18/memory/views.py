from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User

from .models import Memory
from user.models import get_adjusted_name

from operator import itemgetter

import utilities


class MemoryListView(View):
    template_name = 'memory/memory_list.html'

    def sorter(self, e):
        return get_adjusted_name(e['user'])

    def get(self, request):
        memories = Memory.objects.all()
        collection = []
        for user in User.objects.all():
            user_memories = memories.filter(user=user)
            if user_memories:
                collection.append({'user':user, 'memories':user_memories})
            collection.sort(key=self.sorter)
        context = {'memory':utilities.get_random_memory(), 'collection':collection}
        return render(request, self.template_name, context)


class MemoryEditView(View):
    template_name = 'memory/memory_edit.html'

    def get(self, request, memory_id=None):
        if memory_id:
            current_memory = Memory.objects.get(pk=memory_id)
        else:
            current_memory = None
        context = {'memory':utilities.get_random_memory(), 'current_memory':current_memory}
        return render(request, self.template_name, context)