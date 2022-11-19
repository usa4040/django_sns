from app import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('post/list/', views.PostMylistView.as_view(), name='mylist'),
    path('post/create', views.PostCreateView.as_view(), name='create'),
    path('post/detail/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('post/detail/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete'),
    path('post/detail/<int:pk>/update', views.PostUpdateView.as_view(), name='update'),
    path('like_for_post/', views.like_for_post, name='like_for_post'), 
]
