from django.db import models

# Create your models here.
class Article(models.Model):
    # modles.Model 이라는 클래스를 상속 받아서 사용할 것이다.
     title = models.CharField(max_length=100)   
     content = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)  
     updated_at = models.DateTimeField(auto_now=True)   

# class Comment(models.Model):
#      pass