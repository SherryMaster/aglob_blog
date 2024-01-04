from django.urls import path

from members import views

app_name = 'members'

urlpatterns = [
    path('register/', views.SignUp.as_view(), name='register'),
]