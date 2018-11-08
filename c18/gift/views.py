from django.shortcuts import render
from django.views import View

class GiftListView(View):
    template = 'gift/temp.html'

    def get(self, request):
        return render(request, self.template)
