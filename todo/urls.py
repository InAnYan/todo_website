from django.urls import path

from todo import views


urlpatterns = [
    path("", views.index, name="index"),
    path("another", views.another, name="another"),
]
