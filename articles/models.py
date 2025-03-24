from django.db import models

# Create your models here.
class Article(models.Model):
    # modles.Model 이라는 클래스를 상속 받아서 사용할 것이다.
     title = models.CharField(max_length=100)   
     content = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)  
     updated_at = models.DateTimeField(auto_now=True)   

class Comment(models.Model):
     content = models.TextField()
     article = models.ForeignKey(Article, on_delete=models.CASCADE) # 부모가 지워졌을때, 자식이 같이 지워진다.
     # 1:N 관계에서 1은 Article, N은 Comment이다.