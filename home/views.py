from django.shortcuts import render
from article.models import Article , Category

def home_page(request):

    articles = Article.objects.filter(status=True)

    recent_art = Article.objects.filter(status=True).order_by('-update' , '-create')[:3]

    categories = Category.objects.all()[:7]

    return render(request , "home/home.html" , {'articles': articles , "categories": categories , "recentest": recent_art})
