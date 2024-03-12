
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add", views.addstu, name="add"),
    path("view", views.view, name="view")
]
