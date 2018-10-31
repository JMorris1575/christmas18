from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import GiftListView

app_name = 'gift'
urlpatterns = [
    path('gift-list', login_required(GiftListView), name="home"),
]