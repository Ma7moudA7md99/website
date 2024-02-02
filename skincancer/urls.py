from django.urls import path
from . import views

urlpatterns = [
  path('', views.skinCancer, name='skin cancer'),
]