from django.shortcuts import render
from hello.models import Post

def myView(request):
	context = {
        'posts': Post.objects.all() # Query datas from DB
	}
	return render(request, 'hello/blog.html', context)