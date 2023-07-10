from django.shortcuts import render
from article.models import Article
def home_page(request):

    articles = Article.objects.filter(status=True)

    return render(request , "home/home.html" , {'articles':articles})
