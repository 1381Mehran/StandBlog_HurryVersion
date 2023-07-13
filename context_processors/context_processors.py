from article.models import Article , Category


def recent_articles(request):

    articles = Article.objects.order_by("-update")

    return {"recent_article": articles}


def categories(request):

    categories = Category.objects.order_by("-create")

    return {"categories" : categories}
