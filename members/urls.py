from django.urls import path
from django.contrib.auth import views as auth_views
from members import views

app_name = 'members'

urlpatterns = [
    path('register/', views.SignUp.as_view(), name='register'),
    path('edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),
    path('password/', views.PasswordsChangeView.as_view(), name='change_password'),
]