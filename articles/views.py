from django.shortcuts import render, redirect
from . forms import ArticleForm
from .models import Article
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


def index(request):
	articles = Article.objects.all()

	context = {
		'articles' : articles,
	}
	return render(request, 'index.html', context)


def detail(request, id):
	article = Article.objects.get(id=id)

	context = {
		'article' : article,
	}

	return render(request, 'detail.html', context)