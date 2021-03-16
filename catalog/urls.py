from django.conf import settings
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homePage, name='homePage.html'),
]