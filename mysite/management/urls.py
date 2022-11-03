from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("projektas/", views.projektas, name="projektas"),
    path('register/', views.register, name='register'),
]