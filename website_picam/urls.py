"""Defines URLS for the website_picam site"""
from django.urls import path
from . import views

app_name = 'website_picam'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Login page
    path('login/', views.user_login, name='login'),
]

