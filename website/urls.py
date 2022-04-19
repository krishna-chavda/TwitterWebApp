from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome,name='welcome'),
    path('recent_tweets',views.recent_tweets,name='recent_tweets'),
    path('search_tweets',views.search_tweets,name='search_tweets'),
    path('find',views.find,name='find'),
    path('follower',views.follower,name='follower'),
    path('following',views.following,name='following'),
    path('tweets',views.tweets,name='tweets'),
    path('all',views.all,name='all'),
    path('refollowing',views.refollowing,name='refollowing'),
    path('refollower',views.refollower,name='refollower')
]