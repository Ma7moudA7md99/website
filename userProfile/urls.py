from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.profile_page, name='profile'),
]