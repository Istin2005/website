from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from accounts import views
from django.urls import path, include  # Add 'include'


urlpatterns = [
    # Login and Logout paths
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Registration path
    path('register/', views.register, name='register'),

   path('', views.home, name='home'),
   path('admin/', admin.site.urls),
   path('accounts/', include('accounts.urls')),
   path('users/', views.user_list, name='user_list'),
]