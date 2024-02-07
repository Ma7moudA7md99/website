from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('sign_in', views.sign_in, name='sign_in'),
  path('send_msg', views.send_msg, name='send_msg'),
  path('sign_up', views.sign_up, name='sign_up'),
  path('skinCancer', views.skinCancer, name='skinCancer')
]