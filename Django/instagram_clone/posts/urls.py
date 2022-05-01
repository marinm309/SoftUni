from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', views.create_post, name='create-post'),
    path('delete_post/<str:pk>/', views.delete_post, name='delete-post'),
    path('edit_post/<str:pk>/', views.edit_post, name='edit-post'),
    path('like_post/<str:pk>/', views.like_post, name='like-post'),
    path('create_comment/<str:pk>/', views.create_comment, name='create-comment'),
    path('delete_comment/<str:pk>/<str:ck>/', views.delete_comment, name='delete-comment'),
    path('single_post/<str:pk>/', views.single_post, name='single-post'),
    path('like_comment/<str:pk>/', views.like_comment, name='like-comment'),
    path('start_reply/<str:pk>/<str:ck>/', views.start_reply, name='start-reply'),
]