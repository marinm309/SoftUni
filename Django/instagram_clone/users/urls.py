from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('edit_profile/<str:pk>/', views.edit_profile, name='edit-profile'),
    path('logout/', views.user_logout, name='logout'),
    path('search_result/', views.search_results, name='search-result'),
    path('follow/<str:pk>/', views.follow, name='follow'),
    path('unfollow/<str:pk>/', views.unfollow, name='unfollow'),
    path('followers/<str:pk>/', views.view_followers, name='followers'),
]