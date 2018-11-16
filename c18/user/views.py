from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

class CustomLoginView(View):

    template_name = 'user/login.html'

    def get(self, request):
        print(request.user)
        return redirect(reverse('user:login'))

