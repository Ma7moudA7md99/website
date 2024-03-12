from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
  path('skin cancer', views.skinCancer, name='skin cancer'),
  path('medical terminology', views.medicalTerm, name='medical terminology'),
  path('virus c', views.virus_c, name='virus c'),
  path('doctors/<str:specialization>', views.doctor, name='doctors'),
  path('doctors/message/<int:doctor_id>', views.doctor_message, name="message")
]