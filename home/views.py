from django.shortcuts import render
from home.models import Article

# Create your views here.
def index(request):
    article_list = Article.objects.all()
    return render(request, 'home/index.html', {"article_list":article_list})
