from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(f"wiki/<str:wiki>", views.wiki, name="wiki"),
    path("add-new-page", views.add, name="add"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("random", views.random, name="random")
]
