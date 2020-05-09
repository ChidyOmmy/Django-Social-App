from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class UserInfo(models.Model):
  GENDER = (('M', 'Male'),('F', 'Female'),)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userinfo")
  sex = models.CharField(max_length=1, choices = GENDER)
  dp = models.CharField(max_length=64)
  
  def __str__(self):
    return f'{self.user.username} info'
    
