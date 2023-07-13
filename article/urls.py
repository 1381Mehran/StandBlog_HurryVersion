from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('detail/<slug:slug>' , views.article_detail_page , name="article_detail_page"),
    path('detail/category/<slug:slug>' , views.categories_detail , name="categories_detail"),
    path('list' , views.articles_list , name="articles_list"),
]
