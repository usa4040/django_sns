from django.urls import path

from app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('post/list/', views.PostMylistView.as_view(), name='mylist'),
    path('post/create', views.PostCreateView.as_view(), name='create'),
    path('post/detail/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('post/detail/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete'),
    path('post/detail/<int:pk>/update', views.PostUpdateView.as_view(), name='update'),
]
