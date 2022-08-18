import json
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Keyword(models.Model):
    name = models.CharField(max_length=32)

class Article(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    keyword = models.ManyToManyField(Keyword)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at", "-updated_at"]

    def get_api_url(self):
        try:
            return reverse("article_api:article_detail", kwargs={"pk": self.pk})
        except:
            None

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter(parent=instance)
        return qs

    
class Comment(models.Model):
    parent = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ["-created_at", "-updated_at"]

