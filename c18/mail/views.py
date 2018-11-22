from django.shortcuts import render
from django.views.generic import View
from django.core.mail import send_mail
from django.contrib.auth.models import User


class ManageEmail(View):
    template_name = 'mail/manage-mail.html'

    def get(self, request):
        users = User.objects.all()
        context = {'users': users}
        return render(request, self.template_name, context)


class SendMail(View):
    pass


class MailCompose(View):
    pass