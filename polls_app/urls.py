from django.urls import path
# обращаемся к файлу собственной директории
from . import views

urlpatterns = [
    path('', views.index),
]