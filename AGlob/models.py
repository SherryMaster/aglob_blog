from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('AGlob:category_list')


class Post(models.Model):
    title = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    summary = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('AGlob:post_detail', args=[str(self.id)])
