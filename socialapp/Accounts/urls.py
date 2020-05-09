from django.urls import path

from . import views
urlpatterns = [
  path('', views.index, name='index'),
  path('register', views.register, name='register'),
  path('register/check/<str:username>/', views.username_present, name='username_present'),
  path('login', views.login_view, name='login'),
  path('logout', views.logout_view, name='logout'),
  path('profile/', views.profile, name='profile'),
  path('<str:username>', views.profile_view, name='profile_view'),
  
  ]