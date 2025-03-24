from django.shortcuts import render, redirect
from . forms import ArticleForm
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