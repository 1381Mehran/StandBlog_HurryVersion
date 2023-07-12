from django.shortcuts import render , get_object_or_404
from .models import Article , Category


def article_detail_page(request , slug):

    article = get_object_or_404(Article , slug=slug)

    return render(request , "article/article_detail.html" , {'article': article})


def articles_list(request):

    articles = Article.objects.filter(status=True).order_by('-update' , '-create')

    recent_article = Article.objects.filter(status=True).order_by('-update' , '-create')[:3]

    categories = Category.objects.all().order_by('-create',)[:6]

    return render(request , "article/articles_list.html" , {'articles': articles , "recentest": recent_article , "categories": categories})
