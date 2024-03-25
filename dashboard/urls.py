from django.urls import path
from . import views

urlpatterns = [
  path('dash/', views.dashboard, name='dash'),
  path('update doctor/<int:doctor_id>/', views.update_doctor, name='update doctor'),
  path('add doctor', views.add_doctor, name='add doctor'),
  path('delete/<int:id_delete>/', views.delete_, name='delete'),
  path('user_status/<int:user_id>/', views.user_status, name='user status' ),
  path('get_user_info/<int:user_id>/', views.get_user_info, name='get_user_info'), #ajax request to get user info by username
]