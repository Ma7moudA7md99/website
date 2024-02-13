from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
  path('skin cancer', views.skinCancer, name='skin cancer'),
  path('medical terminology', views.medicalTerm, name='medical terminology'),
]