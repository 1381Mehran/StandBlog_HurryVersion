from django.shortcuts import render , get_object_or_404
from .models import Article


def article_detail_page(request , slug):

    article = get_object_or_404(Article , slug=slug)

    return render(request , "article/article_detail.html" , {'article': article})
