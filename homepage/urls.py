from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('sign_in', views.sign_in, name='sign_in'),
  path('sign_up', views.sign_up, name='sign_up'),
  path('logout', views.log_out, name='logout'),
  path('send_msg', views.send_msg, name='send_msg'),
  path('skinCancer', views.skinCancer, name='skinCancer'),
  path('terminology', views.medicalTerm, name='terminology')
]