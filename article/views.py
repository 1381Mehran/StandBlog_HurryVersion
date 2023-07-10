from django.shortcuts import render , get_object_or_404
from .models import Article


def article_detail_page(request , pk):

    article = get_object_or_404(Article , id=pk)

    return render(request , "article/article_detail.html" , {'article': article})
