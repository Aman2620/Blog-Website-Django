from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index,name='index'),
    path('index', views.index,name='index'),
    path('login', views.loginuser,name='login'),
    path('register', views.register,name='register'),
    path('home', views.home,name='home'),
    path('blogs', views.blogs,name='blogs'),
    path('blog_detail/<int:post_id>/', views.blog_detail, name='blog_detail'),
     path('logout/', views.logout_view, name='logout')
]