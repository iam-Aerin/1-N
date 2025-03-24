from django.forms import ModelForm
from .models import Article, Comment

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta():
        model = Comment
        # fields = '__all__'
        # fields = ('content', ) # 튜플로 해야함
        # fields => 추가할 필드 목록
                
        exclude = ('article', )
        # exclude => 제외할 필드 목록