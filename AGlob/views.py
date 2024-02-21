from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from AGlob.models import Post, Category
from AGlob.forms import CreatePostForm, UpdatePostForm, CategoryForm
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


class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'


class UpdateCategoryView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'update_category.html'


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'category_list.html'
    success_url = reverse_lazy('AGlob:category_list')


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category=self.object)
        return context