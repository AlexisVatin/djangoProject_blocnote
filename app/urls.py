from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.FirstView.as_view(), name='first'),
    path('home/', views.BoardView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', views.postedit, name='edit'),
    path('create/', views.postcreate, name='create'),
    path('delere/<int:pk>/', views.postdelete, name='delete'),
    path('login/', views.LogView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
