from django.shortcuts import render , get_object_or_404
from .models import Article , Category
from django.core.paginator import Paginator

def article_detail_page(request , slug):

    article = get_object_or_404(Article , slug=slug)

    return render(request , "article/article_detail.html" , {'article': article})


def articles_list(request):

    articles = Article.objects.filter(status=True).order_by('-update' , '-create')
    page_number = request.GET.get("page")
    paginator = Paginator(articles , 2)
    objects_list = paginator.get_page(page_number)

    return render(request , "article/articles_list.html" , {'articles': objects_list})


def categories_detail(request , slug):

    category_articles = get_object_or_404(Category , slug=slug)
    articles = category_articles.articles.filter(status=True)

    return render(request, "article/articles_list.html" , {"articles": articles})




