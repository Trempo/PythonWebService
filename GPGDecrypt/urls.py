from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.decrypt_view, name='decrypt_view'),

]