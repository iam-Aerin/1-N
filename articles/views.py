from django.shortcuts import render, redirect
from . forms import ArticleForm, CommentForm
from .models import Article, Comment
# Create your views here.

# Create 함수 만들기

def create(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('articles:index')

	else: 
		form = ArticleForm()
		
	context = {
        'form': form,
	}

	return render(request, 'create.html', context)


# Read 함수 만들기
def index(request):
	articles = Article.objects.all()

	context = {
		'articles' : articles,
	}
	return render(request, 'index.html', context)

# Read (detail -> 기능 구현 (게시물 자세히 보기))
def detail(request, id):
	article = Article.objects.get(id=id) # 전체에서 하나의 article을 고르고
	comments = article.comment_set.all() # 하나의 article에 있는 모든 댓글을 가져오기
 
	form = CommentForm()

	context = {
		'article' : article,
		'form' : form,
		'comments': comments,
	}

	return render(request, 'detail.html', context)


def update(request, id):
	article = Article.objects.get(id=id) 

	if request.method == 'POST':
		form = ArticleForm(request.POST, instance=article) # 새로운 데이터 (request.POST) & 뒤는 기존 정보의 article.
		if form.is_valid():
				form.save()
				return redirect('articles:detail', id=id)
		
	else:
		form = ArticleForm(instance=article) # 기존 게시물을 폼에 넣자

	context = {
		'form' : form,
	}

	return render(request, 'update.html', context)


# Delete 함수 만들기

def delete(request, id):
       article = Article.objects.get(id=id)
       article.delete()
       
       return redirect('articles:index')
       
       
 # Comment Create 함수 만들기
def comment_create(request, article_id):
       if request.method == 'POST':
              form = CommentForm(request. POST)
              if form.is_valid():
                     comment = form.save(commit=False)
                     article = Article.objects.get(id=article_id)
                     comment.article = article
                     comment.save()
                     
                     return redirect('articles:detail', id=article_id)
       else:
              return redirect('articles:index')
       
       
# Comment Delete 함수 만들기
def comment_delete(request, article_id, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('articles:detail', id=article_id)
