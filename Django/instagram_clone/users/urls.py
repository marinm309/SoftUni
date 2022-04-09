from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('search_result/', views.search_results, name='search-result'),
    path('follow/<str:pk>/', views.follow, name='follow'),
]