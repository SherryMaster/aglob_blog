from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from AGlob.models import Post
from AGlob.forms import CreatePostForm, UpdatePostForm
from django.urls import reverse_lazy


# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-id']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'


class AddPostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'



class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_detail.html'
    success_url = reverse_lazy('AGlob:index')
