from django.shortcuts import render , get_object_or_404 , redirect
from .models import Article, Category, Comment, Contact
from django.core.paginator import Paginator
from .forms import ContactUs, MassageForm


def article_detail_page(request , slug):

    article = get_object_or_404(Article , slug=slug)

    if request.method == "POST":
        parent_id = request.POST.get("parent_id")
        body = request.POST.get("body")
        Comment.objects.create(body=body, article=article , user=request.user , parent_id=parent_id )

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


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get("page")
    paginator = Paginator(articles , 1)
    object_list = paginator.get_page(page_number)

    return render(request, "article/articles_list.html", {"articles": object_list})

def contact_us(request):
    if request.method == "POST":
        form = MassageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            massage = form.cleaned_data["Massage"]

            Contact.objects.create(name=name , email=email , subject=subject , Massage=massage)

            return redirect("home:home_page")

    else:
        form = MassageForm()

    return render(request , "article/contactUs.html", {"form": form})

