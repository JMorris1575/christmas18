from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import ManageEmail, SendMail, MailCompose

app_name = 'mail'

urlpatterns = [
    path('', login_required(ManageEmail.as_view()), name='manage-mail'),
    path('invitation/', login_required(SendMail.as_view()), name='send-mail'),
    path('compose/', login_required(MailCompose.as_view()), name='compose'),
]