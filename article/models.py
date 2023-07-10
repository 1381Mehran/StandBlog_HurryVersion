from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=15)
    create = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):

    author = models.ForeignKey(User , on_delete=models.SET_DEFAULT , default="1")
    title = models.CharField(max_length=25)
    category = models.ManyToManyField(Category)
    body = models.TextField()
    image_banner = models.ImageField(upload_to="images/banners")
    image_post = models.ImageField(upload_to="images/posts")
    image_thumb = models.ImageField(upload_to="images/thumbs")
    status = models.BooleanField(default=False)


    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("article:article_detail_page" , args=[self.id])

    def __str__(self):
        return f"{self.title} - {self.author}"
