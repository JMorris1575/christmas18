from django.shortcuts import render
from django.views import View

from .models import Gift

class GiftListView(View):
    template = 'gift/gift_list.html'

    def get(self, request):
        gifts = Gift.objects.all()
        print(gifts)
        context = {'gifts': gifts}
        return render(request, self.template, context)
