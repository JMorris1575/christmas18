from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User

from .models import Memory

from operator import itemgetter

import utilities


class MemoryListView(View):
    template_name = 'memory/memory_list.html'

    def get(self, request):
        memories = Memory.objects.all()
        collection = []
        for user in User.objects.all():
            user_memories = memories.filter(user=user)
            if user_memories:
                collection.append({'user':user, 'memories':user_memories})
            collection_sorted = sorted(collection, key=itemgetter('user'))
        context = {'memory':utilities.get_random_memory(), 'collection':collection}
        return render(request, self.template_name, context)

