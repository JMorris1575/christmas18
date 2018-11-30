from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.urls import reverse_lazy

from .views import MemoryListView

app_name = 'memory'

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('memory:memory_list'))),
    path('collection', login_required(MemoryListView.as_view()), name='memory_list'),
]