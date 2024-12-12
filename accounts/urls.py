from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('user-details/', views.user_details, name='user_details'),
   
]