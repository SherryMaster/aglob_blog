from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from .forms import UserRegisterForm

# Create your views here.
class SignUp(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class EditProfileView(UpdateView):
    form_class = UserChangeForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('AGlob:index')

    def get_object(self):
        return self.request.user

