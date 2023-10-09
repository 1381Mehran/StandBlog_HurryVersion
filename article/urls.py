from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('detail/<slug:slug>' , views.article_detail_page , name="article_detail_page"),
    path('detail/category/<slug:slug>' , views.categories_detail , name="categories_detail"),
    path('list' , views.articles_list , name="articles_list"),
    path('search/list' , views.search , name="search"),
    path('contact' , views.contact_us , name="contact_us"),
    path('about' , views.about_page , name="about_page"),
]
