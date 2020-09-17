from . import views
from django.urls import path
from .views import TweetListView, TweetCreateView, TweetUpdateView, TweetDeleteView

urlpatterns = [
    path('', TweetListView.as_view(), name="home"),
    path('create/', TweetCreateView.as_view(), name="tweetcreate"),
    path('create/<int:pk>/update', TweetUpdateView.as_view(), name="tweetupdate"),
    path('create/<int:pk>/delete', TweetDeleteView.as_view(), name="tweetdelete")
]