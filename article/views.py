from django.shortcuts import render , get_object_or_404
from .models import Article , Category

def article_detail_page(request , slug):

    article = get_object_or_404(Article , slug=slug)

    return render(request , "article/article_detail.html" , {'article': article})


def articles_list(request):

    articles = Article.objects.filter(status=True).order_by('-update' , '-create')

    return render(request , "article/articles_list.html" , {'articles': articles})


def categories_detail(request , slug):

    category_articles = get_object_or_404(Category , slug=slug)
    articles = category_articles.article_set.filter(status=True)

    return render(request, "article/articles_list.html" , {"articles": articles})




