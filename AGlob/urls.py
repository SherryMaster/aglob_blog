from django.urls import path
from . import views

app_name = 'AGlob'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('post<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('add_post', views.AddPostView.as_view(), name='add_post'),
    path('update_post<int:pk>', views.UpdatePostView.as_view(), name='update_post'),
    path('delete_post<int:pk>', views.DeletePostView.as_view(), name='delete_post'),
    path('category_list', views.CategoryListView.as_view(), name='category_list'),
    path('category<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('add_category', views.AddCategoryView.as_view(), name='add_category'),
    path('update_category<int:pk>', views.UpdateCategoryView.as_view(), name='update_category'),
    path('delete_category<int:pk>', views.DeleteCategoryView.as_view(), name='delete_category'),
]