from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('sign_in', views.sign_in_page, name='sign_in'),
  path('sign_in_method', views.sign_in_method, name='sign_in'),
  path('send_msg', views.send_msg, name='send_msg'),
  path('sign_up', views.sign_up_page, name='sign_up_page'),
  path('sign_up_method', views.sign_up, name='sign_up'),
]