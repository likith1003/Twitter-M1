from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('user_login', user_login, name='user_login'),
    path('user_logout', user_logout, name='user_logout'),
    path('create_tweet', create_tweet, name='create_tweet'),
    path('saved', saved, name='saved'),
    path('update<pk>', update, name='update'),
    path('delete<pk>', delete, name='delete'),
    path('save<pk>', save, name='save'),
    path('like<pk>', like, name='like'),
]
