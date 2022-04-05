from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', views.create_post, name='create-post'),
    path('delete_post/<str:pk>/', views.delete_post, name='delete-post'),
    path('edit_post/<str:pk>/', views.edit_post, name='edit-post'),
    path('like_post/<str:pk>/', views.like_post, name='like-post'),
    path('create_comment/<str:pk>/', views.create_comment, name='create-comment'),
]