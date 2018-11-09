from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import GiftListView, GiftSelectView

app_name = 'gift'
urlpatterns = [
    path('gift-list/', login_required(GiftListView.as_view()), name="home"),
    path('<int:gift_number>/select/', login_required(GiftSelectView.as_view()), name="select")
]