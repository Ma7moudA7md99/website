from django.urls import path
from . import views

urlpatterns = [
  path('dash', views.dashboard, name='dash'),
  path('update doctor/<int:doctor_id>/', views.update_doctor, name='update doctor'),
  path('add doctor', views.add_doctor, name='add doctor')
]