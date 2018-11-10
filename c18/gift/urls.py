from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import GiftListView, GiftSelectView, GiftChangeMindView, GiftCommentView

app_name = 'gift'
urlpatterns = [
    path('gift-list/', login_required(GiftListView.as_view()), name="home"),
    path('<int:gift_number>/select/', login_required(GiftSelectView.as_view()), name="select"),
    path('<int:gift_number>/change_mind/', login_required(GiftChangeMindView.as_view()), name="change_mind"),
    path('<int:gift_number>/comment/', login_required(GiftCommentView.as_view()), name="comment"),
]