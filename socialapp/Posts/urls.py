from django.urls import path

from . import views

urlpatterns = [
  path('', views.post, name='post'),
  path('like', views.post_like, name='post_like'),
  path('comment/', views.comment, name='comment'),
  path('<int:post_id>', views.post_view, name='post_view'),
  path('edit/<int:post_id>', views.edit_post, name='edit_post'),
  path('comment/like', views.comment_like, name='comment_like'),
  path('reply/like', views.reply_like, name='reply_like'),
  path('reply', views.reply, name='reply'),
  path('likes/<int:post_id>', views.people_liked, name='people_liked'),
  ]