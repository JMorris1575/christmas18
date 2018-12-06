from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .views import ObjectListView

app_name = 'whatsit'

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('whatsit:object_list'))),
    path('objects/', login_required(ObjectListView.as_view()), name='object_list'),
]