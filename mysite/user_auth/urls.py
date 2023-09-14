from django.shortcuts import render, redirect
from django.template.defaulttags import url
from django.urls import path, re_path, include
from . import views

app_name = "user_auth"

urlpatterns = [
    path("login", views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('access/', views.show_user, name='show_user'),
    path('', views.create_user, name='register'),
    # path('', views.user_auth, name='sign'),
    # path('', views.user_auth, name='reg'),

    # re_path(r'^polls/', lambda request: redirect(request, 'polls/poll.html'), name="poll")
    # re_path(r"^$", include("polls.urls"), name="test"),
    # re_path(r"^polls", 'polls.views.index'),
    #url(r'^polls/', 'polls.views.index',  name="poll"),

]
