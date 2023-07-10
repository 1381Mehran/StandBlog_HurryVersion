from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('detail/<slug:slug>' , views.article_detail_page , name="article_detail_page"),
]
