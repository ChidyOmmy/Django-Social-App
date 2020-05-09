import datetime
from django.db import models
from django.contrib.auth.models import User 

from Accounts.models import UserInfo

# Create your models here.
class Like(models.Model):
  author = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
  
class Post(models.Model):
  author = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
  pub_date = models.DateTimeField('Date Published')
  content = models.CharField(max_length=10000)
  likes = models.ManyToManyField(Like, related_name="posts")
  
  def was_published_recently(self):
     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
  
  
class Comment(models.Model):
  author = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  comment = models.CharField(max_length=500)
  likes = models.ManyToManyField(Like, related_name="comments")
  pub_date = models.DateTimeField('Date Published')
  
  def was_published_recently(self):
     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
  
class Reply(models.Model):
  author = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
  comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
  likes = models.ManyToManyField(Like, related_name="replies")
  reply = models.CharField(max_length=500)
  pub_date = models.DateTimeField('Date Published')
  
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
  
  

