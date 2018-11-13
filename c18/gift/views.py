from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .models import Gift

import utilities

class GiftListView(View):
    template = 'gift/gift_list.html'

    def get(self, request):
        gifts = Gift.objects.all()
        context = {'gifts': gifts, 'user_has_gift': utilities.user_has_gift(request.user)}
        return render(request, self.template, context)


class GiftSelectView(View):

    def post(self, request, gift_number):
        current_gift = Gift.objects.get(gift_number=gift_number)
        current_gift.selected = True
        current_gift.receiver = request.user
        current_gift.save()
        return redirect(reverse('gift:home'))


class GiftChangeMindView(View):

    def post(self, request, gift_number):
        current_gift = Gift.objects.get(gift_number=gift_number)
        current_gift.selected = False
        current_gift.receiver = None
        current_gift.save()
        return redirect(reverse('gift:home'))


class AddCommentView(View):
    template_name = 'gift/comment_create.html'

    def get(self, request, gift_number):
        context = {'gift':Gift.objects.get(gift_number=gift_number)}
        return render(request, self.template_name, context)