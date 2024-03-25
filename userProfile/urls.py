from django.urls import path, include
from . import views

urlpatterns = [
  path('profile/', views.profile_page, name='profile'),
  path('doctor_dash', views.doctor_dash, name='doctor dashboard'),
  path('send/' , views.send, name='send message'),
  path('show_messages/', views.show_messages, name='show_messages')
]