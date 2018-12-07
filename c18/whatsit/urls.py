from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .views import ObjectListView, SingleObjectView, DescriptionEditView

app_name = 'whatsit'

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('whatsit:object_list'))),
    path('objects/', login_required(ObjectListView.as_view()), name='object_list'),
    path('<int:object_number>/', login_required(SingleObjectView.as_view()), name='object_view'),
    path('create/<int:object_number>/',
         login_required(SingleObjectView.as_view()), name='create_description'),
    path('edit/<int:object_number>/<int:description_id>/',
         login_required(SingleObjectView.as_view()), name='edit_description'),
]