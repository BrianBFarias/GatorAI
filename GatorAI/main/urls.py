from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search/<slug:query>", views.search, name="search"),


]