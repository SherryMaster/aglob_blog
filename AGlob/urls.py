from django.urls import path
from . import views

app_name = 'AGlob'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('post<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('add_post', views.AddPostView.as_view(), name='add_post'),
    path('update_post<int:pk>', views.UpdatePostView.as_view(), name='update_post'),
    path('delete_post<int:pk>', views.DeletePostView.as_view(), name='delete_post'),
]