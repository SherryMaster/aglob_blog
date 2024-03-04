from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserRegisterForm, EditProfileForm


# Create your views here.
class SignUp(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class EditProfileView(UpdateView):
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('AGlob:index')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(auth_views.PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('AGlob:index')
