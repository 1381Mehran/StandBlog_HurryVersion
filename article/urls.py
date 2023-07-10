from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('detail/<int:pk>' , views.article_detail_page , name="article_detail_page"),
]
